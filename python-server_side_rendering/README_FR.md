# Python - Rendu Côté Serveur

<div align="right">
  <a href="README.md">🇬🇧 English</a> | <a href="README_FR.md">🇫🇷 Français</a>
</div>

![Python Server Side Rendering Banner](../images/Python%20-%20Server-Side%20Rendering.jpg)

## Description

Ce projet explore les fondamentaux du rendu côté serveur (Server-Side Rendering - SSR) avec Python. À travers des exercices pratiques, vous apprendrez à générer du contenu HTML dynamique sur le serveur en utilisant des moteurs de templates, à gérer des données provenant de diverses sources, et à construire des applications web complètes avec Flask et Jinja2.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer sans aide :

### Concepts généraux
- Qu'est-ce que le rendu côté serveur et pourquoi c'est important
- Comment utiliser le moteur de templates Jinja2
- Comment implémenter la logique conditionnelle et les boucles dans les templates
- Comment lire et traiter des données depuis des fichiers (CSV, JSON)
- Comment intégrer des requêtes de base de données avec des templates
- Comment structurer une application Flask avec des templates
- Les bonnes pratiques pour séparer la logique de la présentation

## Ressources

- [Documentation Jinja2](https://jinja.palletsprojects.com/)
- [Documentation Flask](https://flask.palletsprojects.com/)
- [Rendu côté serveur expliqué](https://www.patterns.dev/posts/server-side-rendering/)
- [Vue d'ensemble des moteurs de templates](https://en.wikipedia.org/wiki/Template_processor)
- [Travailler avec CSV en Python](https://docs.python.org/fr/3/library/csv.html)
- [JSON en Python](https://docs.python.org/fr/3/library/json.html)
- [SQLite avec Python](https://docs.python.org/fr/3/library/sqlite3.html)

## Exigences

### Général
- Éditeurs autorisés : Tous
- Tous vos fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS avec Python 3.8
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- La première ligne de tous vos fichiers doit être exactement `#!/usr/bin/python3`
- Votre code doit respecter le style PEP 8 (pycodestyle)
- Tous vos fichiers doivent être exécutables
- Tous vos modules doivent avoir une documentation
- Vous devez utiliser Flask et Jinja2 pour les templates

## Structure du projet

```
python-server_side_rendering/
├── task_00_intro.py         # Introduction aux concepts SSR
├── task_01_jinja.py         # Bases des templates Jinja2
├── task_02_logic.py         # Logique conditionnelle & boucles
├── task_03_files.py         # Lecture de données depuis fichiers (CSV/JSON)
├── task_04_db.py            # Intégration avec base de données
└── README.md
```

## Tâches

### 0. Introduction au rendu côté serveur
**Fichier :** `task_00_intro.py`

Introduction aux concepts du rendu côté serveur. Comprendre la différence entre le rendu côté client et côté serveur, et quand utiliser chaque approche.

### 1. Templates Jinja2 - Bases
**Fichier :** `task_01_jinja.py`

Apprendre à utiliser le moteur de templates Jinja2 pour générer du HTML dynamique. Créer des templates de base avec substitution de variables et comprendre l'héritage de templates.

**Concepts clés :**
- Syntaxe des templates : `{{ variable }}`
- Héritage de templates : `{% extends %}` et `{% block %}`
- Inclusion de templates : `{% include %}`

### 2. Structures de contrôle dans les templates
**Fichier :** `task_02_logic.py`

Implémenter la logique conditionnelle et les boucles dans les templates Jinja2 pour créer du contenu dynamique basé sur des données.

**Concepts clés :**
- Instructions conditionnelles : `{% if %}`, `{% elif %}`, `{% else %}`
- Boucles : `{% for item in items %}`
- Filtres et tests

### 3. Lecture de données depuis des fichiers
**Fichier :** `task_03_files.py`

Lire des données depuis des fichiers CSV et JSON, les traiter en Python, et les afficher dans des templates.

**Concepts clés :**
- Lecture de fichiers CSV avec le module `csv` de Python
- Analyse de données JSON avec le module `json` de Python
- Passage de données aux templates

### 4. Intégration avec base de données
**Fichier :** `task_04_db.py`

Se connecter à une base de données SQLite, exécuter des requêtes, et afficher les résultats dans des templates en utilisant Flask et Jinja2.

**Concepts clés :**
- Connexion à la base de données SQLite
- Exécution de requêtes SQL
- Rendu des résultats de la base de données dans les templates
- Gestion des erreurs

## Installation

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Configuration

```bash
# Cloner le dépôt
cd holbertonschool-higher_level_programming/python-server_side_rendering

# Créer un environnement virtuel (recommandé)
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install Flask jinja2
```

## Utilisation

### Exécuter les tâches individuellement

Chaque fichier de tâche peut être exécuté indépendamment :

```bash
# Rendre le fichier exécutable
chmod +x task_01_jinja.py

# Exécuter la tâche
python3 task_01_jinja.py
# ou
./task_01_jinja.py
```

### Exécuter les applications Flask

Pour les tâches qui utilisent Flask :

```bash
# Démarrer le serveur de développement Flask
python3 task_04_db.py

# Accéder à l'application dans votre navigateur
# Par défaut : http://127.0.0.1:5000
```

### Exemple

```bash
# Exécuter la tâche des templates Jinja2
python3 task_01_jinja.py

# Accéder à la page générée
curl http://localhost:5000
# ou ouvrir dans le navigateur : http://localhost:5000
```

## Technologies utilisées

- **Python 3.8+** : Langage de programmation principal
- **Flask** : Framework web pour construire des applications web
- **Jinja2** : Moteur de templates pour générer du HTML dynamique
- **SQLite3** : Base de données légère pour le stockage de données
- **CSV/JSON** : Formats de données pour la gestion de fichiers

## Bonnes pratiques

- **Séparation des préoccupations** : Garder la logique métier séparée de la présentation
- **Héritage de templates** : Utiliser des templates de base pour éviter la duplication de code
- **Sécurité** : Toujours échapper les entrées utilisateur dans les templates (Jinja2 le fait par défaut)
- **Gestion des erreurs** : Implémenter une gestion appropriée des erreurs pour les opérations de fichiers et les requêtes de base de données
- **Style de code** : Suivre les directives PEP 8 pour le code Python

## Commandes courantes

```bash
# Vérifier la version de Python
python3 --version

# Installer Flask
pip install Flask

# Exécuter une app Flask en mode debug
export FLASK_ENV=development
flask run

# Vérifier le style du code
pycodestyle task_*.py
```

## Auteur

[rpok](https://github.com/rpokman)

## Licence

Ce projet est destiné à des fins éducatives dans le cadre du programme Holberton School.
