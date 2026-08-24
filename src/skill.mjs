/**
 * Skill access: location, frontmatter, archive entries.
 *
 * Shared between the repo tooling (`tools/`) and the published CLI (`bin/`),
 * hence no dependency: the frontmatter is read by pattern, not with a full
 * YAML parser. That's enough — `name` and `description` are single-line
 * scalars, and `tools/check-skill.mjs` verifies they stay that way.
 */
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

/** Root of the skill's source directory, in the repo and in the npm package alike. */
export const SKILL_DIR = fileURLToPath(new URL('../skill/', import.meta.url));

const FRONTMATTER = /^---\r?\n([\s\S]*?)\r?\n---\r?\n/;

/** Strips the quotes off a plain YAML scalar. */
function unquote(value) {
  const m = /^(['"])([\s\S]*)\1$/.exec(value.trim());
  if (!m) return value.trim();
  return m[1] === '"' ? m[2].replace(/\\(.)/g, '$1') : m[2].replace(/''/g, "'");
}

/**
 * @returns {{fields: Record<string,string>, body: string, raw: string}}
 * @throws if the frontmatter is missing — a skill without frontmatter isn't installable
 */
export function readSkill(dir = SKILL_DIR) {
  const raw = readFileSync(join(dir, 'SKILL.md'), 'utf8');
  const m = FRONTMATTER.exec(raw);
  if (!m) throw new Error('SKILL.md : frontmatter YAML absent');

  const fields = {};
  for (const line of m[1].split(/\r?\n/)) {
    const kv = /^([A-Za-z_][\w-]*)\s*:\s*(.*)$/.exec(line);
    if (kv) fields[kv[1]] = unquote(kv[2]);
  }
  return { fields, body: raw.slice(m[0].length), raw };
}

/** The skill's declared name — this, not `skill`, names the installed directory. */
export function skillName(dir = SKILL_DIR) {
  const { fields } = readSkill(dir);
  if (!fields.name) throw new Error("SKILL.md : le champ 'name' est absent du frontmatter");
  return fields.name;
}

/** The skill's files, sorted, directories excluded. */
export function skillFiles(dir = SKILL_DIR) {
  return readdirSync(dir)
    .filter((f) => statSync(join(dir, f)).isFile())
    .sort();
}

/**
 * Archive entries for import into the Claude app.
 *
 * The ZIP must contain a single top-level directory, named after the
 * frontmatter's declared name. This is the most common packaging mistake:
 * zipping `skill/` as-is produces an archive the import rejects.
 */
export function zipEntries(dir = SKILL_DIR) {
  const name = skillName(dir);
  return skillFiles(dir).map((f) => ({
    name: `${name}/${f}`,
    data: readFileSync(join(dir, f)),
  }));
}
