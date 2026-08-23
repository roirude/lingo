#!/usr/bin/env python3
"""Génère skill/curriculum-a2.yaml et valide la cohérence, y compris les prérequis
qui pointent vers A1. À lancer depuis la racine du dépôt."""
import sys, yaml
from collections import Counter

U = {}

U["U00"] = dict(
    theme="Stratégies de discours", theme_en="Discourse strategies",
    functions=["developper", "enchainer", "nuancer", "relancer", "reparer"],
    lexis="L.A2.DISCOURSE", transversal=True,
    comps=[
      ("C01","Développer une réponse au-delà d'une phrase : fait + raison + exemple","Extend an answer beyond one sentence",["PO","I"],["G.CONN-A2","G.CONJ-BECAUSE"],["E.FR.MINIMAL-ANSWER"],["A1.U08.C05"]),
      ("C02","Enchaîner ses idées avec des connecteurs","Link ideas with connectors",["PO","PE"],["G.CONN-A2"],["E.FR.AND-CHAIN"],["A2.U00.C01"]),
      ("C03","Nuancer une affirmation (quite, really, a bit, not very)","Hedge a statement",["PO","I"],["G.HEDGING","G.ADV-DEGREE"],["E.FR.TOO-VERY"],["A2.U00.C01"]),
      ("C04","Relancer l'échange et rendre la parole","Hand the turn back",["I"],["G.SHORT-Q-BACK"],["E.FR.NO-TURN-BACK"],["A1.U08.C06"]),
      ("C05","Contourner un mot qu'on ne connaît pas par la paraphrase","Paraphrase an unknown word",["PO","I"],["G.PARAPHRASE","G.RELATIVE-BASIC"],["E.FR.CODE-SWITCH"],["A2.U00.C01"]),
      ("C06","Demander une clarification précise","Ask for precise clarification",["I"],["G.EMBEDDED-Q"],["E.FR.EMBEDDED-Q-ORDER"],["A1.U00.C04"]),
      ("C07","Gagner du temps sans se taire (well, let me think, actually)","Buy time without freezing",["I"],["G.FILLERS"],["E.FR.FALSE-FRIEND"],["A2.U00.C01"]),
      ("C08","Comprendre un interlocuteur à débit normal et faire répéter le point manqué","Understand normal-speed speech and target the repair",["RO","I"],["G.EMBEDDED-Q"],[],["A2.U00.C06"]),
    ])

U["U01"] = dict(
    theme="Expériences vécues", theme_en="Life experiences",
    functions=["raconter-une-experience","interroger-sur-l-experience"],
    lexis="L.A2.EXPERIENCE",
    comps=[
      ("C01","Dire ce qu'on a déjà fait et ce qu'on n'a jamais fait","Say what you have and haven't done",["PO","I"],["G.PRES-PERF","G.PRES-PERF-EVER-NEVER"],["E.FR.PP-FORM","E.FR.PP-FOR-PAST"],["A1.U12.C03"]),
      ("C02","Demander à quelqu'un s'il a déjà fait quelque chose","Ask about someone's experience",["I"],["G.PRES-PERF-Q"],["E.FR.PP-FORM"],["A2.U01.C01"]),
      ("C03","Raconter une expérience marquante et la développer","Narrate a memorable experience and develop it",["PO"],["G.PRES-PERF","G.PAST-SIMPLE-REG","G.CONN-A2"],["E.FR.PP-FOR-PAST","E.FR.MINIMAL-ANSWER"],["A2.U00.C01","A2.U01.C01"]),
      ("C04","Employer just, already et yet","Use just, already and yet",["PO","PE"],["G.PRES-PERF-JUST-ALREADY-YET"],["E.FR.YET-PLACE"],["A2.U01.C01"]),
      ("C05","Comprendre un récit d'expérience et en extraire l'essentiel","Understand a spoken account of an experience",["RO"],["G.PRES-PERF"],[],["A2.U01.C01"]),
      ("C06","Écrire un court texte sur une expérience","Write a short text about an experience",["PE"],["G.PRES-PERF","G.CONN-A2"],["E.FR.PP-FOR-PAST"],["A2.U01.C03"]),
    ])

U["U02"] = dict(
    theme="Récit au passé", theme_en="Past narrative",
    functions=["raconter","decrire-un-decor","situer"],
    lexis="L.A2.NARRATIVE",
    comps=[
      ("C01","Raconter une suite d'événements dans l'ordre","Narrate a sequence of events",["PO","PE"],["G.PAST-SIMPLE-IRREG","G.CONN-NARRATIVE"],["E.FR.PAST-PRESENT-MIX"],["A1.U12.C07"]),
      ("C02","Décrire le décor et l'arrière-plan d'un récit","Describe the background of a story",["PO"],["G.PAST-CONT"],["E.FR.PAST-CONT-BE"],["A2.U02.C01"]),
      ("C03","Articuler une action et son arrière-plan (when / while)","Combine action and background",["PO","PE"],["G.PAST-CONT-WHEN-WHILE"],["E.FR.WHEN-WHILE"],["A2.U02.C02"]),
      ("C04","Employer les connecteurs du récit","Use narrative connectors",["PO","PE"],["G.CONN-NARRATIVE"],["E.FR.AND-CHAIN"],["A2.U02.C01"]),
      ("C05","Poser des questions sur un récit qu'on vient d'entendre","Ask questions about a story",["I"],["G.PAST-Q","G.PAST-CONT"],["E.FR.DID-DOUBLE-PAST"],["A2.U02.C01"]),
      ("C06","Écrire un récit de huit à dix phrases liées","Write an 8-10 sentence narrative",["PE"],["G.PAST-CONT-WHEN-WHILE","G.CONN-NARRATIVE"],["E.FR.AND-CHAIN"],["A2.U02.C03"]),
      ("C07","Comprendre un récit oral et en restituer la chronologie","Understand a spoken narrative and restate its order",["RO"],["G.PAST-CONT-WHEN-WHILE"],[],["A2.U02.C03"]),
    ])

U["U03"] = dict(
    theme="Comparer", theme_en="Comparing",
    functions=["comparer","choisir","justifier"],
    lexis="L.A2.COMPARISON",
    comps=[
      ("C01","Comparer deux choses ou deux personnes","Compare two things or people",["PO","PE"],["G.COMPAR"],["E.FR.COMPAR-MORE","E.FR.COMPAR-THAN"],["A1.U04.C03"]),
      ("C02","Désigner l'extrême d'un ensemble","Pick out the extreme of a set",["PO"],["G.SUPERL"],["E.FR.SUPERL-THE"],["A2.U03.C01"]),
      ("C03","Exprimer une égalité ou une différence de degré","Express equality or difference of degree",["PO"],["G.AS-AS"],["E.FR.AS-AS"],["A2.U03.C01"]),
      ("C04","Justifier une comparaison avec une raison et un exemple","Justify a comparison",["PO"],["G.COMPAR","G.CONN-A2"],["E.FR.MINIMAL-ANSWER"],["A2.U00.C01","A2.U03.C01"]),
      ("C05","Comparer deux options et défendre son choix","Compare two options and defend a choice",["PO","I"],["G.COMPAR","G.OPINION-PHRASES"],["E.FR.MINIMAL-ANSWER"],["A2.U03.C04"]),
      ("C06","Lire un tableau comparatif et en tirer une conclusion","Read a comparison table",["RE"],["G.COMPAR","G.SUPERL"],[],["A2.U03.C02"]),
    ])

U["U04"] = dict(
    theme="Projets et prédictions", theme_en="Plans and predictions",
    functions=["annoncer-un-projet","predire","exprimer-la-certitude"],
    lexis="L.A2.FUTURE",
    comps=[
      ("C01","Annoncer un projet déjà décidé","Announce a decided plan",["PO","I"],["G.GOING-TO"],["E.FR.WILL-FOR-PLAN"],["A1.U12.C05"]),
      ("C02","Faire une prédiction","Make a prediction",["PO"],["G.WILL"],["E.FR.WILL-INFINITIVE"],["A2.U04.C01"]),
      ("C03","Distinguer projet, prédiction et décision spontanée","Distinguish plan, prediction and spontaneous decision",["PO"],["G.WILL-VS-GOING-TO"],["E.FR.WILL-FOR-PLAN"],["A2.U04.C02"]),
      ("C04","Parler d'un rendez-vous déjà fixé","Talk about a fixed arrangement",["PO","I"],["G.PRES-CONT-FUTURE"],["E.FR.FUTURE-ARRANGEMENT"],["A2.U04.C01"]),
      ("C05","Exprimer un degré de certitude","Express a degree of certainty",["PO"],["G.MODAL-CERTAINTY","G.HEDGING"],["E.FR.CERTAINTY-FLAT"],["A2.U00.C03"]),
      ("C06","Comprendre l'annonce d'un programme ou d'un planning","Understand an announced schedule",["RO"],["G.PRES-CONT-FUTURE"],[],["A2.U04.C04"]),
    ])

U["U05"] = dict(
    theme="Obligation, interdiction, conseil", theme_en="Obligation, prohibition, advice",
    functions=["obliger","interdire","conseiller"],
    lexis="L.A2.RULES",
    comps=[
      ("C01","Exprimer une obligation","Express obligation",["PO","I"],["G.HAVE-TO","G.MUST"],["E.FR.MUST-TO"],["A1.U09.C01"]),
      ("C02","Exprimer une absence d'obligation","Express absence of obligation",["PO"],["G.DONT-HAVE-TO"],["E.FR.MUSTNT-VS-DONT-HAVE-TO"],["A2.U05.C01"]),
      ("C03","Exprimer une interdiction","Express prohibition",["PO"],["G.MUSTNT"],["E.FR.MUSTNT-VS-DONT-HAVE-TO"],["A2.U05.C01"]),
      ("C04","Donner un conseil et le justifier","Give advice and justify it",["PO","I"],["G.SHOULD","G.CONJ-BECAUSE"],["E.FR.SHOULD-TO","E.FR.MINIMAL-ANSWER"],["A2.U00.C01"]),
      ("C05","Demander un conseil et réagir à celui qu'on reçoit","Ask for advice and react to it",["I"],["G.SHOULD","G.EMBEDDED-Q"],["E.FR.SHOULD-TO"],["A2.U05.C04"]),
      ("C06","Écrire des consignes ou un règlement simple","Write instructions or simple rules",["PE"],["G.MUST","G.MUSTNT","G.IMPERATIVE"],["E.FR.MUST-TO"],["A2.U05.C03"]),
      ("C07","Comprendre un règlement ou des conditions d'usage simples","Understand simple rules or terms",["RE"],["G.MUST","G.MUSTNT"],[],["A2.U05.C03"]),
    ])

U["U06"] = dict(
    theme="Opinion et argumentation", theme_en="Opinion and simple argument",
    functions=["donner-son-avis","concéder","structurer"],
    lexis="L.A2.OPINION",
    comps=[
      ("C01","Donner son opinion et la justifier par une raison","State an opinion and justify it",["PO","I"],["G.OPINION-PHRASES","G.CONJ-BECAUSE"],["E.FR.IAM-AGREE","E.FR.MINIMAL-ANSWER"],["A2.U00.C01"]),
      ("C02","Marquer son accord et son désaccord","Agree and disagree",["I"],["G.AGREE-DISAGREE"],["E.FR.IAM-AGREE"],["A2.U06.C01"]),
      ("C03","Donner un avantage et un inconvénient","Give an advantage and a drawback",["PO","PE"],["G.OPINION-PHRASES","G.CONN-A2"],["E.FR.MINIMAL-ANSWER"],["A2.U06.C01"]),
      ("C04","Concéder puis objecter","Concede then object",["PO"],["G.ALTHOUGH"],["E.FR.ALTHOUGH-BUT"],["A2.U06.C03"]),
      ("C05","Structurer un avis en trois temps","Structure an opinion in three moves",["PO","PE"],["G.CONN-A2","G.OPINION-PHRASES"],["E.FR.AND-CHAIN"],["A2.U06.C04"]),
      ("C06","Réagir à l'opinion de l'autre et rebondir","React to someone's opinion and build on it",["I"],["G.AGREE-DISAGREE","G.SHORT-Q-BACK"],["E.FR.NO-TURN-BACK"],["A2.U06.C02"]),
      ("C07","Écrire un court avis argumenté","Write a short argued opinion",["PE"],["G.ALTHOUGH","G.CONN-A2"],["E.FR.AND-CHAIN"],["A2.U06.C05"]),
      ("C08","Comprendre un échange contradictoire et identifier qui soutient quoi","Follow a disagreement and identify who argues what",["RO"],["G.AGREE-DISAGREE","G.ALTHOUGH"],[],["A2.U06.C02"]),
    ])

U["U07"] = dict(
    theme="Santé et corps", theme_en="Health and the body",
    functions=["decrire-un-symptome","conseiller","prendre-rendez-vous"],
    lexis="L.A2.HEALTH",
    comps=[
      ("C01","Décrire un symptôme avec précision","Describe a symptom precisely",["PO","I"],["G.PRES-PERF-FOR-SINCE"],["E.FR.PP-DEPUIS"],["A2.U01.C01"]),
      ("C02","Donner un conseil de santé","Give health advice",["PO","I"],["G.SHOULD"],["E.FR.SHOULD-TO"],["A2.U05.C04"]),
      ("C03","Prendre rendez-vous et gérer l'échange","Make an appointment",["I"],["G.PRES-CONT-FUTURE","G.EMBEDDED-Q"],["E.FR.EMBEDDED-Q-ORDER"],["A2.U04.C04"]),
      ("C04","Raconter un problème de santé passé","Recount a past health problem",["PO"],["G.PAST-CONT-WHEN-WHILE"],["E.FR.PAST-PRESENT-MIX"],["A2.U02.C03"]),
      ("C05","Comprendre une consigne médicale","Understand medical instructions",["RO"],["G.MUST","G.IMPERATIVE"],[],["A2.U05.C07"]),
      ("C06","Lire une notice ou une posologie simple","Read simple medicine instructions",["RE"],["G.MUST","G.QUANTIFIERS"],["E.FR.FALSE-FRIEND"],["A2.U05.C07"]),
    ])

U["U08"] = dict(
    theme="Voyage et transport", theme_en="Travel and transport",
    functions=["organiser","decrire-un-itineraire","gerer-un-imprevu"],
    lexis="L.A2.TRAVEL",
    comps=[
      ("C01","Organiser un déplacement : réserver, demander un horaire","Arrange a trip",["I"],["G.EMBEDDED-Q","G.PRES-CONT-FUTURE"],["E.FR.EMBEDDED-Q-ORDER"],["A2.U04.C04"]),
      ("C02","Décrire un itinéraire en plusieurs étapes","Describe a multi-step route",["PO"],["G.CONN-NARRATIVE","G.PREP-PLACE"],["E.FR.PREP-CALQUE"],["A1.U05.C06"]),
      ("C03","Raconter un voyage et le développer","Narrate a trip and develop it",["PO"],["G.PAST-CONT-WHEN-WHILE","G.CONN-NARRATIVE"],["E.FR.MINIMAL-ANSWER"],["A2.U02.C03"]),
      ("C04","Gérer un imprévu : retard, perte, changement","Handle a travel problem",["I"],["G.PRES-PERF","G.SHOULD"],["E.FR.PP-FORM"],["A2.U01.C01"]),
      ("C05","Comparer des moyens de transport et choisir","Compare transport options",["PO"],["G.COMPAR","G.SUPERL"],["E.FR.COMPAR-MORE"],["A2.U03.C05"]),
      ("C06","Comprendre une annonce de transport","Understand a transport announcement",["RO"],["G.PRES-CONT-FUTURE"],[],["A2.U04.C06"]),
      ("C07","Lire un horaire ou une confirmation de réservation","Read a timetable or booking confirmation",["RE"],["G.PREP-TIME","G.NUM"],["E.FR.DATE-FORMAT"],["A1.U10.C08"]),
    ])

U["U09"] = dict(
    theme="Nourriture, quantité, restaurant", theme_en="Food, quantity, eating out",
    functions=["quantifier","commander","suggerer"],
    lexis="L.A2.FOOD2",
    comps=[
      ("C01","Exprimer une quantité nuancée","Express nuanced quantity",["PO","PE"],["G.QUANTIFIERS","G.COUNT-UNCOUNT"],["E.FR.UNCOUNT-PLURAL","E.FR.QUANTIFIER-CHOICE"],["A1.U10.C02"]),
      ("C02","Commander puis modifier ou préciser sa commande","Order and then modify it",["I"],["G.WOULD-LIKE","G.EMBEDDED-Q"],["E.FR.WANT-DIRECT"],["A1.U10.C04"]),
      ("C03","Décrire un plat et sa préparation","Describe a dish and how it is made",["PO"],["G.PASSIVE-INTRO","G.CONN-NARRATIVE"],["E.FR.PASSIVE-ON"],["A2.U02.C04"]),
      ("C04","Exprimer une préférence alimentaire et la justifier","State a food preference with reasons",["PO","I"],["G.OPINION-PHRASES","G.CONJ-BECAUSE"],["E.FR.MINIMAL-ANSWER"],["A2.U06.C01"]),
      ("C05","Faire une suggestion et réagir à celle de l'autre","Make and respond to a suggestion",["I"],["G.SUGGESTIONS"],["E.FR.SUGGEST-CALQUE"],["A2.U00.C04"]),
      ("C06","Lire une recette et en suivre les étapes","Read and follow a recipe",["RE"],["G.IMPERATIVE","G.QUANTIFIERS"],[],["A2.U09.C01"]),
    ])

U["U10"] = dict(
    theme="Travail et parcours", theme_en="Work and career",
    functions=["decrire-un-parcours","expliquer-ses-responsabilites","se-projeter"],
    lexis="L.A2.CAREER",
    comps=[
      ("C01","Décrire son parcours professionnel dans le temps","Describe your career path over time",["PO","I"],["G.PRES-PERF-FOR-SINCE","G.PAST-SIMPLE-IRREG"],["E.FR.PP-DEPUIS","E.FR.SINCE-FOR"],["A2.U01.C01"]),
      ("C02","Décrire ses responsabilités en détail","Describe your responsibilities in detail",["PO"],["G.PRES-SIMPLE-AFF","G.CONN-A2"],["E.FR.MINIMAL-ANSWER"],["A2.U00.C01"]),
      ("C03","Parler de ses compétences et de son niveau de maîtrise","Talk about your skills and how well you do them",["PO"],["G.ADV-MANNER","G.CAN-ABILITY"],["E.FR.MANNER-ADV"],["A1.U09.C01"]),
      ("C04","Répondre aux questions d'un entretien simple","Handle a simple job interview",["I"],["G.PRES-PERF-FOR-SINCE","G.OPINION-PHRASES"],["E.FR.MINIMAL-ANSWER"],["A2.U10.C01"]),
      ("C05","Parler de ses ambitions et les justifier","Talk about ambitions and justify them",["PO"],["G.WILL","G.GOING-TO","G.PURPOSE-TO"],["E.FR.PURPOSE-FOR-ING"],["A2.U04.C03"]),
      ("C06","Écrire un court profil professionnel","Write a short professional profile",["PE"],["G.PRES-PERF-FOR-SINCE"],["E.FR.PP-DEPUIS"],["A2.U10.C01"]),
      ("C07","Comprendre une offre d'emploi","Understand a job advert",["RE"],["G.MUST","G.PRES-PERF"],["E.FR.FALSE-FRIEND"],["A2.U05.C07"]),
    ])

U["U11"] = dict(
    theme="Technologie et Internet", theme_en="Technology and the internet",
    functions=["expliquer-une-procedure","signaler-un-probleme","peser-le-pour-et-le-contre"],
    lexis="L.A2.TECH",
    comps=[
      ("C01","Décrire un usage numérique et sa fréquence","Describe a digital habit",["PO"],["G.PRES-SIMPLE-AFF","G.ADV-FREQ"],["E.FR.ADV-FREQ-PLACE"],["A1.U06.C05"]),
      ("C02","Expliquer comment on fait quelque chose, étape par étape","Explain a procedure step by step",["PO","PE"],["G.CONN-NARRATIVE","G.IMPERATIVE"],["E.FR.EXPLAIN-ME"],["A2.U02.C04"]),
      ("C03","Donner un avantage et un risque du numérique","Give a benefit and a risk of technology",["PO"],["G.OPINION-PHRASES","G.ALTHOUGH"],["E.FR.MINIMAL-ANSWER"],["A2.U06.C03"]),
      ("C04","Signaler un problème technique et demander de l'aide","Report a technical problem",["I"],["G.PRES-PERF","G.PRES-CONT"],["E.FR.PP-FORM"],["A2.U01.C01"]),
      ("C05","Comparer deux outils ou deux applications","Compare two tools or apps",["PO"],["G.COMPAR","G.AS-AS"],["E.FR.COMPAR-MORE"],["A2.U03.C03"]),
      ("C06","Comprendre une explication technique simple","Understand a simple technical explanation",["RO"],["G.CONN-NARRATIVE"],[],["A2.U11.C02"]),
    ])

U["U12"] = dict(
    theme="Ville, logement, environnement", theme_en="City, housing, environment",
    functions=["decrire-un-lieu","comparer","proposer-une-solution"],
    lexis="L.A2.CITY",
    comps=[
      ("C01","Décrire un quartier et ses services","Describe a neighbourhood and its facilities",["PO"],["G.THERE-IS-ARE","G.QUANTIFIERS"],["E.FR.THERE-HAVE"],["A1.U05.C03"]),
      ("C02","Comparer la ville et le village","Compare city and village life",["PO","PE"],["G.COMPAR","G.SUPERL"],["E.FR.COMPAR-MORE"],["A2.U03.C04"]),
      ("C03","Parler d'un problème d'environnement local","Talk about a local environmental problem",["PO"],["G.PRES-PERF","G.OPINION-PHRASES"],["E.FR.MINIMAL-ANSWER"],["A2.U06.C01"]),
      ("C04","Proposer une solution et en expliquer l'effet","Propose a solution and explain its effect",["PO"],["G.FIRST-COND","G.SO-THAT"],["E.FR.COND-WILL"],["A2.U13.C01"]),
      ("C05","Décrire un changement entre avant et maintenant","Describe a change between past and present",["PO","PE"],["G.USED-TO"],["E.FR.USED-TO"],["A2.U02.C02"]),
      ("C06","Lire une annonce immobilière","Read a property advert",["RE"],["G.QUANTIFIERS","G.COMPAR"],["E.FR.FALSE-FRIEND"],["A2.U12.C01"]),
    ])

U["U13"] = dict(
    theme="Condition, but et conséquence", theme_en="Condition, purpose and consequence",
    functions=["conditionner","exprimer-un-but","negocier"],
    lexis="L.A2.CONDITION",
    comps=[
      ("C01","Exprimer une condition réelle et sa conséquence","Express a real condition and its consequence",["PO","PE"],["G.FIRST-COND"],["E.FR.COND-WILL"],["A2.U04.C02"]),
      ("C02","Exprimer une conséquence","Express a consequence",["PO"],["G.SO-THAT","G.CONN-A2"],["E.FR.SO-CALQUE"],["A2.U00.C02"]),
      ("C03","Exprimer un but","Express purpose",["PO","PE"],["G.PURPOSE-TO","G.SO-THAT"],["E.FR.PURPOSE-FOR-ING"],["A2.U13.C02"]),
      ("C04","Exprimer une limite : trop, assez","Express excess and sufficiency",["PO"],["G.TOO-ENOUGH"],["E.FR.ENOUGH-ORDER","E.FR.TOO-VERY"],["A2.U00.C03"]),
      ("C05","Poser une condition dans une négociation","Set a condition in a negotiation",["I"],["G.FIRST-COND","G.TIME-CLAUSE-PRESENT"],["E.FR.FUTURE-AFTER-WHEN"],["A2.U13.C01"]),
      ("C06","Comprendre une consigne conditionnelle","Understand a conditional instruction",["RE"],["G.FIRST-COND"],[],["A2.U13.C01"]),
    ])

U["U14"] = dict(
    theme="Present perfect et prétérit", theme_en="Present perfect vs past simple",
    functions=["situer-dans-la-duree","raconter-un-parcours"],
    lexis="L.A2.TIME", pivot=True,
    comps=[
      ("C01","Choisir entre present perfect et prétérit","Choose between present perfect and past simple",["PO","PE"],["G.PRES-PERF-VS-PAST"],["E.FR.PP-FOR-PAST"],["A2.U01.C01"]),
      ("C02","Exprimer une durée qui continue avec for et since","Express ongoing duration with for and since",["PO"],["G.PRES-PERF-FOR-SINCE"],["E.FR.SINCE-FOR","E.FR.PP-DEPUIS"],["A2.U14.C01"]),
      ("C03","Répondre à « How long have you… ? »","Answer How long have you…?",["I"],["G.PRES-PERF-FOR-SINCE"],["E.FR.PP-DEPUIS"],["A2.U14.C02"]),
      ("C04","Raconter un parcours en articulant durée et événements","Narrate a path combining duration and events",["PO"],["G.PRES-PERF-VS-PAST","G.CONN-NARRATIVE"],["E.FR.PP-FOR-PAST","E.FR.MINIMAL-ANSWER"],["A2.U14.C02"]),
      ("C05","Corriger le calque « I am here since… »","Repair the I-am-here-since calque",["PO","I"],["G.PRES-PERF-FOR-SINCE"],["E.FR.PP-DEPUIS"],["A2.U14.C02"]),
      ("C06","Écrire une biographie courte mêlant les deux temps","Write a short bio using both tenses",["PE"],["G.PRES-PERF-VS-PAST"],["E.FR.PP-FOR-PAST"],["A2.U14.C04"]),
      ("C07","Comprendre un récit mêlant les deux temps","Understand a narrative using both tenses",["RO"],["G.PRES-PERF-VS-PAST"],[],["A2.U14.C01"]),
    ])

# points hérités de A1 et consolidés en A2, plus les points propres au niveau
GRAMMAR = """G.PRES-PERF G.PRES-PERF-Q G.PRES-PERF-EVER-NEVER G.PRES-PERF-JUST-ALREADY-YET
G.PRES-PERF-FOR-SINCE G.PRES-PERF-VS-PAST G.PAST-CONT G.PAST-CONT-WHEN-WHILE
G.PAST-SIMPLE-IRREG G.PAST-Q G.PAST-SIMPLE-REG G.COMPAR G.SUPERL G.AS-AS
G.GOING-TO G.WILL G.WILL-VS-GOING-TO G.PRES-CONT-FUTURE G.MODAL-CERTAINTY
G.HAVE-TO G.MUST G.MUSTNT G.DONT-HAVE-TO G.SHOULD G.USED-TO
G.CONN-A2 G.CONN-NARRATIVE G.ALTHOUGH G.OPINION-PHRASES G.AGREE-DISAGREE
G.HEDGING G.ADV-DEGREE G.ADV-MANNER G.QUANTIFIERS G.COUNT-UNCOUNT
G.SUGGESTIONS G.FIRST-COND G.PURPOSE-TO G.SO-THAT G.TOO-ENOUGH
G.TIME-CLAUSE-PRESENT G.RELATIVE-BASIC G.EMBEDDED-Q G.PARAPHRASE G.FILLERS
G.SHORT-Q-BACK G.PASSIVE-INTRO G.IMPERATIVE G.WOULD-LIKE G.CAN-ABILITY
G.PRES-SIMPLE-AFF G.PRES-CONT G.ADV-FREQ G.THERE-IS-ARE G.PREP-PLACE
G.PREP-TIME G.NUM G.CONJ-BECAUSE""".split()

CORE_ERRORS = ["E.FR.PP-DEPUIS", "E.FR.COND-WILL", "E.FR.MINIMAL-ANSWER",
               "E.FR.IAM-AGREE", "E.FR.COMPAR-MORE"]

PRONUNCIATION_ERRORS = ["E.FR.PP-FORM-PRON"]

ERROR_DEFS = {
 "E.FR.PP-DEPUIS": ("depuis rendu par un présent", "I am here since two years", "I have been here for two years"),
 "E.FR.COND-WILL": ("futur après if", "If I will have time, I will come", "If I have time, I will come"),
 "E.FR.MINIMAL-ANSWER": ("réponse minimale non développée", "I am a software engineer.", "I'm a software engineer — I build web apps for a startup in Douala."),
 "E.FR.IAM-AGREE": ("être d'accord rendu par be", "I am agree with you", "I agree with you"),
 "E.FR.COMPAR-MORE": ("more devant un adjectif court", "more big, more easy", "bigger, easier"),
 "E.FR.PP-FOR-PAST": ("present perfect pour un passé daté", "I have gone to Paris last year", "I went to Paris last year"),
 "E.FR.PP-FORM": ("formation du present perfect", "I have go / I am gone", "I have gone"),
 "E.FR.SINCE-FOR": ("confusion since / for", "for 2020, since two years", "since 2020, for two years"),
 "E.FR.COMPAR-THAN": ("comparatif sans than, ou avec that", "bigger that mine", "bigger than mine"),
 "E.FR.SUPERL-THE": ("superlatif sans the", "He is best student", "He is the best student"),
 "E.FR.AS-AS": ("calque de aussi... que", "as big than", "as big as"),
 "E.FR.WILL-FOR-PLAN": ("will pour un projet déjà décidé", "I will travel tomorrow, I have my ticket", "I'm going to travel tomorrow"),
 "E.FR.WILL-INFINITIVE": ("to après will", "I will to call you", "I will call you"),
 "E.FR.FUTURE-ARRANGEMENT": ("présent simple pour un rendez-vous fixé", "I meet him tomorrow at 5", "I'm meeting him tomorrow at 5"),
 "E.FR.FUTURE-AFTER-WHEN": ("futur après when", "when I will arrive", "when I arrive"),
 "E.FR.MUST-TO": ("to après must", "I must to go", "I must go"),
 "E.FR.MUSTNT-VS-DONT-HAVE-TO": ("interdiction et absence d'obligation confondues", "You mustn't come (pour: ce n'est pas obligatoire)", "You don't have to come"),
 "E.FR.SHOULD-TO": ("to après should", "You should to rest", "You should rest"),
 "E.FR.ALTHOUGH-BUT": ("although et but cumulés", "Although it's expensive, but I like it", "Although it's expensive, I like it"),
 "E.FR.AND-CHAIN": ("phrases enchaînées uniquement par and", "I woke up and I ate and I went and…", "I woke up, then I had breakfast. After that…"),
 "E.FR.PAST-CONT-BE": ("omission de be au past continuous", "I working when he called", "I was working when he called"),
 "E.FR.WHEN-WHILE": ("when et while intervertis", "While he called, I was cooking", "When he called, I was cooking"),
 "E.FR.USED-TO": ("used to mal formé", "I used to went / I use to go", "I used to go"),
 "E.FR.QUANTIFIER-CHOICE": ("quantifieur inadapté au dénombrable", "much people, few water", "many people, little water"),
 "E.FR.TOO-VERY": ("too employé pour very", "It's too good", "It's very good"),
 "E.FR.ENOUGH-ORDER": ("place de enough", "enough big", "big enough"),
 "E.FR.MANNER-ADV": ("adverbe de manière sans -ly", "He speaks slow", "He speaks slowly"),
 "E.FR.EMBEDDED-Q-ORDER": ("ordre interrogatif dans une subordonnée", "I don't know where is he", "I don't know where he is"),
 "E.FR.PURPOSE-FOR-ING": ("for + -ing pour exprimer un but", "I came for learning English", "I came to learn English"),
 "E.FR.SO-CALQUE": ("donc rendu par so mal placé", "So I like it, I bought it", "I like it, so I bought it"),
 "E.FR.SUGGEST-CALQUE": ("suggestion calquée du français", "We go to the restaurant?", "How about going to the restaurant?"),
 "E.FR.PASSIVE-ON": ("on rendu par un sujet indéfini", "On cooks it with rice", "It is cooked with rice"),
 "E.FR.EXPLAIN-ME": ("verbe suivi directement du complément d'attribution", "Explain me the rule", "Explain the rule to me"),
 "E.FR.NO-TURN-BACK": ("échange non relancé", "réponse close, aucune question en retour", "…And you? What do you think?"),
 "E.FR.CODE-SWITCH": ("bascule vers le français sur un mot inconnu", "It's a… un tournevis", "It's a thing you use to turn screws"),
 "E.FR.CERTAINTY-FLAT": ("certitude non graduée", "It will rain. / It won't rain.", "It'll probably rain. / I don't think it will."),
 "E.FR.YET-PLACE": ("place de yet et already", "I have yet finished", "I have already finished / I haven't finished yet"),
 "E.FR.PP-FORM-PRON": ("contraction du present perfect non perçue", "I've entendu comme I", "/aɪv/"),
 "E.FR.ADV-FREQ-PLACE": ("place de l'adverbe de fréquence", "I go often", "I often go"),
 "E.FR.THERE-HAVE": ("calque de il y a", "It has a market", "There is a market"),
 "E.FR.PREP-CALQUE": ("préposition calquée du français", "on the morning", "in the morning"),
 "E.FR.UNCOUNT-PLURAL": ("pluriel d'indénombrable", "informations, advices", "information, advice"),
 "E.FR.FALSE-FRIEND": ("faux ami", "actually, eventually, assist", "now, possibly, attend"),
 "E.FR.WANT-DIRECT": ("demande trop directe", "I want a coffee", "I'd like a coffee, please"),
 "E.FR.DID-DOUBLE-PAST": ("double marque du passé après did", "Did you went?", "Did you go?"),
 "E.FR.PAST-PRESENT-MIX": ("mélange passé et présent dans un récit", "Yesterday I go", "Yesterday I went"),
 "E.FR.DATE-FORMAT": ("format de date ambigu", "12/06", "12 June / June 12"),
}


def all_comps():
    for unit, d in U.items():
        for c in d["comps"]:
            yield unit, d, c


def build_yaml():
    n = sum(len(d["comps"]) for d in U.values())
    L = ["# Lingo — Inventaire des compétences A2",
         "# Généré par tools/build_a2.py — ne pas éditer à la main.",
         f"# SOMMAIRE : {len(U)} unités (U00-U14), {n} compétences,",
         f"#            {len(GRAMMAR)} points de grammaire, {len(ERROR_DEFS)} erreurs francophones.",
         "# Sections : units | grammar_inventory | core_errors |",
         "#            pronunciation_out_of_scope_v1 | errors",
         "# Modes : I interaction | PO production orale | PE production écrite",
         "#         RO réception orale | RE réception écrite",
         "# U00 est transversal : il porte l'exigence d'élaboration, enseignée avant tout le reste.",
         "---", "level: A2", "l1_target: fr", "units:"]
    for unit, d in U.items():
        L.append(f"  {unit}:")
        L.append(f"    theme: {d['theme']!r}")
        L.append(f"    theme_en: {d['theme_en']!r}")
        L.append(f"    lexis: {d['lexis']}")
        if d.get("transversal"):
            L.append("    transversal: true")
        if d.get("pivot"):
            L.append("    pivot: true")
        L.append("    functions: [%s]" % ", ".join(d["functions"]))
        L.append("    competencies:")
        for cid, fr, en, modes, gram, errs, pre in d["comps"]:
            L.append(f"      - id: A2.{unit}.{cid}")
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


def validate(a1_ids):
    problems, ids = [], []
    modes, gram_used, err_used, per_unit = Counter(), Counter(), Counter(), Counter()

    for unit, d, (cid, fr, en, m, g, e, pre) in all_comps():
        full = f"A2.{unit}.{cid}"
        ids.append(full); per_unit[unit] += 1
        for x in m: modes[x] += 1
        for x in g: gram_used[x] += 1
        for x in e: err_used[x] += 1
        if not m: problems.append(f"{full} : aucun mode")
        if not g: problems.append(f"{full} : aucune ressource grammaticale")
        for x in g:
            if x not in GRAMMAR: problems.append(f"{full} : grammaire inconnue {x}")

    for k, v in Counter(ids).items():
        if v > 1: problems.append(f"identifiant dupliqué : {k}")

    known = set(ids) | a1_ids
    for unit, d, c in all_comps():
        for p in c[6]:
            if p not in known:
                problems.append(f"A2.{unit}.{c[0]} : prérequis inexistant {p}")

    for g in GRAMMAR:
        if g not in gram_used: problems.append(f"grammaire jamais utilisée : {g}")
    for u in U:
        if not any("RO" in c[3] or "RE" in c[3] for c in U[u]["comps"]):
            problems.append(f"{u} : aucune compétence réceptive")
    for ce in CORE_ERRORS:
        if err_used[ce] < 2:
            problems.append(f"erreur noyau {ce} surveillée sur {err_used[ce]} compétence(s)")
    for code in err_used:
        if code not in ERROR_DEFS: problems.append(f"erreur sans définition : {code}")
    for code in ERROR_DEFS:
        if code not in err_used and code not in PRONUNCIATION_ERRORS:
            problems.append(f"erreur définie mais rattachée à aucune compétence : {code}")

    # l'exigence d'élaboration doit irriguer le niveau, pas rester dans U00
    outside = {u for u, d, c in all_comps() if "E.FR.MINIMAL-ANSWER" in c[5]} - {"U00"}
    if len(outside) < 5:
        problems.append(f"E.FR.MINIMAL-ANSWER n'est surveillée que dans {len(outside)} unités hors U00 "
                        f"— l'exigence d'élaboration doit traverser le niveau")

    return problems, ids, modes, gram_used, err_used, per_unit


if __name__ == "__main__":
    a1 = yaml.safe_load(open("skill/curriculum-a1.yaml", encoding="utf-8"))
    a1_ids = {c["id"] for u in a1["units"].values() for c in u["competencies"]}

    open("skill/curriculum-a2.yaml", "w", encoding="utf-8").write(build_yaml())
    problems, ids, modes, gram_used, err_used, per_unit = validate(a1_ids)

    print("=" * 62)
    print("VALIDATION — Inventaire A2")
    print("=" * 62)
    print(f"Compétences         : {len(ids)}   (uniques : {len(set(ids))})")
    print(f"Unités              : {len(U)}")
    print(f"Grammaire           : {len(GRAMMAR)} déclarés, {len(gram_used)} utilisés")
    print(f"Erreurs FR          : {len(ERROR_DEFS)} définies, {len(err_used)} rattachées")
    print(f"Prérequis vers A1   : {sum(1 for u,d,c in all_comps() for p in c[6] if p.startswith('A1.'))}")
    print()
    print("Par unité :", "  ".join(f"{k}:{v}" for k, v in sorted(per_unit.items())))
    print()
    print("Modes :", "  ".join(f"{m}:{modes[m]}" for m in ["I", "PO", "PE", "RO", "RE"]))
    print()
    print("Erreurs les plus surveillées :")
    for e, n in err_used.most_common(6):
        print(f"   {e:<28} {n}")
    print()
    if problems:
        print(f"PROBLÈMES ({len(problems)}) :")
        for p in problems: print("   -", p)
        sys.exit(1)
    print("Aucun problème détecté.")
