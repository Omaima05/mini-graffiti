# 🎨 Mini-Graffiti

Projet réalisé en L2 Informatique et Gestion.

Ce projet est une version simplifiée et pédagogique du logiciel **Graffiti**, utilisé en théorie des graphes pour générer automatiquement des conjectures mathématiques.  
Le programme génère des conjectures entre invariants de graphes, les teste sur un ensemble de graphes (zoo de graphes) et détecte automatiquement des contre-exemples lorsque les conjectures sont fausses.

---

## 🎯 Objectifs du projet

L’objectif principal du projet est de comprendre une démarche expérimentale :
* formuler des hypothèses,
* les tester automatiquement,
* analyser les résultats,
* et mettre en évidence les limites des conjectures générées par une intelligence artificielle.


## ✨ Fonctionnalités

- Construction automatique d’un **zoo de graphes** (chemins, cycles, arbres, graphes complets, bipartis, graphes aléatoires)
- Calcul de plusieurs **invariants de graphes**
- Génération automatique de **conjectures** à l’aide d’une IA locale
- Test systématique des conjectures sur tous les graphes du zoo
- Détection automatique de **contre-exemples**
- Visualisation et sauvegarde des graphes contre-exemples
- Stockage des résultats dans une base de données **SQLite**

---

## Prérequis

- Python 3.10 ou plus
- Git
- Ollama installé en local

Bibliothèques Python utilisées :
- networkx
- matplotlib
- sqlite3
- requests

---

## 🚀 Installation

### 1️⃣ Cloner le dépôt GitHub
bash git clone https://github.com/Omaima05/mini-graffiti.git cd Mini-Graffiti
`

---

### 2️⃣ Créer un environnement virtuel (recommandé)
bash python3 -m venv .venv source .venv/bin/activate
---

### 3️⃣ Installer les dépendances Python
bash pip install networkx matplotlib requests
> ⚠️ `sqlite3` est déjà inclus avec Python, il n’y a rien à installer pour cette bibliothèque.

---

### 4️⃣ Installer Ollama et le modèle Mistral

Installer Ollama depuis le site officiel :
👉 [https://ollama.com](https://ollama.com)

Puis, dans un terminal, lancer :
bash ollama pull mistral
Ollama doit être lancé avant l’exécution du programme.

---

## Exécution du programme

Lancer le fichier principal :
bash python main.py
Le programme :

* génère un zoo de graphes,
* demande à l’IA de proposer des conjectures,
* teste ces conjectures automatiquement,
* affiche le résultat (validée ou réfutée),
* sauvegarde les contre-exemples sous forme d’images,
* enregistre toutes les informations dans une base de données SQLite.

---

## Organisation du projet

```text
Mini-Graffiti/
├── main.py          # Lancement principal du programme
├── zoo.py           # Construction du zoo de graphes
├── invariants.py    # Calcul des invariants de graphes
├── llm.py           # Interaction avec l’IA (Ollama / Mistral)
├── tester.py        # Test des conjectures
├── visualizer.py    # Visualisation des graphes
├── database.py      # Gestion de la base SQLite
│
├── rapport/
│   ├── images/      # Images des graphes contre-exemples
│   └── rapport.tex  # Fichiers LaTeX du rapport
│
├── README.md
└── requirements.txt
```
---

## Remarque importante

Une conjecture validée sur le zoo de graphes **n’est pas une preuve mathématique**.
Le zoo est fini et limité en taille.
Un seul contre-exemple suffit à réfuter une conjecture, mais l’absence de contre-exemple ne garantit pas qu’elle soit vraie en général.

---

## Auteurs

Mahjoub Omaïma et Cherfaoui Abdelkader
---
