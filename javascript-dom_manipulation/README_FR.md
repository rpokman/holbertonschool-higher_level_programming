# JavaScript - Manipulation du DOM

<div align="right">
  <a href="README.md">🇬🇧 English</a> | <a href="README_FR.md">🇫🇷 Français</a>
</div>

![JavaScript DOM Manipulation Banner](../images/JavaScript%20DOM%20manipulation.jpg)

## Description

Ce projet explore les fondamentaux de la manipulation du DOM (Document Object Model) en JavaScript. À travers une série d'exercices pratiques, vous apprendrez à interagir dynamiquement avec les éléments HTML, à gérer les événements utilisateur et à effectuer des requêtes réseau en utilisant l'API Fetch.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer sans aide :

### Concepts généraux
- Comment sélectionner des éléments HTML en JavaScript
- Quelles sont les différences entre les sélecteurs ID, classe et nom de balise
- Comment modifier le style d'un élément HTML
- Comment obtenir et mettre à jour le contenu d'un élément HTML
- Comment modifier le DOM
- Comment faire une requête avec XMLHttpRequest
- Comment faire une requête avec l'API Fetch
- Comment écouter/lier des événements DOM
- Comment écouter/lier des événements utilisateur

## Ressources

- [Qu'est-ce que JavaScript ?](https://developer.mozilla.org/fr/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Introduction au DOM](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model/Introduction)
- [Interface Document](https://developer.mozilla.org/fr/docs/Web/API/Document)
- [Classe Element](https://developer.mozilla.org/fr/docs/Web/API/Element)
- [Localiser les éléments DOM avec les sélecteurs](https://developer.mozilla.org/fr/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)
- [Sélecteurs CSS](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Selectors)
- [CSS Diner - Jouer avec les sélecteurs](https://flukeout.github.io/)
- [DOM Scripting](https://en.wikipedia.org/wiki/Dynamic_HTML)
- [Que s'est-il passé ? Dépannage JavaScript](https://developer.mozilla.org/fr/docs/Learn/JavaScript/First_steps/What_went_wrong)

## Exigences

### Général
- Éditeurs autorisés : Tous
- Tous vos fichiers seront interprétés sur le navigateur Chrome (version 57.0 ou ultérieure)
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- Votre code doit être conforme à `semistandard`
- Vous n'êtes pas autorisé à utiliser `var`
- Le HTML ne doit pas se recharger pour chaque action : manipulation du DOM, mise à jour des valeurs, récupération de données...

## Structure du projet

```
javascript-dom_manipulation/
├── 0-script.js          # Changer la couleur du header
├── 1-script.js          # Changer la couleur au clic
├── 2-script.js          # Ajouter une classe CSS
├── 3-script.js          # Basculer entre deux classes
├── 4-script.js          # Ajouter un élément à une liste
├── 5-script.js          # Mettre à jour le texte
├── 6-script.js          # Fetch API - Personnage Star Wars
├── 7-script.js          # Fetch API - Films Star Wars
├── 8-script.js          # Fetch API - Traduction "Hello"
└── README.md
```

## Tâches

### 0. Color Me
**Fichier :** `0-script.js`

Script JavaScript qui met à jour la couleur du texte de l'élément `header` en rouge (#FF0000) en utilisant `document.querySelector`.

### 1. Click and turn red
**Fichier :** `1-script.js`

Script qui met à jour la couleur du texte du `header` en rouge (#FF0000) lorsque l'utilisateur clique sur l'élément avec l'id `red_header`.

### 2. Add `.red` class
**Fichier :** `2-script.js`

Script qui ajoute la classe `red` à l'élément `header` lorsque l'utilisateur clique sur l'élément avec l'id `red_header`.

### 3. Toggle classes
**Fichier :** `3-script.js`

Script qui bascule la classe de l'élément `header` entre `red` et `green` lorsque l'utilisateur clique sur l'élément avec l'id `toggle_header`.

### 4. List of elements
**Fichier :** `4-script.js`

Script qui ajoute un élément `<li>Item</li>` à une liste `ul` avec la classe `my_list` lorsque l'utilisateur clique sur l'élément avec l'id `add_item`.

### 5. Change the text
**Fichier :** `5-script.js`

Script qui met à jour le texte de l'élément `header` avec "New Header!!!" lorsque l'utilisateur clique sur l'élément avec l'id `update_header`.

### 6. Star Wars character
**Fichier :** `6-script.js`

Script qui récupère le nom d'un personnage depuis l'API Star Wars (`https://swapi-api.hbtn.io/api/people/5/?format=json`) et l'affiche dans l'élément avec l'id `character` en utilisant l'API Fetch.

### 7. Star Wars movies
**Fichier :** `7-script.js`

Script qui récupère et liste tous les titres de films Star Wars depuis l'API (`https://swapi-api.hbtn.io/api/films/?format=json`) dans un élément `ul` avec l'id `list_movies`.

### 8. Say Hello!
**Fichier :** `8-script.js`

Script qui récupère la traduction du mot "hello" en français depuis l'API (`https://hellosalut.stefanbohacek.com/?lang=fr`) et l'affiche dans l'élément avec l'id `hello`. Le script doit fonctionner lorsqu'il est importé depuis la balise `<head>`.

## Utilisation

Pour tester chaque script :

1. Ouvrez le fichier HTML correspondant dans votre navigateur Chrome
2. Observez le comportement attendu selon la tâche
3. Utilisez la console développeur (F12) pour déboguer si nécessaire

### Exemple

```bash
# Ouvrir le fichier HTML dans Chrome
google-chrome 0-main.html
```

## Technologies utilisées

- **JavaScript ES6+** : Langage de programmation principal
- **DOM API** : Interface pour manipuler les éléments HTML
- **Fetch API** : Pour effectuer des requêtes HTTP asynchrones
- **Event Listeners** : Pour gérer les interactions utilisateur

## Auteur

[rpok](https://github.com/rpokman)

## Licence

Ce projet est destiné à des fins éducatives dans le cadre du programme Holberton School.
