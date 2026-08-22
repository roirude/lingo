#!/usr/bin/env python3
"""Génère lingo-a1-competences.yaml depuis la source unique, et valide la cohérence."""
import sys
from collections import Counter, defaultdict

# (id, fr, en, modes, grammar, errors, prereqs)
U = {}

U["U00"] = dict(
    theme="Langue de classe et de survie",
    theme_en="Classroom and survival language",
    functions=["gerer-l-incomprehension", "demander-de-l-aide"],
    lexis="L.A1.CLASSROOM",
    comps=[
        ("C01", "Comprendre les consignes courantes du tuteur", "Understand common classroom instructions", ["RO"], ["G.IMPERATIVE"], [], []),
        ("C02", "Demander de répéter, de ralentir ou d'expliquer", "Ask for repetition, slower speech or explanation", ["I"], ["G.CAN-REQUEST"], ["E.FR.CAN-TO"], []),
        ("C03", "Épeler son nom et comprendre un mot épelé", "Spell own name and understand a spelled word", ["I"], ["G.ALPHABET"], ["E.FR.SPELL-VOWELS"], []),
        ("C04", "Dire qu'on ne comprend pas et demander le sens d'un mot", "Say you don't understand and ask what a word means", ["I"], ["G.WH-Q", "G.DO-AUX"], ["E.FR.DO-AUX-OMIT"], []),
        ("C05", "Reconnaître et produire les nombres 0 à 20 à l'oral", "Recognise and produce numbers 0-20 orally", ["I"], ["G.NUM"], ["E.FR.NUM-TEEN-TY"], []),
        ("C06", "Comprendre une consigne écrite d'exercice simple", "Understand a simple written exercise instruction", ["RE"], ["G.IMPERATIVE"], [], ["A1.U00.C01"]),
    ])

U["U01"] = dict(
    theme="Identité et salutations", theme_en="Identity and greetings",
    functions=["saluer", "se-presenter", "presenter-un-tiers", "prendre-conge"],
    lexis="L.A1.GREETINGS",
    comps=[
        ("C01", "Saluer et prendre congé selon le moment de la journée", "Greet and say goodbye appropriately", ["I"], [], [], []),
        ("C02", "Se présenter en donnant son nom", "Introduce yourself by name", ["PO", "I"], ["G.BE-AFF", "G.POSS-ADJ", "G.CONTRACTIONS"], ["E.FR.BE-OMIT"], []),
        ("C03", "Demander le nom de quelqu'un et répondre à la question", "Ask someone's name and answer", ["I"], ["G.BE-Q", "G.WH-Q"], ["E.FR.BE-OMIT", "E.FR.Q-INTONATION"], ["A1.U01.C02"]),
        ("C04", "Présenter une tierce personne", "Introduce a third person", ["PO", "I"], ["G.DEMONSTRATIVES", "G.BE-AFF"], ["E.FR.THIS-IT"], ["A1.U01.C02"]),
        ("C05", "Dire d'où l'on vient (pays et ville)", "Say where you are from", ["PO", "I"], ["G.BE-AFF", "G.PREP-PLACE"], ["E.FR.BE-OMIT"], ["A1.U01.C02"]),
        ("C06", "Demander à quelqu'un d'où il vient", "Ask where someone is from", ["I"], ["G.BE-Q", "G.WH-Q"], ["E.FR.Q-INTONATION"], ["A1.U01.C05"]),
        ("C07", "Comprendre une présentation orale simple (nom, origine, métier)", "Understand a simple spoken self-introduction", ["RO"], ["G.BE-AFF"], [], ["A1.U01.C02"]),
        ("C08", "Écrire une présentation de soi de 3 à 4 phrases", "Write a 3-4 sentence self-introduction", ["PE"], ["G.BE-AFF", "G.PRON-SUBJ", "G.CONJ-BASIC"], ["E.FR.BE-OMIT", "E.FR.CAPITAL-NATION", "E.FR.AGE-HAVE"], ["A1.U01.C05"]),
    ])

U["U02"] = dict(
    theme="Informations personnelles", theme_en="Personal details",
    functions=["informer", "corriger", "confirmer"],
    lexis="L.A1.PERSONAL",
    comps=[
        ("C01", "Donner son âge et demander l'âge de quelqu'un", "Give and ask age", ["I"], ["G.BE-AFF", "G.BE-Q", "G.NUM"], ["E.FR.AGE-HAVE"], ["A1.U00.C05"]),
        ("C02", "Donner sa nationalité et les langues qu'on parle", "State nationality and languages spoken", ["PO", "I"], ["G.BE-AFF", "G.PRES-SIMPLE-AFF"], ["E.FR.CAPITAL-NATION", "E.FR.BE-OMIT"], ["A1.U01.C05"]),
        ("C03", "Donner son numéro de téléphone et son adresse e-mail à l'oral", "Give phone number and email orally", ["I"], ["G.NUM", "G.ALPHABET"], ["E.FR.NUM-TEEN-TY"], ["A1.U00.C03", "A1.U00.C05"]),
        ("C04", "Corriger une information fausse à son sujet", "Correct false information about yourself", ["I"], ["G.BE-NEG"], ["E.FR.NEG-PLACE"], ["A1.U02.C02"]),
        ("C05", "Répondre à des questions fermées avec la reprise correcte", "Answer yes/no questions with correct short answers", ["I"], ["G.SHORT-ANSWERS"], ["E.FR.SHORT-ANSWER-FLAT"], ["A1.U01.C03"]),
        ("C06", "Comprendre un formulaire d'inscription simple", "Understand a simple registration form", ["RE"], ["G.WH-Q", "G.NUM"], ["E.FR.FALSE-FRIEND"], []),
        ("C07", "Remplir un formulaire d'informations personnelles", "Fill in a personal details form", ["PE"], ["G.NUM", "G.ALPHABET"], ["E.FR.DATE-FORMAT", "E.FR.AGE-HAVE"], ["A1.U02.C06"]),
    ])

U["U03"] = dict(
    theme="Famille et entourage", theme_en="Family and people",
    functions=["decrire", "exprimer-la-possession", "interroger"],
    lexis="L.A1.FAMILY",
    comps=[
        ("C01", "Nommer les membres de sa famille", "Name family members", ["PO"], ["G.PLURAL-REG", "G.PLURAL-IRREG"], [], []),
        ("C02", "Décrire sa famille en plusieurs phrases liées", "Describe your family in connected sentences", ["PO"], ["G.HAVE-GOT", "G.POSS-ADJ", "G.CONJ-BASIC"], ["E.FR.3SG-S", "E.FR.POSS-AGREE"], ["A1.U03.C01"]),
        ("C03", "Dire à qui appartient quelque chose (génitif 's)", "Express possession with the Saxon genitive", ["PO", "PE"], ["G.POSS-S"], ["E.FR.OF-CALQUE"], ["A1.U03.C01"]),
        ("C04", "Poser des questions sur la famille de quelqu'un", "Ask about someone's family", ["I"], ["G.HAVE-GOT-Q", "G.WH-Q"], ["E.FR.DO-AUX-OMIT"], ["A1.U03.C02"]),
        ("C05", "Dire ce qu'on possède et ne possède pas", "Say what you have and don't have", ["PO", "I"], ["G.HAVE-GOT", "G.HAVE-GOT-NEG"], ["E.FR.HAVE-NEG"], []),
        ("C06", "Comprendre une description orale d'une famille", "Understand a spoken family description", ["RO"], ["G.POSS-S"], [], ["A1.U03.C03"]),
        ("C07", "Écrire un court texte sur sa famille (4 à 5 phrases)", "Write a short text about your family", ["PE"], ["G.HAVE-GOT", "G.POSS-ADJ"], ["E.FR.3SG-S", "E.FR.POSS-AGREE"], ["A1.U03.C02"]),
    ])

U["U04"] = dict(
    theme="Décrire personnes et objets", theme_en="Describing people and things",
    functions=["decrire", "designer", "identifier"],
    lexis="L.A1.DESCRIPTION",
    comps=[
        ("C01", "Décrire l'apparence physique d'une personne", "Describe someone's physical appearance", ["PO"], ["G.BE-AFF", "G.HAVE-GOT", "G.ADJ-POSITION"], ["E.FR.ADJ-AGREE", "E.FR.ADJ-ORDER"], ["A1.U03.C05"]),
        ("C02", "Décrire le caractère de quelqu'un en termes simples", "Describe someone's character simply", ["PO"], ["G.BE-AFF", "G.ADJ-POSITION"], ["E.FR.ADJ-AGREE", "E.FR.FALSE-FRIEND"], ["A1.U04.C01"]),
        ("C03", "Nommer et décrire un objet du quotidien (couleur, taille)", "Name and describe an everyday object", ["PO"], ["G.ART-A-AN", "G.ADJ-POSITION"], ["E.FR.ADJ-ORDER", "E.FR.ART-A-AN"], []),
        ("C04", "Désigner un objet proche ou éloigné", "Point out near and distant objects", ["I"], ["G.DEMONSTRATIVES"], ["E.FR.THIS-THAT"], ["A1.U04.C03"]),
        ("C05", "Demander le nom d'un objet et y répondre", "Ask what something is and answer", ["I"], ["G.WH-Q", "G.BE-Q"], ["E.FR.THIS-IT"], ["A1.U04.C04"]),
        ("C06", "Comprendre une description simple de personne ou d'objet", "Understand a simple description", ["RO", "RE"], ["G.ADJ-POSITION"], [], ["A1.U04.C01"]),
        ("C07", "Lire une petite annonce d'objet et en extraire l'essentiel", "Read a simple classified ad", ["RE"], ["G.ADJ-POSITION", "G.NUM"], ["E.FR.FALSE-FRIEND"], ["A1.U04.C03"]),
    ])

U["U05"] = dict(
    theme="Logement et lieux", theme_en="Home and places",
    functions=["decrire-un-lieu", "situer", "demander-son-chemin"],
    lexis="L.A1.HOME",
    comps=[
        ("C01", "Dire où l'on habite", "Say where you live", ["PO", "I"], ["G.PRES-SIMPLE-AFF", "G.PREP-PLACE"], ["E.FR.PREP-CALQUE"], ["A1.U01.C05"]),
        ("C02", "Nommer les pièces d'un logement et le mobilier courant", "Name rooms and common furniture", ["PO"], ["G.PLURAL-REG"], [], []),
        ("C03", "Dire ce qu'il y a et ce qu'il n'y a pas dans un lieu", "Say what there is and isn't in a place", ["PO", "PE"], ["G.THERE-IS-ARE", "G.SOME-ANY"], ["E.FR.THERE-HAVE", "E.FR.THERE-AGREE"], ["A1.U05.C02"]),
        ("C04", "Situer un objet dans l'espace", "Locate an object in space", ["PO"], ["G.PREP-PLACE"], ["E.FR.PREP-CALQUE"], ["A1.U05.C02"]),
        ("C05", "Nommer les lieux courants de la ville", "Name common places in town", ["PO"], ["G.ART-THE"], ["E.FR.ART-THE-ABSTRACT"], []),
        ("C06", "Demander et donner une indication de chemin très simple", "Ask for and give very simple directions", ["I"], ["G.IMPERATIVE", "G.PREP-PLACE"], ["E.FR.GO-TO-HOME"], ["A1.U05.C05"]),
        ("C07", "Comprendre des indications de lieu et suivre un itinéraire simple", "Understand simple directions", ["RO"], ["G.PREP-PLACE", "G.IMPERATIVE"], [], ["A1.U05.C06"]),
        ("C08", "Écrire une description de son logement (5 à 6 phrases)", "Write a description of your home", ["PE"], ["G.THERE-IS-ARE", "G.PREP-PLACE"], ["E.FR.THERE-HAVE"], ["A1.U05.C03"]),
    ])

U["U06"] = dict(
    theme="Routine quotidienne", theme_en="Daily routine",
    functions=["parler-d-habitudes", "situer-dans-le-temps", "interroger-sur-les-habitudes"],
    lexis="L.A1.ROUTINE", pivot=True,
    comps=[
        ("C01", "Décrire sa journée type dans l'ordre chronologique", "Describe your typical day in order", ["PO", "PE"], ["G.PRES-SIMPLE-AFF", "G.PREP-TIME", "G.CONJ-BASIC"], ["E.FR.PREP-CALQUE"], []),
        ("C02", "Dire l'heure et demander l'heure", "Tell and ask the time", ["I"], ["G.NUM", "G.PREP-TIME"], ["E.FR.NUM-TEEN-TY"], ["A1.U00.C05"]),
        ("C03", "Décrire les habitudes d'une autre personne (3e personne)", "Describe another person's habits", ["PO"], ["G.PRES-SIMPLE-3S"], ["E.FR.3SG-S"], ["A1.U06.C01"]),
        ("C04", "Nommer les jours, les mois et les moments de la journée", "Name days, months and parts of the day", ["PO"], ["G.PREP-TIME"], ["E.FR.PREP-CALQUE", "E.FR.CAPITAL-DAYS"], []),
        ("C05", "Dire à quelle fréquence on fait quelque chose", "Say how often you do something", ["PO"], ["G.ADV-FREQ"], ["E.FR.ADV-FREQ-PLACE"], ["A1.U06.C01"]),
        ("C06", "Dire ce qu'on ne fait pas (forme négative)", "Say what you don't do", ["PO"], ["G.PRES-SIMPLE-NEG"], ["E.FR.DO-AUX-OMIT", "E.FR.NEG-3S-DOUBLE"], ["A1.U06.C01"]),
        ("C07", "Poser des questions sur la routine de quelqu'un", "Ask about someone's routine", ["I"], ["G.PRES-SIMPLE-Q", "G.WH-Q"], ["E.FR.DO-AUX-OMIT", "E.FR.Q-INTONATION"], ["A1.U06.C03"]),
        ("C08", "Comprendre le récit oral d'une routine et en extraire les horaires", "Understand a spoken routine and extract times", ["RO"], ["G.PRES-SIMPLE-AFF", "G.PREP-TIME"], [], ["A1.U06.C02"]),
    ])

U["U07"] = dict(
    theme="Travail et études", theme_en="Work and study",
    functions=["parler-de-son-activite", "interroger"],
    lexis="L.A1.WORK",
    comps=[
        ("C01", "Dire quel est son métier ou ce qu'on étudie", "Say what your job is or what you study", ["PO", "I"], ["G.ART-A-JOBS", "G.BE-AFF"], ["E.FR.ART-A-JOBS"], ["A1.U01.C02"]),
        ("C02", "Demander à quelqu'un ce qu'il fait dans la vie", "Ask what someone does for a living", ["I"], ["G.PRES-SIMPLE-Q"], ["E.FR.DO-AUX-OMIT"], ["A1.U06.C07"]),
        ("C03", "Décrire son lieu de travail ou d'études", "Describe your workplace or school", ["PO"], ["G.THERE-IS-ARE", "G.PREP-PLACE"], ["E.FR.THERE-HAVE"], ["A1.U05.C03"]),
        ("C04", "Dire ce qu'on fait concrètement dans son travail", "Say what you actually do at work", ["PO"], ["G.PRES-SIMPLE-AFF"], ["E.FR.3SG-S"], ["A1.U07.C01"]),
        ("C05", "Parler de ses horaires de travail ou de cours", "Talk about your working or class hours", ["PO", "I"], ["G.PREP-TIME", "G.NUM"], ["E.FR.PREP-CALQUE"], ["A1.U06.C02"]),
        ("C06", "Comprendre une présentation professionnelle simple", "Understand a simple professional introduction", ["RO"], ["G.PRES-SIMPLE-AFF"], [], ["A1.U07.C01"]),
        ("C07", "Lire une carte de visite ou une offre d'emploi très simple", "Read a business card or very simple job ad", ["RE"], ["G.ART-A-JOBS", "G.NUM"], ["E.FR.FALSE-FRIEND"], ["A1.U07.C01"]),
    ])

U["U08"] = dict(
    theme="Goûts et temps libre", theme_en="Likes and free time",
    functions=["exprimer-un-gout", "exprimer-une-preference", "justifier", "reagir"],
    lexis="L.A1.LEISURE",
    comps=[
        ("C01", "Dire ce qu'on aime et ce qu'on n'aime pas", "Say what you like and dislike", ["PO", "I"], ["G.LIKE-ING", "G.PRES-SIMPLE-NEG", "G.OBJ-PRON"], ["E.FR.LIKE-INFINITIVE", "E.FR.ADV-MUCH-PLACE"], ["A1.U06.C06"]),
        ("C02", "Exprimer une préférence entre deux choses", "Express a preference between two things", ["PO", "I"], ["G.PREFER", "G.CONJ-BASIC"], ["E.FR.PREFER-THAN"], ["A1.U08.C01"]),
        ("C03", "Demander à quelqu'un ce qu'il aime", "Ask what someone likes", ["I"], ["G.PRES-SIMPLE-Q", "G.LIKE-ING"], ["E.FR.DO-AUX-OMIT"], ["A1.U08.C01"]),
        ("C04", "Parler de ses loisirs et du sport qu'on pratique", "Talk about hobbies and sport", ["PO"], ["G.PRES-SIMPLE-AFF", "G.PLAY-DO-GO"], ["E.FR.PLAY-DO-GO"], []),
        ("C05", "Justifier un goût avec « because »", "Justify a preference with because", ["PO"], ["G.CONJ-BECAUSE"], ["E.FR.BECAUSE-OF"], ["A1.U08.C01"]),
        ("C06", "Réagir à ce que dit l'interlocuteur", "React to what the other person says", ["I"], ["G.SO-NEITHER", "G.SHORT-ANSWERS"], ["E.FR.ME-TOO-FLAT"], ["A1.U02.C05"]),
        ("C07", "Écrire un court message sur ses loisirs", "Write a short message about your free time", ["PE"], ["G.LIKE-ING", "G.CONJ-BECAUSE"], ["E.FR.LIKE-INFINITIVE"], ["A1.U08.C05"]),
        ("C08", "Comprendre quelqu'un qui parle de ses goûts et identifier ce qu'il aime", "Understand someone talking about their likes", ["RO"], ["G.LIKE-ING", "G.CONJ-BECAUSE"], [], ["A1.U08.C01"]),
    ])

U["U09"] = dict(
    theme="Capacités, demandes et permission", theme_en="Ability, requests and permission",
    functions=["exprimer-une-capacite", "demander", "autoriser", "refuser"],
    lexis="L.A1.ABILITY",
    comps=[
        ("C01", "Dire ce qu'on sait faire et ce qu'on ne sait pas faire", "Say what you can and can't do", ["PO", "I"], ["G.CAN-ABILITY"], ["E.FR.CAN-TO", "E.FR.CAN-3S"], []),
        ("C02", "Demander à quelqu'un s'il sait faire quelque chose", "Ask if someone can do something", ["I"], ["G.CAN-Q"], ["E.FR.CAN-TO", "E.FR.DO-AUX-CAN"], ["A1.U09.C01"]),
        ("C03", "Demander quelque chose poliment", "Make a polite request", ["I"], ["G.CAN-REQUEST", "G.WOULD-LIKE"], ["E.FR.WANT-DIRECT"], ["A1.U00.C02"]),
        ("C04", "Demander et donner la permission", "Ask for and give permission", ["I"], ["G.CAN-REQUEST"], ["E.FR.CAN-TO"], ["A1.U09.C03"]),
        ("C05", "Accepter ou refuser poliment une proposition", "Accept or politely decline an offer", ["I"], ["G.SHORT-ANSWERS"], ["E.FR.REFUSE-BLUNT"], ["A1.U09.C03"]),
        ("C06", "Comprendre une demande ou une consigne polie", "Understand a polite request", ["RO"], ["G.CAN-REQUEST"], [], ["A1.U09.C03"]),
        ("C07", "Écrire un message court de demande (SMS, e-mail bref)", "Write a short request message", ["PE"], ["G.CAN-REQUEST", "G.WOULD-LIKE"], ["E.FR.EMAIL-FORMAL-CALQUE"], ["A1.U09.C03"]),
    ])

U["U10"] = dict(
    theme="Nourriture, achats et prix", theme_en="Food, shopping and prices",
    functions=["commander", "acheter", "demander-un-prix", "parler-d-habitudes"],
    lexis="L.A1.FOOD",
    comps=[
        ("C01", "Nommer les aliments et boissons courants", "Name common food and drink", ["PO"], ["G.PLURAL-REG"], [], []),
        ("C02", "Employer correctement dénombrables et indénombrables", "Use countable and uncountable nouns correctly", ["PO", "PE"], ["G.COUNT-UNCOUNT", "G.SOME-ANY"], ["E.FR.UNCOUNT-PLURAL"], ["A1.U10.C01"]),
        ("C03", "Demander une quantité et un prix", "Ask about quantity and price", ["I"], ["G.HOW-MUCH-MANY", "G.NUM"], ["E.FR.HOW-MUCH-MANY", "E.FR.NUM-TEEN-TY"], ["A1.U10.C02"]),
        ("C04", "Commander dans un café ou un restaurant", "Order in a cafe or restaurant", ["I"], ["G.WOULD-LIKE"], ["E.FR.WANT-DIRECT"], ["A1.U09.C03"]),
        ("C05", "Faire un achat simple et gérer la transaction", "Make a simple purchase", ["I"], ["G.WOULD-LIKE", "G.NUM"], ["E.FR.WANT-DIRECT"], ["A1.U10.C03"]),
        ("C06", "Dire ses habitudes alimentaires", "Talk about your eating habits", ["PO"], ["G.PRES-SIMPLE-AFF", "G.ADV-FREQ"], ["E.FR.ADV-FREQ-PLACE", "E.FR.UNCOUNT-PLURAL"], ["A1.U06.C05"]),
        ("C07", "Comprendre un prix annoncé oralement et vérifier la monnaie", "Understand a spoken price and check change", ["RO"], ["G.NUM"], ["E.FR.NUM-TEEN-TY"], ["A1.U10.C03"]),
        ("C08", "Lire un menu et une étiquette de prix", "Read a menu and a price tag", ["RE"], ["G.NUM"], ["E.FR.FALSE-FRIEND"], ["A1.U10.C01"]),
    ])

U["U11"] = dict(
    theme="Ce qui se passe maintenant", theme_en="What is happening now",
    functions=["decrire-l-instant", "decrire-une-image"],
    lexis="L.A1.NOW",
    comps=[
        ("C01", "Dire ce qu'on est en train de faire", "Say what you are doing right now", ["PO", "I"], ["G.PRES-CONT"], ["E.FR.CONT-BE-OMIT", "E.FR.ING-SPELLING"], ["A1.U06.C01"]),
        ("C02", "Demander ce que quelqu'un fait en ce moment", "Ask what someone is doing now", ["I"], ["G.PRES-CONT-Q"], ["E.FR.CONT-BE-OMIT"], ["A1.U11.C01"]),
        ("C03", "Décrire une image ou une scène", "Describe a picture or scene", ["PO", "PE"], ["G.PRES-CONT", "G.THERE-IS-ARE"], ["E.FR.THERE-HAVE"], ["A1.U11.C01"]),
        ("C04", "Distinguer une habitude d'une action en cours", "Distinguish a habit from an action in progress", ["PO"], ["G.PRES-CONT-VS-SIMPLE"], ["E.FR.CONT-FOR-HABIT"], ["A1.U11.C01", "A1.U06.C03"]),
        ("C05", "Parler du temps qu'il fait", "Talk about the weather", ["PO", "I"], ["G.WEATHER-IT"], ["E.FR.WEATHER-HAVE"], []),
        ("C06", "Nommer les vêtements et décrire ce que quelqu'un porte", "Name clothes and describe what someone is wearing", ["PO"], ["G.PRES-CONT", "G.ADJ-POSITION"], ["E.FR.ADJ-AGREE"], ["A1.U11.C01"]),
        ("C07", "Écrire une légende décrivant ce qui se passe sur une photo", "Write a caption describing a photo", ["PE"], ["G.PRES-CONT"], ["E.FR.ING-SPELLING"], ["A1.U11.C03"]),
        ("C08", "Comprendre une description orale d'une scène en cours", "Understand a spoken description of an ongoing scene", ["RO"], ["G.PRES-CONT", "G.THERE-IS-ARE"], [], ["A1.U11.C01"]),
    ])

U["U12"] = dict(
    theme="Passé et futur simples", theme_en="Simple past and future",
    functions=["raconter", "situer-dans-le-temps", "annoncer-une-intention"],
    lexis="L.A1.PASTFUTURE",
    comps=[
        ("C01", "Dire où l'on était et comment c'était", "Say where you were and how it was", ["PO"], ["G.PAST-BE"], ["E.FR.PAST-BE-AGREE"], ["A1.U01.C05"]),
        ("C02", "Raconter une action passée avec des verbes réguliers", "Narrate a past action with regular verbs", ["PO", "PE"], ["G.PAST-SIMPLE-REG"], ["E.FR.ED-ENDING", "E.FR.PAST-PRESENT-MIX"], ["A1.U12.C01"]),
        ("C03", "Employer les 15 verbes irréguliers les plus fréquents au passé", "Use the 15 most frequent irregular past forms", ["PO", "PE"], ["G.PAST-SIMPLE-IRREG"], ["E.FR.IRREG-REGULARISED"], ["A1.U12.C02"]),
        ("C04", "Poser une question au passé", "Ask a question in the past", ["I"], ["G.PAST-Q"], ["E.FR.DID-DOUBLE-PAST", "E.FR.DO-AUX-OMIT"], ["A1.U12.C02"]),
        ("C05", "Dire ce qu'on va faire (intention)", "Say what you are going to do", ["PO", "I"], ["G.GOING-TO"], ["E.FR.GOING-TO-OMIT-BE"], ["A1.U11.C01"]),
        ("C06", "Situer un événement dans le temps", "Place an event in time", ["PO", "PE"], ["G.TIME-MARKERS"], ["E.FR.PREP-CALQUE"], ["A1.U12.C02"]),
        ("C07", "Raconter brièvement son week-end à l'oral", "Briefly narrate your weekend orally", ["PO"], ["G.PAST-SIMPLE-REG", "G.PAST-SIMPLE-IRREG", "G.CONJ-BASIC"], ["E.FR.PAST-PRESENT-MIX"], ["A1.U12.C03"]),
        ("C08", "Écrire un court récit au passé (4 à 5 phrases liées)", "Write a short past narrative", ["PE"], ["G.PAST-SIMPLE-REG", "G.CONJ-BASIC"], ["E.FR.ED-ENDING"], ["A1.U12.C07"]),
        ("C09", "Comprendre un court récit au passé et en extraire les événements", "Understand a short past narrative and extract the events", ["RO"], ["G.PAST-SIMPLE-REG", "G.PAST-SIMPLE-IRREG", "G.TIME-MARKERS"], [], ["A1.U12.C03"]),
    ])

GRAMMAR = """G.BE-AFF G.BE-NEG G.BE-Q G.SHORT-ANSWERS G.CONTRACTIONS G.PRON-SUBJ
G.ART-A-AN G.ART-THE G.ART-A-JOBS G.PLURAL-REG G.PLURAL-IRREG G.DEMONSTRATIVES
G.COUNT-UNCOUNT G.SOME-ANY G.POSS-ADJ G.POSS-S G.HAVE-GOT G.HAVE-GOT-NEG
G.HAVE-GOT-Q G.ADJ-POSITION G.PRES-SIMPLE-AFF G.PRES-SIMPLE-3S G.PRES-SIMPLE-NEG
G.PRES-SIMPLE-Q G.PRES-CONT G.PRES-CONT-Q G.PRES-CONT-VS-SIMPLE G.PAST-BE
G.PAST-SIMPLE-REG G.PAST-SIMPLE-IRREG G.PAST-Q G.GOING-TO G.CAN-ABILITY G.CAN-Q
G.CAN-REQUEST G.WOULD-LIKE G.IMPERATIVE G.PREP-PLACE G.PREP-TIME G.ADV-FREQ
G.TIME-MARKERS G.CONJ-BASIC G.CONJ-BECAUSE G.WH-Q G.DO-AUX G.OBJ-PRON G.NUM
G.ALPHABET G.THERE-IS-ARE G.SO-NEITHER G.LIKE-ING G.PREFER G.PLAY-DO-GO
G.WEATHER-IT G.HOW-MUCH-MANY""".split()

CORE_ERRORS = ["E.FR.AGE-HAVE", "E.FR.3SG-S", "E.FR.DO-AUX-OMIT", "E.FR.BE-OMIT"]
PRONUNCIATION_ERRORS = ["E.FR.ED-ENDING", "E.FR.TH", "E.FR.H-DROP", "E.FR.NUM-TEEN-TY", "E.FR.SPELL-VOWELS"]

# code: (libellé FR, forme fautive typique, forme correcte)
ERROR_DEFS = {
 "E.FR.AGE-HAVE": ("avoir l'âge au lieu de être", "I have 25 years", "I'm 25"),
 "E.FR.3SG-S": ("omission du -s à la 3e personne", "He work in marketing", "He works in marketing"),
 "E.FR.DO-AUX-OMIT": ("question sans auxiliaire do", "Where you live?", "Where do you live?"),
 "E.FR.BE-OMIT": ("omission du verbe be", "I student", "I'm a student"),
 "E.FR.ADJ-AGREE": ("accord de l'adjectif", "greens cars", "green cars"),
 "E.FR.ADJ-ORDER": ("adjectif postposé", "a car red", "a red car"),
 "E.FR.ADV-FREQ-PLACE": ("place de l'adverbe de fréquence", "I go often to church", "I often go to church"),
 "E.FR.ADV-MUCH-PLACE": ("place de very much", "I like very much football", "I like football very much"),
 "E.FR.NEG-PLACE": ("place de la négation", "I not am tired", "I'm not tired"),
 "E.FR.Q-INTONATION": ("question marquée par la seule intonation", "You like football?", "Do you like football?"),
 "E.FR.NEG-3S-DOUBLE": ("double marque de 3e personne au négatif", "He doesn't works", "He doesn't work"),
 "E.FR.DID-DOUBLE-PAST": ("double marque du passé après did", "Did you went?", "Did you go?"),
 "E.FR.CAN-TO": ("to après un modal", "I can to swim", "I can swim"),
 "E.FR.CAN-3S": ("accord de can", "He cans swim", "He can swim"),
 "E.FR.DO-AUX-CAN": ("do avec can", "Do you can swim?", "Can you swim?"),
 "E.FR.LIKE-INFINITIVE": ("to + -ing après like", "I like to swimming", "I like swimming"),
 "E.FR.THERE-HAVE": ("calque de il y a", "It has a table", "There is a table"),
 "E.FR.THERE-AGREE": ("accord de there is/are", "There is three rooms", "There are three rooms"),
 "E.FR.WEATHER-HAVE": ("calque météo", "It has sun / It makes cold", "It's sunny / It's cold"),
 "E.FR.CONT-FOR-HABIT": ("continu employé pour l'habitude", "I am working every day", "I work every day"),
 "E.FR.CONT-BE-OMIT": ("omission de be au continu", "I working now", "I'm working now"),
 "E.FR.ING-SPELLING": ("orthographe du -ing", "writting, comeing", "writing, coming"),
 "E.FR.IRREG-REGULARISED": ("irrégulier régularisé", "goed, buyed", "went, bought"),
 "E.FR.PAST-BE-AGREE": ("accord de was/were", "They was late", "They were late"),
 "E.FR.PAST-PRESENT-MIX": ("mélange passé/présent dans un récit", "Yesterday I go to the market", "Yesterday I went to the market"),
 "E.FR.GOING-TO-OMIT-BE": ("omission de be devant going to", "I going to travel", "I'm going to travel"),
 "E.FR.PLAY-DO-GO": ("mauvais verbe support pour le sport", "I make football", "I play football"),
 "E.FR.UNCOUNT-PLURAL": ("pluriel d'indénombrable", "informations, advices, furnitures", "information, advice, furniture"),
 "E.FR.HOW-MUCH-MANY": ("how much / how many", "How much apples?", "How many apples?"),
 "E.FR.FALSE-FRIEND": ("faux ami", "actually, eventually, sensible, library, assist, deception", "now, possibly, sensitive, bookshop, attend, disappointment"),
 "E.FR.OF-CALQUE": ("calque du complément du nom", "the phone of my sister", "my sister's phone"),
 "E.FR.PREP-CALQUE": ("préposition calquée du français", "on the morning, in Monday, depend of", "in the morning, on Monday, depend on"),
 "E.FR.GO-TO-HOME": ("to devant home", "I go to home", "I go home"),
 "E.FR.POSS-AGREE": ("accord de l'adjectif possessif sur le possédé", "his sister for a woman's sister", "her sister"),
 "E.FR.HAVE-NEG": ("négation de have got", "I have not a car", "I haven't got a car / I don't have a car"),
 "E.FR.THIS-IT": ("this au lieu de it/he/she", "This is my brother, this is tall", "This is my brother, he is tall"),
 "E.FR.THIS-THAT": ("confusion this/that, these/those", "that book here", "this book here"),
 "E.FR.ART-A-AN": ("choix de a/an", "a apple, an university", "an apple, a university"),
 "E.FR.ART-A-JOBS": ("omission de l'article devant le métier", "I am developer", "I am a developer"),
 "E.FR.ART-THE-ABSTRACT": ("the devant un nom général", "The life is difficult", "Life is difficult"),
 "E.FR.SHORT-ANSWER-FLAT": ("réponse courte sans reprise", "Yes.", "Yes, I am."),
 "E.FR.ME-TOO-FLAT": ("réaction sans reprise adaptée", "Me too (après une négative)", "Me neither"),
 "E.FR.PREFER-THAN": ("prefer ... than", "I prefer tea than coffee", "I prefer tea to coffee"),
 "E.FR.BECAUSE-OF": ("because of + proposition", "because of it is cheap", "because it is cheap"),
 "E.FR.WANT-DIRECT": ("demande trop directe", "I want a coffee", "I'd like a coffee, please"),
 "E.FR.REFUSE-BLUNT": ("refus abrupt", "No.", "No, thank you."),
 "E.FR.EMAIL-FORMAL-CALQUE": ("formule de politesse calquée", "I pray you to accept...", "Best regards"),
 "E.FR.CAPITAL-NATION": ("majuscule aux nationalités et langues", "I am cameroonian, I speak french", "I am Cameroonian, I speak French"),
 "E.FR.CAPITAL-DAYS": ("majuscule aux jours et mois", "on monday in january", "on Monday in January"),
 "E.FR.DATE-FORMAT": ("format de date", "12/06 lu comme 12 juin", "préciser jour et mois en toutes lettres"),
 "E.FR.NUM-TEEN-TY": ("confusion thirteen/thirty", "thirteen prononcé comme thirty", "accentuation contrastive"),
 "E.FR.ED-ENDING": ("terminaison -ed non prononcée", "worked prononcé /wɜːk/", "/wɜːkt/"),
 "E.FR.SPELL-VOWELS": ("noms des voyelles à l'épellation", "E lu comme /e/, I comme /i/", "/iː/, /aɪ/"),
 "E.FR.TH": ("th réalisé /s/ ou /z/", "think prononcé sink", "/θɪŋk/"),
 "E.FR.H-DROP": ("h non aspiré", "'ouse, 'e is", "house, he is"),
}


def all_comps():
    for unit, d in U.items():
        for c in d["comps"]:
            yield unit, d, c


def build_yaml():
    L = []
    L.append("# Lingo — Inventaire des compétences A1")
    L.append("# Généré par build_a1.py — ne pas éditer à la main.")
    n_comp = sum(len(d["comps"]) for d in U.values())
    L.append(f"# SOMMAIRE : {len(U)} unités (U00-U12), {n_comp} compétences,")
    L.append(f"#            {len(GRAMMAR)} points de grammaire, {len(ERROR_DEFS)} erreurs francophones indexées.")
    L.append("# Sections de ce fichier : units | grammar_inventory | core_errors |")
    L.append("#                          pronunciation_out_of_scope_v1 | errors")
    L.append("# Modes : I interaction | PO production orale | PE production écrite")
    L.append("#         RO réception orale | RE réception écrite")
    L.append("---")
    L.append("level: A1")
    L.append("l1_target: fr")
    L.append("units:")
    for unit, d in U.items():
        L.append(f"  {unit}:")
        L.append(f"    theme: {d['theme']!r}")
        L.append(f"    theme_en: {d['theme_en']!r}")
        L.append(f"    lexis: {d['lexis']}")
        if d.get("pivot"):
            L.append("    pivot: true")
        L.append("    functions: [%s]" % ", ".join(d["functions"]))
        L.append("    competencies:")
        for cid, fr, en, modes, gram, errs, pre in d["comps"]:
            L.append(f"      - id: A1.{unit}.{cid}")
            L.append(f"        fr: {fr!r}")
            L.append(f"        en: {en!r}")
            L.append("        modes: [%s]" % ", ".join(modes))
            L.append("        grammar: [%s]" % ", ".join(gram))
            L.append("        errors: [%s]" % ", ".join(errs))
            L.append("        prereqs: [%s]" % ", ".join(pre))
    L.append("grammar_inventory: [%s]" % ", ".join(GRAMMAR))
    L.append("core_errors: [%s]" % ", ".join(CORE_ERRORS))
    L.append("pronunciation_out_of_scope_v1: [%s]" % ", ".join(PRONUNCIATION_ERRORS))
    L.append("errors:")
    for code in sorted(ERROR_DEFS):
        lab, bad, good = ERROR_DEFS[code]
        L.append(f"  {code}:")
        L.append(f"    label: {lab!r}")
        L.append(f"    wrong: {bad!r}")
        L.append(f"    right: {good!r}")
        L.append(f"    core: {str(code in CORE_ERRORS).lower()}")
        L.append(f"    scored_v1: {str(code not in PRONUNCIATION_ERRORS).lower()}")
    return "\n".join(L) + "\n"


def validate():
    problems, ids = [], []
    modes, gram_used, err_used = Counter(), Counter(), Counter()
    per_unit = Counter()

    for unit, d, (cid, fr, en, m, g, e, pre) in all_comps():
        full = f"A1.{unit}.{cid}"
        ids.append(full)
        per_unit[unit] += 1
        for x in m:
            modes[x] += 1
        for x in g:
            gram_used[x] += 1
        for x in e:
            err_used[x] += 1
        if not m:
            problems.append(f"{full} : aucun mode")
        if not g and unit != "U01":
            problems.append(f"{full} : aucune ressource grammaticale")
        for x in g:
            if x not in GRAMMAR:
                problems.append(f"{full} : grammaire inconnue {x}")

    dupes = [k for k, v in Counter(ids).items() if v > 1]
    for dnm in dupes:
        problems.append(f"identifiant dupliqué : {dnm}")

    idset = set(ids)
    for unit, d, (cid, *_rest) in all_comps():
        pre = _rest[5]
        for p in pre:
            if p not in idset:
                problems.append(f"A1.{unit}.{cid} : prérequis inexistant {p}")

    unused = [g for g in GRAMMAR if g not in gram_used]
    for g in unused:
        problems.append(f"grammaire jamais utilisée : {g}")

    for u in U:
        if not any("RO" in c[3] or "RE" in c[3] for c in U[u]["comps"]):
            problems.append(f"{u} : aucune compétence réceptive (condition 4 de maîtrise inatteignable)")

    for ce in CORE_ERRORS:
        if err_used[ce] < 2:
            problems.append(f"erreur noyau {ce} surveillée sur {err_used[ce]} compétence(s) seulement")

    for code in err_used:
        if code not in ERROR_DEFS:
            problems.append(f"erreur sans définition : {code}")
    for code in ERROR_DEFS:
        if code not in err_used and code not in PRONUNCIATION_ERRORS:
            problems.append(f"erreur définie mais rattachée à aucune compétence : {code}")

    return problems, ids, modes, gram_used, err_used, per_unit


if __name__ == "__main__":
    open("/home/claude/lingo-a1-competences.yaml", "w").write(build_yaml())
    problems, ids, modes, gram_used, err_used, per_unit = validate()

    print("=" * 62)
    print("VALIDATION — Inventaire A1")
    print("=" * 62)
    print(f"Compétences        : {len(ids)}")
    print(f"Identifiants uniques: {len(set(ids))}")
    print(f"Unités             : {len(U)}")
    print(f"Grammaire déclarée : {len(GRAMMAR)}  |  utilisée : {len(gram_used)}")
    print(f"Erreurs FR indexées: {len(err_used)}")
    print()
    print("Par unité :", "  ".join(f"{k}:{v}" for k, v in sorted(per_unit.items())))
    print()
    print("Répartition par mode :")
    for m in ["I", "PO", "PE", "RO", "RE"]:
        print(f"   {m:<3} {modes[m]:>3}")
    print()
    print("Top erreurs surveillées :")
    for e, n in err_used.most_common(8):
        print(f"   {e:<24} {n} compétence(s)")
    print()
    if problems:
        print(f"PROBLÈMES ({len(problems)}) :")
        for p in problems:
            print("   -", p)
        sys.exit(1)
    print("Aucun problème détecté.")
