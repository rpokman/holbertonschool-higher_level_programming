# Python - Exceptions

## Description
Ce projet fait partie du cursus **Foundations v2.1 - Part 2**.  
Il couvre la gestion des erreurs et des exceptions en Python, en particulier l’utilisation des blocs `try` / `except` / `finally`, ainsi que l’instruction `raise`.

## Objectifs d’apprentissage
À la fin de ce projet, vous devez être capable d’expliquer, sans Google :
- Pourquoi la programmation en Python est géniale
- La différence entre une erreur et une exception
- Ce que sont les exceptions et comment les utiliser
- Quand et pourquoi utiliser des exceptions
- Comment gérer correctement une exception
- Le rôle du bloc `try` / `except` / `finally`
- L’intérêt de capturer une exception
- Comment lever une exception intégrée (`raise`)
- Quand et pourquoi implémenter une action de nettoyage après une exception

## Tasks

### 0. Safe list printing
Écrire une fonction qui affiche `x` éléments d’une liste.  
- Utilise `try` / `except`  
- Retourne le nombre réel d’éléments affichés  

### 1. Safe printing of an integers list
Écrire une fonction qui affiche un entier avec `"{:d}".format()`.  
- Retourne `True` si l’affichage est réussi  
- Retourne `False` sinon  

### 2. Print and count integers
Écrire une fonction qui affiche les `x` premiers éléments d’une liste **en ne gardant que les entiers**.  
- Retourne le nombre d’entiers réellement affichés  

### 3. Integers division with debug
Écrire une fonction qui divise deux entiers et affiche le résultat.  
- Utiliser `try` / `except` / `finally`  
- Affiche toujours `Inside result: <valeur>`  

### 4. Divide a list
Écrire une fonction qui divise, élément par élément, deux listes.  
- Retourne une nouvelle liste avec les résultats des divisions  
- Gère les erreurs : type invalide, division par zéro, index hors limite  

### 5. Raise exception
Écrire une fonction qui lève une exception de type `TypeError`.  

### 6. Raise a message
Écrire une fonction qui lève une exception `NameError` avec un message personnalisé.  

## Fichiers
Chaque exercice est composé de deux fichiers :
- `X-function.py` → le code de la fonction (à compléter)  
- `X-main.py` → fichier de test fourni (exemples d’utilisation)  

Exemples :
- `0-safe_print_list.py` et `0-main.py`  
- `1-safe_print_integer.py` et `1-main.py`  
- etc.

## Exigences
- Tous les fichiers commencent par `#!/usr/bin/python3`
- Tous les fichiers doivent être exécutables
- Le style doit respecter **pycodestyle (2.7.\*)**
- Les fichiers seront testés avec `wc` pour la longueur
- Aucun module externe n’est autorisé (sauf indication contraire)

## Auteur
Projet réalisé dans le cadre du cursus Holberton. ✨