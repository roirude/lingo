#!/usr/bin/env node
/**
 * Regenerates a curriculum YAML file from its source of truth and validates it.
 *
 *   node tools/build.mjs a1
 *   node tools/build.mjs a2      (also checks prerequisites toward A1)
 *
 * The YAML is a build artifact: never edit it by hand, edit
 * `tools/data/<level>.mjs` and rerun instead.
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { load } from 'js-yaml';
import a1 from './data/a1.mjs';
import a2 from './data/a2.mjs';
import { emitYaml, validate, allComps, idsOf } from './lib/curriculum.mjs';

/**
 * The elaboration requirement is A2's core idea: if it's only tracked in the
 * unit that teaches it, it doesn't actually run through the level.
 */
function minimalAnswerSpread(spec) {
  const units = new Set();
  for (const { unit, comp } of allComps(spec)) {
    if (comp.errors.includes('E.FR.MINIMAL-ANSWER') && unit !== 'U00') units.add(unit);
  }
  return units.size >= 5
    ? []
    : [`E.FR.MINIMAL-ANSWER n'est surveillée que dans ${units.size} unités hors U00 ` +
       `— l'exigence d'élaboration doit traverser le niveau`];
}

const LEVELS = {
  a1: { data: a1, out: 'skill/curriculum-a1.yaml', grammarOptionalUnits: ['U01'] },
  a2: { data: a2, out: 'skill/curriculum-a2.yaml', below: 'skill/curriculum-a1.yaml',
        extraChecks: [minimalAnswerSpread] },
};

const level = process.argv[2];
const cfg = LEVELS[level];
if (!cfg) {
  console.error(`usage : node tools/build.mjs ${Object.keys(LEVELS).join('|')}`);
  process.exit(2);
}

const spec = { ...cfg.data, grammarOptionalUnits: cfg.grammarOptionalUnits, extraChecks: cfg.extraChecks };
const knownIds = cfg.below ? idsOf(load(readFileSync(cfg.below, 'utf8'))) : new Set();

writeFileSync(cfg.out, emitYaml(spec), 'utf8');
const { problems, ids, modes, gramUsed, errUsed, perUnit } = validate(spec, knownIds);

const top = (map, n) => [...map.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])).slice(0, n);
const crossLevel = [...allComps(spec)].filter(({ comp }) =>
  comp.prereqs.some((p) => !p.startsWith(spec.level))).length;

console.log('='.repeat(62));
console.log(`VALIDATION — Inventaire ${spec.level}   →  ${cfg.out}`);
console.log('='.repeat(62));
console.log(`Compétences         : ${ids.length}   (uniques : ${new Set(ids).size})`);
console.log(`Unités              : ${Object.keys(spec.units).length}`);
console.log(`Grammaire           : ${spec.grammar.length} déclarés, ${gramUsed.size} utilisés`);
console.log(`Erreurs FR          : ${Object.keys(spec.errorDefs).length} définies, ${errUsed.size} rattachées`);
if (cfg.below) console.log(`Prérequis vers A1   : ${crossLevel} compétence(s)`);
console.log();
console.log('Par unité :', [...perUnit.entries()].sort().map(([u, n]) => `${u}:${n}`).join('  '));
console.log('Modes     :', ['I', 'PO', 'PE', 'RO', 'RE'].map((m) => `${m}:${modes.get(m) ?? 0}`).join('  '));
console.log();
console.log('Erreurs les plus surveillées :');
for (const [e, n] of top(errUsed, 6)) console.log(`   ${e.padEnd(28)} ${n} compétence(s)`);
console.log();

if (problems.length) {
  console.error(`PROBLÈMES (${problems.length}) :`);
  for (const p of problems) console.error('   -', p);
  process.exit(1);
}
console.log('Aucun problème détecté.');
