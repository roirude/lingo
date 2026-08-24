#!/usr/bin/env node
/**
 * Packages `skill/` into `dist/<skill-name>.zip`, ready to import into the
 * Claude app and into Cowork.
 *
 *   npm run zip
 *
 * The source directory is named `skill/`, but the archive must contain a
 * directory named after the frontmatter's declared name. The rename happens
 * here rather than in the repo: keeping `skill/` locally avoids confusing the
 * source directory with the installable package.
 */
import { mkdirSync, writeFileSync } from 'node:fs';
import { createZip, readZipNames } from '../src/zip.mjs';
import { skillName, zipEntries } from '../src/skill.mjs';

const name = skillName();
const out = `dist/${name}.zip`;

const archive = createZip(zipEntries());
mkdirSync('dist', { recursive: true });
writeFileSync(out, archive);

const entries = readZipNames(archive);
console.log(`${out}  (${Math.round(archive.length / 1024)} Ko)`);
for (const e of entries) console.log('   ', e);

const problems = [];
const roots = new Set(entries.map((e) => e.split('/')[0]));
if (roots.size !== 1 || !roots.has(name)) {
  problems.push(`racine du ZIP = {${[...roots].join(', ')}}, attendu {${name}}`);
}
if (!entries.includes(`${name}/SKILL.md`)) {
  problems.push('SKILL.md absent de la racine du dossier');
}

if (problems.length) {
  console.error();
  for (const p of problems) console.error('ERREUR :', p);
  process.exit(1);
}
console.log('\nStructure conforme.');
