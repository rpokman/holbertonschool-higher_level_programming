# Python - Classes and Objects

## Description
Ce projet fait partie du cursus **Foundations v2.1 - Part 2** (badge *Python - Classes and Objects*, auteur : Guillaume, poids 1).  
Il introduit la **Programmation Orientée Objet (POO) en Python** : classes, instances, attributs (public/protégé/privé), méthodes, propriétés, validation des données et impression personnalisée.

## Contexte
Lisez (et testez au clavier) toutes les ressources listées ci-dessous dans l’ordre. Le but n’est pas de mémoriser, mais **d’expérimenter** : tapez, exécutez, modifiez, recommencez.

## Ressources
À lire / regarder :
- **Object Oriented Programming** (jusqu’à *Inheritance* exclu) – pas besoin d’apprendre `classmethod`/`staticmethod` à ce stade.
- **Object-Oriented Programming** (attention : l’auteur montre souvent quoi ne PAS faire pour mieux expliquer les concepts)  
  Lisez : *General Introduction*, *First-class Everything*, *A Minimal Class in Python*, *Attributes* (sans les attributs de classe), *Methods*, *The `__init__` Method*, *Data Abstraction/Encapsulation/Information Hiding*, *Public/Protected/Private Attributes*.
- **Properties vs. Getters and Setters**
- **Learn to Program 9: Object Oriented Programming** (vidéo)
- **Python Classes and Objects**
- **Object Oriented Programming** (rappels)

## Objectifs d’apprentissage
À la fin, vous devez pouvoir expliquer (sans Google) :
- Ce qu’est la **POO** et le principe *first-class everything*
- **Classe** vs **objet/instance**
- Ce qu’est un **attribut** (public/protégé/privé) et comment les utiliser
- Le rôle de **`self`**
- Ce qu’est une **méthode**
- Le rôle de **`__init__`** et comment l’utiliser
- **Abstraction**, **Encapsulation**, **Information Hiding**
- Ce qu’est une **propriété**
- Différence entre **attribut** et **propriété**
- La manière *pythonic* d’écrire **getters et setters**
- Comment créer dynamiquement des attributs pour une instance
- Comment lier des attributs aux objets et aux classes
- Ce que contient **`__dict__`** et son rôle
- Comment Python cherche les attributs d’un objet ou d’une classe
- Comment utiliser la fonction **`getattr`**

## Exigences
- Éditeurs autorisés : `vi`, `vim`, `emacs`  
- Exécution sur **Ubuntu 20.04 LTS** avec **python3 (3.8.5)**  
- Tous les fichiers doivent se terminer par une nouvelle ligne  
- Première ligne de chaque fichier : `#!/usr/bin/python3`  
- Respect de la norme **pycodestyle (2.7.\*)**  
- Tous les fichiers doivent être exécutables  
- Documentation obligatoire (modules, classes, fonctions) sous forme de **docstrings** clairs et complets  
- La longueur des fichiers sera testée avec `wc`

## Tasks

### 0. My first square
Écrire une classe vide `Square`.

### 1. Square with size
Ajouter un attribut privé `size`.  
- Instanciation avec `size` (sans vérification de type/valeur).

### 2. Size validation
Validation du `size` :  
- Doit être un entier (`TypeError` sinon).  
- Doit être >= 0 (`ValueError` sinon).

### 3. Area of a square
Ajouter une méthode publique `area()` qui retourne l’aire du carré.

### 4. Access and update private attribute
Ajouter un **getter** et un **setter** pour `size` avec validation.  
- Utilisation de `@property`.

### 5. Printing a square
Ajouter la méthode publique `my_print()` :  
- Affiche le carré avec `#`.  
- Si `size == 0`, affiche une ligne vide.

### 6. Coordinates of a square
Ajouter un attribut privé `position` (tuple de 2 entiers positifs).  
- Getter et setter avec validation.  
- Adapter `my_print()` pour prendre en compte `position`.

## Auteur
Projet réalisé dans le cadre du cursus Holberton. ✨
