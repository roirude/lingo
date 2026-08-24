# Lingo

Un professeur d'anglais pour apprenants francophones, sous forme de skill Claude.

Lingo n'est pas un partenaire de conversation en anglais. C'est un système pédagogique qui utilise Claude comme professeur : il enseigne une notion, la fait pratiquer, vérifie qu'elle est acquise par des preuves comptables, corrige les erreurs avec reprise, et y revient en révision espacée jusqu'à ce que la compétence tienne.

**Le test auquel toute la conception se soumet :**

> À chaque session, l'apprenant doit produire correctement, sans modèle affiché, au moins une chose qu'il ne savait pas produire au début — et cette production doit être enregistrée comme preuve datée.

---

## Installer

**Vous voulez juste utiliser Lingo ?** Repérez votre outil ci-dessous.
**Vous voulez modifier le skill ou contribuer au projet ?** Passez directement à [Pour un contributeur](#pour-un-contributeur).

### Claude Code

```bash
npx lingo-english-tutor install
```

Copie le skill dans `~/.claude/skills/lingo-english-tutor/`. Vérifiez avec `/skills` qu'il apparaît. Options : `--project` (installe dans `.claude/skills/` du projet plutôt que dans votre dossier personnel), `--dir <chemin>` (destination choisie), `--dry-run` (montre ce qui serait écrit, sans rien écrire). Un fichier déjà présent que le paquet ne fournit pas n'est jamais supprimé, seulement signalé.

**Si `npx` ne fonctionne pas** (pas de Node.js, réseau restreint, etc.), copiez le dossier `skill/` directement :

```bash
git clone https://github.com/roirude/lingo.git
mkdir -p ~/.claude/skills/lingo-english-tutor
cp lingo/skill/* ~/.claude/skills/lingo-english-tutor/
```

### App Claude (web ou bureau) et Cowork

```bash
npx lingo-english-tutor zip
```

Produit `lingo-english-tutor.zip` dans le dossier courant. Pour l'importer :

1. Ouvrez **Settings** (réglages du compte, pas les réglages de la conversation).
2. Allez dans l'onglet **Skills**.
3. Cliquez sur **Add skill** (ou **+**, selon la version), puis **Import skill**.
4. Sélectionnez `lingo-english-tutor.zip`.
5. Vérifiez que Lingo apparaît **activé** dans la liste.

L'exécution de code doit être activée dans les réglages : les skills en dépendent.

> **Cowork** ne lit pas `~/.claude/skills/` — même si le skill est déjà installé pour Claude Code, il faut quand même passer par l'import du ZIP ci-dessus (compte claude.ai), puis redémarrer la session pour resynchroniser.

### Ensuite, dans les deux cas

Dites : « commence mon cours d'anglais ». Sans carte de progression, Lingo lance un placement d'une quinzaine de minutes.

Le paquet `lingo-english-tutor` n'a aucune dépendance : `npx` ne télécharge rien d'autre que lui.

**Mettre à jour** — relancez la même commande (`install` ou `zip`), ou réimportez le ZIP dans l'app.

### Pour un contributeur

Cloner le dépôt plutôt que d'utiliser `npx` :

```bash
npm install          # installe js-yaml, seule dépendance — de l'outillage, pas du skill
npm run verify        # régénère les deux curriculums, contrôle le skill, reconstruit le ZIP
npm test               # vérifie que le YAML commité correspond bien à sa source
```

Puis installez comme un utilisateur, mais depuis le dépôt local plutôt que depuis npm : `node bin/lingo.mjs install` (Claude Code), ou `node bin/lingo.mjs zip` (app / Cowork). Après toute modification du curriculum, relancez `npm run verify` et `npm test` avant de committer.

### En cas de problème

- **Le ZIP est refusé à l'import.** Il doit contenir `lingo-english-tutor/` à sa racine — c'est ce que produit `npx lingo-english-tutor zip` ou `npm run zip`. Si vous avez zippé `skill/` vous-même, c'est le nom du dossier qui coince.
- **La `description` est refusée à l'import.** L'app plafonne à 200 caractères ; celle de Lingo en fait 196. Si vous l'avez modifiée dans `skill/SKILL.md`, `npm run check` vous préviendra avant de réempaqueter.
- **Lingo ne se déclenche pas tout seul.** Appelez-le explicitement : `/lingo-english-tutor`. C'est un problème de `description` (Claude ne comprend pas quand le déclencher), pas un problème d'installation.
- **Lingo part en conversation libre, ou annonce un pourcentage/une note.** C'est un bug, pas un comportement voulu — signalez-le, c'est le retour terrain que le projet attend.

---

## Arborescence

```
lingo/
├── skill/                    ← ce qui est chargé à l'exécution
│   ├── SKILL.md              point d'entrée — toujours lu, sous 500 lignes
│   ├── curriculum-a1.yaml    98 compétences, 55 points de grammaire, 55 erreurs
│   ├── curriculum-a2.yaml    99 compétences, 58 points de grammaire, 47 erreurs
│   ├── grammar-a1.md         14 fiches — lues une à une, à la demande
│   ├── grammar-a2.md         12 fiches, dont A01 « la règle du +1 »
│   └── placement.md          lu seulement au premier contact
│
├── docs/                     ← conception et raisonnement — jamais chargés à l'exécution
│   ├── 00-etat-des-lieux.md  analyse initiale, contraintes techniques, arbitrages
│   ├── 01-modele-etat.md     carte de progression, statuts, seuils de maîtrise
│   ├── 02-competences-A1.md  inventaire lisible + matrice thème × grammaire × fonction
│   ├── 03-grammaire-A1.md    fiches + critère de sélection des 14 points
│   ├── 04-lesson-engine.md   algorithme de session, phases, interdits, exemple tracé
│   └── 06-placement.md       escalier adaptatif, production de la carte initiale
│
├── bin/
│   └── lingo.mjs             ← CLI publiée sur npm : `install`, `zip`
│
├── src/                      ← partagé entre la CLI publiée et l'outillage
│   ├── skill.mjs             emplacement du skill, frontmatter, entrées d'archive
│   └── zip.mjs               écriture et relecture d'archives ZIP, sans dépendance
│
├── tools/                    ← outillage du dépôt, jamais publié sur npm
│   ├── data/a1.mjs           source de vérité du curriculum A1
│   ├── data/a2.mjs           idem A2, prérequis vers A1 vérifiés
│   ├── lib/curriculum.mjs    émission YAML et validation, communes aux deux niveaux
│   ├── lib/pyrepr.mjs        règles de citation héritées du générateur d'origine
│   ├── build.mjs             régénère un curriculum et le valide
│   ├── check-align.mjs       vérifie que docs/ et le YAML ne divergent pas
│   ├── check-skill.mjs       contrôle les contraintes d'un skill Claude
│   └── package.mjs           produit le ZIP installable
│
├── test/                     ← node --test : identité du YAML, validations, ZIP
│
├── dist/                     ← paquet installable, régénérable
│   └── lingo-english-tutor.zip
│
├── package.json
└── README.md
```

Le dossier source s'appelle `skill/` mais le skill s'appelle `lingo-english-tutor` : `tools/package.mjs` fait le renommage au moment d'empaqueter. C'est voulu — garder `skill/` en local évite de confondre le dossier source avec le paquet installable.

### La séparation `skill/` vs `docs/`

`skill/` contient des **instructions** : impératives, denses, écrites pour être exécutées.
`docs/` contient le **raisonnement** : pourquoi chaque règle existe, quels arbitrages ont été faits, ce qui a été écarté.

Cette séparation n'est pas cosmétique. Un fichier de conception chargé à l'exécution dilue les instructions dans de l'argumentation, et le modèle suit moins bien. Ne déplacez rien de `docs/` vers `skill/`.

### État

| Pièce | État |
|---|---|
| Modèle d'état et carte de progression | fait |
| Inventaire A1 — 98 compétences | fait |
| Inventaire A2 — 99 compétences | fait |
| Fiches de grammaire — 14 points A1, 12 points A2 | fait |
| Moteur de leçon | fait |
| Test de placement — 11 échelons, A1 et A2 | fait |
| Assemblage du skill | fait |
| **Test sur de vrais apprenants** | **en cours** |
| Portage ChatGPT | à faire |
| Niveaux B1 à C2 | à faire |

A1 et A2 existent. Le placement sait dire à un apprenant que son niveau dépasse ce que Lingo enseigne — c'est la seule réponse honnête, et elle vaut mieux qu'un curriculum B1 improvisé.

---

## Comment ça marche

Un skill Claude **ne peut ni écrire ni conserver d'état entre les sessions**. La progression est donc portée par l'apprenant : à la fin de chaque session, Lingo émet une carte texte d'environ 700 octets que l'apprenant conserve et recolle au début de la suivante.

```
Fin de session       Lingo émet la CARTE        l'apprenant l'enregistre
                              ↓
                     (entre les sessions)
                              ↓
Début de session     l'apprenant la colle       Lingo reconstruit l'état
```

Trois règles rendent le modèle viable, et elles sont dans `SKILL.md` :

1. La carte est réémise à la fin de **chaque** session, même écourtée.
2. Lingo ne prétend jamais se souvenir de ce qui n'y figure pas.
3. Sans carte au démarrage, il lance un placement plutôt que de deviner.

Le jour où un backend remplace la carte, **rien de la conception ne change** — seul le transport change. Les statuts, les seuils et les compteurs restent identiques.

---

## Deux principes qui distinguent Lingo

**Les preuves remplacent les pourcentages.** `Pronunciation: 74 %` est un nombre inventé : le modèle ne mesure rien. Lingo compte des occurrences sur des dénominateurs réels — *structure cible correcte 3 fois sur 4, dont 2 sans amorce* ; *omission du -s : 1 contexte obligatoire sur 6, contre 4 sur 6 en session 2*. Vérifiable, comparable d'une session à l'autre, lisible par l'apprenant.

**Les erreurs francophones sont anticipées, pas détectées après coup.** *I have 25 years*, *he work*, *Where you live?*, *I am agree*, *his sister* pour la sœur d'une femme : ces erreurs sont prévisibles à 90 % chez un francophone. Le curriculum les nomme avant qu'elles soient commises, les surveille sur des contextes comptés, et bloque le passage en A2 tant que les quatre erreurs du noyau dépassent 20 % de leurs contextes.

---

## Modifier le curriculum

`skill/curriculum-a1.yaml` est **généré** — ne l'éditez pas à la main. La source de vérité est `tools/data/a1.mjs`.

```bash
node tools/build.mjs a1     # régénère le YAML et valide la cohérence
node tools/check-align.mjs  # vérifie l'alignement avec docs/02-competences-A1.md
npm run build               # les deux niveaux d'un coup
```

La validation contrôle : unicité des identifiants, prérequis existants, aucune compétence sans grammaire ni mode, aucun point de grammaire orphelin, présence d'une compétence réceptive dans chaque unité, et surveillance de chaque erreur du noyau sur au moins deux compétences. A2 vérifie en plus que ses prérequis vers A1 existent, et que l'exigence d'élaboration est surveillée hors de l'unité qui l'enseigne.

Ces contrôles ne sont pas décoratifs : la première passe de l'inventaire contenait dix incohérences réelles, dont trois unités sans compétence réceptive — ce qui rendait la condition 4 de la règle de maîtrise littéralement inatteignable dans ces unités.

---
