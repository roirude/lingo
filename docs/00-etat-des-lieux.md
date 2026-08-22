# Lingo — État des lieux et analyse critique

*Analyse du document de conception issu de la conversation ChatGPT — 21 août 2026*

---

## Verdict en une phrase

Vous avez **une pédagogie juste, un curriculum vide, aucun runtime spécifié, et un problème de persistance non résolu**.

Le document §1–29 est un manifeste, pas une spécification. Tout y est au niveau « ce qui doit se passer » ; rien n'est au niveau « ce qui est écrit dans quel fichier, et ce que fait le modèle à l'exécution ». L'écart entre les deux est plus grand qu'il n'y paraît, et ce n'est pas un écart de volume de contenu — c'est un écart d'architecture.

---

## 1. Ce qui est solide (à garder tel quel)

**Le diagnostic de l'échec v1 (§3, §25, §26).** Vous avez identifié correctement, et sans qu'on vous le dise, la façon dont la quasi-totalité des tuteurs de langue basés sur l'IA échouent : ils font *produire* ce que l'apprenant sait déjà et appellent ça un cours. C'est le point le plus précieux du document.

**La boucle pédagogique (§4, §14).** Découverte → explication → pratique contrôlée → production guidée → production libre → feedback → révision. C'est du PPP / ESA classique. Ce n'est pas original, et c'est bien : c'est éprouvé.

**La matrice thème × grammaire × fonction (§6).** L'intuition est exactement celle des vraies méthodes de langue (le *syllabus grid*). Refuser des piliers séparés est le bon réflexe. À garder comme structure de données centrale.

**L'exigence de preuves multiples (§21).** Une bonne réponse ne vaut pas maîtrise. Correct, et rarement respecté.

**La boucle erreur → correction → explication → retry → production réussie (§14).** C'est le mécanisme à plus forte valeur du document, et c'est précisément ce qu'un LLM sait très bien faire. Il doit devenir le cœur du runtime, pas un module parmi seize.

---

## 2. Les cinq problèmes bloquants

### P1 — La persistance. Bloquant n°1.

Le §19 suppose que l'apprenant dit « continue mon parcours » et que le skill sait tout : niveau, acquis, erreurs récurrentes, révisions dues.

Or, un skill Claude est un dossier d'instructions **en lecture seule**. La documentation Anthropic est explicite : *« Skills cannot write or persist state between sessions »* — pas de base, pas de stockage, rien ne survit d'une session à l'autre. Côté ChatGPT, les fichiers de connaissance d'un GPT sont eux aussi en lecture seule (20 fichiers max), et leur récupération est **sémantique par extraits** : vous ne pouvez pas demander de façon déterministe « donne-moi la fiche A1.1.03 ». La mémoire Claude existe mais est organisée par projet, non structurée, et absente de certains environnements.

Autrement dit : **le « Learner Progress Model » du §23 n'a aujourd'hui nulle part où vivre.**

Trois options réalistes :

| Option | Fonctionnement | Coût | Limite |
|---|---|---|---|
| **(a) Fiche portée par l'apprenant** | En fin de session, Lingo émet un bloc d'état (JSON/markdown) que l'apprenant recolle ou téléverse au début de la suivante | Zéro infra, marche sur les deux plateformes | Dépend de la discipline de l'utilisateur |
| **(b) Projet Claude + fichier de progression** | Le fichier vit dans un Projet ; Claude le relit à chaque session | Faible | L'écriture reste manuelle ; pas d'équivalent propre côté GPT |
| **(c) Backend minimal + Action GPT / MCP côté Claude** | Une petite API et une base, une clé par apprenant | ~200 lignes + hébergement | La seule solution réellement adaptative |

**Recommandation :** concevez le **schéma d'état une seule fois** (le même JSON), et branchez-le sur (a) en v1, (c) en v2. Le format ne change pas ; seul le transport change. Mais il faut trancher **maintenant**, parce que la première instruction du Lesson Engine est « retrieve learner profile ».

### P2 — 720 leçons rédigées est une impasse

120 thèmes × 6 niveaux, chacun avec vocabulaire, grammaire, exercices, évaluations : c'est plusieurs années-homme d'édition, et ça ne tient de toute façon pas dans un skill.

La sortie n'est pas de réduire le nombre de thèmes. Elle est de **ne pas rédiger le contenu, mais les contraintes**. Séparez :

**À écrire à la main et à figer** — ce que le modèle ne peut pas improviser de façon cohérente d'une session à l'autre :

- l'inventaire des compétences par niveau, avec identifiants stables
- l'ordre de progression grammaticale
- la matrice thème × grammaire × fonction
- les rubriques de maîtrise
- la taxonomie d'erreurs et la table de remédiation
- l'algorithme de session

**À générer à l'exécution** — ce que le modèle fait bien, et où la variation est un *atout* (indispensable pour la répétition espacée : on ne revoit pas deux fois le même item) :

- les phrases d'exemple
- les items à trous, QCM, transformations
- les consignes et les amorces
- les tours de conversation
- la formulation du feedback

Cela fait passer le chantier de « impossible » à « quelques semaines de travail sérieux ». Le vrai corpus n'est pas 720 leçons : c'est **80 à 120 descripteurs de compétence pour A1**, plus six fichiers système.

**Corollaire :** ne construisez pas six niveaux. Construisez **A1 de bout en bout**, testez sur de vrais apprenants, puis étendez. A2 conçu après un vrai A1 testé vaudra dix fois C2 conçu sur papier.

### P3 — Les pourcentages d'évaluation sont faux

`Pronunciation: 74%`, `Fluency: 68%` (§16, §22) : le modèle ne mesure rien. Il produit un nombre plausible. Deux raisons concrètes :

1. **En mode vocal, le skill ne voit pas l'audio — il voit une transcription.** Et la reconnaissance vocale *corrige silencieusement* les erreurs de l'apprenant (« he work » devient « he works ») et supprime hésitations, répétitions et pauses. C'est-à-dire **exactement les preuves dont votre §16 a besoin**.
2. Aucun scoring phonémique n'est exposé par les deux plateformes.

**Correctif :** passez d'une évaluation en pourcentages à une évaluation **par preuves comptables**.

> Structure cible produite correctement 3/4 tentatives, dont 2/4 sans amorce.
> Erreur « omission du -s » : 1 occurrence sur 6 contextes obligatoires (était 4/6 en session 2).
> Question formée spontanément : 1 fois.

C'est vérifiable, reproductible entre sessions, lisible par l'apprenant — et ça satisfait **rigoureusement** l'exigence de preuves multiples du §21, que les pourcentages ne satisfaisaient qu'en apparence.

Et sortez explicitement la prononciation du périmètre v1, plutôt que de la simuler.

### P4 — La leçon à 16 étapes ne tient pas dans une session

Une vraie session d'apprentissage utile fait 10 à 20 minutes. Seize phases épuisent l'apprenant et saturent la fenêtre de contexte bien avant l'évaluation.

Il faut des **types de session** de formes différentes, avec un budget explicite (nombre d'items, durée cible) :

| Type | Contenu | Durée |
|---|---|---|
| **Nouvelle notion** | Diagnostic court → enseignement → pratique contrôlée → production guidée | 15 min |
| **Entraînement** | Reprise de la notion de la veille → production libre → feedback → retry | 10 min |
| **Révision** | Items dus en répétition espacée, mélangés | 5–8 min |
| **Évaluation** | Compétences en statut DEVELOPING, sans aide | 10 min |

Le Lesson Engine choisit le type avant de choisir le contenu.

### P5 — Le vocal change la forme de la leçon, pas seulement le canal

Le §17 a raison sur le principe (ne pas construire sa propre couche vocale), mais sous-estime la contrainte. En voix : pas de texte à trous affiché, pas de tableau, pas de production écrite, et l'apprenant ne peut pas relire ce qui vient d'être dit.

Une session vocale a besoin de sa propre conception — répétition orale, transformation à l'oral, dictée inverse, reformulation — pas d'une leçon texte lue à voix haute. C'est une **branche de conception**, à traiter comme telle.

---

## 3. Ce qui manque totalement au document

**1. Le test de placement initial.** Le §9 traite le diagnostic *à l'intérieur* d'une leçon, mais rien ne décide A1 ou B1 au premier contact. C'est pourtant la toute première chose que rencontre un apprenant.

**2. La prédiction d'erreurs liées à la langue maternelle.** Votre public est francophone. Les francophones font des erreurs **prévisibles** :

- `I have 25 years` (au lieu de *I am 25*)
- `he work` — omission du -s à la 3ᵉ personne
- `I am agree` (au lieu de *I agree*)
- confusion *since* / *for*
- `informations`, `advices` — pluriels d'indénombrables
- faux amis : *actually*, *sensible*, *library*, *eventually*, *assist*
- `I go to home`, `Do you can...?`
- finales `-ed` non prononcées, /h/ muet, /θ/ réalisé en /s/ ou /z/

Un tuteur qui **anticipe** ces erreurs — qui les enseigne avant qu'elles apparaissent, et les surveille spécifiquement — est nettement supérieur à un tuteur générique. C'est votre vrai différenciateur, et il coûte un fichier de soixante lignes.

**3. La langue d'instruction.** Pour un vrai débutant A1 francophone, une explication grammaticale en anglais est inutilisable. Il faut une politique explicite : français en A1, réduction progressive en A2, anglais seul à partir de B1. Rien dans le document ne l'aborde.

**4. Ce qui fait revenir l'apprenant demain.** La répétition espacée du §15 suppose qu'il revient à J+2, J+4, J+7, J+14, J+30. Rien dans la conception ne le provoque. Sans mécanique d'engagement, le modèle de mémoire reste théorique.

**5. Les règles anti-dérive.** Le modèle retombera naturellement dans le rôle de chatbot sympathique — c'est son comportement par défaut, et c'est **exactement l'échec de la v1**. Le skill a besoin d'interdictions explicites et vérifiables :

> Ne jamais ouvrir la phase de conversation libre avant que la structure cible ait été produite correctement deux fois en pratique contrôlée.
> Ne jamais poser une question dont la réponse n'exige pas la notion du jour.
> Ne jamais enchaîner plus de deux tours sans feedback correctif.

**6. Le critère de passage de niveau.** Le §20 pose les six niveaux, mais rien ne dit à quelle condition on passe de A1 à A2.

---

## 4. Contraintes techniques à connaître avant de concevoir

| Contrainte | Conséquence pour Lingo |
|---|---|
| Un skill ne persiste aucun état entre sessions | Le suivi de progression doit être porté par un fichier ou un backend (P1) |
| `SKILL.md` : garder sous ~500 lignes | Le curriculum va dans des fichiers de référence, pas dans le skill principal |
| `description` du skill : 1 024 caractères max | C'est elle qui décide du déclenchement — à rédiger avec soin |
| Divulgation progressive, **un seul niveau de profondeur** | `SKILL.md` doit pointer directement vers chaque fichier ; pas de références en cascade |
| Fichiers de référence > 100 lignes : prévoir un sommaire | Le modèle peut ne lire qu'une partie du fichier |
| Les scripts s'exécutent sans être chargés en contexte | Utilisable pour la logique de sélection et de planification des révisions |
| GPT : 20 fichiers de connaissance, récupération sémantique par extraits | Pas d'accès déterministe à une fiche précise ; prévoir des Actions pour la version ChatGPT |
| Mémoire Claude : par projet, non structurée, indisponible dans certains environnements | Ne pas fonder le modèle de progression dessus |

---

## 5. Ordre de travail proposé

**0. Trancher le modèle d'état** — 30 minutes de décision, mais tout en dépend.

**1. Schéma de compétence + inventaire A1** — identifiants stables, descripteurs observables, ~80–120 entrées. C'est le squelette de tout le système.

**2. Rubrique de maîtrise en preuves comptables** — remplace les pourcentages. Définit MASTERED / DEVELOPING / NOT MASTERED / NEEDS REMEDIATION en critères vérifiables.

**3. Lesson Engine en pseudo-code** — pas en prose. Plus les quatre types de session et leur budget.

**4. Taxonomie d'erreurs francophone + table de remédiation** — votre différenciateur.

**5. Règles anti-dérive + politique de langue d'instruction.**

**6. `SKILL.md` A1 + fichiers de référence**, puis test sur trois apprenants réels avant d'écrire quoi que ce soit pour A2.

**7. Portage ChatGPT** — en dernier, pas en parallèle.

Le §28 avait raison de viser le Lesson Engine comme prochaine étape, mais il ne peut pas être spécifié avant l'étape 0 : sa toute première instruction est « retrieve learner profile ».

---

## 6. Le principe du §29, reformulé en contrainte d'ingénierie

> Lingo ne doit pas seulement faire parler l'apprenant anglais. Il doit lui apprendre l'anglais.

Traduit en règle exécutable :

**À chaque session, l'apprenant doit produire correctement, sans modèle affiché, au moins une chose qu'il ne savait pas produire au début de la session — et cette production doit être enregistrée comme preuve datée dans son profil.**

Si une session ne peut pas produire cette preuve, elle a échoué, quelle que soit la qualité de la conversation. C'est le test unique auquel toute la conception doit se soumettre.

---

## Sources

- [Skill authoring best practices — Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Equipping agents for the real world with Agent Skills — Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Use Claude's chat search and memory — Anthropic Help Center](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- [Knowledge in GPTs — OpenAI Help Center](https://help.openai.com/en/articles/8843948-knowledge-in-gpts)
