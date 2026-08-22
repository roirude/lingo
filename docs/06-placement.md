# Lingo — Test de placement (v1)

*La porte d'entrée. 15 minutes, 30 tours, aucune note.*

Dépend de : `lingo-01-modele-etat.md` · `lingo-02-competences-A1.md` · `lingo-04-lesson-engine.md`

---

## 1. Ce que le placement cherche — et ce qu'il ne cherche pas

Il ne cherche **pas** un niveau. « Vous êtes A2 » n'est pas une information exploitable par le moteur : le moteur a besoin d'un `next_objective` et d'une carte, pas d'une étiquette.

Il cherche **la frontière** : la ligne entre ce que l'apprenant produit de façon fiable et ce qu'il ne produit pas. Le niveau CECR se déduit de la frontière ; il n'est jamais l'objectif de la mesure.

### La frontière n'est pas la même selon la compétence

C'est le point qui décide de la qualité du placement pour un public francophone. Un francophone scolarisé a presque toujours une **réception très en avance sur sa production** : il comprend des séries en anglais, lit de la documentation technique, et ne peut pas produire trois phrases correctes au passé. Deux à trois niveaux d'écart sont courants.

Conséquence directe :

> **On place sur la production. Jamais sur la réception, jamais sur la moyenne des deux.**

Placer sur la réception envoie l'apprenant dans des leçons qu'il ne peut pas suivre, il échoue, il abandonne. Placer sur la production l'envoie exactement là où il a quelque chose à gagner. La réception est mesurée quand même — mais elle sert à choisir la **difficulté des supports d'entrée**, pas le point de départ du curriculum.

### Ce que le placement doit pouvoir dire

Trois issues, dont la troisième est celle qu'on oublie de prévoir :

1. **Pré-A1** — commencer à `A1.U00.C01`.
2. **A1 partiel** — commencer à la frontière, avec une carte pré-remplie.
3. **Au-dessus de A1** — *« Ton niveau dépasse ce que Lingo sait enseigner aujourd'hui. »*

La troisième issue n'est pas un échec du produit : c'est la seule réponse honnête tant que seul A1 existe. Un placement incapable de la formuler renverra un apprenant B1 vers des leçons sur *I'm from Cameroon*, et il ne reviendra pas.

---

## 2. Structure — 5 phases, 27 tours typiques

| Phase | Objet | Tours |
|---|---|---|
| A — Amorce | fixer le point de départ des sondes | 3 |
| B — Sonde de production | trouver la frontière | 14 |
| C — Sonde des erreurs noyau | établir le plan de remédiation | 4 |
| D — Sonde réceptive | mesurer l'écart réception/production | 3 |
| E — Restitution | dire ce qui a été observé, émettre la carte | 3 |

**Aucun feedback pendant les phases B, C et D.** Même règle que pour une session `ÉVALUATION` du moteur : corriger en cours de route contamine les sondes suivantes — l'apprenant réutilise la forme qu'on vient de lui donner, et la mesure ne mesure plus rien. Tout le retour est donné en phase E.

---

## 3. Phase A — Amorce · 3 tours

Deux fonctions : cadrer, et éviter de faire perdre dix tours à tout le monde.

**Cadrer.** Le mot « test » n'apparaît jamais.

> Dix minutes pour que je sache d'où partir. Il n'y a rien à réussir — si tu ne sais pas, dis-le, c'est une information utile.

**Fixer le point d'entrée des sondes.** Trois questions fermées, en français, non notées :

1. As-tu déjà appris l'anglais ? (jamais / à l'école il y a longtemps / récemment)
2. Peux-tu tenir une conversation simple en anglais ? (non / avec difficulté / oui)
3. Écris-tu parfois en anglais ? (jamais / parfois / souvent)

L'auto-évaluation est un mauvais juge de niveau — les apprenants se sous-estiment ou se surestiment de façon systématique — mais c'est un bon **point de départ de recherche**. Elle ne décide de rien ; elle choisit seulement l'échelon d'attaque, ce qui économise 5 à 8 tours.

| Réponses | Échelon d'attaque |
|---|---|
| majorité « jamais / non » | 0 |
| profil intermédiaire | 2 |
| majorité « oui / souvent » | 4 |

---

## 4. Phase B — Sonde de production adaptative · plafond 14 tours

### L'échelle

Neuf échelons. Chacun est une tâche de **production ouverte** — jamais un QCM. Un QCM mesure la reconnaissance, et chez un francophone la reconnaissance est précisément la mesure trompeuse.

| # | Tâche | Compétences visées | Ce que l'échelon discrimine |
|---|---|---|---|
| 0 | *Tell me your name and where you're from.* | `A1.U01.C02`, `A1.U01.C05` | pré-A1 / A1 |
| 1 | *Tell me about your family.* | `A1.U03.C02`, `A1.U03.C05` | have got, possessifs |
| 2 | *What do you do every day?* | `A1.U06.C01` | present simple, 1ʳᵉ personne |
| 3 | *Now tell me about your brother's day — or a friend's.* | `A1.U06.C03` | **le -s de la 3ᵉ personne** |
| 4 | *What did you do last weekend?* | `A1.U12.C02`, `A1.U12.C07` | past simple |
| 5 | *What are you going to do next month?* | `A1.U12.C05` | going to |
| 6 | *Compare life in the city and life in the village.* | au-delà de A1 | comparatifs |
| 7 | *What would you do if you had more free time?* | au-delà de A1 | conditionnel |
| 8 | *Is social media good or bad for young people? Argue.* | au-delà de A1 | argumentation |

**L'échelon 3 est le discriminant central pour ce public.** Beaucoup de francophones franchissent 0, 1 et 2 sans difficulté et butent net sur 3 : ils parlent d'eux-mêmes correctement et perdent la morphologie dès qu'ils parlent de quelqu'un d'autre. C'est précisément la frontière que le curriculum A1 est construit pour traiter — U06 est l'unité pivot pour cette raison.

### La règle d'escalier

```
échelon ← point d'entrée de la phase A
succès_max ← aucun ;  échecs_consécutifs ← 0

répéter jusqu'à convergence ou 14 tours :

    poser la tâche de l'échelon courant
    évaluer : RÉUSSI  = la structure visée est produite correctement
                        au moins deux fois, spontanément
              PARTIEL = produite une fois, ou correcte mais très hésitante
              ÉCHOUÉ  = absente, ou systématiquement fautive

    si RÉUSSI :   succès_max ← échelon ; échecs ← 0 ; échelon ← échelon + 2
    si PARTIEL :  succès_max ← échelon ; échecs ← 0 ; échelon ← échelon + 1
    si ÉCHOUÉ :   échecs ← échecs + 1 ; échelon ← échelon − 1

    convergence si : échecs_consécutifs = 2
                     ou échelon ≤ succès_max
                     ou échelon > 8

frontière ← succès_max
```

Le pas de +2 après un succès net est ce qui fait tenir la sonde en 8 à 12 tours au lieu de 20. Un apprenant qui réussit l'échelon 0 sans hésiter n'a pas besoin qu'on lui demande de parler de sa famille.

### Contrôle de cohérence

Si un échelon élevé réussit alors qu'un échelon inférieur a échoué — succès en 7, échec en 3 — le profil est incohérent. Deux causes : un outil de traduction, ou un échelon inférieur mal formulé qui a été mal compris.

**Ne pas accuser. Re-sonder.** Reposer l'échelon bas avec une tâche différente, sur un autre thème. Si l'incohérence persiste, placer sur l'échelon **bas** et le noter dans la carte : `NOTES: profil incoherent au placement, a reverifier session 2`. Le moteur corrigera de lui-même dès la première session réelle, où la porte de la phase 3 fera son travail.

---

## 5. Phase C — Sonde des erreurs noyau · 4 tours

Indépendante du niveau. Les quatre erreurs du noyau déterminent le plan de remédiation, et elles survivent très haut : un francophone dit encore *I have 25 years* en B1.

Quatre tâches courtes, chacune conçue pour créer le contexte obligatoire sans jamais montrer la forme :

| Tâche | Erreur sondée | Ce qu'on attend |
|---|---|---|
| *How old is your sister?* | `E.FR.AGE-HAVE` | She's 22 — pas *She has 22 years* |
| *Now ask me three questions about my job.* | `E.FR.DO-AUX-OMIT` | Where do you work? — pas *Where you work?* |
| *Describe what your best friend does at the weekend.* | `E.FR.3SG-S` | He plays… — pas *He play…* |
| *Introduce yourself in writing, three sentences.* | `E.FR.BE-OMIT` | I'm a student — pas *I student* |

Chaque tâche alimente le compteur **et son dénominateur** : trois questions posées = 3 contextes obligatoires pour `E.FR.DO-AUX-OMIT`, qu'il y ait erreur ou non. C'est ce dénominateur qui rendra la progression mesurable à partir de la session 2.

**En mode vocal, cette phase est peu fiable** : la transcription corrige silencieusement *he play* en *he plays* et *I student* en *I'm a student*. Si le placement se fait à la voix, la phase C est marquée `non fiable` dans la carte et rejouée à l'écrit lors de la première session. C'est la même contrainte qu'au §10 du moteur, appliquée au placement.

---

## 6. Phase D — Sonde réceptive · 3 tours

Un seul item, calibré **un échelon au-dessus de la frontière**.

Lingo produit un court passage à ce niveau et pose deux questions de compréhension factuelle. Ni note, ni placement : on mesure l'écart.

```
écart ← niveau_réception − frontière_production
```

À quoi il sert :

- `écart ≥ 2` — profil francophone typique. Les supports d'entrée (textes, consignes, questions ouvertes) peuvent être tirés vers le haut sans perdre l'apprenant, et c'est même souhaitable : il s'ennuierait avec des supports calés sur sa production. À signaler à l'apprenant, c'est motivant et c'est vrai.
- `écart ≤ 0` — rare, et c'est le signal d'un apprenant qui produit des formules mémorisées sans les comprendre. Le moteur doit alors renforcer les compétences réceptives avant d'avancer.

---

## 7. Phase E — Restitution et carte · 3 tours

En français. En preuves, jamais en pourcentages.

> Voilà où tu en es. Tu parles de toi sans difficulté — nom, origine, famille, ta journée. Tu bloques dès qu'il s'agit de quelqu'un d'autre : tu as dit *he work*, *my brother get up*, cinq fois sur six occasions. C'est le point de départ.
>
> Tu comprends nettement mieux que tu ne produis, ce qui est normal et plutôt une bonne nouvelle : on pourra travailler sur des supports plus riches que ton niveau de production.
>
> Premier objectif : parler des habitudes de quelqu'un d'autre. Trois sessions devraient suffire.

Puis la carte est émise, avec la consigne de la conserver.

### Règles de production de la carte

Le placement ne peut rien marquer `MASTERED` — cela exigerait les cinq conditions du §4 de `lingo-01`, et une sonde de deux tours n'en fournit aucune. Mais tout marquer `NOT_STARTED` renverrait un apprenant intermédiaire dans quarante sessions de choses qu'il sait déjà.

Trois règles :

| Situation | Statut attribué |
|---|---|
| Compétence produite correctement et spontanément pendant la sonde | `DEVELOPING`, avec `f 1/1` ou `2/2` amorcé, daté |
| Compétence **sous** la frontière, non sondée directement, mais dont tous les prérequis ont été démontrés | `DEVELOPING` avec le drapeau `presumed`, aucun compteur, révision programmée à **J+1** |
| Compétence au-dessus de la frontière | absente de la carte (`NOT_STARTED`) |

Le drapeau `presumed` est la façon honnête de sauter du contenu sans le créditer faussement. Ces compétences n'entrent pas dans la file d'enseignement mais dans la **file de révision**, dès le lendemain. Si la révision réussit, elles progressent normalement. Si elle échoue, elles retombent en `TAUGHT` et sont enseignées. Le coût d'une erreur de placement est ainsi d'un item de révision, pas d'une session entière perdue — dans un sens comme dans l'autre.

> **Amendement à `lingo-01-modele-etat.md`** — ajouter au schéma de compétence le champ booléen `presumed` (défaut `false`), et à la carte compacte le suffixe `~` sur les identifiants présumés :
> `DEVELOPING  A1.U01.C02~ A1.U03.C05~ ...`
> Le drapeau se retire définitivement à la première preuve réelle, réussie ou non.

### Exemple de carte issue d'un placement

```
LINGO-STATE v1
learner: Junior | l1:fr | level:A1 | sessions:1 | last:2026-08-21 | lang:fr
--
DEVELOPING
  A1.U01.C02 f2/2 last:2026-08-21 next:2026-08-24 st:1
  A1.U01.C05 f2/2 last:2026-08-21 next:2026-08-24 st:1
  A1.U03.C02 f1/1 last:2026-08-21 next:2026-08-22 st:0
  A1.U06.C01 f2/2 last:2026-08-21 next:2026-08-24 st:1
  A1.U00.C03~ A1.U01.C01~ A1.U02.C01~ A1.U02.C02~ A1.U03.C01~ A1.U03.C05~
  A1.U05.C01~ A1.U06.C02~ A1.U06.C04~ A1.U07.C01~
TAUGHT
REMEDIATE
--
ERRORS   E.FR.3SG-S 5/6 | E.FR.DO-AUX-OMIT 2/3 | E.FR.AGE-HAVE 0/1 | E.FR.BE-OMIT 0/3
DUE      2026-08-22 (10 items presumes)
NEXT     A1.U06.C03
NOTES    placement 2026-08-21 | frontiere: echelon 2 | ecart reception +2
         | phase C fiable (ecrit)
```

Lecture : la frontière est à l'échelon 2, le premier objectif est `A1.U06.C03` — le `-s` de la troisième personne, échoué 5 fois sur 6 —, dix compétences sont présumées acquises et seront vérifiées dès demain, et `E.FR.BE-OMIT` est à 0 sur 3 contextes, donc sous contrôle.

---

## 8. Exemple tracé

*Apprenant : francophone camerounais, anglais scolaire ancien, lit de la documentation technique en anglais.*

```
A   Phase A — auto-évaluation : « à l'école il y a longtemps » /
    « avec difficulté » / « parfois »  → échelon d'attaque 2

B   Échelon 2 : "What do you do every day?"
    → "I wake up at 6. I take my bath, I go to work. I am a developer.
       I work in a startup in Douala."
    → RÉUSSI (present simple 1re personne, 4 phrases liées, 0 erreur)
    → succès_max 2, échelon ← 4

    Échelon 4 : "What did you do last weekend?"
    → "I go to my village. I visit my mother. It was very nice."
    → ÉCHOUÉ (2 verbes au présent sur 3 ; seul "was" est au passé)
    → échecs 1, échelon ← 3

    Échelon 3 : "Tell me about your brother's day."
    → "He wake up at 5. He work in a bank. He finish at 6."
    → ÉCHOUÉ (0/3 sur le -s)
    → échecs 2 → CONVERGENCE

    frontière = 2

C   "How old is your sister?"        → "She is 22."          ✓  0/1
    "Ask me three questions."         → "Where you work?"
                                         "You like Douala?"
                                         "What is your name?"  → 2/3 ✗
    "Your best friend at the weekend" → "He play football."    → 1/1 ✗
    "Introduce yourself, in writing"  → "I am a developer.
                                         I am from Douala.
                                         I am 28."             ✓  0/3

D   Passage de niveau A2 lu, 2 questions factuelles → 2/2
    → réception ≈ échelon 4-5, production = 2  →  écart +2

E   Restitution, puis carte du §7.
    NEXT = A1.U06.C03
```

Le placement a duré 21 tours. Il a produit un objectif précis, quatre compteurs d'erreurs avec leurs dénominateurs, dix compétences présumées à vérifier, et une information que l'apprenant ne connaissait pas sur lui-même : il comprend deux niveaux au-dessus de ce qu'il produit.

Un test classique aurait rendu « A2 — 58 % ». Ce chiffre n'aurait dit ni par où commencer, ni quoi corriger.

---

## 9. Règles de rejeu

| Situation | Décision |
|---|---|
| Carte perdue | rejouer le placement ; c'est le filet de sécurité de l'option « carte portée » |
| Retour après ≥ 90 jours d'inactivité | rejouer — la frontière a bougé, à la baisse le plus souvent |
| Retour après < 90 jours | ne pas rejouer ; le moteur reprend sur la carte, avec les révisions en retard |
| L'apprenant demande à refaire le test | accepter, mais **fusionner** : conserver les compétences déjà `MASTERED+`, ne recalculer que la frontière |
| Passage A1 → A2 | pas de placement ; c'est l'évaluation de sortie du §6 de `lingo-01` qui fait foi |

---

## 10. Ce que le placement ne fait pas

- **Il ne note pas.** Aucun pourcentage, aucune étiquette CECR affichée comme un résultat. La restitution est en preuves observées.
- **Il n'enseigne pas.** Aucun feedback avant la phase E. La tentation de corriger *he work* au moment où on l'entend est forte, et elle détruit la sonde suivante.
- **Il ne dépasse pas 30 tours.** Au-delà, l'apprenant a l'impression de passer un examen avant d'avoir appris quoi que ce soit, et c'est le meilleur moyen de ne jamais le revoir.
- **Il ne prétend pas mesurer la prononciation.** Hors périmètre v1, comme partout ailleurs dans Lingo.

---

## 11. État du chantier

| Pièce | Fichier | État |
|---|---|---|
| Modèle d'état, statuts, seuils, carte | `lingo-01-modele-etat.md` | fait *(+ amendement `presumed`)* |
| Inventaire A1, grammaire, erreurs FR | `lingo-02-competences-A1.md` + `.yaml` | fait |
| Moteur de leçon | `lingo-04-lesson-engine.md` | fait |
| Test de placement | `lingo-06-placement.md` | **ce fichier** |
| Fiches de grammaire délicates pour francophones | `lingo-03-grammaire-A1.md` | à faire |
| Assemblage `SKILL.md` + fichiers de référence | `SKILL.md` | à faire |
| Test sur 3 apprenants réels | — | à faire |

Le noyau pédagogique est complet : Lingo sait maintenant **où placer un apprenant, quoi lui enseigner, dans quel ordre, sous quelles contraintes, comment vérifier qu'il a appris, et quand y revenir.**

La suite n'est plus de la conception mais de l'assemblage : écrire le `SKILL.md` qui charge ces fichiers en divulgation progressive, et le confronter à de vrais apprenants. C'est là que se découvriront les erreurs que la conception ne peut pas anticiper.
