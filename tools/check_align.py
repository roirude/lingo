import re, yaml, sys
md = open('lingo-02-competences-A1.md').read()
d  = yaml.safe_load(open('lingo-a1-competences.yaml'))
md_ids = set(re.findall(r'A1\.U\d\d\.C\d\d', md))
yl_ids = {c['id'] for u in d['units'].values() for c in u['competencies']}
md_gram = set(re.findall(r'G\.[A-Z0-9-]+', md))
md_err  = set(re.findall(r'E\.FR\.[A-Z0-9-]+', md))
problems = []
for lbl, a, b in [("ID md\\yaml", md_ids, yl_ids), ("ID yaml\\md", yl_ids, md_ids),
                  ("GRAM md\\yaml", md_gram, set(d['grammar_inventory'])),
                  ("GRAM yaml\\md", set(d['grammar_inventory']), md_gram),
                  ("ERR md\\yaml", md_err, set(d['errors'])),
                  ("ERR yaml\\md", set(d['errors']), md_err)]:
    if a - b: problems.append(f"{lbl}: {sorted(a-b)}")
print("Competences md:%d yaml:%d | Grammaire md:%d yaml:%d | Erreurs md:%d yaml:%d"
      % (len(md_ids), len(yl_ids), len(md_gram), len(d['grammar_inventory']), len(md_err), len(d['errors'])))
if problems:
    print("ECARTS:"); [print("  -", p) for p in problems]; sys.exit(1)
print("Markdown et YAML strictement alignes.")
