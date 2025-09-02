# python-if_else_loops_functions

## 📌 Description
Projet “Python - if/else, loops, functions” (poids 1). Découverte des structures conditionnelles, des boucles (`for`, `while`), des fonctions et de la portée des variables. Objectif : produire exactement les sorties demandées et adopter un style conforme à `pycodestyle`.

## 🎯 Learning Objectives
À la fin du projet, vous devez pouvoir expliquer :
- Pourquoi l’indentation est si importante en Python.
- Comment utiliser `if`, `if ... else` et `elif`.
- Comment écrire des commentaires.
- Comment affecter des valeurs à des variables.
- Comment utiliser les boucles `while` et `for`.
- Comment utiliser les instructions `break` et `continue`.
- Comment utiliser les clauses `else` sur les boucles.
- À quoi sert l’instruction `pass`.
- Comment utiliser `range`.
- Ce qu’est une fonction et comment l’utiliser.
- Ce que retourne une fonction sans `return`.
- La portée (scope) des variables.
- Ce qu’est un traceback et comment le lire.
- Les opérateurs arithmétiques et comment les utiliser.

## ✅ Exigences
- Interprétation/Compilation sur Ubuntu 20.04 LTS, Python 3.8.*.
- En-tête shebang obligatoire : `#!/usr/bin/python3`.
- Tous les fichiers exécutables.
- Style : `pycodestyle` 2.7.*.
- `README.md` obligatoire à la racine de ce dossier.
- La longueur de vos fichiers peut être contrôlée via `wc`.

## 📚 Ressources utiles
- “More Control Flow Tools” (jusqu’à « 4.6. Defining Functions »).
- “IndentationError”.
- “How To Use String Formatters in Python 3”.
- “Learn to Program 2 : Looping”.
- “Pycodestyle – Style Guide for Python Code”.
- `man` ou `help` : `python3`.

## 📂 Fichiers attendus
- `0-positive_or_negative.py` — Affiche si `number` est positif, négatif ou nul.
- `1-last_digit.py` — Affiche le dernier chiffre de `number` avec les conditions données.
- `2-print_alphabet.py` — Imprime l’alphabet en minuscule sans retour à la ligne.
- `3-print_alphabt.py` — Imprime l’alphabet en minuscule sauf `q` et `e`.
- `4-print_hexa.py` — Imprime les nombres de 0 à 98 en décimal et en hexadécimal.
- `5-print_comb2.py` — Imprime les nombres de 00 à 99 séparés par `, `.
- `6-print_comb3.py` — Imprime toutes les combinaisons de deux chiffres différents.
- `7-islower.py` — Fonction `islower(c)` qui retourne `True` si `c` est minuscule.
- `8-uppercase.py` — Fonction `uppercase(str)` qui affiche la chaîne en majuscules.
- `9-print_last_digit.py` — Fonction `print_last_digit(number)` qui affiche et retourne le dernier chiffre.
- `10-add.py` — Fonction `add(a, b)` qui retourne la somme.
- `11-pow.py` — Fonction `pow(a, b)` qui retourne `a` à la puissance `b`.
- `12-fizzbuzz.py` — Fonction `fizzbuzz()` qui affiche les nombres de 1 à 100 en remplaçant les multiples de 3 et 5 par `Fizz`, `Buzz` ou `FizzBuzz`.

## 🧪 Sorties d’exemple (référence)
- `./0-positive_or_negative.py`  
  Sortie : `-4 is negative` / `0 is zero` / `7 is positive`
- `./1-last_digit.py`  
  Sortie : `Last digit of -626 is -6 and is less than 6 and not 0`
- `./2-print_alphabet.py`  
  Sortie : `abcdefghijklmnopqrstuvwxyz`
- `./3-print_alphabt.py`  
  Sortie : `abcdfghijklmnoprstuvwxyz`
- `./4-print_hexa.py`  
  Sortie : `0 = 0x0` … `98 = 0x62`
- `./5-print_comb2.py`  
  Sortie : `00, 01, 02, ..., 99`
- `./6-print_comb3.py`  
  Sortie : `01, 02, ..., 89`
- `./7-islower.py` (via `7-main.py`)  
  Sortie : `a is lower`, `H is upper`, etc.
- `./8-uppercase.py`  
  Sortie : `BEST SCHOOL 98 BATTERY STREET`
- `./9-print_last_digit.py`  
  Sortie : `8044`
- `./10-add.py`  
  Sortie : `3`, `98`, `98`
- `./11-pow.py`  
  Sortie : `4`, `9604`, `1`, `0.0001`, `-1024`
- `./12-fizzbuzz.py`  
  Sortie : `1 2 Fizz 4 Buzz ... 98 Fizz Buzz`

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
- Dossier de ce projet : `python-if_else_loops_functions`
