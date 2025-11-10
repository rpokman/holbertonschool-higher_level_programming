# JavaScript - DOM Manipulation

<div align="right">
  <a href="README.md">🇬🇧 English</a> | <a href="README_FR.md">🇫🇷 Français</a>
</div>

![JavaScript DOM Manipulation Banner](../images/JavaScript%20DOM%20manipulation.jpg)

## Description

This project explores the fundamentals of DOM (Document Object Model) manipulation in JavaScript. Through a series of practical exercises, you will learn how to dynamically interact with HTML elements, handle user events, and perform network requests using the Fetch API.

## Learning Objectives

At the end of this project, you should be able to explain without help:

### General Concepts
- How to select HTML elements in JavaScript
- What are the differences between ID, class, and tag name selectors
- How to modify an HTML element's style
- How to get and update an HTML element's content
- How to modify the DOM
- How to make a request with XMLHttpRequest
- How to make a request with Fetch API
- How to listen/bind to DOM events
- How to listen/bind to user events

## Resources

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
- [CSS Diner - Play with Selectors](https://flukeout.github.io/)
- [DOM Scripting](https://en.wikipedia.org/wiki/Dynamic_HTML)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

## Requirements

### General
- Allowed editors: All of them
- All your files will be interpreted on Chrome browser (version 57.0 or later)
- All your files should end with a new line
- Your code should be semistandard compliant
- You are not allowed to use `var`
- HTML should not reload for each action: DOM manipulation, update values, fetch data…


## Project Structure

```
javascript-dom_manipulation/
├── 0-script.js          # Change header color
├── 1-script.js          # Change color on click
├── 2-script.js          # Add a CSS class
├── 3-script.js          # Toggle between two classes
├── 4-script.js          # Add element to a list
├── 5-script.js          # Update text content
├── 6-script.js          # Fetch API - Star Wars character
├── 7-script.js          # Fetch API - Star Wars movies
├── 8-script.js          # Fetch API - "Hello" translation
└── README.md
```

## Tasks

### 0. Color Me
**File:** `0-script.js`

JavaScript script that updates the text color of the `header` element to red (#FF0000) using `document.querySelector`.

### 1. Click and turn red
**File:** `1-script.js`

Script that updates the text color of the `header` to red (#FF0000) when the user clicks on the element with id `red_header`.

### 2. Add `.red` class
**File:** `2-script.js`

Script that adds the `red` class to the `header` element when the user clicks on the element with id `red_header`.

### 3. Toggle classes
**File:** `3-script.js`

Script that toggles the `header` element's class between `red` and `green` when the user clicks on the element with id `toggle_header`.

### 4. List of elements
**File:** `4-script.js`

Script that adds a `<li>Item</li>` element to a `ul` list with class `my_list` when the user clicks on the element with id `add_item`.

### 5. Change the text
**File:** `5-script.js`

Script that updates the `header` element's text to "New Header!!!" when the user clicks on the element with id `update_header`.

### 6. Star Wars character
**File:** `6-script.js`

Script that fetches a character's name from the Star Wars API (`https://swapi-api.hbtn.io/api/people/5/?format=json`) and displays it in the element with id `character` using the Fetch API.

### 7. Star Wars movies
**File:** `7-script.js`

Script that fetches and lists all Star Wars movie titles from the API (`https://swapi-api.hbtn.io/api/films/?format=json`) in a `ul` element with id `list_movies`.

### 8. Say Hello!
**File:** `8-script.js`

Script that fetches the French translation of the word "hello" from the API (`https://hellosalut.stefanbohacek.com/?lang=fr`) and displays it in the element with id `hello`. The script must work when imported from the `<head>` tag.

## Usage

To test each script:

1. Open the corresponding HTML file in your Chrome browser
2. Observe the expected behavior according to the task
3. Use the developer console (F12) for debugging if necessary

### Example

```bash
# Open the HTML file in Chrome
google-chrome 0-main.html
```

## Technologies Used

- **JavaScript ES6+**: Main programming language
- **DOM API**: Interface to manipulate HTML elements
- **Fetch API**: For asynchronous HTTP requests
- **Event Listeners**: To handle user interactions

## Author

[rpok](https://github.com/rpokman)

## License

This project is intended for educational purposes as part of the Holberton School program.
