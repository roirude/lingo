# Installer Lingo

*Vérifié le 21 août 2026. Les menus des applications Claude bougent ; si un libellé ne correspond plus, le principe reste le même — cherchez « Skills » dans les réglages.*

---

## Avant de commencer

| Prérequis | Détail |
|---|---|
| Plan | Free, Pro, Max, Team ou Enterprise |
| Exécution de code | doit être **activée** dans les réglages — les skills en dépendent |
| Team / Enterprise | un administrateur peut avoir restreint les skills personnels |

Le paquet à installer est **`dist/lingo-english-tutor.zip`**, pas la racine du dépôt. S'il n'existe pas encore :

```bash
python3 tools/package.py
```

Le script vérifie au passage que le ZIP a la bonne structure — c'est l'erreur d'installation la plus fréquente (voir [Dépannage](#dépannage)).

---

## Choisir sa méthode

| Vous utilisez… | Méthode | Section |
|---|---|---|
| Claude sur le web ou l'app de bureau | import du ZIP | [A](#a--app-claude-web-ou-bureau) |
| **Cowork** | import du ZIP — **et rien d'autre ne marche** | [A](#a--app-claude-web-ou-bureau) |
| Claude Code | copie du dossier | [B](#b--claude-code) |
| Claude Code **et** Cowork | les deux, indépendamment | A + B |

> **Le piège Cowork.** Une session Cowork **ne lit pas** `~/.claude/skills/` sur votre machine. Elle charge les skills activés sur votre **compte claude.ai**, synchronisés au démarrage de la session. Déposer le dossier sur votre disque ne suffira pas : il faut passer par la méthode A. Même chose pour les tâches planifiées, qui démarrent chacune une session distante neuve.

---

## A — App Claude (web ou bureau)

1. Ouvrir **Customize → Skills** (dans la barre latérale de l'app de bureau, ou dans les réglages sur claude.ai).
2. Importer `dist/lingo-english-tutor.zip`.
3. Vérifier que le skill apparaît **activé** dans la liste.

C'est tout. Le skill est maintenant disponible dans vos conversations, et — s'il est activé sur le compte — dans vos sessions Cowork après un redémarrage de session.

---

## B — Claude Code

Le dossier source s'appelle `skill/` dans le dépôt ; à destination il doit porter le nom du skill.

**Installation personnelle** — disponible dans tous vos projets :

```bash
mkdir -p ~/.claude/skills/lingo-english-tutor
cp skill/* ~/.claude/skills/lingo-english-tutor/
```

**Installation projet** — versionnée avec un dépôt, disponible à toute l'équipe :

```bash
mkdir -p .claude/skills/lingo-english-tutor
cp skill/* .claude/skills/lingo-english-tutor/
```

Claude Code surveille ces dossiers : la modification est prise en compte **sans redémarrer**. Une exception — si le dossier `~/.claude/skills/` n'existait pas du tout au démarrage de la session, redémarrez pour qu'il soit surveillé.

Vérifier :

```
/skills
```

Lingo doit apparaître dans la liste. Vous pouvez l'appeler explicitement avec `/lingo-english-tutor`, ou simplement demander un cours d'anglais et laisser Claude le déclencher.

> Si un skill du même nom existe à la fois en personnel et en projet, **c'est le personnel qui gagne**.

---

## Première session

Dites simplement :

> Commence mon cours d'anglais.

Lingo n'ayant aucune carte de progression, il lancera un **placement** d'une quinzaine de minutes, puis émettra votre première carte.

### La carte — le point à comprendre absolument

Un skill Claude **ne conserve aucun état entre deux sessions**. Toute votre progression tient dans un bloc de texte d'environ 700 octets que Lingo émet à la fin de chaque session :

```
LINGO-STATE v1
learner: Junior | l1:fr | level:A1 | sessions:1 | last:2026-08-21 | lang:fr
--
DEVELOPING
  A1.U01.C02 f2/2 last:2026-08-21 next:2026-08-24 st:1
  ...
--
NEXT     A1.U06.C03
```

**Conservez-la.** Dans un fichier, une note, n'importe où. Au début de chaque session, collez-la — ou joignez le fichier — et Lingo reprend exactement où vous en étiez.

Sans elle, il recommence à zéro : il ne se souvient de rien, et il ne prétendra jamais le contraire.

Un fichier `lingo-etat.txt` dans un dossier synchronisé est la solution la plus simple. Si vous travaillez dans un Projet Claude, y déposer le fichier permet à Lingo de le relire seul.

---

## Mettre à jour

**App** — réimporter le ZIP. La nouvelle version remplace l'ancienne.

**Claude Code** — recopier les fichiers ; la prise en compte est immédiate.

Après toute modification du curriculum, régénérez et vérifiez avant d'empaqueter :

```bash
python3 tools/build_a1.py      # régénère curriculum-a1.yaml + valide
python3 tools/check_skill.py   # contrôle le skill
python3 tools/package.py       # reconstruit le ZIP
```

---

## Désinstaller

**App** — désactiver ou supprimer le skill dans **Customize → Skills**.

**Claude Code** — supprimer le dossier :

```bash
rm -rf ~/.claude/skills/lingo-english-tutor
```

Un skill synchronisé depuis claude.ai se désactive **sur le compte**, pas en supprimant le dossier local : la synchronisation suivante le retéléchargerait.

---

## Dépannage

### « Le ZIP n'a pas la bonne structure »

Le ZIP doit contenir le dossier du skill **à sa racine**, et ce dossier doit porter le nom déclaré dans le frontmatter :

```
lingo-english-tutor.zip
└── lingo-english-tutor/
    ├── SKILL.md
    ├── curriculum-a1.yaml
    ├── grammar-a1.md
    └── placement.md
```

Ne zippez pas le dossier `skill/` tel quel — son nom ne correspond pas. `tools/package.py` fait le renommage et vérifie le résultat.

### La description est refusée à l'import

L'import dans l'app plafonne la description à **200 caractères**. Celle de Lingo en fait 196 — au ras du plafond. Si vous la modifiez, `tools/check_skill.py` vous préviendra avant l'import.

Claude Code est plus permissif : il tolère jusqu'à 1 536 caractères en combinant `description` et le champ optionnel `when_to_use`. Si vous n'installez **que** sur Claude Code, vous pouvez enrichir le déclenchement en ajoutant au frontmatter :

```yaml
when_to_use: >
  Quand l'utilisateur demande un cours ou une leçon d'anglais, dit « commence mon cours »,
  « continue mon parcours », « fais-moi réviser mon anglais », "teach me English",
  "English lesson", ou fournit une carte LINGO-STATE.
```

Ne l'ajoutez pas si vous comptez aussi importer le ZIP dans l'app : ce champ n'y est pas documenté et pourrait être refusé.

### Lingo ne se déclenche pas tout seul

Appelez-le explicitement — `/lingo-english-tutor` en Claude Code, ou « utilise le skill Lingo » dans l'app. S'il fonctionne ainsi, c'est un problème de déclenchement, pas d'installation : la `description` du frontmatter est ce que Claude lit pour décider, et elle seule. Ajoutez-y les formulations que vous employez réellement.

### Le skill marche dans l'app mais pas en Cowork

C'est le piège du haut de page. Cowork ignore `~/.claude/skills/` : le skill doit être **activé sur le compte claude.ai**, et la session doit être redémarrée pour resynchroniser.

### Lingo part en conversation libre

C'est la dérive que le skill est conçu pour empêcher — signalez-la, c'est une information utile. Dites-lui : « relis tes interdits ». S'il y retombe systématiquement à un endroit précis, notez lequel : c'est exactement le retour terrain que le projet attend, et cela se corrige en renforçant la règle concernée dans `SKILL.md`.

### Lingo annonce un pourcentage ou une note de prononciation

Bug. L'interdit n° 15 l'exclut explicitement — il ne mesure ni l'un ni l'autre. Signalez-le de la même façon.

---

## Sources

- [Skill authoring best practices — Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [How to create custom skills — Anthropic Help Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Extend Claude with skills — Claude Code Docs](https://code.claude.com/docs/en/skills)
