#!/usr/bin/env python3
"""Empaquette skill/ en dist/lingo-english-tutor.zip, prêt à importer dans l'app Claude.

Le ZIP doit contenir le dossier du skill à sa racine, et ce dossier doit porter le nom
déclaré dans le frontmatter — pas 'skill'. C'est pourquoi le dossier est renommé ici
plutôt que dans le dépôt : garder 'skill/' en local évite de confondre le dossier source
avec le paquet installable.

Usage :  python3 tools/package.py
"""
import os, re, sys, zipfile, yaml

SRC, DIST = "skill", "dist"

raw = open(f"{SRC}/SKILL.md", encoding="utf-8").read()
m = re.match(r"^---\n(.*?)\n---\n", raw, re.S)
if not m:
    sys.exit("SKILL.md : frontmatter absent")
name = yaml.safe_load(m.group(1))["name"]

os.makedirs(DIST, exist_ok=True)
out = f"{DIST}/{name}.zip"

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir(SRC)):
        path = os.path.join(SRC, f)
        if os.path.isfile(path):
            z.write(path, arcname=f"{name}/{f}")          # <- dossier nommé à la racine

with zipfile.ZipFile(out) as z:
    entries = z.namelist()

print(f"{out}  ({os.path.getsize(out) / 1024:.0f} Ko)")
for e in entries:
    print("   ", e)

roots = {e.split("/")[0] for e in entries}
if roots != {name}:
    sys.exit(f"ERREUR : racine du ZIP = {roots}, attendu {{{name}}}")
if f"{name}/SKILL.md" not in entries:
    sys.exit("ERREUR : SKILL.md absent de la racine du dossier")
print("\nStructure conforme.")
