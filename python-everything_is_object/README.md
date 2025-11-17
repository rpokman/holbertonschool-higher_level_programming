# Python - Everything is object

<div align="right">
  <a href="README.md">🇬🇧 English</a> | <a href="README_FR.md">🇫🇷 Français</a>
</div>

![Python Everything is Object Banner](../images/Python%20-%20Everything%20is%20object.jpg)

## Description

This project explores fundamental concepts about how Python handles objects, references, and memory. Through a series of questions and practical exercises, you will understand the difference between mutable and immutable objects, how Python passes variables to functions, and the behavior of references and aliases.

This project is unique because it focuses on understanding Python's internal mechanisms rather than writing complex code. The goal is to develop a deep understanding that will help you predict and explain Python's behavior in various situations.

## Learning Objectives

At the end of this project, you should be able to explain without help:

### General Concepts
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## Resources

- [9.10. Objects and values](https://docs.python.org/3/tutorial/classes.html#objects-and-values)
- [9.11. Aliasing](https://docs.python.org/3/tutorial/classes.html#aliasing)
- [Immutable vs mutable types](https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/)
- [Mutation](https://www.composingprograms.com/pages/24-mutable-data.html)
- [9.12. Cloning lists](https://docs.python.org/3/tutorial/classes.html#cloning-lists)
- [Python tuples: immutable but potentially changing](https://stackoverflow.com/questions/9755990/why-can-tuples-contain-mutable-items)

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### .txt Answer Files
- Only one line
- No Shebang on the first line (i.e. "#!/usr/bin/python3")
- All your files should end with a new line

## Project Structure

```
python-everything_is_object/
├── 0-answer.txt              # Function to print type
├── 1-answer.txt              # Function to get variable identifier
├── 2-answer.txt              # Same object test (different values)
├── 3-answer.txt              # Same object test (same values)
├── 4-answer.txt              # Same object test (assignment)
├── 5-answer.txt              # Same object test (operation)
├── 6-answer.txt              # String equality (==)
├── 7-answer.txt              # String identity (is)
├── 8-answer.txt              # String equality (new strings)
├── 9-answer.txt              # String identity (new strings)
├── 10-answer.txt             # List equality (==)
├── 11-answer.txt             # List identity (is)
├── 12-answer.txt             # List equality (assignment)
├── 13-answer.txt             # List identity (assignment)
├── 14-answer.txt             # List append behavior
├── 15-answer.txt             # List concatenation behavior
├── 16-answer.txt             # Integer incrementation in function
├── 17-answer.txt             # List incrementation in function
├── 18-answer.txt             # List assignment in function
├── 19-copy_list.py           # Function to copy a list
├── 20-answer.txt             # Empty tuple test
├── 21-answer.txt             # Tuple test (2 elements)
├── 22-answer.txt             # Tuple test (1 element, no comma)
├── 23-answer.txt             # Tuple test (1 element, with comma)
├── 24-answer.txt             # Integer identity
├── 25-answer.txt             # Tuple identity (2 elements)
├── 26-answer.txt             # Empty tuple identity
├── 27-answer.txt             # List concatenation and id
├── 28-answer.txt             # List += and id
└── README.md
```

## Tasks Overview

### Questions about Objects and Identity (0-28)

The project consists of 29 tasks that explore various aspects of Python objects:

**Tasks 0-1**: Basic functions
- Identify the function to print object type
- Identify the function to get variable identifier

**Tasks 2-5**: Integer object behavior
- Understand when integers share the same object
- Explore Python's integer caching mechanism

**Tasks 6-9**: String immutability
- Difference between `==` (equality) and `is` (identity)
- String interning in Python

**Tasks 10-18**: List mutability
- How lists behave differently from strings
- References and aliases with mutable objects
- Function parameter passing

**Task 19**: Practical implementation
- Write a function to copy a list

**Tasks 20-26**: Tuple immutability
- Understand tuple syntax
- Tuple identity and caching

**Tasks 27-28**: List operations and memory
- Difference between `+` and `+=` for lists
- How operations affect object identity

### 19. Copy a list object
**File:** `19-copy_list.py`

Write a function that returns a copy of a list. This is the only coding task in the project.

**Requirements:**
- Function prototype: `def copy_list(a_list):`
- Can contain any type of objects
- Maximum 3 lines long (no documentation needed)
- No imports allowed

**Example:**
```python
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
new_list = copy_list(my_list)

print(new_list == my_list)  # True
print(new_list is my_list)  # False
```

## Key Concepts Explained

### Objects and Values

Everything in Python is an object. When you create a variable, you're creating a reference to an object:

```python
a = 42  # 'a' references an integer object with value 42
```

### Identity vs Equality

- **Equality (`==`)**: Compares the values of objects
- **Identity (`is`)**: Checks if two variables reference the same object

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (same values)
print(a is b)  # False (different objects)
```

### Mutable vs Immutable

**Immutable types** (cannot be changed after creation):
- `int`, `float`, `bool`
- `str`
- `tuple`
- `frozenset`

**Mutable types** (can be modified after creation):
- `list`
- `dict`
- `set`

### References and Aliases

```python
# Immutable example
a = 89
b = a  # b references the same object as a
a = 100  # a now references a NEW object
print(b)  # 89 (still references the original object)

# Mutable example
l1 = [1, 2, 3]
l2 = l1  # l2 is an alias of l1 (same object)
l1[0] = 'x'  # modifies the object
print(l2)  # ['x', 2, 3] (same object was modified)
```

### Function Parameter Passing

Python passes arguments by "assignment":
- For **immutable** objects: behaves like pass-by-value
- For **mutable** objects: behaves like pass-by-reference

```python
# Immutable
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # 1 (unchanged)

# Mutable
def append_value(lst):
    lst.append(4)

my_list = [1, 2, 3]
append_value(my_list)
print(my_list)  # [1, 2, 3, 4] (modified)
```

## Usage

### Answer Files

Each `.txt` file should contain only one line with your answer:

```bash
# Create an answer file
echo "type" > 0-answer.txt

# Check the answer
cat 0-answer.txt
```

### Python File (Task 19)

```bash
# Make the file executable
chmod +x 19-copy_list.py

# Test with main file
./19-main.py
```

## Testing Your Understanding

Use the Python interpreter to test concepts:

```bash
python3
>>> a = 89
>>> b = 89
>>> id(a)  # Get memory address
>>> id(b)  # Compare with a's address
>>> a is b  # Test identity
```

**Important**: Think before you test! Try to predict the answer first.

## Tips for Success

1. **Read the documentation first** - Don't jump to the interpreter immediately
2. **Think about why** - Understanding the reasoning is more important than the answer
3. **Test your hypotheses** - Use the interpreter to confirm your understanding
4. **One line answers only** - No spaces before or after
5. **Consider interview scenarios** - These questions are common in Python interviews

## Common Pitfalls

- Confusing `==` (equality) with `is` (identity)
- Not understanding integer caching (small integers are cached)
- Forgetting that strings are immutable
- Not recognizing that `+=` behaves differently for lists vs integers
- Tuple syntax confusion (single element needs a comma: `(1,)`)

## Technologies Used

- **Python 3.8.5**: Main programming language
- **CPython**: Python implementation (for memory address concepts)

## Best Practices

- Always use `==` for value comparison
- Use `is` only for singleton objects (`None`, `True`, `False`)
- Be careful with mutable default arguments in functions
- Use `.copy()` or `list()` to create list copies when needed
- Understand the difference between shallow and deep copies

## Author

[rpok](https://github.com/rpokman)

## License

This project is intended for educational purposes as part of the Holberton School program.
