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
 * A2 has no readable counterpart in `docs/` yet: nothing to align for now.
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

console.log(
  `Compétences md:${mdIds.size} yaml:${ylIds.size} | ` +
    `Grammaire md:${mdGram.size} yaml:${ylGram.size} | ` +
    `Erreurs md:${mdErrs.size} yaml:${ylErrs.size}`,
);

if (problems.length) {
  console.error('ÉCARTS :');
  for (const p of problems) console.error('  -', p);
  process.exit(1);
}
console.log('Markdown et YAML strictement alignés.');
