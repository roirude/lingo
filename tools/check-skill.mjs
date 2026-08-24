#!/usr/bin/env node
/**
 * Checks that `skill/` respects a Claude skill's constraints and stays
 * consistent with the curriculums.
 *
 *   npm run check
 *
 * Run from the repository root.
 */
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { load } from 'js-yaml';
import { readSkill, skillFiles, SKILL_DIR } from '../src/skill.mjs';

const problems = [];
const notes = [];
const check = (ok, msg) => {
  if (!ok) problems.push(msg);
  return ok;
};
const read = (f) => readFileSync(join(SKILL_DIR, f), 'utf8');
const matches = (txt, re) => new Set(txt.match(re) ?? []);
const missing = (a, b) => [...a].filter((x) => !b.has(x)).sort();

// ---------- frontmatter ----------
const { fields, body } = readSkill();
const name = fields.name ?? '';
const desc = fields.description ?? '';

// Count code points, not UTF-16 units: the description is right at the app's
// cap, and `.length` would double-count any character outside the BMP.
const width = (s) => [...s].length;

check(Boolean(name), "frontmatter : 'name' manquant");
check(width(name) <= 64, `name : ${width(name)} caractères (max 64)`);
check(/^[a-z0-9-]+$/.test(name), `name : '${name}' doit être en minuscules/chiffres/tirets`);
check(!/anthropic|claude/.test(name), 'name : mot réservé (anthropic/claude)');
check(Boolean(desc), "frontmatter : 'description' manquante");
check(
  width(desc) <= 200,
  `description : ${width(desc)} caractères — l'import dans l'app Claude plafonne à 200. ` +
    '(Claude Code tolère jusqu\'à 1536 avec when_to_use, mais on vise la limite la plus stricte ' +
    'pour que le même dossier s\'installe partout.)',
);
check(!desc.includes('<') && !name.includes('<'), 'frontmatter : balise XML interdite');
check(!/^\s*(Je |I |Tu |You )/.test(desc), 'description : doit être à la 3e personne');
check(
  /\b(pour|quand|lorsque|à utiliser|utilis\w*|use when)\b/i.test(desc),
  'description : doit dire QUAND utiliser le skill, pas seulement ce qu\'il fait',
);

// ---------- size and structure ----------
const nlines = body.split('\n').length;
check(nlines <= 500, `SKILL.md : ${nlines} lignes de corps (recommandé ≤ 500)`);
notes.push(`SKILL.md : ${nlines} lignes de corps`);

// ---------- referenced files ----------
const REF = /`([a-z0-9-]+\.(?:md|yaml|json|mjs))`/g;
const refNames = (txt) => new Set([...txt.matchAll(REF)].map((m) => m[1]));

const present = new Set(skillFiles().filter((f) => f !== 'SKILL.md'));
const referenced = refNames(body);
referenced.delete('SKILL.md');

for (const f of missing(referenced, present)) {
  problems.push(`SKILL.md référence '${f}' qui n'existe pas dans skill/`);
}
for (const f of missing(present, referenced)) {
  problems.push(`'${f}' présent mais jamais référencé par SKILL.md (jamais chargé)`);
}

// Only one level of depth: no reference file may reference another.
for (const f of present) {
  if (!f.endsWith('.md')) continue;
  const txt = read(f);
  for (const other of refNames(txt)) {
    if (present.has(other) && other !== f) {
      problems.push(`${f} référence ${other} : références imbriquées interdites (lecture partielle probable)`);
    }
  }
  if (txt.split('\n').length - 1 > 100 && !/^##+ Sommaire/m.test(txt)) {
    problems.push(`${f} : plus de 100 lignes sans sommaire en tête`);
  }
}

// ---------- no embedded design directory ----------
for (const d of ['docs', 'doc']) {
  check(!existsSync(join(SKILL_DIR, d)), `skill/${d}/ : les documents de conception ne doivent pas être dans le skill`);
}

// ---------- consistency with the curriculums ----------
const LEVELS = {};
for (const lvl of ['a1', 'a2']) {
  const cur = load(read(`curriculum-${lvl}.yaml`));
  LEVELS[lvl] = {
    ids: new Set(Object.values(cur.units).flatMap((u) => u.competencies.map((c) => c.id))),
    gram: new Set(cur.grammar_inventory),
    errs: new Set(Object.keys(cur.errors)),
    core: new Set(cur.core_errors),
  };
}
const union = (key) => new Set([...LEVELS.a1[key], ...LEVELS.a2[key]]);
const allIds = union('ids');
const allGram = union('gram');
const allErrs = union('errs');
const allCore = union('core');

const placement = read('placement.md');

for (const fname of ['SKILL.md', 'grammar-a1.md', 'grammar-a2.md', 'placement.md']) {
  const txt = fname === 'SKILL.md' ? body : read(fname);
  for (const bad of missing(matches(txt, /A[12]\.U\d\d\.C\d\d/g), allIds)) {
    problems.push(`${fname} : compétence inexistante ${bad}`);
  }
  for (const bad of missing(matches(txt, /G\.[A-Z0-9-]+/g), allGram)) {
    problems.push(`${fname} : point de grammaire inexistant ${bad}`);
  }
  for (const bad of missing(matches(txt, /E\.FR\.[A-Z0-9-]+/g), allErrs)) {
    problems.push(`${fname} : code d'erreur inexistant ${bad}`);
  }
}

// A grammar sheet must only cite grammar from its own level.
for (const [lvl, fname] of [['a1', 'grammar-a1.md'], ['a2', 'grammar-a2.md']]) {
  for (const bad of missing(matches(read(fname), /G\.[A-Z0-9-]+/g), LEVELS[lvl].gram)) {
    problems.push(`${fname} : ${bad} n'appartient pas au niveau ${lvl.toUpperCase()}`);
  }
}

// Every core error must be named in SKILL.md; A1's core errors must be probed at placement.
for (const e of [...allCore].sort()) {
  check(body.includes(e), `SKILL.md ne nomme pas l'erreur du noyau ${e}`);
}
for (const e of [...LEVELS.a1.core].sort()) {
  check(placement.includes(e), `placement.md ne sonde pas l'erreur du noyau A1 ${e}`);
}

// Sheets announced in SKILL.md vs. sheets actually present.
for (const [inBody, inFile, fname] of [
  [/\bF(\d\d)\b/g, /^## F(\d\d) /gm, 'grammar-a1.md'],
  [/\bA(\d\d)\b/g, /^## A(\d\d) /gm, 'grammar-a2.md'],
]) {
  const captured = (txt, re) => new Set([...txt.matchAll(re)].map((m) => m[1]));
  const announced = captured(body, inBody);
  const actual = captured(read(fname), inFile);
  for (const f of missing(announced, actual)) {
    problems.push(`SKILL.md annonce une fiche absente de ${fname} : ${f}`);
  }
  for (const f of missing(actual, announced)) {
    problems.push(`${fname} contient la fiche ${f}, non annoncée dans SKILL.md`);
  }
  notes.push(`${fname} : ${actual.size} fiches`);
}

// The daily cap and the module review must be described.
check(body.includes('today'), "SKILL.md : le champ 'today' du plafond quotidien n'est pas décrit");
check(body.includes('BILAN'), 'SKILL.md : le type de session BILAN n\'est pas décrit');
check(
  /jours? civils? distincts?|jours distincts/.test(body),
  'SKILL.md : la condition 3 doit se compter en jours, pas en sessions',
);
check(body.includes('+1'), "SKILL.md : la règle du +1 n'est pas décrite");

for (const lvl of ['a1', 'a2']) {
  const L = LEVELS[lvl];
  notes.push(`${lvl.toUpperCase()} : ${L.ids.size} compétences | ${L.gram.size} grammaire | ${L.errs.size} erreurs`);
}
notes.push(`fichiers de référence : ${present.size} (${[...present].sort().join(', ')})`);

// ---------- report ----------
console.log('='.repeat(60));
console.log('VÉRIFICATION DU SKILL');
console.log('='.repeat(60));
console.log(`name        : ${name}`);
console.log(`description : ${width(desc)} caractères`);
for (const n of notes) console.log(`  ${n}`);
console.log();

if (problems.length) {
  console.error(`PROBLÈMES (${problems.length}) :`);
  for (const p of problems) console.error('   -', p);
  process.exit(1);
}
console.log('Aucun problème détecté. Le skill est prêt à installer.');
