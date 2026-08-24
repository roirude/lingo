#!/usr/bin/env node
/**
 * Lingo's installer CLI.
 *
 *   npx lingo-english-tutor install     copies the skill for Claude Code
 *   npx lingo-english-tutor zip         builds the archive to import into the app
 *
 * No dependencies: `npx` only downloads this package.
 */
import { copyFileSync, existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { homedir } from 'node:os';
import { join, resolve } from 'node:path';
import { createZip } from '../src/zip.mjs';
import { SKILL_DIR, skillFiles, skillName, zipEntries } from '../src/skill.mjs';

const pkg = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8'));

const HELP = `
Lingo — professeur d'anglais pour francophones, sous forme de skill Claude.

  npx ${pkg.name} install [options]   installe le skill pour Claude Code
  npx ${pkg.name} zip [options]       produit le ZIP à importer dans l'app Claude

Options de « install »
  --project        installe dans ./.claude/skills/ (versionné avec le dépôt)
                   au lieu de ~/.claude/skills/ (tous vos projets)
  --dir <chemin>   installe dans un dossier choisi
  --dry-run        montre ce qui serait écrit, sans rien écrire

Options de « zip »
  --out <chemin>   chemin du fichier à écrire (défaut : ./<nom-du-skill>.zip)

Autres
  --help, -h       cette aide
  --version, -v    version du paquet

L'app Claude et Cowork n'installent pas depuis le disque : pour elles, passez
par « zip », puis importez l'archive dans Customize → Skills.
`.trim();

function parseArgs(argv) {
  const flags = {};
  const rest = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--dir' || a === '--out') flags[a.slice(2)] = argv[++i];
    else if (a.startsWith('--')) flags[a.slice(2)] = true;
    else if (a.startsWith('-') && a !== '-') flags[a.slice(1)] = true;
    else rest.push(a);
  }
  return { command: rest[0], flags };
}

/** Install destination, based on the options. */
function targetDir(flags, name) {
  if (flags.dir) return resolve(flags.dir);
  const root = flags.project ? resolve('.claude') : join(homedir(), '.claude');
  return join(root, 'skills', name);
}

function install(flags) {
  const name = skillName();
  const dest = targetDir(flags, name);
  const files = skillFiles();
  const existed = existsSync(dest);

  const plan = files.map((f) => {
    const to = join(dest, f);
    if (!existsSync(to)) return { file: f, action: 'ajouté' };
    const same = readFileSync(join(SKILL_DIR, f)).equals(readFileSync(to));
    return { file: f, action: same ? 'inchangé' : 'mis à jour' };
  });

  // Never delete what we didn't write: just flag it.
  const foreign = existed
    ? readdirSync(dest).filter((f) => !files.includes(f) && statSync(join(dest, f)).isFile())
    : [];

  console.log(`${flags['dry-run'] ? 'Simulation' : 'Installation'} → ${dest}`);
  if (!flags['dry-run']) {
    mkdirSync(dest, { recursive: true });
    for (const f of files) copyFileSync(join(SKILL_DIR, f), join(dest, f));
  }
  for (const { file, action } of plan) console.log(`   ${action.padEnd(11)} ${file}`);

  if (foreign.length) {
    console.log(`\nLaissés en place, non fournis par ce paquet : ${foreign.join(', ')}`);
  }
  if (flags['dry-run']) return;

  console.log(`\nLingo ${pkg.version} est installé. Dans Claude Code, vérifiez avec /skills,`);
  console.log('puis dites : « commence mon cours d\'anglais ».');
  if (!flags.project && !flags.dir) {
    console.log('\nSi ~/.claude/skills/ n\'existait pas au lancement de votre session, redémarrez-la.');
  }
  console.log('L\'app Claude et Cowork ne lisent pas ce dossier : pour elles, faites');
  console.log(`« npx ${pkg.name} zip » et importez l'archive dans Customize → Skills.`);
}

function zip(flags) {
  const name = skillName();
  const out = resolve(flags.out ?? `${name}.zip`);
  const archive = createZip(zipEntries());
  writeFileSync(out, archive);
  console.log(`${out}  (${Math.round(archive.length / 1024)} Ko)`);
  console.log('\nImportez cette archive dans l\'app Claude : Customize → Skills.');
  console.log('Cowork charge les skills activés sur le compte claude.ai : redémarrez la session après l\'import.');
}

const { command, flags } = parseArgs(process.argv.slice(2));

if (flags.version || flags.v) console.log(pkg.version);
else if (flags.help || flags.h || !command) console.log(HELP);
else if (command === 'install') install(flags);
else if (command === 'zip') zip(flags);
else {
  console.error(`Commande inconnue : ${command}\n`);
  console.error(HELP);
  process.exit(2);
}
