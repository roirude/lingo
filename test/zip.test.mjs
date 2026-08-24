import { test } from 'node:test';
import assert from 'node:assert/strict';
import { inflateRawSync } from 'node:zlib';
import { createZip, readZipNames } from '../src/zip.mjs';
import { skillName, zipEntries } from '../src/skill.mjs';

/** Reads back an entry from its local header — the inverse of `createZip`. */
function extract(buf, wanted) {
  let at = 0;
  while (at < buf.length && buf.readUInt32LE(at) === 0x04034b50) {
    const method = buf.readUInt16LE(at + 8);
    const compressedSize = buf.readUInt32LE(at + 18);
    const nameLen = buf.readUInt16LE(at + 26);
    const extraLen = buf.readUInt16LE(at + 28);
    const name = buf.toString('utf8', at + 30, at + 30 + nameLen);
    const start = at + 30 + nameLen + extraLen;
    const data = buf.subarray(start, start + compressedSize);
    if (name === wanted) return method === 8 ? inflateRawSync(data) : Buffer.from(data);
    at = start + compressedSize;
  }
  throw new Error(`entrée absente : ${wanted}`);
}

test('une archive se relit telle qu\'elle a été écrite', () => {
  const contenu = 'Bonjour — accents, apostrophe d\'essai.\n'.repeat(50);
  const buf = createZip([
    { name: 'dossier/a.txt', data: contenu },
    { name: 'dossier/b.bin', data: Buffer.from([0, 1, 2, 253, 254, 255]) },
  ]);

  assert.deepEqual(readZipNames(buf), ['dossier/a.txt', 'dossier/b.bin']);
  assert.equal(extract(buf, 'dossier/a.txt').toString('utf8'), contenu);
  assert.deepEqual([...extract(buf, 'dossier/b.bin')], [0, 1, 2, 253, 254, 255]);
});

test('un contenu incompressible est stocké tel quel, sans grossir', () => {
  // Random data: deflate can't shrink it and would add bytes instead.
  const bruit = Buffer.from(Array.from({ length: 4096 }, (_, i) => (i * 2654435761) % 256));
  const buf = createZip([{ name: 'bruit', data: bruit }]);
  assert.deepEqual(extract(buf, 'bruit'), bruit);
});

test('le ZIP du skill a un dossier unique à sa racine, portant le nom du skill', () => {
  const name = skillName();
  const names = readZipNames(createZip(zipEntries()));
  assert.deepEqual([...new Set(names.map((n) => n.split('/')[0]))], [name]);
  assert.ok(names.includes(`${name}/SKILL.md`));
});
