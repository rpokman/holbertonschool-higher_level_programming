# Python - Server Side Rendering

<div align="right">
  <a href="README.md">🇬🇧 English</a> | <a href="README_FR.md">🇫🇷 Français</a>
</div>

![Python Server Side Rendering Banner](../images/Python%20-%20Server-Side%20Rendering.jpg)

## Description

This project explores the fundamentals of Server-Side Rendering (SSR) with Python. Through practical exercises, you will learn how to generate dynamic HTML content on the server using template engines, handle data from various sources, and build complete web applications with Flask and Jinja2.

## Learning Objectives

At the end of this project, you should be able to explain without help:

### General Concepts
- What is Server-Side Rendering and why it's important
- How to use Jinja2 template engine
- How to implement conditional logic and loops in templates
- How to read and process data from files (CSV, JSON)
- How to integrate database queries with templates
- How to structure a Flask application with templates
- Best practices for separating logic from presentation

## Resources

- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Server-Side Rendering Explained](https://www.patterns.dev/posts/server-side-rendering/)
- [Template Engines Overview](https://en.wikipedia.org/wiki/Template_processor)
- [Working with CSV in Python](https://docs.python.org/3/library/csv.html)
- [JSON in Python](https://docs.python.org/3/library/json.html)
- [SQLite with Python](https://docs.python.org/3/library/sqlite3.html)

## Requirements

### General
- Allowed editors: All of them
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the PEP 8 style (pycodestyle)
- All your files must be executable
- All your modules should have documentation
- You must use Flask and Jinja2 for templating

## Project Structure

```
python-server_side_rendering/
├── task_00_intro.py         # Introduction to SSR concepts
├── task_01_jinja.py         # Jinja2 template basics
├── task_02_logic.py         # Conditional logic & loops in templates
├── task_03_files.py         # Reading data from files (CSV/JSON)
├── task_04_db.py            # Database integration with templates
└── README.md
```

## Tasks

### 0. Introduction to Server-Side Rendering
**File:** `task_00_intro.py`

Introduction to the concepts of Server-Side Rendering. Understanding the difference between client-side and server-side rendering, and when to use each approach.

### 1. Jinja2 Templates - Basics
**File:** `task_01_jinja.py`

Learn how to use Jinja2 template engine to generate dynamic HTML. Create basic templates with variable substitution and understand template inheritance.

**Key concepts:**
- Template syntax: `{{ variable }}`
- Template inheritance: `{% extends %}` and `{% block %}`
- Including templates: `{% include %}`

### 2. Control Structures in Templates
**File:** `task_02_logic.py`

Implement conditional logic and loops in Jinja2 templates to create dynamic content based on data.

**Key concepts:**
- Conditional statements: `{% if %}`, `{% elif %}`, `{% else %}`
- Loops: `{% for item in items %}`
- Filters and tests

### 3. Reading Data from Files
**File:** `task_03_files.py`

Read data from CSV and JSON files, process it in Python, and render it in templates.

**Key concepts:**
- Reading CSV files with Python's `csv` module
- Parsing JSON data with Python's `json` module
- Passing data to templates

### 4. Database Integration
**File:** `task_04_db.py`

Connect to a SQLite database, execute queries, and display the results in templates using Flask and Jinja2.

**Key concepts:**
- SQLite database connection
- Executing SQL queries
- Rendering database results in templates
- Error handling

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

```bash
# Clone the repository
cd holbertonschool-higher_level_programming/python-server_side_rendering

# Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install Flask jinja2
```

## Usage

### Running Individual Tasks

Each task file can be run independently:

```bash
# Make the file executable
chmod +x task_01_jinja.py

# Run the task
python3 task_01_jinja.py
# or
./task_01_jinja.py
```

### Running Flask Applications

For tasks that use Flask:

```bash
# Start the Flask development server
python3 task_04_db.py

# Access the application in your browser
# Default: http://127.0.0.1:5000
```

### Example

```bash
# Run the Jinja2 template task
python3 task_01_jinja.py

# Access the rendered page
curl http://localhost:5000
# or open in browser: http://localhost:5000
```

## Technologies Used

- **Python 3.8+**: Main programming language
- **Flask**: Web framework for building web applications
- **Jinja2**: Template engine for generating dynamic HTML
- **SQLite3**: Lightweight database for data storage
- **CSV/JSON**: Data formats for file handling

## Best Practices

- **Separation of Concerns**: Keep business logic separate from presentation
- **Template Inheritance**: Use base templates to avoid code duplication
- **Security**: Always escape user input in templates (Jinja2 does this by default)
- **Error Handling**: Implement proper error handling for file operations and database queries
- **Code Style**: Follow PEP 8 guidelines for Python code

## Common Commands

```bash
# Check Python version
python3 --version

# Install Flask
pip install Flask

# Run a Flask app in debug mode
export FLASK_ENV=development
flask run

# Check code style
pycodestyle task_*.py
```

## Author

[rpok](https://github.com/rpokman)

## License

This project is intended for educational purposes as part of the Holberton School program.
