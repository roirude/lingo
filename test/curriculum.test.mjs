import { readFileSync } from 'node:fs';
import { test } from 'node:test';
import assert from 'node:assert/strict';
import a1 from '../tools/data/a1.mjs';
import a2 from '../tools/data/a2.mjs';
import { emitYaml, validate, idsOf, counts } from '../tools/lib/curriculum.mjs';
import { pyRepr } from '../tools/lib/pyrepr.mjs';
import { load } from 'js-yaml';

const specs = {
  a1: { ...a1, grammarOptionalUnits: ['U01'] },
  a2: a2,
};

for (const [lvl, spec] of Object.entries(specs)) {
  // The YAML is a committed artifact: if it drifts from its source, the
  // skill teaches something other than what the source describes.
  test(`${lvl} : le YAML commité est identique à ce que produit la source`, () => {
    const committed = readFileSync(`skill/curriculum-${lvl}.yaml`, 'utf8');
    assert.equal(emitYaml(spec), committed, `lancez « npm run build » : ${lvl} a dérivé`);
  });

  test(`${lvl} : l'inventaire passe ses propres contrôles`, () => {
    const knownIds = lvl === 'a2' ? idsOf(load(readFileSync('skill/curriculum-a1.yaml', 'utf8'))) : new Set();
    const { problems } = validate(spec, knownIds);
    assert.deepEqual(problems, []);
  });
}

test('les comptes annoncés par le README tiennent', () => {
  assert.deepEqual(counts(specs.a1), { units: 13, comps: 98, grammar: 55, errors: 55 });
  assert.deepEqual(counts(specs.a2), { units: 15, comps: 99, grammar: 58, errors: 47 });
});

/** Deep-clones only the data: the spec also carries a `header` function. */
const mutable = (spec) => ({ ...spec, units: JSON.parse(JSON.stringify(spec.units)) });

test('validate signale un prérequis inexistant', () => {
  const broken = mutable(specs.a1);
  broken.units.U01.comps[0].prereqs = ['A1.U99.C01'];
  const { problems } = validate(broken);
  assert.ok(problems.some((p) => p.includes('prérequis inexistant A1.U99.C01')), problems.join('\n'));
});

test('validate signale une unité sans compétence réceptive', () => {
  const broken = mutable(specs.a1);
  for (const c of broken.units.U00.comps) c.modes = ['I'];
  const { problems } = validate(broken);
  assert.ok(problems.some((p) => p.startsWith('U00 : aucune compétence réceptive')), problems.join('\n'));
});

// pyRepr is the piece that guarantees bit-identical output with the Python
// version: its quoting rules are those of `repr()`, not YAML's.
test('pyRepr suit les règles de citation de Python', () => {
  assert.equal(pyRepr('simple'), "'simple'");
  assert.equal(pyRepr("d'expliquer"), '"d\'expliquer"');
  assert.equal(pyRepr('dit "oui"'), '\'dit "oui"\'');
  assert.equal(pyRepr('l\'un dit "oui"'), '\'l\\\'un dit "oui"\'');
  assert.equal(pyRepr('a\\b'), "'a\\\\b'");
  assert.equal(pyRepr('ligne\nsuite'), "'ligne\\nsuite'");
  assert.equal(pyRepr('accentué é'), "'accentué é'");
});
