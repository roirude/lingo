# Lingo — Modèle d'état de l'apprenant (v1)

*Option retenue : fiche de progression portée par l'apprenant.*

---

## 1. Le principe

Un skill Claude ne peut ni écrire ni conserver d'état entre deux sessions. La progression doit donc **sortir** de la session à la fin et **y rentrer** au début. C'est l'apprenant qui la transporte.

```
Fin de session          Lingo émet la CARTE           l'apprenant copie/enregistre
                                 ↓
                          (entre les sessions)
                                 ↓
Début de session        l'apprenant colle la CARTE     Lingo reconstruit l'état
```

Trois règles non négociables, sans quoi le modèle s'effondre :

1. **Lingo réémet la carte à la fin de CHAQUE session**, même écourtée, même ratée. Une session sans carte émise est une session perdue.
2. **La carte est le seul état qui fait foi.** Lingo ne doit jamais prétendre se souvenir de quoi que ce soit qui n'y figure pas.
3. **Si aucune carte n'est fournie au démarrage**, Lingo ne devine pas : il lance le test de placement, ou demande explicitement la carte.

Cette contrainte a un effet secondaire heureux : la carte est **lisible par l'apprenant**. Il voit sa propre progression, ce qui règle en partie le problème d'engagement (§4 du diagnostic).

---

## 2. Format de la carte

Format texte compact, pensé pour le copier-coller. Environ 600 à 900 octets pour un parcours A1 complet — tient dans un message, se lit à l'œil nu, se parse sans ambiguïté.

```
LINGO-STATE v1
learner: Junior | l1:fr | level:A1 | sessions:7 | last:2026-08-20 | lang:fr
--
MASTERED+ A1.U00.C01 A1.U00.C03 A1.U01.C01 A1.U01.C02
MASTERED  A1.U01.C05 A1.U02.C01
DEVELOPING
  A1.U01.C03 c6/6 g3/4 f1/3 r4/4 last:2026-08-20 next:2026-08-23 st:2
  A1.U06.C01 c4/6 g1/4 f0/1 r2/3 last:2026-08-20 next:2026-08-21 st:1
TAUGHT    A1.U06.C02 A1.U06.C04
REMEDIATE A1.U03.C03 (echec revision 2026-08-18)
--
ERRORS   E.FR.3SG-S 9/24 improving | E.FR.AGE-HAVE 2/3 | E.FR.DO-AUX-OMIT 5/11
DUE      2026-08-21 A1.U06.C01 | 2026-08-23 A1.U01.C03
NEXT     A1.U06.C05
NOTES    hesite sur les questions inattendues ; bon lexique travail
```

### Lecture des compteurs

| Code | Signification | Ce qu'il compte |
|---|---|---|
| `c` | *controlled* | Items de pratique contrôlée réussis / tentés (texte à trous, transformation, QCM) |
| `g` | *guided* | Productions guidées réussies / tentées (amorce ou éléments fournis) |
| `f` | *free* | Productions **spontanées et sans amorce** correctes / occasions |
| `r` | *receptive* | Reconnaissances correctes / tentées (comprendre la forme produite par autrui) |
| `st` | *stage* | Palier de répétition espacée atteint (0 à 5) |

Les compteurs sont **cumulatifs sur les 3 dernières sessions concernées**, pas sur toute la vie du parcours. Une compétence non pratiquée depuis longtemps voit ses compteurs conservés mais son statut soumis à révision.

### Le champ `ERRORS`

`E.FR.3SG-S 9/24 improving` se lit : *l'erreur « omission du -s à la 3ᵉ personne » est apparue 9 fois sur 24 contextes où elle était possible ; la tendance est à l'amélioration.*

Le dénominateur est essentiel. « 9 erreurs » ne veut rien dire ; « 9 sur 24 contextes obligatoires » est mesurable et comparable d'une session à l'autre. C'est le remplacement direct des pourcentages inventés.

---

## 3. Les statuts

| Statut | Code carte | Définition |
|---|---|---|
| Non commencé | *(absent de la carte)* | Jamais enseigné |
| Enseigné | `TAUGHT` | Présenté, aucune preuve suffisante encore |
| En cours d'acquisition | `DEVELOPING` | Preuves partielles ; c'est le statut le plus fréquent |
| Maîtrisé | `MASTERED` | Les cinq conditions ci-dessous sont réunies |
| Maîtrisé confirmé | `MASTERED+` | A survécu à une révision au moins 7 jours après |
| À remédier | `REMEDIATE` | Régression avérée |

Correspondance avec le vocabulaire du document d'origine : `NOT MASTERED` couvre *non commencé* + `TAUGHT` ; `NEEDS REMEDIATION` correspond à `REMEDIATE`.

---

## 4. Règle de maîtrise — en preuves comptables

Une compétence passe à `MASTERED` quand **les cinq conditions sont réunies simultanément** :

| # | Condition | Seuil |
|---|---|---|
| 1 | Pratique contrôlée | ≥ 5 réussites sur 6 tentatives |
| 2 | Production guidée | ≥ 3 sur 4 |
| 3 | **Production libre sans amorce** | ≥ 2 occurrences correctes, réparties sur **au moins 2 sessions différentes** |
| 4 | Réception | ≥ 3 sur 4 |
| 5 | Erreur associée | absente des **2 dernières sessions** où la compétence était en contexte |

La condition 3 est la plus importante et la plus souvent contournée par les systèmes existants. *Réparties sur au moins deux sessions* est ce qui distingue l'apprentissage de la mémoire de travail : réussir deux fois d'affilée dans la même session ne prouve rien, l'apprenant recopie ce qu'il vient de voir.

La condition 5 est ce qui empêche le système de déclarer « maîtrisé » alors que l'apprenant produit la structure cible correctement **tout en** commettant systématiquement l'erreur qu'elle est censée corriger.

### Confirmation

`MASTERED` → `MASTERED+` : réussite d'une révision menée **au moins 7 jours plus tard**, sur des items que l'apprenant n'a jamais vus, ≥ 2 réussites sur 3.

Tant qu'une compétence n'est pas `MASTERED+`, elle reste dans la file de révision. C'est la traduction opérationnelle du §21 du document d'origine : *une connaissance maîtrisée ne doit pas être considérée comme définitivement acquise*.

### Régression

Passage en `REMEDIATE` si **l'un** des cas suivants :

- échec en révision : < 2 réussites sur 3
- réapparition de l'erreur associée 2 fois sur 2 sessions consécutives
- production libre incorrecte 2 fois d'affilée après un statut `MASTERED`

Une compétence en `REMEDIATE` est **prioritaire absolue** sur tout nouvel apprentissage. Le moteur de leçon ne doit pas enseigner de nouvelle notion tant qu'une remédiation est en attente depuis plus de 2 sessions.

---

## 5. Répétition espacée

| Palier `st` | Délai après la dernière réussite |
|---|---|
| 0 | J+1 |
| 1 | J+3 |
| 2 | J+7 |
| 3 | J+14 |
| 4 | J+30 |
| 5 | J+90 |

- Révision réussie → `st + 1`
- Révision échouée → `st − 2` (plancher 0) et statut ramené à `DEVELOPING` ou `REMEDIATE`
- Une compétence à `st: 5` réussie est retirée de la file active et n'est plus revue qu'en évaluation de niveau

**Gestion du retard.** L'apprenant ne reviendra pas tous les jours. Si plusieurs révisions sont en retard, Lingo n'en traite que **5 au maximum par session**, par ordre d'ancienneté d'échéance, et ne fait jamais d'une session entière une session de rattrapage : au moins un item nouveau ou une production libre doit rester au programme, sans quoi l'apprenant décroche.

---

## 6. Règle de passage de niveau (A1 → A2)

Absente du document d'origine. Quatre conditions, toutes requises :

1. **≥ 85 %** des compétences A1 en `MASTERED+`
2. **Aucune** compétence en `REMEDIATE` depuis plus de 14 jours
3. **Évaluation de sortie réussie** : 12 compétences tirées au hasard dans l'inventaire A1, production **sans amorce**, ≥ 80 % de réussite, dont au moins 4 à l'oral
4. **Erreurs du noyau sous contrôle** : `E.FR.BE-OMIT`, `E.FR.3SG-S`, `E.FR.DO-AUX-OMIT`, `E.FR.AGE-HAVE` chacune ≤ 20 % de leurs contextes obligatoires

La condition 4 existe parce qu'un apprenant francophone peut cocher toutes les cases de contenu tout en fossilisant les quatre erreurs qui le trahiront à chaque phrase. Les laisser passer en A2 revient à les rendre permanentes.

---

## 7. Schéma JSON (chemin fichier / backend)

Même modèle, forme structurée. À utiliser quand l'apprenant conserve un fichier `lingo-etat.json` — et sans modification le jour où vous passez à un backend.

```json
{
  "lingo_state_version": "1.0",
  "learner": {
    "name": "Junior",
    "l1": "fr",
    "level": "A1",
    "instruction_language": "fr",
    "sessions_count": 7,
    "started": "2026-07-30",
    "last_session": "2026-08-20"
  },
  "competencies": {
    "A1.U01.C03": {
      "status": "DEVELOPING",
      "evidence": {
        "controlled": [6, 6],
        "guided": [3, 4],
        "free_unprompted": [1, 3],
        "receptive": [4, 4],
        "free_sessions": ["2026-08-18"]
      },
      "first_taught": "2026-08-14",
      "last_practised": "2026-08-20",
      "next_review": "2026-08-23",
      "review_stage": 2
    }
  },
  "grammar": {
    "G.PRES-SIMPLE-3S": { "status": "WEAK", "linked_error": "E.FR.3SG-S" }
  },
  "errors": {
    "E.FR.3SG-S": {
      "occurrences": 9,
      "obligatory_contexts": 24,
      "last_seen": "2026-08-20",
      "trend": "improving"
    }
  },
  "review_queue": [
    { "id": "A1.U06.C01", "due": "2026-08-21" },
    { "id": "A1.U01.C03", "due": "2026-08-23" }
  ],
  "next_objective": "A1.U06.C05",
  "notes": "Hésite sur les questions inattendues. Bon lexique du travail."
}
```

`free_sessions` porte les dates des productions libres réussies : c'est ce champ, et lui seul, qui permet de vérifier la condition 3 (« réparties sur au moins deux sessions »).

---

## 8. Ce que Lingo doit faire au démarrage d'une session

```
1. Une carte est-elle fournie ?
   NON → carte demandée. Toujours absente ? → test de placement.
   OUI → parser, valider la version, reconstruire l'état.

2. Y a-t-il une compétence en REMEDIATE depuis > 2 sessions ?
   OUI → type de session = REMÉDIATION.

3. Y a-t-il des révisions échues ?
   ≥ 5 → type = RÉVISION (max 5 items) + 1 item nouveau.
   1 à 4 → les insérer en ouverture de la session prévue.

4. Sinon → type = NOUVELLE NOTION sur `next_objective`,
   ou ENTRAÎNEMENT si la notion de la session précédente
   n'a pas encore de production libre.

5. Annoncer à l'apprenant, en une phrase, l'objectif du jour
   et ce qu'il saura faire à la fin.
```

L'étape 5 n'est pas cosmétique : un apprenant qui sait ce qu'il vient chercher apprend mesurablement mieux qu'un apprenant à qui l'on fait la conversation.

---

## 9. Limites assumées de cette option

À dire clairement à l'apprenant plutôt qu'à masquer :

- **Si la carte est perdue, la progression est perdue.** Atténuation : Lingo rappelle à chaque émission de conserver la carte, et la carte contient assez d'informations pour qu'un tuteur humain la relise.
- **L'apprenant peut modifier sa carte.** Ce n'est pas un système d'examen ; ce n'est pas grave. Un apprenant qui triche sur sa propre carte se punit lui-même.
- **Rien ne force le retour à J+1.** C'est la vraie faiblesse de l'option (a), et elle n'est pas technique. Elle se traite au niveau produit, pas au niveau du skill.

Le jour où vous passez au backend (option c), **rien de ce document ne change** sauf le transport : les statuts, les seuils, les compteurs et les règles restent identiques.
