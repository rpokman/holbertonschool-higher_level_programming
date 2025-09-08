# Python - Data Structures: Lists, Tuples

## Description
Ce projet fait partie du cursus **Foundations v2.1 - Part 2**.  
Il couvre les bases des structures de données en Python, en particulier **les listes** et **les tuples**.

## Objectifs d’apprentissage
À la fin de ce projet, vous devez être capable d’expliquer, sans Google :
- Ce que sont les listes et comment les utiliser
- Les différences et similarités entre les chaînes de caractères et les listes
- Les méthodes les plus courantes des listes
- Comment utiliser les listes comme piles (stacks) et files (queues)
- Les compréhensions de listes
- Ce que sont les tuples et quand les utiliser à la place des listes
- Les séquences, le packing et unpacking des tuples
- L’instruction `del` et son usage

## Tasks

### 0. Print a list of integers
Écrire une fonction qui affiche tous les entiers d’une liste.  
- Un entier par ligne  
- Utiliser `str.format()`  

### 1. Secure access to an element in a list
Écrire une fonction qui récupère un élément d’une liste en fonction de son index.  
- Retourne `None` si l’index est invalide  

### 2. Replace element
Écrire une fonction qui remplace un élément d’une liste à une position donnée.  
- Ne modifie rien si l’index est invalide  

### 3. Print a list of integers... in reverse!
Écrire une fonction qui affiche tous les entiers d’une liste en ordre inverse.  

### 4. Replace in a copy
Écrire une fonction qui remplace un élément d’une liste à une position donnée **sans modifier la liste originale**.  

### 5. Can you C me now?
Écrire une fonction qui supprime toutes les occurrences de `c` et `C` dans une chaîne de caractères.  

### 6. Lists of lists = Matrix
Écrire une fonction qui affiche une matrice d’entiers.  

### 7. Tuples addition
Écrire une fonction qui additionne 2 tuples.  
- Les tuples ont maximum 2 éléments (les manquants sont remplacés par 0)  

### 8. More returns!
Écrire une fonction qui retourne un tuple avec la longueur d’une chaîne et son premier caractère.  

### 9. Find the max
Écrire une fonction qui trouve le plus grand entier d’une liste.  
- Retourne `None` si la liste est vide  

### 10. Only by 2
Écrire une fonction qui retourne une nouvelle liste de booléens indiquant si chaque entier est multiple de 2.  

### 11. Delete at
Écrire une fonction qui supprime l’élément d’une liste à une position donnée.  

### 12. Switch
Compléter un script pour inverser les valeurs de `a` et `b`.  
- Le programme doit contenir exactement 5 lignes  

## Fichiers
Chaque exercice est composé de deux fichiers :
- `X-function.py` → le code de la fonction (à compléter)
- `X-main.py` → fichier de test fourni (exemples d’utilisation)

Exemples :
- `0-print_list_integer.py` et `0-main.py`
- `1-element_at.py` et `1-main.py`
- etc.

## Exigences
- Tous les fichiers commencent par `#!/usr/bin/python3`
- Tous les fichiers doivent être exécutables
- Le style doit respecter **pycodestyle (2.7.\*)**
- Les fichiers seront testés avec `wc` pour la longueur
- Aucun module externe n’est autorisé (sauf indication contraire)