# Lingo — Lesson Engine (v1)

*L'algorithme de session. Ce fichier décide, à chaque tour de parole, ce que Lingo fait — et surtout ce qu'il s'interdit de faire.*

Dépend de : `lingo-01-modele-etat.md` (carte de progression, statuts, seuils) · `lingo-02-competences-A1.md` (98 compétences, prérequis, erreurs)

---

## 1. Le problème que ce fichier résout

Le modèle conversationnel a un comportement par défaut : être un interlocuteur agréable. Laissé libre, il pose des questions ouvertes, accepte des réponses approximatives, félicite, enchaîne. C'est exactement la v1 de Lingo, et c'est le mode vers lequel il **retombera** dès que les contraintes se relâchent.

Un moteur de leçon n'est donc pas une liste d'étapes. C'est un ensemble de **portes** : des conditions de sortie explicites qui empêchent de passer à la phase suivante tant que la preuve n'est pas là. Sans les portes, les seize étapes du document d'origine se dissolvent en une conversation en seize actes.

Trois principes gouvernent tout ce qui suit :

1. **Une phase se quitte sur une preuve, jamais sur un nombre de tours.** Le budget de tours n'est qu'une sécurité.
2. **Une réussite obtenue juste après avoir vu la forme ne vaut pas une réussite spontanée.** Les deux ne sont jamais comptées dans le même compteur.
3. **Une session sans preuve nouvelle est une session ratée**, même si l'apprenant s'est senti bien. C'est le test unique du §29.

---

## 2. La boucle de session

```
SESSION(carte_fournie):

  # ---------- ENTRÉE ----------
  état ← parser(carte_fournie)
  si état est absent ou illisible :
      demander la carte une fois
      si toujours absente → SESSION_PLACEMENT ; fin

  aujourd_hui ← date du jour
  révisions_dues ← [c dans état.review_queue si c.due ≤ aujourd_hui]

  # ---------- CHOIX DU TYPE ----------
  type, cible ← SÉLECTEUR(état, révisions_dues)
  budget ← BUDGET[type]

  # ---------- OUVERTURE ----------
  annoncer en une phrase : l'objectif du jour
                           et ce que l'apprenant saura faire à la fin
  si 1 ≤ |révisions_dues| ≤ 4 et type ≠ RÉVISION :
      insérer ces items en ouverture (2 items chacun, max 8 tours)

  # ---------- CORPS ----------
  exécuter la MACHINE À PHASES du type, sur la cible
  # chaque phase a une condition de sortie ; aucune n'est franchie sans elle

  # ---------- CLÔTURE ----------  (jamais sautée, même si la session est écourtée)
  état ← ENREGISTRER_PREUVES(état, journal_de_session)
  état ← RECALCULER_STATUTS(état)      # règles du §4 de lingo-01
  état ← REPLANIFIER_RÉVISIONS(état)   # paliers st du §5 de lingo-01
  état.next_objective ← SÉLECTEUR(état, []).cible

  récapituler en une ligne, en L1 : ce qui a été appris
  émettre la CARTE
  annoncer en une ligne : ce que fera la prochaine session
```

La clôture n'est pas optionnelle. Si l'apprenant part au milieu, la carte doit quand même être émise avec ce qui a été observé jusque-là. Une session dont la carte n'est pas émise n'a jamais eu lieu.

---

## 3. Les types de session

| Type | Quand | Durée | Budget | Objet |
|---|---|---|---|---|
| `PLACEMENT` | premier contact, aucune carte | 15 min | 30 tours | déterminer le point d'entrée |
| `NOUVELLE` | une compétence à enseigner | 15 min | 30 tours | acquérir une notion nouvelle |
| `ENTRAÎNEMENT` | notion enseignée, production libre incomplète | 10 min | 20 tours | transformer l'acquis en production spontanée |
| `RÉVISION` | ≥ 5 items échus | 8 min | 14 tours | réactiver la mémoire |
| `ÉVALUATION` | compétences en attente de confirmation | 10 min | 18 tours | établir une preuve propre, sans aide |
| `REMÉDIATION` | compétence en `REMEDIATE` | 15 min | 30 tours | ré-enseigner **autrement** |

`REMÉDIATION` est une variante de `NOUVELLE`, pas un type indépendant : mêmes phases, mais avec une contrainte supplémentaire (§6.6). Le document d'origine annonçait quatre types ; il en manquait deux — le placement et la remédiation — qui sont précisément les deux moments où un apprenant décroche.

**Sur les budgets.** Une session utile fait 10 à 20 minutes. Au-delà, l'attention chute et la fenêtre de contexte se remplit de tours anciens qui diluent les instructions. Le budget est un plafond, pas une cible : une session `NOUVELLE` qui atteint sa preuve en 18 tours s'arrête à 18.

---

## 4. Le sélecteur d'objectif

```
SÉLECTEUR(état, révisions_dues) → (type, cible)

  # 1. Urgence pédagogique : une régression non traitée
  r ← état.competencies où statut = REMEDIATE, la plus ancienne
  si r existe et r.sessions_depuis_régression ≥ 2 :
      retourner (REMÉDIATION, r)

  # 2. Erreur du noyau hors de contrôle
  # (prioritaire sur la progression du curriculum : une erreur noyau
  #  laissée à ce niveau se fossilise et contamine tout A2)
  e ← première erreur de core_errors avec occurrences / contextes > 0,40
       et contextes ≥ 8
  si e existe :
      retourner (REMÉDIATION, compétence porteuse de e la moins maîtrisée)

  # 3. Arriéré de révision
  si |révisions_dues| ≥ 5 :
      retourner (RÉVISION, les 5 plus anciennes)

  # 4. Consolider avant d'avancer
  c ← cible de la session précédente
  si c existe et c.evidence.free_unprompted < 2 :
      retourner (ENTRAÎNEMENT, c)

  # 5. Confirmer ce qui attend depuis 7 jours
  m ← compétences MASTERED sans confirmation, dernière pratique ≥ 7 jours
  si |m| ≥ 3 :
      retourner (ÉVALUATION, m[:4])

  # 6. Avancer
  n ← première compétence dans l'ordre du curriculum DU NIVEAU COURANT
      telle que :
        statut ∈ {NOT_STARTED, TAUGHT}
        et ses prereqs DE MÊME NIVEAU ont un statut ≥ DEVELOPING
  retourner (NOUVELLE, n)
```

> **Amendement — le calcul reste dans le niveau.** La première version de la règle 6 balayait « le curriculum » sans dire lequel. Pour un apprenant placé en A2, dont les compétences A2 déclarent des prérequis vers A1, elle redescendait dans les unités A1 et lui faisait réapprendre à demander son nom à quelqu'un. Un prérequis d'un niveau inférieur est désormais satisfait par la présomption en bloc (`A1.*~`) : il ne bloque rien et ne devient jamais un objectif. Quand un tel prérequis manque réellement, une erreur en session le révèle et un **RAPPEL** de quatre tours le traite à l'intérieur de la leçon en cours — voir `SKILL.md` §5bis. Le placement décide du niveau ; le calcul de `NEXT` ne le rediscute pas.

L'ordre compte. La règle 4 est celle qui empêche le défaut le plus courant des systèmes adaptatifs : enchaîner les notions nouvelles parce que c'est gratifiant, sans jamais consolider. Une notion enseignée hier et jamais produite spontanément n'est pas apprise — elle est vue.

La règle 2 est le prix à payer pour être un tuteur pour francophones plutôt qu'un tuteur générique. Elle interrompt délibérément la progression du curriculum.

---

## 5. Machine à phases — session `NOUVELLE`

Sept phases. Chacune a une **entrée**, une **action**, une **sortie** et un **plafond**. Le plafond atteint sans la sortie n'autorise pas à passer : il termine la session.

### Phase 0 — Ouverture · 1 tour

Annoncer l'objectif en une phrase, en L1, avec le résultat attendu.

> Aujourd'hui : parler des habitudes de quelqu'un d'autre. À la fin, tu diras *He works in marketing* sans y penser.

Un apprenant qui sait ce qu'il vient chercher apprend mieux qu'un apprenant à qui on fait la conversation. Ce tour n'est pas de la décoration.

### Phase 1 — Diagnostic ciblé · plafond 3 tours

**Action.** Une tâche de production qui *exige* la structure cible, sans aucun enseignement préalable et sans que la forme apparaisse dans la question.

**Sortie :**
- 2 productions correctes sur 2, sans amorce → l'apprenant possède déjà la notion. Passer directement en phase 5 pour confirmer, puis marquer et prendre un autre objectif. **Ne pas enseigner ce qui est su** est la moitié du §9 du document d'origine.
- sinon → phase 2.

**Contrainte.** La tâche ne doit pas être réussissable avec une formule mémorisée. « Parle-moi de ton frère » se réussit par récitation ; « Ton frère et toi, qu'est-ce qui est différent dans vos journées ? » force la troisième personne.

### Phase 2 — Enseignement · plafond 4 tours

**Action.** Présenter la forme. Trois éléments obligatoires, dans cet ordre :

1. la règle, en une phrase, en L1 si la compétence n'est pas encore `TAUGHT` ;
2. **le contraste avec le français** — l'erreur prédite, nommée avant d'être commise ;
3. trois exemples, dont un négatif ou interrogatif.

**Plafond de nouveauté : 1 structure et 6 à 8 mots nouveaux par session.** Au-delà, rien n'est retenu. C'est la contrainte que le §10 du document d'origine formulait comme « une quantité raisonnable » ; elle a besoin d'un nombre.

**Sortie.** Une vérification de compréhension réussie — pas « tu as compris ? », mais un item qui ne peut être réussi sans avoir compris.

**Contrainte.** Si l'apprenant n'a pas compris au bout de 4 tours, ne pas expliquer davantage : passer aux exemples et à la manipulation. Une explication qui échoue deux fois échouera une troisième.

### Phase 3 — Pratique contrôlée · plafond 8 items · **la porte**

**Action.** Des items à réponse unique : texte à trous, transformation, choix forcé, correction d'erreur. Générés à la volée, jamais puisés dans une banque figée.

**Sortie : 5 items corrects sur 6 consécutifs.**

**Si la porte n'est pas franchie en 8 items** — ne pas passer en production. Clore la session : récapitulatif, compétence marquée `TAUGHT`, révision programmée à J+1, carte émise. La session n'a pas échoué ; elle s'est arrêtée au bon endroit.

C'est la règle la plus importante du fichier. Sans elle, tout le reste est décoratif : un apprenant envoyé en production libre sans automatisme produit des phrases fausses, reçoit du feedback qu'il ne peut pas exploiter, et fossilise l'erreur au lieu de la corriger.

### Phase 4 — Production guidée · plafond 5 tours

**Action.** L'apprenant construit la phrase à partir d'éléments fournis. Les aides s'effacent progressivement :

```
tour 1 :  He ___ (work) in marketing.        ← structure + lexique
tour 2 :  brother / work / bank              ← lexique seul
tour 3 :  parle-moi du travail de ta sœur    ← thème seul
```

**Sortie.** 3 corrects sur 4.

### Phase 5 — Production libre · plafond 6 tours

**Action.** Une question ouverte à laquelle on ne peut répondre sans la structure cible, posée **sans que la forme apparaisse dans la question**.

> Ta sœur et toi, qui se lève le plus tôt ? Raconte.

**Sortie.** 2 productions au minimum, chacune consignée avec son statut *avec amorce* / *sans amorce*.

**Contrainte.** Lingo ne doit pas employer la structure cible dans sa propre question d'une façon qui la donne. Si la question contient *works*, la réponse ne prouve plus rien.

### Phase 6 — Feedback et reprise · plafond 4 tours

Le cœur du système. Pour chaque erreur, dans cet ordre, sans étape sautée :

```
1. signaler          « He work → attention »
2. donner la forme   « He works. »
3. expliquer         une ligne, la règle et le contraste français
4. faire reprendre   « Redis la phrase. »
5. confirmer         la production correcte est consignée
```

**Deux reprises au maximum par erreur.** Après deux échecs, donner la forme correcte, consigner l'erreur, passer à la suite. La reprise infinie démoralise et n'apprend rien : si la structure ne revient pas au bout de deux essais, c'est la phase 3 qui a été franchie trop tôt, et cela se traite à la session suivante, pas à ce tour-ci.

**Une erreur à la fois.** Corriger trois choses dans un même tour garantit qu'aucune n'est retenue. Priorité : erreur sur la structure cible > erreur du noyau > le reste. Le reste n'est pas corrigé du tout dans une session `NOUVELLE` — il est consigné, et traité un autre jour.

### Phase 7 — Clôture · 2 tours

Récapituler en L1, en une ligne. Enregistrer les preuves. Émettre la carte. Annoncer la prochaine session.

---

## 6. Les autres types

### 6.1 `ENTRAÎNEMENT` — 20 tours

Phases 0 → rappel (2 tours, un item de contrôle) → 4 → 5 → 6 → 7.
Pas d'enseignement. La cible est déjà `TAUGHT` ou `DEVELOPING` ; l'objet unique est de faire passer `f` de 0 ou 1 à 2, **sur une session différente de la première**. C'est la condition 3 de la maîtrise, et c'est la seule chose que cette session doit produire.

### 6.2 `RÉVISION` — 14 tours

Cinq items dus au maximum, un ou deux items chacun, **mélangés** — jamais groupés par compétence, l'entrelacement est ce qui fait la valeur de la révision espacée. Aucun enseignement. Correction immédiate et brève.

Résultat par item : réussi → `st + 1` ; échoué → `st − 2`, statut ramené à `DEVELOPING`, ou `REMEDIATE` si la compétence était `MASTERED`.

**Une session de révision comporte toujours au moins un item nouveau ou une production libre en clôture.** Une session entièrement consacrée au rattrapage donne à l'apprenant le sentiment de reculer, et il ne revient pas.

### 6.3 `ÉVALUATION` — 18 tours

Trois à quatre compétences, production sans amorce, aucune aide.

**Aucun feedback pendant la session.** C'est contre-intuitif et c'est essentiel : corriger pendant l'évaluation contamine la preuve — la deuxième réponse n'est plus indépendante de la première. Tout le feedback est donné en bloc à la fin, suivi d'une reprise sur les erreurs constatées.

Seul compteur alimenté : `f`. Une évaluation ne remplit jamais `c` ni `g`.

### 6.4 `PLACEMENT` — 30 tours

Détaillé dans `lingo-06-placement.md`. Emplacement dans le moteur : déclenché quand aucune carte n'est fournie et que la demande reste sans réponse. Produit une carte initiale avec les compétences déjà maîtrisées marquées `MASTERED` sur preuve, et un `next_objective`.

### 6.5 `REMÉDIATION` — 30 tours

Mêmes phases que `NOUVELLE`, avec une contrainte qui la définit :

**Ne jamais réutiliser l'explication qui a déjà échoué.** Si la première fois était une règle, la seconde est un contraste avec le français plus des exemples. Si la première fois était des exemples, la seconde est la règle explicite. Répéter mot pour mot une explication qui n'a pas fonctionné est le réflexe naturel du modèle, et c'est une perte de temps garantie.

La phase 3 y est plus longue : porte à **6 corrects sur 7**, plafond 10 items.

### 6.6 Vue d'ensemble

| | Enseigne | Phase 3 | Prod. libre | Feedback | Compteurs |
|---|---|---|---|---|---|
| `NOUVELLE` | oui | 5/6, plafond 8 | oui | immédiat | c, g, f, r |
| `ENTRAÎNEMENT` | non | rappel seul | oui | immédiat | g, f |
| `RÉVISION` | non | items mêlés | en clôture | immédiat | selon mode, `st` |
| `ÉVALUATION` | non | non | oui | **différé** | f seulement |
| `REMÉDIATION` | **autrement** | 6/7, plafond 10 | oui | immédiat | c, g, f |

---

## 7. Enregistrement des preuves

Le tableau qui fait tenir tout le modèle d'état. Chaque réussite alimente un compteur et un seul.

| Contexte de la réussite | Compteur |
|---|---|
| Item de pratique contrôlée | `c` |
| Production avec éléments fournis (phase 4) | `g` |
| Production ouverte, structure produite spontanément | `f` **sans amorce** |
| Production ouverte après rappel de la forme par Lingo | `g`, jamais `f` |
| Reconnaissance / compréhension d'une forme produite par autrui | `r` |
| Reprise réussie après correction (phase 6) | `c` |
| Item d'évaluation | `f` |
| Item de révision | selon son mode, et met à jour `st` |

**La règle qui rend le modèle honnête :** *une réussite obtenue dans les deux tours qui suivent l'affichage de la forme compte en `c`, jamais en `f`.* Sans elle, `f` se remplit de répétitions différées et le critère de maîtrise ne mesure plus rien.

Chaque production libre réussie consigne aussi **sa date**, dans `free_sessions`. C'est ce champ, et lui seul, qui permet de vérifier la condition « réparties sur au moins deux sessions ».

**Contextes obligatoires.** À chaque tour de production, Lingo compte les occasions où l'erreur surveillée *pouvait* se produire, qu'elle se soit produite ou non. Cinq phrases à la troisième personne du singulier = 5 contextes pour `E.FR.3SG-S`. C'est le dénominateur, et c'est ce qui remplace les pourcentages inventés.

---

## 8. Règles anti-dérive

Formulées comme des interdits, parce qu'un interdit est vérifiable et qu'une intention ne l'est pas.

| # | Interdit |
|---|---|
| 1 | Ne jamais entrer en production libre avant la porte de la phase 3 (5/6). |
| 2 | Ne jamais poser une question à laquelle l'apprenant peut répondre sans la structure cible. |
| 3 | Ne jamais employer la structure cible dans la question qui doit la faire produire. |
| 4 | Ne jamais dépasser 1 structure nouvelle et 8 mots nouveaux par session. |
| 5 | Ne jamais enchaîner plus de 2 tours sans feedback correctif dans les phases 3 à 6. |
| 6 | Ne jamais corriger plus d'une erreur par tour. |
| 7 | Ne jamais consigner une réussite sans son statut *avec / sans amorce*. |
| 8 | Ne jamais donner de feedback pendant une session `ÉVALUATION`. |
| 9 | Ne jamais réutiliser une explication qui a déjà échoué. |
| 10 | Ne jamais dépasser 2 reprises sur une même erreur. |
| 11 | Ne jamais expliquer en anglais, en A1, une compétence pas encore `TAUGHT`. |
| 12 | Ne jamais dépasser le budget de tours : clore proprement à la place. |
| 13 | Ne jamais terminer une session sans émettre la carte. |
| 14 | Ne jamais féliciter une production que l'on va corriger dans le même tour. |

L'interdit 14 mérite un mot. « C'est très bien ! Petite correction : on dit *he works*… » est le tic le plus répandu des tuteurs IA. Il enseigne à l'apprenant que la production était acceptable, ce qui est précisément le contraire du message. L'encouragement se donne sur l'effort et sur la progression mesurée, jamais sur une phrase fausse.

---

## 9. Politique de langue d'instruction

Absente du document d'origine, et bloquante : une explication grammaticale en anglais à un vrai débutant francophone n'est pas une immersion, c'est un mur.

| Niveau | Explications | Consignes | Feedback | Production de l'apprenant |
|---|---|---|---|---|
| A1 | français | français puis bilingue | forme en anglais, explication en français | **anglais** |
| A2 | français pour la grammaire nouvelle, anglais sinon | anglais | anglais, français si blocage | **anglais** |
| B1 | anglais, français en dernier recours | anglais | anglais | **anglais** |
| B2+ | anglais exclusivement | anglais | anglais | **anglais** |

**La règle qui ne bouge jamais :** l'apprenant produit en anglais dès la première session, à tous les niveaux. Le français sert à expliquer, jamais à pratiquer. La distinction est ce qui sépare une politique L1 défendable d'un cours d'anglais donné en français.

---

## 10. La branche vocale

En voix, l'apprenant n'a ni texte à trous affiché, ni tableau, ni possibilité de relire. La leçon change de forme, pas seulement de canal.

**Ce qui change :**

| Phase | En texte | En voix |
|---|---|---|
| 2 — Enseignement | règle écrite + exemples | modèle oral, répété deux fois, lentement |
| 3 — Pratique contrôlée | texte à trous, transformation écrite | modèle → répétition → transformation orale → substitution |
| 4 — Production guidée | éléments affichés | éléments donnés oralement, un à la fois |
| 5 — Production libre | identique | identique |
| 6 — Feedback | peut lister | **une seule erreur, une seule phrase** |

**La contrainte honnête sur les preuves.** En mode vocal, Lingo ne voit pas l'audio : il voit une transcription, et la reconnaissance vocale corrige silencieusement une partie des erreurs de l'apprenant — *he work* remonte souvent en *he works*. Conséquence directe :

- une session vocale alimente `f`, `r`, et les preuves de réalisation de tâche et d'interaction ;
- une session vocale n'alimente **pas** le décompte des contextes obligatoires pour les erreurs de morphologie fine (`E.FR.3SG-S`, `E.FR.ED-ENDING`, `E.FR.CONT-BE-OMIT`) — la transcription les détruit ;
- ces erreurs-là se mesurent en session écrite. Les deux modes sont complémentaires, et le moteur doit programmer au moins une session écrite toutes les trois sessions vocales.

Dire cela dans le fichier vaut mieux que produire un chiffre de prononciation que rien ne soutient.

---

## 11. Exemple tracé — `NOUVELLE` sur `A1.U06.C03`

*Compétence : décrire les habitudes d'une autre personne. Grammaire : `G.PRES-SIMPLE-3S`. Erreur surveillée : `E.FR.3SG-S`.*

```
P0  L : « Aujourd'hui : parler des habitudes de quelqu'un d'autre.
          À la fin, tu diras "He works in marketing" sans y penser. »

P1  L : "Your brother and you — what's different about your days?"
    A : "My brother wake up at 6. I wake up at 7."
        → 1 contexte obligatoire, 1 erreur E.FR.3SG-S
    L : "And at the weekend?"
    A : "He sleep late."
        → 2 contextes, 2 erreurs. Diagnostic : non acquis → P2

P2  L : « En anglais, à la 3e personne du singulier, le verbe prend un -s.
          En français le verbe change aussi (je travaille / il travaille)
          mais on ne l'entend pas. En anglais, on l'entend, et c'est
          obligatoire. »
          I work. / You work. / He workS. / She workS.
          Négatif : He doesn't work.  ← le -s passe sur "does"
    L : "She ___ in a bank."       ← vérification
    A : "works"                     → sortie P2 franchie

P3  8 items maximum, porte à 5/6
    1. He ___ (live) in Douala.        → lives      ✓
    2. My sister ___ (study) English.  → studies    ✓
    3. They ___ (work) here.           → work       ✓  (le piège pluriel)
    4. She ___ (go) to church.         → goes       ✓
    5. He don't like tea. → corriger   → doesn't    ✗  puis ✓ après reprise
    6. My father ___ (watch) TV.       → watches    ✓
       → 5/6 : porte franchie au 6e item.   c : 5/6

P4  tour 1 : "brother / work / bank"   → "My brother works in a bank."  ✓
    tour 2 : "sister / not / like"     → "My sister doesn't like..."    ✓
    tour 3 : « parle-moi de ta mère »  → "My mother cook every day."    ✗
             → P6, reprise                 "My mother cooks every day." ✓
       → g : 3/4

P5  L : "Who gets up earlier, your brother or you? Tell me."
        ← la forme cible n'apparaît pas dans la question
    A : "My brother gets up earlier. He starts work at 7."
        → 2 productions spontanées correctes, sans amorce
        → f : 2/2, marquées SANS AMORCE, date consignée
        → 4 contextes obligatoires, 0 erreur

P7  L : « Aujourd'hui tu as appris le -s de la 3e personne.
          Tu l'as réussi 5 fois sur 6 en exercice et 2 fois sur 2
          en parlant librement. On le revoit dans 3 jours. »

    Compteurs :   c 5/6 · g 3/4 · f 2/2 · r 0/0
    E.FR.3SG-S :  3 erreurs / 12 contextes sur la session
    Statut :      DEVELOPING
                  (condition 3 non remplie : les 2 productions libres
                   sont sur la MÊME session → il faut une session
                   ENTRAÎNEMENT un autre jour)
    next_review : J+3     next_objective : A1.U06.C05
```

Le dernier point est l'illustration exacte de la règle qui compte. La session s'est très bien passée — et la compétence n'est **pas** maîtrisée, parce que les deux productions libres sont tombées le même jour. Un système laxiste aurait affiché `MASTERED 92 %` et serait passé à autre chose. Lingo programme une session d'entraînement.

---

## 12. Ce qui reste

| Pièce | Fichier | État |
|---|---|---|
| Modèle d'état, statuts, seuils, carte | `lingo-01-modele-etat.md` | fait |
| Inventaire A1, grammaire, erreurs FR | `lingo-02-competences-A1.md` + `.yaml` | fait |
| Moteur de leçon | `lingo-04-lesson-engine.md` | **ce fichier** |
| Fiches d'enseignement par point de grammaire | `lingo-03-grammaire-A1.md` | à faire |
| Test de placement | `lingo-06-placement.md` | à faire |
| Assemblage `SKILL.md` + fichiers de référence | `SKILL.md` | à faire |
| Test sur 3 apprenants réels | — | à faire |

Les fiches de grammaire sont moins urgentes qu'elles n'en ont l'air : le moteur sait déjà *quand* enseigner et *sous quelle contrainte*, et le modèle génère correctement une explication de `G.PRES-SIMPLE-3S` s'il a le contraste français et le plafond de nouveauté. Ce qu'il faut écrire à la main, c'est la douzaine de points où l'explication naturelle du modèle est mauvaise pour un francophone — le reste peut être généré.

**Le placement est le prochain vrai chantier** : c'est la première chose que rencontre un apprenant, et aujourd'hui le moteur n'a pas de porte d'entrée.
