# Lingo

Un professeur d'anglais pour apprenants francophones, sous forme de skill Claude.

Lingo n'est pas un partenaire de conversation en anglais. C'est un système pédagogique qui utilise Claude comme professeur : il enseigne une notion, la fait pratiquer, vérifie qu'elle est acquise par des preuves comptables, corrige les erreurs avec reprise, et y revient en révision espacée jusqu'à ce que la compétence tienne.

**Le test auquel toute la conception se soumet :**

> À chaque session, l'apprenant doit produire correctement, sans modèle affiché, au moins une chose qu'il ne savait pas produire au début — et cette production doit être enregistrée comme preuve datée.

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

---

## Installer

### Le plus court

```bash
npx lingo-english-tutor install     # Claude Code
npx lingo-english-tutor zip         # app Claude et Cowork : produit le ZIP à importer
```

`install` copie le skill dans `~/.claude/skills/lingo-english-tutor/` ; `--project` l'installe dans `.claude/skills/` pour le versionner avec un dépôt, `--dir` choisit la destination, `--dry-run` montre ce qui serait écrit sans rien écrire. Un fichier déjà présent que le paquet ne fournit pas n'est jamais supprimé : il est signalé, c'est tout.

Le paquet n'a aucune dépendance : `npx` ne télécharge que Lingo.

### Depuis le dépôt cloné

```bash
npm install     # js-yaml, pour l'outillage seulement
npm run zip     # produit dist/lingo-english-tutor.zip
```

- **App Claude (web ou bureau)** — importer le ZIP dans **Customize → Skills**, vérifier qu'il apparaît activé. L'exécution de code doit être activée dans les réglages : les skills en dépendent.
- **Claude Code** — `node bin/lingo.mjs install`, ou copier `skill/*` dans `~/.claude/skills/lingo-english-tutor/` à la main. Pris en compte sans redémarrage, sauf si `~/.claude/skills/` n'existait pas au lancement de la session. Vérifier avec `/skills`.

Puis : « commence mon cours d'anglais ». Sans carte de progression, Lingo lance un placement d'une quinzaine de minutes.

> **Cowork** ne lit pas `~/.claude/skills/`. Il charge les skills activés sur le compte claude.ai — donc il faut passer par l'import du ZIP, même si le dossier est déjà sur le disque, et redémarrer la session pour resynchroniser.

**Mettre à jour** — relancer `npx lingo-english-tutor install`, réimporter le ZIP, ou recopier les fichiers. Après toute modification du curriculum :

```bash
npm run verify     # build les deux niveaux, contrôle le skill, reconstruit le ZIP
npm test           # verrouille l'identité du YAML avec sa source
```

**Si ça coince.** Le ZIP doit contenir `lingo-english-tutor/` à sa racine — `npm run zip` fait le renommage et le vérifie ; ne zippez pas `skill/` tel quel. L'import dans l'app plafonne la `description` à 200 caractères, celle de Lingo en fait 196 ; `npm run check` prévient avant l'import. Si Lingo ne se déclenche pas seul, appelez-le explicitement (`/lingo-english-tutor`) : c'est un problème de `description`, pas d'installation. S'il part en conversation libre ou annonce un pourcentage, c'est un bug d'interdit — signalez-le, c'est le retour terrain que le projet attend.

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

## État

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

## Ce que le premier test terrain a corrigé

Trois retours d'un apprenant réel, trois corrections dans le moteur :

- **L'accueil demandait « envoie ta carte »** à quelqu'un qui n'avait jamais entendu ce mot. Le skill ouvre maintenant par une question simple, et le défaut sans carte est le placement — jamais A1.
- **« Deux sessions différentes » ne voulait pas dire deux jours.** Dix sessions dans un après-midi validaient une maîtrise. La condition se compte désormais en jours civils, et un plafond limite à trois compétences nouvelles par jour.
- **Un apprenant fort ne recevait aucun cours.** Le diagnostic réussi faisait sauter l'enseignement : plus il était bon, moins on lui apprenait. Le moteur monte maintenant d'un cran — le pourquoi de la forme, le développement, la variation, le contraste — au lieu de passer au suivant.

S'y ajoute **la règle du +1**, qui traverse tout A2 : une production correcte mais minimale compte en production guidée, jamais en production libre. C'est ce qui empêche de valider un niveau en produisant des phrases justes du niveau inférieur.

**La suite n'est pas de la conception.** C'est de continuer à faire tourner le skill avec de vrais apprenants francophones et de regarder où il dérive.
