# python-hello_world

## 📌 Description
Projet “Python - Hello, World” (poids 1). Découverte de Python, de son interpréteur et des opérations de base sur les chaînes. Objectif : produire exactement les sorties demandées et adopter un style conforme à `pycodestyle`.

## 🎯 Learning Objectives
À la fin du projet, vous devez pouvoir expliquer :
- Comment utiliser l’interpréteur Python.
- Comment afficher du texte et des variables avec `print`.
- Comment utiliser les chaînes de caractères (indexing et slicing).
- Quelle est la convention de style Python (Pycodestyle) et comment vérifier votre code.

## ✅ Exigences
- Interprétation/Compilation sur Ubuntu 20.04 LTS, Python 3.8.*.
- En-tête shebang obligatoire : `#!/usr/bin/python3`.
- Tous les fichiers exécutables.
- Style : `pycodestyle` 2.7.*.
- `README.md` obligatoire à la racine de ce dossier.
- La longueur de vos fichiers peut être contrôlée via `wc`.

## 📚 Ressources utiles
- Playlist “Learn to Program”.
- “Whetting Your Appetite”.
- “Using the Python Interpreter”.
- “An Informal Introduction to Python” (jusqu’à “3.1.2. Strings”).
- “How To Use String Formatters in Python 3”.
- “Pycodestyle – Style Guide for Python Code”.

## 📂 Fichiers attendus
- `2-print.py` — Affiche exactement `"Programming is like building a multilingual puzzle` puis un retour à la ligne. Utiliser `print`.
- `3-print_number.py` — Affiche un entier stocké dans `number` suivi de `Battery street`. Contraintes : pas de cast en string, exactement 3 lignes, utiliser f-strings.
- `4-print_float.py` — Affiche `Float: ` suivi du float `number` avec 2 décimales (précision 2). Pas de cast string, utiliser f-strings.
- `5-print_string.py` — Affiche 3 fois la chaîne `str` sur une première ligne, puis ses 9 premiers caractères sur la deuxième ligne. Pas de boucles ni conditions. Max 5 lignes.
- `6-concat.py` — Affiche `Welcome to Holberton School!` en utilisant `str1` et `str2`. Pas de boucles ni conditions. Le fichier doit faire exactement 5 lignes.
- `7-edges.py` — Sans boucles ni conditions. Doit définir :
  - `word_first_3` = 3 premières lettres de `word`
  - `word_last_2` = 2 dernières lettres de `word`
  - `middle_word` = `word` sans la première et la dernière lettre
  Sortie attendue au format :
  - `First 3 letters: Hol`
  - `Last 2 letters: on`
  - `Middle word: olberto`
  Fichier de 8 lignes exactement.
- `8-concat_edges.py` — Affiche `object-oriented programming with Python` sans boucles ni conditions, exactement 5 lignes, pas de nouvelles variables, pas de littéraux de chaîne.
- `9-easter_egg.py` — Imprime “The Zen of Python, by Tim Peters” suivi d’un retour à la ligne. Longueur maximale 98 caractères (contrôle avec `wc -m 9-easter_egg.py`).

## 🧪 Sorties d’exemple (référence)
- `./2-print.py`  
  Sortie : `"Programming is like building a multilingual puzzle`
- `./3-print_number.py`  
  Sortie : `98 Battery street`
- `./4-print_float.py`  
  Sortie : `Float: 3.14`
- `./5-print_string.py`  
  Sortie :
  - `Holberton SchoolHolberton SchoolHolberton School`
  - `Holberton`
- `./6-concat.py`  
  Sortie : `Welcome to Holberton School!`
- `./7-edges.py`  
  Sortie :
  - `First 3 letters: Hol`
  - `Last 2 letters: on`
  - `Middle word: olberto`
- `./8-concat_edges.py`  
  Sortie : `object-oriented programming with Python`
- `./9-easter_egg.py`  
  Affiche le Zen of Python (texte de Tim Peters).

## ▶️ Lancer et vérifier
- Rendre exécutable : `chmod +x fichier.py`, lancer avec `./fichier.py`.
- Style : `pycodestyle *.py`.
- Longueur : `wc -l fichier.py` ou `wc -m fichier.py` selon la contrainte.

## 📝 Bonnes pratiques
- Respecter à la lettre l’orthographe, la casse, les espaces et les retours à la ligne des sorties demandées.
- Utiliser les f-strings lorsque requis.
- Éviter tout code superflu (boucles/conditions non autorisées).
- Tester localement sur Ubuntu 20.04 ou en environnement équivalent.

## 🔗 Repo et dossier
- Repository : `holbertonschool-higher_level_programming`
- Dossier de ce projet : `python-hello_world`
