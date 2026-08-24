# Lingo — Inventaire des compétences A1

**98 compétences observables · 13 unités · 55 points de grammaire · 55 erreurs francophones indexées.**

*Chiffres générés et vérifiés par `tools/build.mjs` — identifiants uniques, prérequis résolus, aucune grammaire orpheline, réception présente dans chaque unité.*

---

## Comment lire cet inventaire

Une **compétence** est un *can-do* observable : quelque chose que l'apprenant fait, que l'on peut voir réussir ou échouer. C'est l'unité de suivi de la maîtrise.

La grammaire et le vocabulaire ne sont **pas** des compétences — ce sont des **ressources** mobilisées par une compétence. On ne suit pas « connaît le present simple » ; on suit « peut décrire sa journée type », qui a besoin du present simple pour exister. C'est la fidélité au CECR, et c'est aussi ce qui empêche le système de récompenser la récitation de règles.

### Colonnes

| Colonne | Contenu |
|---|---|
| **ID** | Identifiant stable. Ne change jamais, même si le libellé est reformulé. |
| **Compétence** | Le *can-do*, formulé du point de vue de l'apprenant. |
| **Mode** | `I` interaction · `PO` production orale · `PE` production écrite · `RO` réception orale · `RE` réception écrite |
| **Grammaire** | Ressources grammaticales requises (voir §14). |
| **Erreurs** | Erreurs francophones à surveiller spécifiquement sur cette compétence (voir §15). |

Les modes déterminent **quelles preuves sont exigées** pour la maîtrise : une compétence marquée `PO` ne peut pas être validée uniquement à l'écrit.

### Prérequis

Une compétence n'est enseignable que si ses prérequis sont au moins `DEVELOPING`. Les prérequis figurent dans l'export YAML ; ils suivent globalement l'ordre des unités, avec les exceptions signalées.

---

## U00 — Langue de survie et de classe

*Transversal. Enseigné en premier, révisé en permanence. Sans cette unité, l'apprenant ne peut pas participer à sa propre leçon.*

**Thème** : la salle de classe, l'interaction avec le tuteur
**Fonctions** : demander de l'aide, gérer l'incompréhension
**Grammaire** : `G.IMPERATIVE`, `G.CAN-REQUEST`, `G.WH-Q`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U00.C01 | Comprendre les consignes courantes du tuteur (*listen, repeat, write, choose, look at*) | RO | G.IMPERATIVE | — |
| A1.U00.C02 | Demander de répéter, de ralentir ou d'expliquer (*Can you repeat, please? Sorry?*) | I | G.CAN-REQUEST | E.FR.CAN-TO |
| A1.U00.C03 | Épeler son nom et comprendre un mot épelé | I | G.ALPHABET | E.FR.SPELL-VOWELS |
| A1.U00.C04 | Dire qu'on ne comprend pas et demander le sens d'un mot (*What does X mean?*) | I | G.WH-Q, G.DO-AUX | E.FR.DO-AUX-OMIT |
| A1.U00.C05 | Reconnaître et produire les nombres 0 à 20 à l'oral | I | G.NUM | E.FR.NUM-TEEN-TY |
| A1.U00.C06 | Comprendre une consigne écrite d'exercice simple | RE | G.IMPERATIVE | — |

---

## U01 — Identité et salutations

**Thème** : se présenter, rencontrer quelqu'un
**Fonctions** : saluer, se présenter, présenter un tiers, prendre congé
**Grammaire** : `G.BE-AFF`, `G.BE-Q`, `G.PRON-SUBJ`, `G.POSS-ADJ`, `G.CONTRACTIONS`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U01.C01 | Saluer et prendre congé selon le moment de la journée | I | — | — |
| A1.U01.C02 | Se présenter en donnant son nom (*I'm… / My name is…*) | PO, I | G.BE-AFF, G.POSS-ADJ | E.FR.BE-OMIT |
| A1.U01.C03 | Demander le nom de quelqu'un et répondre à la question | I | G.BE-Q, G.WH-Q | E.FR.BE-OMIT, E.FR.Q-INTONATION |
| A1.U01.C04 | Présenter une tierce personne (*This is my friend Paul.*) | PO, I | G.DEMONSTRATIVES, G.BE-AFF | E.FR.THIS-IT |
| A1.U01.C05 | Dire d'où l'on vient — pays et ville (*I'm from Cameroon.*) | PO, I | G.BE-AFF, G.PREP-PLACE | E.FR.BE-OMIT |
| A1.U01.C06 | Demander à quelqu'un d'où il vient | I | G.BE-Q, G.WH-Q | E.FR.Q-INTONATION |
| A1.U01.C07 | Comprendre une présentation orale simple et en extraire nom, origine, métier | RO | G.BE-AFF | — |
| A1.U01.C08 | Écrire une présentation de soi de 3 à 4 phrases | PE | G.BE-AFF, G.PRON-SUBJ, G.CONJ-BASIC | E.FR.BE-OMIT, E.FR.CAPITAL-NATION, **E.FR.AGE-HAVE** |

---

## U02 — Informations personnelles

**Thème** : âge, nationalité, langues, coordonnées
**Fonctions** : donner et demander des informations factuelles sur soi
**Grammaire** : `G.BE-NEG`, `G.WH-Q`, `G.NUM`, `G.ART-A-AN`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U02.C01 | Donner son âge et demander l'âge de quelqu'un | I | G.BE-AFF, G.BE-Q | **E.FR.AGE-HAVE** |
| A1.U02.C02 | Donner sa nationalité et la ou les langues qu'on parle | PO, I | G.BE-AFF, G.PRES-SIMPLE-AFF | E.FR.CAPITAL-NATION, E.FR.BE-OMIT |
| A1.U02.C03 | Donner son numéro de téléphone et son adresse e-mail à l'oral | I | G.NUM, G.ALPHABET | E.FR.NUM-TEEN-TY |
| A1.U02.C04 | Corriger une information fausse à son sujet (*No, I'm not… I'm…*) | I | G.BE-NEG | E.FR.NEG-PLACE |
| A1.U02.C05 | Répondre à des questions fermées sur soi avec la reprise correcte (*Yes, I am. / No, I don't.*) | I | G.SHORT-ANSWERS | E.FR.SHORT-ANSWER-FLAT |
| A1.U02.C06 | Comprendre un formulaire d'inscription simple et savoir ce que chaque champ demande | RE | G.WH-Q, G.NUM | E.FR.FALSE-FRIEND |
| A1.U02.C07 | Remplir un formulaire d'informations personnelles | PE | G.NUM, G.ALPHABET | E.FR.DATE-FORMAT, **E.FR.AGE-HAVE** |

---

## U03 — Famille et entourage

**Thème** : la famille, les amis
**Fonctions** : décrire son entourage, dire à qui appartient quelque chose
**Grammaire** : `G.POSS-S`, `G.POSS-ADJ`, `G.HAVE-GOT`, `G.PLURAL-REG`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U03.C01 | Nommer les membres de sa famille | PO | G.PLURAL-REG, G.PLURAL-IRREG | — |
| A1.U03.C02 | Décrire sa famille en plusieurs phrases liées | PO | G.HAVE-GOT, G.POSS-ADJ | E.FR.3SG-S, E.FR.POSS-AGREE |
| A1.U03.C03 | Dire à qui appartient quelque chose avec le génitif (*my sister's phone*) | PO, PE | G.POSS-S | **E.FR.OF-CALQUE** |
| A1.U03.C04 | Poser des questions sur la famille de quelqu'un | I | G.HAVE-GOT-Q, G.WH-Q | E.FR.DO-AUX-OMIT |
| A1.U03.C05 | Dire ce qu'on possède et ne possède pas | PO, I | G.HAVE-GOT, G.HAVE-GOT-NEG | E.FR.HAVE-NEG |
| A1.U03.C06 | Comprendre une description orale d'une famille et identifier les liens | RO | G.POSS-S | — |
| A1.U03.C07 | Écrire un court texte sur sa famille (4 à 5 phrases) | PE | G.HAVE-GOT, G.POSS-ADJ | E.FR.3SG-S, E.FR.POSS-AGREE |

---

## U04 — Décrire personnes et objets

**Thème** : apparence, caractère, objets du quotidien, couleurs
**Fonctions** : décrire, désigner, identifier
**Grammaire** : `G.ADJ-POSITION`, `G.ART-A-AN`, `G.DEMONSTRATIVES`, `G.PLURAL-REG`, `G.PLURAL-IRREG`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U04.C01 | Décrire l'apparence physique d'une personne | PO | G.BE-AFF, G.HAVE-GOT, G.ADJ-POSITION | **E.FR.ADJ-AGREE**, E.FR.ADJ-ORDER |
| A1.U04.C02 | Décrire le caractère de quelqu'un en termes simples | PO | G.BE-AFF, G.ADJ-POSITION | E.FR.ADJ-AGREE, E.FR.FALSE-FRIEND |
| A1.U04.C03 | Nommer et décrire un objet du quotidien (couleur, taille) | PO | G.ART-A-AN, G.ADJ-POSITION | **E.FR.ADJ-ORDER**, E.FR.ART-A-AN |
| A1.U04.C04 | Désigner un objet proche ou éloigné (*this / that / these / those*) | I | G.DEMONSTRATIVES | E.FR.THIS-THAT |
| A1.U04.C05 | Demander le nom d'un objet et y répondre (*What's this? — It's a…*) | I | G.WH-Q, G.BE-Q | E.FR.THIS-IT |
| A1.U04.C06 | Comprendre une description simple de personne ou d'objet | RO, RE | G.ADJ-POSITION | — |
| A1.U04.C07 | Lire une petite annonce d'objet et en extraire l'essentiel | RE | G.ADJ-POSITION, G.NUM | E.FR.FALSE-FRIEND |

---

## U05 — Logement et lieux

**Thème** : la maison, les pièces, le mobilier, la ville
**Fonctions** : décrire un lieu, situer, demander son chemin
**Grammaire** : `G.THERE-IS-ARE`, `G.PREP-PLACE`, `G.ART-THE`, `G.SOME-ANY`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U05.C01 | Dire où l'on habite (ville, quartier, type de logement) | PO, I | G.PRES-SIMPLE-AFF, G.PREP-PLACE | E.FR.PREP-CALQUE |
| A1.U05.C02 | Nommer les pièces d'un logement et le mobilier courant | PO | G.PLURAL-REG | — |
| A1.U05.C03 | Dire ce qu'il y a et ce qu'il n'y a pas dans un lieu | PO, PE | **G.THERE-IS-ARE**, G.SOME-ANY | **E.FR.THERE-HAVE**, E.FR.THERE-AGREE |
| A1.U05.C04 | Situer un objet dans l'espace | PO | G.PREP-PLACE | E.FR.PREP-CALQUE |
| A1.U05.C05 | Nommer les lieux courants de la ville | PO | G.ART-THE | E.FR.ART-THE-ABSTRACT |
| A1.U05.C06 | Demander et donner une indication de chemin très simple | I | G.IMPERATIVE, G.PREP-PLACE | E.FR.GO-TO-HOME |
| A1.U05.C07 | Comprendre des indications de lieu et suivre un itinéraire simple | RO | G.PREP-PLACE, G.IMPERATIVE | — |
| A1.U05.C08 | Écrire une description de son logement (5 à 6 phrases) | PE | G.THERE-IS-ARE, G.PREP-PLACE | E.FR.THERE-HAVE |

---

## U06 — Routine quotidienne

*L'unité pivot de A1. C'est ici que se joue l'installation du present simple, et donc la moitié des erreurs francophones du niveau.*

**Thème** : la journée type, l'heure, les jours
**Fonctions** : parler d'habitudes, situer dans le temps, interroger sur les habitudes
**Grammaire** : `G.PRES-SIMPLE-AFF`, `G.PRES-SIMPLE-3S`, `G.PRES-SIMPLE-NEG`, `G.PRES-SIMPLE-Q`, `G.ADV-FREQ`, `G.PREP-TIME`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U06.C01 | Décrire sa journée type dans l'ordre chronologique | PO, PE | G.PRES-SIMPLE-AFF, G.PREP-TIME | E.FR.PREP-CALQUE |
| A1.U06.C02 | Dire l'heure et demander l'heure | I | G.NUM, G.PREP-TIME | E.FR.NUM-TEEN-TY |
| A1.U06.C03 | Décrire les habitudes d'une **autre personne** (3ᵉ personne) | PO | **G.PRES-SIMPLE-3S** | **E.FR.3SG-S** |
| A1.U06.C04 | Nommer les jours, les mois et les moments de la journée | PO | G.PREP-TIME | E.FR.PREP-CALQUE, E.FR.CAPITAL-DAYS |
| A1.U06.C05 | Dire à quelle fréquence on fait quelque chose | PO | G.ADV-FREQ | **E.FR.ADV-FREQ-PLACE** |
| A1.U06.C06 | Dire ce qu'on ne fait pas (forme négative) | PO | G.PRES-SIMPLE-NEG | E.FR.DO-AUX-OMIT, E.FR.NEG-3S-DOUBLE |
| A1.U06.C07 | Poser des questions sur la routine de quelqu'un | I | **G.PRES-SIMPLE-Q**, G.WH-Q | **E.FR.DO-AUX-OMIT**, E.FR.Q-INTONATION |
| A1.U06.C08 | Comprendre le récit oral d'une routine et en extraire les horaires | RO | G.PRES-SIMPLE-AFF, G.PREP-TIME | — |

---

## U07 — Travail et études

**Thème** : les métiers, le lieu de travail, l'école
**Fonctions** : parler de son activité professionnelle, interroger sur celle d'autrui
**Grammaire** : `G.ART-A-JOBS`, `G.PRES-SIMPLE-Q`, `G.PREP-TIME`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U07.C01 | Dire quel est son métier ou ce qu'on étudie | PO, I | **G.ART-A-JOBS**, G.BE-AFF | **E.FR.ART-A-JOBS** |
| A1.U07.C02 | Demander à quelqu'un ce qu'il fait dans la vie | I | G.PRES-SIMPLE-Q | E.FR.DO-AUX-OMIT |
| A1.U07.C03 | Décrire son lieu de travail ou d'études | PO | G.THERE-IS-ARE, G.PREP-PLACE | E.FR.THERE-HAVE |
| A1.U07.C04 | Dire ce qu'on fait concrètement dans son travail | PO | G.PRES-SIMPLE-AFF | E.FR.3SG-S |
| A1.U07.C05 | Parler de ses horaires de travail ou de cours | PO, I | G.PREP-TIME, G.NUM | E.FR.PREP-CALQUE |
| A1.U07.C06 | Comprendre une présentation professionnelle simple | RO | G.PRES-SIMPLE-AFF | — |
| A1.U07.C07 | Lire une carte de visite ou une offre d'emploi très simple | RE | G.ART-A-JOBS, G.NUM | E.FR.FALSE-FRIEND |

---

## U08 — Goûts et temps libre

**Thème** : loisirs, sport, musique, préférences
**Fonctions** : exprimer un goût, une préférence, justifier, réagir
**Grammaire** : `G.LIKE-ING`, `G.OBJ-PRON`, `G.CONJ-BECAUSE`, `G.SO-NEITHER`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U08.C01 | Dire ce qu'on aime et ce qu'on n'aime pas | PO, I | **G.LIKE-ING**, G.PRES-SIMPLE-NEG, G.OBJ-PRON | **E.FR.LIKE-INFINITIVE**, E.FR.ADV-MUCH-PLACE |
| A1.U08.C02 | Exprimer une préférence entre deux choses | PO, I | G.PREFER, G.CONJ-BASIC | E.FR.PREFER-THAN |
| A1.U08.C03 | Demander à quelqu'un ce qu'il aime | I | G.PRES-SIMPLE-Q, G.LIKE-ING | E.FR.DO-AUX-OMIT |
| A1.U08.C04 | Parler de ses loisirs et du sport qu'on pratique | PO | G.PRES-SIMPLE-AFF, G.PLAY-DO-GO | E.FR.PLAY-DO-GO |
| A1.U08.C05 | Justifier un goût avec *because* | PO | G.CONJ-BECAUSE | E.FR.BECAUSE-OF |
| A1.U08.C06 | Réagir à ce que dit l'interlocuteur (*Me too / I don't / Really?*) | I | G.SO-NEITHER | E.FR.ME-TOO-FLAT |
| A1.U08.C07 | Écrire un court message sur ses loisirs | PE | G.LIKE-ING, G.CONJ-BECAUSE | E.FR.LIKE-INFINITIVE |
| A1.U08.C08 | Comprendre quelqu'un qui parle de ses goûts et identifier ce qu'il aime | RO | G.LIKE-ING, G.CONJ-BECAUSE | — |

---

## U09 — Capacités, demandes et permission

**Thème** : ce qu'on sait faire, les demandes polies
**Fonctions** : exprimer une capacité, demander, autoriser, refuser
**Grammaire** : `G.CAN-ABILITY`, `G.CAN-REQUEST`, `G.WOULD-LIKE`, `G.IMPERATIVE`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U09.C01 | Dire ce qu'on sait faire et ce qu'on ne sait pas faire | PO, I | **G.CAN-ABILITY** | **E.FR.CAN-TO**, E.FR.CAN-3S |
| A1.U09.C02 | Demander à quelqu'un s'il sait faire quelque chose | I | G.CAN-Q | E.FR.CAN-TO, E.FR.DO-AUX-CAN |
| A1.U09.C03 | Demander quelque chose poliment | I | G.CAN-REQUEST, G.WOULD-LIKE | E.FR.WANT-DIRECT |
| A1.U09.C04 | Demander et donner la permission | I | G.CAN-REQUEST | E.FR.CAN-TO |
| A1.U09.C05 | Accepter ou refuser poliment une proposition | I | G.SHORT-ANSWERS | E.FR.REFUSE-BLUNT |
| A1.U09.C06 | Comprendre une demande ou une consigne polie | RO | G.CAN-REQUEST | — |
| A1.U09.C07 | Écrire un message court de demande (SMS, e-mail bref) | PE | G.CAN-REQUEST, G.WOULD-LIKE | E.FR.EMAIL-FORMAL-CALQUE |

---

## U10 — Nourriture, achats et prix

**Thème** : aliments, boissons, commerces, argent
**Fonctions** : commander, acheter, demander un prix, dire ses habitudes
**Grammaire** : `G.COUNT-UNCOUNT`, `G.SOME-ANY`, `G.HOW-MUCH-MANY`, `G.WOULD-LIKE`, `G.NUM`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U10.C01 | Nommer les aliments et boissons courants | PO | G.PLURAL-REG | — |
| A1.U10.C02 | Employer correctement dénombrables et indénombrables | PO, PE | **G.COUNT-UNCOUNT**, G.SOME-ANY | **E.FR.UNCOUNT-PLURAL** |
| A1.U10.C03 | Demander une quantité et un prix | I | G.HOW-MUCH-MANY, G.NUM | E.FR.HOW-MUCH-MANY, E.FR.NUM-TEEN-TY |
| A1.U10.C04 | Commander dans un café ou un restaurant | I | G.WOULD-LIKE | E.FR.WANT-DIRECT |
| A1.U10.C05 | Faire un achat simple et gérer la transaction | I | G.WOULD-LIKE, G.NUM | E.FR.WANT-DIRECT |
| A1.U10.C06 | Dire ses habitudes alimentaires | PO | G.PRES-SIMPLE-AFF, G.ADV-FREQ | E.FR.ADV-FREQ-PLACE, E.FR.UNCOUNT-PLURAL |
| A1.U10.C07 | Comprendre un prix annoncé oralement et vérifier la monnaie | RO | G.NUM | E.FR.NUM-TEEN-TY |
| A1.U10.C08 | Lire un menu et une étiquette de prix | RE | G.NUM | E.FR.FALSE-FRIEND |

---

## U11 — Ce qui se passe maintenant

**Thème** : actions en cours, météo, vêtements
**Fonctions** : décrire une action en cours, décrire une image
**Grammaire** : `G.PRES-CONT`, `G.PRES-CONT-Q`, `G.PRES-CONT-VS-SIMPLE`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U11.C01 | Dire ce qu'on est en train de faire | PO, I | **G.PRES-CONT** | E.FR.CONT-BE-OMIT, E.FR.ING-SPELLING |
| A1.U11.C02 | Demander ce que quelqu'un fait en ce moment | I | G.PRES-CONT-Q | E.FR.CONT-BE-OMIT |
| A1.U11.C03 | Décrire une image ou une scène | PO, PE | G.PRES-CONT, G.THERE-IS-ARE | E.FR.THERE-HAVE |
| A1.U11.C04 | Distinguer une habitude d'une action en cours | PO | **G.PRES-CONT-VS-SIMPLE** | **E.FR.CONT-FOR-HABIT** |
| A1.U11.C05 | Parler du temps qu'il fait | PO, I | G.WEATHER-IT | **E.FR.WEATHER-HAVE** |
| A1.U11.C06 | Nommer les vêtements et décrire ce que quelqu'un porte | PO | G.PRES-CONT, G.ADJ-POSITION | E.FR.ADJ-AGREE |
| A1.U11.C07 | Écrire une légende décrivant ce qui se passe sur une photo | PE | G.PRES-CONT | E.FR.ING-SPELLING |
| A1.U11.C08 | Comprendre une description orale d'une scène en cours | RO | G.PRES-CONT, G.THERE-IS-ARE | — |

---

## U12 — Passé et futur simples

**Thème** : le week-end, les vacances, les projets
**Fonctions** : raconter, situer dans le temps, annoncer une intention
**Grammaire** : `G.PAST-BE`, `G.PAST-SIMPLE-REG`, `G.PAST-SIMPLE-IRREG`, `G.PAST-Q`, `G.GOING-TO`, `G.TIME-MARKERS`

| ID | Compétence | Mode | Grammaire | Erreurs |
|---|---|---|---|---|
| A1.U12.C01 | Dire où l'on était et comment c'était | PO | **G.PAST-BE** | E.FR.PAST-BE-AGREE |
| A1.U12.C02 | Raconter une action passée avec des verbes réguliers | PO, PE | **G.PAST-SIMPLE-REG** | **E.FR.ED-ENDING**, E.FR.PAST-PRESENT-MIX |
| A1.U12.C03 | Employer les 15 verbes irréguliers les plus fréquents au passé | PO, PE | G.PAST-SIMPLE-IRREG | E.FR.IRREG-REGULARISED |
| A1.U12.C04 | Poser une question au passé | I | **G.PAST-Q** | **E.FR.DID-DOUBLE-PAST**, E.FR.DO-AUX-OMIT |
| A1.U12.C05 | Dire ce qu'on va faire (intention) | PO, I | **G.GOING-TO** | E.FR.GOING-TO-OMIT-BE |
| A1.U12.C06 | Situer un événement dans le temps (*yesterday, last week, next month*) | PO, PE | G.TIME-MARKERS | E.FR.PREP-CALQUE |
| A1.U12.C07 | Raconter brièvement son week-end à l'oral | PO | G.PAST-SIMPLE-REG, G.PAST-SIMPLE-IRREG | E.FR.PAST-PRESENT-MIX |
| A1.U12.C08 | Écrire un court récit au passé (4 à 5 phrases liées) | PE | G.PAST-SIMPLE-REG, G.CONJ-BASIC | E.FR.ED-ENDING |
| A1.U12.C09 | Comprendre un court récit au passé et en extraire les événements | RO | G.PAST-SIMPLE-REG, G.PAST-SIMPLE-IRREG, G.TIME-MARKERS | — |

---

## 13. Matrice de synthèse

Le tableau que le §6 du document d'origine appelait de ses vœux, complété.

| Unité | Thème | Lexique | Grammaire dominante | Fonction communicative |
|---|---|---|---|---|
| U00 | Classe | consignes, alphabet, 0–20 | impératif, *can* | gérer l'incompréhension |
| U01 | Identité | salutations, pays | *be*, pronoms sujets | se présenter |
| U02 | Infos perso | âge, nationalités, chiffres | *be* nég./interro., réponses courtes | informer |
| U03 | Famille | liens de parenté | génitif 's, *have got* | décrire, posséder |
| U04 | Description | apparence, couleurs, objets | adjectifs, démonstratifs | décrire, identifier |
| U05 | Logement | pièces, mobilier, ville | *there is/are*, prépositions de lieu | situer, décrire un lieu |
| U06 | Routine | journée, heure, jours | **present simple complet**, adv. de fréquence | parler d'habitudes |
| U07 | Travail | métiers, lieu de travail | *a* + métier, questions au présent | parler de son activité |
| U08 | Loisirs | sport, musique, hobbies | *like* + -ing, pronoms objets | exprimer un goût |
| U09 | Capacités | verbes d'action | *can*, *would like* | demander, autoriser |
| U10 | Nourriture | aliments, prix | dénombrables, *some/any* | commander, acheter |
| U11 | Maintenant | vêtements, météo | present continuous | décrire l'instant |
| U12 | Passé/futur | week-end, vacances | past simple, *going to* | raconter, projeter |

**Répartition par mode** — comptée sur la source, pas estimée :

| Mode | Occurrences |
|---|---|
| Production orale `PO` | 44 |
| Interaction `I` | 43 |
| Production écrite `PE` | 16 |
| Réception orale `RO` | 12 |
| Réception écrite `RE` | 6 |

*(Une compétence peut relever de plusieurs modes ; le total dépasse donc 98.)*

L'oral domine largement, ce qui est correct pour A1. La production écrite est volontairement minoritaire. La réception est présente dans **chacune des 13 unités** — c'est une contrainte dure, sans quoi la condition 4 de la règle de maîtrise serait inatteignable dans cette unité. La première passe de l'inventaire l'avait violée en U08, U11 et U12 ; le contrôle automatique l'a détecté et les trois compétences réceptives manquantes ont été ajoutées.

---

## 14. Inventaire grammatical A1 (55 points)

*Ressources, pas compétences. Chacune est enseignée au service d'un can-do, jamais pour elle-même.*

**Le verbe *be* et l'identité** — `G.BE-AFF` · `G.BE-NEG` · `G.BE-Q` · `G.SHORT-ANSWERS` · `G.CONTRACTIONS` · `G.PRON-SUBJ`

**Détermination et nom** — `G.ART-A-AN` · `G.ART-THE` · `G.ART-A-JOBS` · `G.PLURAL-REG` · `G.PLURAL-IRREG` · `G.DEMONSTRATIVES` · `G.COUNT-UNCOUNT` · `G.SOME-ANY`

**Possession** — `G.POSS-ADJ` · `G.POSS-S` · `G.HAVE-GOT` · `G.HAVE-GOT-NEG` · `G.HAVE-GOT-Q`

**Qualification** — `G.ADJ-POSITION`

**Le présent** — `G.PRES-SIMPLE-AFF` · `G.PRES-SIMPLE-3S` · `G.PRES-SIMPLE-NEG` · `G.PRES-SIMPLE-Q` · `G.PRES-CONT` · `G.PRES-CONT-Q` · `G.PRES-CONT-VS-SIMPLE`

**Le passé et le futur** — `G.PAST-BE` · `G.PAST-SIMPLE-REG` · `G.PAST-SIMPLE-IRREG` · `G.PAST-Q` · `G.GOING-TO`

**Modalité** — `G.CAN-ABILITY` · `G.CAN-Q` · `G.CAN-REQUEST` · `G.WOULD-LIKE` · `G.IMPERATIVE`

**Circonstants et liens** — `G.PREP-PLACE` · `G.PREP-TIME` · `G.ADV-FREQ` · `G.TIME-MARKERS` · `G.CONJ-BASIC` · `G.CONJ-BECAUSE`

**Interrogation et divers** — `G.WH-Q` · `G.DO-AUX` · `G.OBJ-PRON` · `G.NUM` · `G.ALPHABET` · `G.THERE-IS-ARE` · `G.SO-NEITHER` · `G.LIKE-ING` · `G.PREFER` · `G.PLAY-DO-GO` · `G.WEATHER-IT` · `G.HOW-MUCH-MANY`

*Les 55 points sont tous rattachés à au moins une compétence — vérifié automatiquement. Un point de grammaire orphelin serait un point enseigné pour lui-même, c'est-à-dire exactement ce que ce découpage cherche à empêcher.*

---

## 15. Erreurs francophones surveillées (55)

*Le fichier différenciant. Ces erreurs ne sont pas détectées après coup : elles sont **anticipées**, enseignées en amont, et comptées en contextes obligatoires.*

Les 55 codes sont définis en entier dans `lingo-a1-competences.yaml` (libellé, forme fautive, forme correcte, noyau oui/non, évaluée en v1 oui/non). Ci-dessous les plus structurantes ; le tableau final liste le reste.

### Noyau — les quatre à ne jamais laisser passer en A2

| Code | Erreur type | Forme correcte | Où elle apparaît |
|---|---|---|---|
| `E.FR.AGE-HAVE` | *I have 25 years* | I'm 25 | U02 |
| `E.FR.3SG-S` | *He work in marketing* | He works | U03, U06, U07 |
| `E.FR.DO-AUX-OMIT` | *Where you live? / You like football?* | Where do you live? | U00, U03, U06, U08, U12 |
| `E.FR.BE-OMIT` | *I student / He 25* | I'm a student | U01, U02 |

### Structure de la phrase

| Code | Erreur type | Forme correcte |
|---|---|---|
| `E.FR.ADJ-AGREE` | *greens cars, differents* | green cars |
| `E.FR.ADJ-ORDER` | *a car red* | a red car |
| `E.FR.ADV-FREQ-PLACE` | *I go often to church* | I often go |
| `E.FR.ADV-MUCH-PLACE` | *I like very much football* | I like football very much |
| `E.FR.NEG-PLACE` | *I not am tired* | I'm not tired |
| `E.FR.Q-INTONATION` | question marquée par la seule intonation | inversion ou *do* |
| `E.FR.NEG-3S-DOUBLE` | *He doesn't works* | He doesn't work |
| `E.FR.DID-DOUBLE-PAST` | *Did you went?* | Did you go? |

### Verbes et construction

| Code | Erreur type | Forme correcte |
|---|---|---|
| `E.FR.CAN-TO` | *I can to swim* | I can swim |
| `E.FR.CAN-3S` | *He cans* | He can |
| `E.FR.LIKE-INFINITIVE` | *I like to swimming* | I like swimming |
| `E.FR.THERE-HAVE` | *It has a table* (calque de *il y a*) | There is a table |
| `E.FR.WEATHER-HAVE` | *It has sun / It makes cold* | It's sunny / It's cold |
| `E.FR.CONT-FOR-HABIT` | *I am working every day* | I work every day |
| `E.FR.IRREG-REGULARISED` | *goed, buyed* | went, bought |
| `E.FR.PLAY-DO-GO` | *I make football* | I play football |

### Lexique et prononciation

| Code | Erreur type | Forme correcte |
|---|---|---|
| `E.FR.UNCOUNT-PLURAL` | *informations, advices, furnitures* | information, advice |
| `E.FR.FALSE-FRIEND` | *actually, eventually, sensible, library, assist, deception* | now, possibly, sensitive, bookshop… |
| `E.FR.OF-CALQUE` | *the phone of my sister* | my sister's phone |
| `E.FR.PREP-CALQUE` | *on the morning, in Monday, depend of* | in the morning, on Monday, depend on |
| `E.FR.NUM-TEEN-TY` | confusion *thirteen / thirty* | accentuation contrastive |
| `E.FR.ED-ENDING` | terminaison *-ed* non prononcée | /t/ /d/ /ɪd/ |
| `E.FR.TH` | /θ/ réalisé /s/ ou /z/ | *think* ≠ *sink* |
| `E.FR.H-DROP` | *'ouse, 'e is* | /h/ aspiré |

*(Les trois dernières relèvent de la prononciation et sont **hors périmètre d'évaluation v1** — voir le §P3 de l'état des lieux. Elles restent enseignées et signalées, mais ne sont pas notées.)*

### Les 27 autres codes

| Code | Erreur type | Forme correcte |
|---|---|---|
| `E.FR.ART-A-AN` | *a apple, an university* | an apple, a university |
| `E.FR.ART-A-JOBS` | *I am developer* | I am a developer |
| `E.FR.ART-THE-ABSTRACT` | *The life is difficult* | Life is difficult |
| `E.FR.BECAUSE-OF` | *because of it is cheap* | because it is cheap |
| `E.FR.CAPITAL-DAYS` | *on monday in january* | on Monday in January |
| `E.FR.CAPITAL-NATION` | *I am cameroonian, I speak french* | I am Cameroonian, I speak French |
| `E.FR.CONT-BE-OMIT` | *I working now* | I'm working now |
| `E.FR.DATE-FORMAT` | *12/06* lu comme 12 juin | jour et mois en toutes lettres |
| `E.FR.DO-AUX-CAN` | *Do you can swim?* | Can you swim? |
| `E.FR.EMAIL-FORMAL-CALQUE` | *I pray you to accept…* | Best regards |
| `E.FR.GO-TO-HOME` | *I go to home* | I go home |
| `E.FR.GOING-TO-OMIT-BE` | *I going to travel* | I'm going to travel |
| `E.FR.HAVE-NEG` | *I have not a car* | I haven't got a car / I don't have a car |
| `E.FR.HOW-MUCH-MANY` | *How much apples?* | How many apples? |
| `E.FR.ING-SPELLING` | *writting, comeing* | writing, coming |
| `E.FR.ME-TOO-FLAT` | *Me too* après une négative | Me neither |
| `E.FR.PAST-BE-AGREE` | *They was late* | They were late |
| `E.FR.PAST-PRESENT-MIX` | *Yesterday I go to the market* | Yesterday I went to the market |
| `E.FR.POSS-AGREE` | *his sister* pour la sœur d'une femme | her sister |
| `E.FR.PREFER-THAN` | *I prefer tea than coffee* | I prefer tea to coffee |
| `E.FR.REFUSE-BLUNT` | *No.* | No, thank you. |
| `E.FR.SHORT-ANSWER-FLAT` | *Yes.* | Yes, I am. |
| `E.FR.SPELL-VOWELS` | E lu /e/, I lu /i/ à l'épellation | /iː/, /aɪ/ |
| `E.FR.THERE-AGREE` | *There is three rooms* | There are three rooms |
| `E.FR.THIS-IT` | *This is my brother, this is tall* | …, he is tall |
| `E.FR.THIS-THAT` | *that book here* | this book here |
| `E.FR.WANT-DIRECT` | *I want a coffee* | I'd like a coffee, please |

`E.FR.POSS-AGREE` mérite un mot : c'est l'erreur francophone la plus tenace de toutes, parce qu'en français le possessif s'accorde avec l'objet possédé (*sa sœur*) et en anglais avec le possesseur (*his* / *her sister*). Un francophone la commet encore couramment en B2. La traiter dès A1, en U03, est un investissement disproportionné en rendement.

---

## 16. Ce qui n'est pas dans ce fichier — et où ça va

| Élément | Fichier |
|---|---|
| Les phrases d'exemple, les exercices, les items à trous | **Générés à l'exécution** — jamais stockés |
| Les fiches d'enseignement détaillées par point de grammaire | `lingo-03-grammaire-A1.md` *(à produire)* |
| L'algorithme de session et les 4 types de session | `lingo-04-lesson-engine.md` *(à produire)* |
| Les règles anti-dérive et la politique de langue d'instruction | `lingo-05-regles-tuteur.md` *(à produire)* |
| Le test de placement initial | `lingo-06-placement.md` *(à produire)* |
| Les statuts, seuils et la carte de progression | `lingo-01-modele-etat.md` ✓ |

---

*Inventaire aligné sur les quatre modes du CECR — réception, production, interaction, médiation — la médiation n'étant pas descriptible en A1 au-delà de l'épellation et de la reformulation élémentaire, déjà couvertes en U00.*

**Source cadre** : [CEFR Companion Volume with New Descriptors — Council of Europe](https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2018/1680787989)
