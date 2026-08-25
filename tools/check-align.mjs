#!/usr/bin/env node
/**
 * Checks that the human-readable inventory and the generated curriculum don't drift apart.
 *
 *   node tools/check-align.mjs
 *
 * `docs/02-competences-A1.md` is the design document: it's what gets reread
 * to reason about the curriculum. `skill/curriculum-a1.yaml` is what the
 * skill actually loads. If the two diverge, decisions get made against an
 * inventory the tutor doesn't teach.
 *
 * A2 has no readable counterpart in `docs/`, but it does point back into A1:
 * the second half of this file checks that those cross-level prerequisites
 * stay reachable for a learner who is placed at A2 and never revisits A1.
 */
import { readFileSync } from 'node:fs';
import { load } from 'js-yaml';
import { idsOf } from './lib/curriculum.mjs';

const MD = 'docs/02-competences-A1.md';
const YAML = 'skill/curriculum-a1.yaml';

const md = readFileSync(MD, 'utf8');
const curriculum = load(readFileSync(YAML, 'utf8'));

const found = (txt, re) => new Set(txt.match(re) ?? []);
const mdIds = found(md, /A1\.U\d\d\.C\d\d/g);
const mdGram = found(md, /G\.[A-Z0-9-]+/g);
const mdErrs = found(md, /E\.FR\.[A-Z0-9-]+/g);

const ylIds = idsOf(curriculum);
const ylGram = new Set(curriculum.grammar_inventory);
const ylErrs = new Set(Object.keys(curriculum.errors));

const problems = [];
for (const [label, a, b] of [
  ['ID présents dans le markdown, absents du YAML', mdIds, ylIds],
  ['ID présents dans le YAML, absents du markdown', ylIds, mdIds],
  ['GRAMMAIRE markdown \\ YAML', mdGram, ylGram],
  ['GRAMMAIRE YAML \\ markdown', ylGram, mdGram],
  ['ERREURS markdown \\ YAML', mdErrs, ylErrs],
  ['ERREURS YAML \\ markdown', ylErrs, mdErrs],
]) {
  const gap = [...a].filter((x) => !b.has(x)).sort();
  if (gap.length) problems.push(`${label} : ${gap.join(', ')}`);
}

// ---------- cross-level prerequisites ----------
// A2 competencies point back into A1. A learner placed at A2 never walks the
// A1 curriculum again, so those prerequisites are satisfied by the blanket
// presumption `A1.*~` written at placement. When that blanket is replaced by a
// hand-written list, the ids it forgets become unmet prerequisites, `NEXT`
// falls back into A1, and the learner is sent to relearn "What's your name?".
// That regression is what this section exists to catch.
const comps = (cur) => Object.values(cur.units).flatMap((u) => u.competencies);
const a2 = load(readFileSync('skill/curriculum-a2.yaml', 'utf8'));
const a1Prereqs = new Map(comps(curriculum).map((c) => [c.id, c.prereqs ?? []]));

// Close the seed set under A1's own prerequisites: a prerequisite whose own
// prerequisite is missing isn't actually reachable.
const seeds = comps(a2).flatMap((c) => (c.prereqs ?? []).filter((p) => p.startsWith('A1.')));
const crossLevel = new Set(seeds);
const closure = new Set();
for (const stack = [...crossLevel]; stack.length; ) {
  const id = stack.pop();
  if (closure.has(id)) continue;
  closure.add(id);
  if (!a1Prereqs.has(id)) {
    problems.push(`prérequis A1 référencé depuis A2 mais inexistant : ${id}`);
    continue;
  }
  stack.push(...a1Prereqs.get(id).filter((p) => p.startsWith('A1.')));
}

for (const f of ['skill/placement.md', 'skill/SKILL.md']) {
  if (!readFileSync(f, 'utf8').includes('A1.*~')) {
    problems.push(
      `${f} : la présomption en bloc « A1.*~ » a disparu — sans elle, ` +
        `${crossLevel.size} prérequis A2→A1 deviennent bloquants et le parcours redescend en A1`,
    );
  }
}

// placement.md cites the count as an argument against hand-written lists;
// a stale number there is an argument the reader can check and disbelieve.
const cited = /(\d+) prérequis vers A1/.exec(readFileSync('skill/placement.md', 'utf8'));
if (!cited) {
  problems.push('placement.md : la phrase citant le nombre de prérequis vers A1 a disparu');
} else if (Number(cited[1]) !== crossLevel.size) {
  problems.push(`placement.md annonce ${cited[1]} prérequis vers A1, le curriculum en déclare ${crossLevel.size}`);
}

console.log(
  `Compétences md:${mdIds.size} yaml:${ylIds.size} | ` +
    `Grammaire md:${mdGram.size} yaml:${ylGram.size} | ` +
    `Erreurs md:${mdErrs.size} yaml:${ylErrs.size}`,
);
console.log(
  `Prérequis A2→A1 : ${crossLevel.size} cibles A1 distinctes, ${closure.size} avec leur fermeture dans A1`,
);

if (problems.length) {
  console.error('ÉCARTS :');
  for (const p of problems) console.error('  -', p);
  process.exit(1);
}
console.log('Markdown et YAML strictement alignés.');
