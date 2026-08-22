#!/usr/bin/env python3
"""Vérifie que skill/ respecte les contraintes d'un skill Claude et reste cohérent
avec le curriculum. À lancer depuis la racine du dépôt."""
import os, re, sys, yaml

SKILL = "skill"
problems, notes = [], []


def check(cond, msg):
    if not cond:
        problems.append(msg)
    return cond


# ---------- frontmatter ----------
raw = open(f"{SKILL}/SKILL.md", encoding="utf-8").read()
m = re.match(r"^---\n(.*?)\n---\n", raw, re.S)
check(m, "SKILL.md : frontmatter YAML absent")
fm = yaml.safe_load(m.group(1)) if m else {}
body = raw[m.end():] if m else raw

name, desc = fm.get("name", ""), fm.get("description", "")
check(bool(name), "frontmatter : 'name' manquant")
check(len(name) <= 64, f"name : {len(name)} caractères (max 64)")
check(re.fullmatch(r"[a-z0-9-]+", name or ""), f"name : '{name}' doit être en minuscules/chiffres/tirets")
check(not re.search(r"anthropic|claude", name or ""), "name : mot réservé (anthropic/claude)")
check(bool(desc), "frontmatter : 'description' manquante")
check(len(desc) <= 200,
      f"description : {len(desc)} caractères — l'import dans l'app Claude plafonne à 200. "
      f"(Claude Code tolère jusqu'à 1536 avec when_to_use, mais on vise la limite la plus stricte "
      f"pour que le même dossier s'installe partout.)")
check("<" not in desc and "<" not in (name or ""), "frontmatter : balise XML interdite")
check(not re.match(r"\s*(Je |I |Tu |You )", desc), "description : doit être à la 3e personne")
check(re.search(r"\b(pour|quand|lorsque|à utiliser|utilis\w*|use when)\b", desc, re.I),
      "description : doit dire QUAND utiliser le skill, pas seulement ce qu'il fait")

# ---------- taille et structure ----------
nlines = body.count("\n") + 1
check(nlines <= 500, f"SKILL.md : {nlines} lignes de corps (recommandé ≤ 500)")
notes.append(f"SKILL.md : {nlines} lignes de corps")

# ---------- fichiers référencés ----------
present = {f for f in os.listdir(SKILL) if f != "SKILL.md"}
referenced = set(re.findall(r"`([a-z0-9-]+\.(?:md|yaml|json|py))`", body)) - {"SKILL.md"}

for f in referenced - present:
    problems.append(f"SKILL.md référence '{f}' qui n'existe pas dans {SKILL}/")
for f in present - referenced:
    problems.append(f"'{f}' présent mais jamais référencé par SKILL.md (jamais chargé)")

# un seul niveau de profondeur : aucun fichier de référence ne doit en référencer un autre
for f in present:
    if not f.endswith(".md"):
        continue
    txt = open(f"{SKILL}/{f}", encoding="utf-8").read()
    for other in re.findall(r"`([a-z0-9-]+\.(?:md|yaml))`", txt):
        if other in present and other != f:
            problems.append(f"{f} référence {other} : références imbriquées interdites "
                            f"(lecture partielle probable)")
    if txt.count("\n") > 100 and not re.search(r"^##+ Sommaire", txt, re.M):
        problems.append(f"{f} : plus de 100 lignes sans sommaire en tête")

# ---------- pas de dossier de conception embarqué ----------
for d in ("docs", "doc"):
    check(not os.path.isdir(f"{SKILL}/{d}"),
          f"{SKILL}/{d}/ : les documents de conception ne doivent pas être dans le skill")

# ---------- cohérence avec le curriculum ----------
cur = yaml.safe_load(open(f"{SKILL}/curriculum-a1.yaml", encoding="utf-8"))
ids = {c["id"] for u in cur["units"].values() for c in u["competencies"]}
gram, errs = set(cur["grammar_inventory"]), set(cur["errors"])
core = set(cur["core_errors"])

for fname in ["SKILL.md", "grammar-a1.md", "placement.md"]:
    txt = open(f"{SKILL}/{fname}", encoding="utf-8").read()
    for bad in sorted(set(re.findall(r"A1\.U\d\d\.C\d\d", txt)) - ids):
        problems.append(f"{fname} : compétence inexistante {bad}")
    for bad in sorted(set(re.findall(r"G\.[A-Z0-9-]+", txt)) - gram):
        problems.append(f"{fname} : point de grammaire inexistant {bad}")
    for bad in sorted(set(re.findall(r"E\.FR\.[A-Z0-9-]+", txt)) - errs):
        problems.append(f"{fname} : code d'erreur inexistant {bad}")

# les 4 erreurs du noyau doivent être nommées dans SKILL.md ET sondées au placement
plc = open(f"{SKILL}/placement.md", encoding="utf-8").read()
for e in sorted(core):
    check(e in body, f"SKILL.md ne nomme pas l'erreur du noyau {e}")
    check(e in plc, f"placement.md ne sonde pas l'erreur du noyau {e}")

# toute fiche annoncée dans SKILL.md doit exister dans grammar-a1.md
gr = open(f"{SKILL}/grammar-a1.md", encoding="utf-8").read()
annonced = set(re.findall(r"\bF(\d\d)\b", body))
actual = set(re.findall(r"^## F(\d\d) ", gr, re.M))
for f in sorted(annonced - actual):
    problems.append(f"SKILL.md annonce la fiche F{f}, absente de grammar-a1.md")
for f in sorted(actual - annonced):
    problems.append(f"grammar-a1.md contient F{f}, non annoncée dans SKILL.md")

notes += [f"fiches de grammaire : {len(actual)}",
          f"compétences : {len(ids)} | grammaire : {len(gram)} | erreurs : {len(errs)}",
          f"fichiers de référence : {len(present)} ({', '.join(sorted(present))})"]

# ---------- rapport ----------
print("=" * 60)
print("VÉRIFICATION DU SKILL")
print("=" * 60)
print(f"name        : {name}")
print(f"description : {len(desc)} caractères")
for n in notes:
    print(f"  {n}")
print()
if problems:
    print(f"PROBLÈMES ({len(problems)}) :")
    for p in problems:
        print("   -", p)
    sys.exit(1)
print("Aucun problème détecté. Le skill est prêt à installer.")
