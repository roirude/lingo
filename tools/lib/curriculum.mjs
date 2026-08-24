/**
 * Emission and validation of one curriculum level.
 *
 * A1 and A2 share the same shape: units, competencies typed by mode, a
 * declared grammar, indexed French-speaker errors. This module carries
 * everything that's common; what differs from one level to the other is
 * declared in `tools/data/<level>.mjs`.
 */
import { pyRepr } from './pyrepr.mjs';

/**
 * Flattens units into (unit, definition, competency). Empty lists are
 * omitted from the data to keep one line per competency; they're restored
 * here, once, so the rest of the code doesn't have to worry about it.
 */
export function* allComps(spec) {
  for (const [unit, def] of Object.entries(spec.units)) {
    for (const comp of def.comps) {
      yield {
        unit,
        def,
        comp: { grammar: [], errors: [], prereqs: [], ...comp },
      };
    }
  }
}

const list = (xs = []) => `[${xs.join(', ')}]`;

export function counts(spec) {
  return {
    units: Object.keys(spec.units).length,
    comps: Object.values(spec.units).reduce((n, u) => n + u.comps.length, 0),
    grammar: spec.grammar.length,
    errors: Object.keys(spec.errorDefs).length,
  };
}

export function emitYaml(spec) {
  const L = spec.header(counts(spec));
  L.push('---', `level: ${spec.level}`, 'l1_target: fr', 'units:');

  for (const [unit, d] of Object.entries(spec.units)) {
    L.push(`  ${unit}:`);
    L.push(`    theme: ${pyRepr(d.theme)}`);
    L.push(`    theme_en: ${pyRepr(d.themeEn)}`);
    L.push(`    lexis: ${d.lexis}`);
    if (d.transversal) L.push('    transversal: true');
    if (d.pivot) L.push('    pivot: true');
    L.push(`    functions: ${list(d.functions)}`);
    L.push('    competencies:');
    for (const c of d.comps) {
      L.push(`      - id: ${spec.level}.${unit}.${c.id}`);
      L.push(`        fr: ${pyRepr(c.fr)}`);
      L.push(`        en: ${pyRepr(c.en)}`);
      L.push(`        modes: ${list(c.modes)}`);
      L.push(`        grammar: ${list(c.grammar)}`);
      L.push(`        errors: ${list(c.errors)}`);
      L.push(`        prereqs: ${list(c.prereqs)}`);
    }
  }

  L.push(`grammar_inventory: ${list(spec.grammar)}`);
  L.push(`core_errors: ${list(spec.coreErrors)}`);
  L.push(`pronunciation_out_of_scope_v1: ${list(spec.pronunciationErrors)}`);
  L.push('errors:');
  for (const code of Object.keys(spec.errorDefs).sort()) {
    const e = spec.errorDefs[code];
    L.push(`  ${code}:`);
    L.push(`    label: ${pyRepr(e.label)}`);
    L.push(`    wrong: ${pyRepr(e.wrong)}`);
    L.push(`    right: ${pyRepr(e.right)}`);
    L.push(`    core: ${spec.coreErrors.includes(code)}`);
    L.push(`    scored_v1: ${!spec.pronunciationErrors.includes(code)}`);
  }
  return L.join('\n') + '\n';
}

/**
 * @param {object} spec           level to validate
 * @param {Set<string>} knownIds  ids from a lower level, legitimate
 *                                prerequisite targets (empty for A1)
 */
export function validate(spec, knownIds = new Set()) {
  const problems = [];
  const ids = [];
  const seen = new Set();
  const tally = (map, key) => map.set(key, (map.get(key) ?? 0) + 1);
  const modes = new Map();
  const gramUsed = new Map();
  const errUsed = new Map();
  const perUnit = new Map();

  for (const { unit, comp } of allComps(spec)) {
    const full = `${spec.level}.${unit}.${comp.id}`;
    if (seen.has(full)) problems.push(`identifiant dupliqué : ${full}`);
    seen.add(full);
    ids.push(full);
    tally(perUnit, unit);
    for (const m of comp.modes) tally(modes, m);
    for (const g of comp.grammar) tally(gramUsed, g);
    for (const e of comp.errors) tally(errUsed, e);

    if (!comp.modes.length) problems.push(`${full} : aucun mode`);
    if (!comp.grammar.length && !spec.grammarOptionalUnits?.includes(unit)) {
      problems.push(`${full} : aucune ressource grammaticale`);
    }
    for (const g of comp.grammar) {
      if (!spec.grammar.includes(g)) problems.push(`${full} : grammaire inconnue ${g}`);
    }
  }

  const reachable = new Set([...ids, ...knownIds]);
  for (const { unit, comp } of allComps(spec)) {
    for (const p of comp.prereqs) {
      if (!reachable.has(p)) {
        problems.push(`${spec.level}.${unit}.${comp.id} : prérequis inexistant ${p}`);
      }
    }
  }

  for (const g of spec.grammar) {
    if (!gramUsed.has(g)) problems.push(`grammaire jamais utilisée : ${g}`);
  }

  for (const [unit, d] of Object.entries(spec.units)) {
    const receptive = d.comps.some((c) => c.modes.includes('RO') || c.modes.includes('RE'));
    if (!receptive) {
      problems.push(`${unit} : aucune compétence réceptive (condition 4 de maîtrise inatteignable)`);
    }
  }

  for (const ce of spec.coreErrors) {
    const n = errUsed.get(ce) ?? 0;
    if (n < 2) problems.push(`erreur noyau ${ce} surveillée sur ${n} compétence(s) seulement`);
  }
  for (const code of errUsed.keys()) {
    if (!(code in spec.errorDefs)) problems.push(`erreur sans définition : ${code}`);
  }
  for (const code of Object.keys(spec.errorDefs)) {
    if (!errUsed.has(code) && !spec.pronunciationErrors.includes(code)) {
      problems.push(`erreur définie mais rattachée à aucune compétence : ${code}`);
    }
  }

  for (const extra of spec.extraChecks ?? []) problems.push(...extra(spec, { errUsed, ids }));

  return { problems, ids, modes, gramUsed, errUsed, perUnit };
}

/** Extracts competency ids from an already-loaded curriculum YAML. */
export function idsOf(curriculum) {
  return new Set(
    Object.values(curriculum.units).flatMap((u) => u.competencies.map((c) => c.id)),
  );
}
