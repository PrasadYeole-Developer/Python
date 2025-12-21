# Python 3 & OOPS 

This repository contains structured Python programs and notes covering **core Python concepts**, **data structures**, **exception handling**, **file handling**, and **OOPS principles**.  
Each topic is organized into folders for clarity and easy navigation.

---

## 📂 Repository Structure

- **Basic Programs** - Core Python syntax and fundamentals  
- **For loop** - Programs using `for` loops  
- **While loop** - Programs using `while` loops  
- **Data Structures** - List, Tuple, Set, Dictionary programs  
- **Exception Handling** - Exception handling concepts and examples  
- **File Handling** - File operations using Python  
- **OOPS** - Object-Oriented Programming concepts  
- **python.py** - Consolidated reference file with core concepts  

---

## 🧩 Python Fundamentals

### Unicode Functions
```python
ord()  # get unicode of character
chr()  # get character from unicode
len()  # length of string
```


- String Operations

- - Indexing
```python
string[0]
string[-2]
```

- Slicing

- - string[start:stop:step]

- Type Conversion
```python
str()
bool()
int()
float()
```

- Input
```python
input()  # default datatype is string
```

### 🔁 Loops

- Range Function
```python
range(start, stop, step)
```

- start default = 0
- step default = 1
- stop is mandatory
- Loop ends just before stop
- Iterating Over Strings
- - Using indexes
- - Using characters directly

### Conditional Statements

- If-Elif-Else Ladder

```python
if condition:
elif condition:
else:
```

### Functions

- Function Definition

```python
def function_name():
    # function body
```

### Types of Arguments

- Positional arguments

- Keyword arguments

- Default arguments

### 📦 Data Structures

- List

- - Ordered

- - Mutable

- - Allows duplicates

- - Heterogeneous

- Tuple

- - Ordered

- - Immutable

- - Allows duplicates

- - Heterogeneous

- - Methods: count(), index()

- Set

- - Unordered

- - Mutable

- - No duplicates

- - Powerful built-in operations

- Set Operations

- - Union (A | B)

- - Intersection (A & B)

- - Difference (A - B)

- - Symmetric Difference (A ^ B)

- Dictionary

- - Mutable

- - Insertion order preserved

- - Duplicate values allowed

- - Unique keys

- - Heterogeneous

- Common Methods

```python
keys()

values()

items()

update()

clear()
```

### Exception Handling

- Types

- - Syntax Errors

- - Indentation Errors

- - Exception Handling Keywords

```python
try

except

else

finally

raise
```

### 📁 File Handling

Files include `.py, .txt, .mp3,` etc.

- Supports CRUD operations

- Basic File Handling Flow

```python
open()
read()
close()
write()
append()
```

### Object-Oriented Programming (OOPS)

- Core Concepts

- - Classes - Blueprint or template for an object

- - Objects - Instance created from a class

- - Constructor - Function called automatically during object creation

- - Attributes - Variables inside a class

- - Methods - Functions inside a class

- OOPS Pillars

- - Inheritance - Child class inherits properties and methods of parent class
- - Polymorphism - Same interface or method behaves differently depending on object or context
- - Encapsulation - Binding data and methods together and hiding internal details
- - Abstraction - Simplifying complex systems by exposing only essential features

### Dunder Methods

- Start and end with double underscores (__)
- Called automatically when certain actions are performed on an object

##### ✅ Notes

Each concept is implemented with programs and explanations inside its respective folder for better understanding and structured learning.