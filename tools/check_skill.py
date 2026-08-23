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

# ---------- cohérence avec les curriculums ----------
LEVELS = {}
for lvl in ("a1", "a2"):
    cur = yaml.safe_load(open(f"{SKILL}/curriculum-{lvl}.yaml", encoding="utf-8"))
    LEVELS[lvl] = dict(
        ids={c["id"] for u in cur["units"].values() for c in u["competencies"]},
        gram=set(cur["grammar_inventory"]),
        errs=set(cur["errors"]),
        core=set(cur["core_errors"]),
        units=cur["units"])

all_ids = LEVELS["a1"]["ids"] | LEVELS["a2"]["ids"]
all_gram = LEVELS["a1"]["gram"] | LEVELS["a2"]["gram"]
all_errs = LEVELS["a1"]["errs"] | LEVELS["a2"]["errs"]
all_core = LEVELS["a1"]["core"] | LEVELS["a2"]["core"]

plc = open(f"{SKILL}/placement.md", encoding="utf-8").read()

for fname in ["SKILL.md", "grammar-a1.md", "grammar-a2.md", "placement.md"]:
    txt = open(f"{SKILL}/{fname}", encoding="utf-8").read()
    for bad in sorted(set(re.findall(r"A[12]\.U\d\d\.C\d\d", txt)) - all_ids):
        problems.append(f"{fname} : compétence inexistante {bad}")
    for bad in sorted(set(re.findall(r"G\.[A-Z0-9-]+", txt)) - all_gram):
        problems.append(f"{fname} : point de grammaire inexistant {bad}")
    for bad in sorted(set(re.findall(r"E\.FR\.[A-Z0-9-]+", txt)) - all_errs):
        problems.append(f"{fname} : code d'erreur inexistant {bad}")

# une fiche ne doit citer que la grammaire de son propre niveau
for lvl, fname in (("a1", "grammar-a1.md"), ("a2", "grammar-a2.md")):
    txt = open(f"{SKILL}/{fname}", encoding="utf-8").read()
    for bad in sorted(set(re.findall(r"G\.[A-Z0-9-]+", txt)) - LEVELS[lvl]["gram"]):
        problems.append(f"{fname} : {bad} n'appartient pas au niveau {lvl.upper()}")

# toute erreur du noyau doit être nommée dans SKILL.md ; celles de A1 sondées au placement
for e in sorted(all_core):
    check(e in body, f"SKILL.md ne nomme pas l'erreur du noyau {e}")
for e in sorted(LEVELS["a1"]["core"]):
    check(e in plc, f"placement.md ne sonde pas l'erreur du noyau A1 {e}")

# fiches annoncées dans SKILL.md vs fiches réellement présentes
for pat_body, pat_file, fname in ((r"\bF(\d\d)\b", r"^## F(\d\d) ", "grammar-a1.md"),
                                  (r"\bA(\d\d)\b", r"^## A(\d\d) ", "grammar-a2.md")):
    gr = open(f"{SKILL}/{fname}", encoding="utf-8").read()
    annonced = set(re.findall(pat_body, body))
    actual = set(re.findall(pat_file, gr, re.M))
    for f in sorted(annonced - actual):
        problems.append(f"SKILL.md annonce une fiche absente de {fname} : {f}")
    for f in sorted(actual - annonced):
        problems.append(f"{fname} contient la fiche {f}, non annoncée dans SKILL.md")
    notes.append(f"{fname} : {len(actual)} fiches")

# le plafond du jour et le bilan de module doivent être décrits
check("today" in body, "SKILL.md : le champ 'today' du plafond quotidien n'est pas décrit")
check("BILAN" in body, "SKILL.md : le type de session BILAN n'est pas décrit")
check(re.search(r"jours? civils? distincts?|jours distincts", body),
      "SKILL.md : la condition 3 doit se compter en jours, pas en sessions")
check("+1" in body, "SKILL.md : la règle du +1 n'est pas décrite")

for lvl in ("a1", "a2"):
    notes.append(f"{lvl.upper()} : {len(LEVELS[lvl]['ids'])} compétences | "
                 f"{len(LEVELS[lvl]['gram'])} grammaire | {len(LEVELS[lvl]['errs'])} erreurs")
notes.append(f"fichiers de référence : {len(present)} ({', '.join(sorted(present))})")

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
