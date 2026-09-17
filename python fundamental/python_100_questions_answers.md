# 100 Python Questions and Answers

A practical Python fundamentals guide with short explanations and examples. The examples use Python 3.

## 1. Python Basics

### 1. What is Python?

Python is a high-level, general-purpose programming language known for readable syntax. It is used for automation, web development, data analysis, testing, and more.

```python
print("Hello, Python!")
```

### 2. How do you print text in Python?

Use the `print()` function.

```python
print("Welcome to Python")
print(10)
```

### 3. What is a variable?

A variable is a name that refers to a value.

```python
age = 25
name = "Maya"
print(name, age)
```

### 4. Do you need to declare a variable type?

No. Python determines the type from the assigned value.

```python
value = 10       # int
value = "ten"    # str
```

### 5. What are comments?

Comments are notes ignored by Python. Start a single-line comment with `#`.

```python
# Calculate the total price
total = 20 + 5
```

### 6. Why is indentation important?

Indentation defines code blocks. Python normally uses four spaces.

```python
if True:
    print("This line belongs to the if block")
```

### 7. What are common built-in data types?

Common types include `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, and `dict`.

```python
count = 3
price = 9.99
active = True
```

### 8. How do you check a value's type?

Use `type()`.

```python
value = 42
print(type(value))  # <class 'int'>
```

### 9. What is `None`?

`None` represents the absence of a value.

```python
result = None
if result is None:
    print("No result yet")
```

### 10. What are Python naming conventions?

Use lowercase words separated by underscores for variables and functions. Use `PascalCase` for classes.

```python
first_name = "Sam"

def calculate_total():
    pass
```

## 2. Numbers and Strings

### 11. What arithmetic operators does Python support?

Python supports `+`, `-`, `*`, `/`, `//`, `%`, and `**`.

```python
print(7 + 2)   # 9
print(7 // 2)  # 3
print(7 % 2)   # 1
print(2 ** 3)  # 8
```

### 12. What is the difference between `/` and `//`?

`/` returns normal division, while `//` returns floor division.

```python
print(5 / 2)   # 2.5
print(5 // 2)  # 2
```

### 13. How do you convert a string to an integer?

Use `int()`.

```python
quantity_text = "4"
quantity = int(quantity_text)
print(quantity + 2)  # 6
```

### 14. How do you convert a value to a float?

Use `float()`.

```python
rating = float("4.5")
print(rating)
```

### 15. How do you convert a value to a string?

Use `str()`.

```python
order_id = 125
message = "Order: " + str(order_id)
print(message)
```

### 16. What is an f-string?

An f-string inserts expressions directly into a string and is usually the clearest way to format text.

```python
name = "Asha"
score = 95
print(f"{name} scored {score}%")
```

### 17. How do you find the length of a string?

Use `len()`.

```python
password = "python123"
print(len(password))  # 9
```

### 18. How do you access a character in a string?

Use an index. Indexing starts at zero.

```python
word = "Python"
print(word[0])   # P
print(word[-1])  # n
```

### 19. What is string slicing?

Slicing extracts part of a sequence using `start:stop:step`.

```python
text = "abcdef"
print(text[1:4])  # bcd
print(text[::-1]) # fedcba
```

### 20. Are strings mutable?

No. Strings are immutable, so operations create new strings instead of changing the original.

```python
word = "cat"
word = "b" + word[1:]
print(word)  # bat
```

### 21. How do you change string case?

Use methods such as `upper()`, `lower()`, and `title()`.

```python
city = "london"
print(city.upper())  # LONDON
print(city.title())  # London
```

### 22. How do you remove whitespace from a string?

Use `strip()`, `lstrip()`, or `rstrip()`.

```python
email = "  user@example.com  "
print(email.strip())
```

### 23. How do you split a string?

Use `split()` to produce a list of pieces.

```python
csv_line = "red,green,blue"
colors = csv_line.split(",")
print(colors)
```

### 24. How do you join strings?

Use a separator's `join()` method.

```python
words = ["Python", "is", "useful"]
sentence = " ".join(words)
print(sentence)
```

### 25. How do you compare values?

Use `==`, `!=`, `<`, `>`, `<=`, or `>=`.

```python
minimum_age = 18
age = 20
print(age >= minimum_age)  # True
```

## 3. Conditions and Loops

### 26. What is an `if` statement?

It runs code only when a condition is true.

```python
balance = 100
if balance > 0:
    print("Account has funds")
```

### 27. What are `elif` and `else` used for?

`elif` checks another condition, and `else` handles all remaining cases.

```python
score = 72
if score >= 90:
    grade = "A"
elif score >= 60:
    grade = "Pass"
else:
    grade = "Fail"
print(grade)
```

### 28. What are logical operators?

`and` requires both conditions, `or` requires at least one, and `not` reverses a condition.

```python
age = 25
has_ticket = True
if age >= 18 and has_ticket:
    print("Entry allowed")
```

### 29. What are truthy and falsy values?

Empty containers, `0`, `False`, and `None` are falsy. Most other values are truthy.

```python
items = []
if not items:
    print("The cart is empty")
```

### 30. What is a `for` loop?

A `for` loop repeats once for every item in an iterable.

```python
for fruit in ["apple", "banana"]:
    print(fruit)
```

### 31. What does `range()` do?

`range()` produces a sequence of numbers, commonly for counting.

```python
for number in range(3):
    print(number)  # 0, 1, 2
```

### 32. How do you use a `while` loop?

A `while` loop repeats while its condition remains true.

```python
attempts = 3
while attempts > 0:
    print("Attempts left:", attempts)
    attempts -= 1
```

### 33. What does `break` do?

`break` exits the nearest loop immediately.

```python
for number in range(10):
    if number == 4:
        break
    print(number)
```

### 34. What does `continue` do?

`continue` skips the rest of the current iteration.

```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```

### 35. What does `pass` do?

`pass` does nothing and is useful as a temporary placeholder.

```python
def future_feature():
    pass
```

### 36. How do you loop with both an index and a value?

Use `enumerate()`.

```python
names = ["Ana", "Ben"]
for index, name in enumerate(names, start=1):
    print(index, name)
```

### 37. How do you loop over two lists together?

Use `zip()`.

```python
products = ["Book", "Pen"]
prices = [10, 2]
for product, price in zip(products, prices):
    print(product, price)
```

### 38. What is a nested loop?

A nested loop is a loop inside another loop.

```python
for row in range(2):
    for column in range(3):
        print(row, column)
```

### 39. How do you find a number's factors with a loop?

Test divisibility using the remainder operator.

```python
number = 12
factors = []
for candidate in range(1, number + 1):
    if number % candidate == 0:
        factors.append(candidate)
print(factors)
```

### 40. What is a conditional expression?

It is a short one-line `if/else` expression.

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)
```

## 4. Lists, Tuples, Sets, and Dictionaries

### 41. What is a list?

A list is an ordered, mutable collection.

```python
scores = [80, 92, 75]
scores.append(88)
print(scores)
```

### 42. How do you access list items?

Use zero-based indexes and slices.

```python
colors = ["red", "green", "blue"]
print(colors[1])   # green
print(colors[:2])  # red, green
```

### 43. How do you add an item to a list?

Use `append()` for one item and `extend()` for multiple items.

```python
numbers = [1, 2]
numbers.append(3)
numbers.extend([4, 5])
print(numbers)
```

### 44. How do you insert an item at a specific position?

Use `insert(index, value)`.

```python
queue = ["Sam", "Lee"]
queue.insert(0, "Mia")
print(queue)
```

### 45. How do you remove list items?

Use `remove()` for a value, `pop()` for an index, or `del` for a position or slice.

```python
items = ["pen", "book", "bag"]
items.remove("book")
last_item = items.pop()
print(items, last_item)
```

### 46. What is the difference between `sort()` and `sorted()`?

`sort()` changes a list in place. `sorted()` returns a new sorted list and works with many iterables.

```python
numbers = [3, 1, 2]
ordered = sorted(numbers)
print(ordered)
```

### 47. How do you reverse a list?

Use `reverse()` in place or slicing for a new reversed list.

```python
values = [1, 2, 3]
print(values[::-1])
values.reverse()
print(values)
```

### 48. What is a tuple?

A tuple is an ordered, immutable collection.

```python
location = (10.5, 20.2)
latitude, longitude = location
print(latitude, longitude)
```

### 49. What is a set?

A set stores unique values and is useful for membership checks and removing duplicates.

```python
tags = {"python", "code", "python"}
print(tags)  # python appears once
```

### 50. How do you perform set operations?

Use union (`|`), intersection (`&`), and difference (`-`).

```python
backend = {"Python", "SQL"}
frontend = {"JavaScript", "CSS"}
print(backend | frontend)
```

### 51. What is a dictionary?

A dictionary stores key-value pairs.

```python
user = {"name": "Ravi", "age": 30}
print(user["name"])
```

### 52. How do you safely read a dictionary value?

Use `get()` when a key may be missing.

```python
settings = {"theme": "light"}
language = settings.get("language", "English")
print(language)
```

### 53. How do you add or update dictionary data?

Assign a value using its key or call `update()`.

```python
profile = {"name": "Nora"}
profile["age"] = 28
profile.update({"city": "Pune"})
print(profile)
```

### 54. How do you loop through a dictionary?

Use `items()` for keys and values.

```python
prices = {"tea": 3, "cake": 5}
for item, price in prices.items():
    print(item, price)
```

### 55. What is unpacking?

Unpacking assigns items from an iterable to multiple variables.

```python
first, second, third = [10, 20, 30]
print(first, second, third)
```

## 5. Functions

### 56. What is a function?

A function is a reusable block of code that performs a task.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Ivy"))
```

### 57. What is the difference between a parameter and an argument?

A parameter is the variable in a function definition. An argument is the value passed during a call.

```python
def double(number):  # number is a parameter
    return number * 2

print(double(5))      # 5 is an argument
```

### 58. What does `return` do?

`return` sends a result back to the caller and ends the function.

```python
def area(width, height):
    return width * height

room_area = area(4, 5)
print(room_area)
```

### 59. What happens when a function has no `return`?

It returns `None` automatically.

```python
def show_message():
    print("Done")

result = show_message()
print(result)  # None
```

### 60. What are default parameters?

Default parameters provide fallback values when an argument is omitted.

```python
def connect(host="localhost", port=8000):
    return f"{host}:{port}"

print(connect())
```

### 61. What are keyword arguments?

Keyword arguments pass values by parameter name, improving readability.

```python
def create_user(name, active=True):
    return {"name": name, "active": active}

print(create_user(name="Lina", active=False))
```

### 62. What are `*args`?

`*args` collects extra positional arguments into a tuple.

```python
def total(*numbers):
    return sum(numbers)

print(total(2, 4, 6))
```

### 63. What are `**kwargs`?

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def show_settings(**settings):
    for key, value in settings.items():
        print(key, value)

show_settings(theme="dark", alerts=True)
```

### 64. What is variable scope?

Scope describes where a variable can be accessed. Variables created inside a function are local to that function.

```python
def build_message():
    message = "Private value"
    return message

print(build_message())
```

### 65. What is a lambda function?

A lambda is a small anonymous function, useful for short operations.

```python
triple = lambda number: number * 3
print(triple(4))
```

### 66. What is a docstring?

A docstring documents a module, function, class, or method.

```python
def square(number):
    """Return the square of a number."""
    return number * number
```

### 67. What is recursion?

Recursion is when a function calls itself. It needs a base case to stop.

```python
def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)

countdown(3)
```

### 68. What is a pure function?

A pure function always gives the same output for the same inputs and does not change outside data.

```python
def add_tax(price, rate):
    return price + price * rate
```

### 69. What is a list comprehension?

It creates a list using a compact loop expression.

```python
squares = [number * number for number in range(5)]
print(squares)
```

### 70. How do you add a condition to a list comprehension?

Add an `if` condition at the end.

```python
even_numbers = [number for number in range(10) if number % 2 == 0]
print(even_numbers)
```

## 6. Errors, Files, and Modules

### 71. What is an exception?

An exception is an error that occurs while a program is running.

```python
# This would raise ZeroDivisionError:
# result = 10 / 0
```

### 72. How do you handle exceptions?

Use `try` and `except`.

```python
try:
    number = int("abc")
except ValueError:
    print("That is not a valid number")
```

### 73. What are `else` and `finally` in exception handling?

`else` runs when no exception occurs. `finally` runs whether or not an exception occurs.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(result)
finally:
    print("Operation finished")
```

### 74. How do you raise your own exception?

Use `raise` when input violates a rule.

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount
```

### 75. How do you open a text file?

Use `open()`, preferably with a `with` block so the file closes automatically.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
```

### 76. How do you write to a file?

Open it with mode `w` to replace the file or `a` to append.

```python
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Application started\n")
```

### 77. What are common file modes?

`r` reads, `w` writes and replaces, `a` appends, and `x` creates a new file.

### 78. How do you read a file line by line?

Iterate over the file object.

```python
with open("tasks.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

### 79. What is a module?

A module is a Python file containing reusable code. Import it with `import`.

```python
import math
print(math.sqrt(16))
```

### 80. What is the difference between `import module` and `from module import name`?

The first keeps the module namespace. The second imports a name directly.

```python
import math
print(math.pi)

from math import sqrt
print(sqrt(25))
```

### 81. What does `if __name__ == "__main__"` mean?

It runs code only when the file is executed directly, not when it is imported.

```python
def main():
    print("Program started")

if __name__ == "__main__":
    main()
```

### 82. What is a package?

A package is a directory that groups related Python modules. Modern Python packages can work without `__init__.py`, although adding one is still common.

### 83. How do you install a third-party package?

Use `pip`, usually inside a virtual environment.

```text
python -m pip install requests
```

### 84. What is a virtual environment?

A virtual environment isolates project dependencies from other Python projects.

```text
python -m venv .venv
```

## 7. Object-Oriented Python

### 85. What is a class?

A class is a blueprint for creating objects with data and behavior.

```python
class Dog:
    def bark(self):
        return "Woof"

pet = Dog()
print(pet.bark())
```

### 86. What is an object?

An object is an instance created from a class.

```python
class Counter:
    pass

counter = Counter()
print(type(counter))
```

### 87. What is `__init__`?

`__init__` initializes an object's attributes when the object is created.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

item = Product("Notebook", 5)
print(item.name, item.price)
```

### 88. What is `self`?

`self` refers to the current object. It lets methods access that object's attributes and other methods.

### 89. What is inheritance?

Inheritance lets a child class reuse or extend a parent class.

```python
class Animal:
    def move(self):
        return "Moving"

class Bird(Animal):
    def fly(self):
        return "Flying"

bird = Bird()
print(bird.move(), bird.fly())
```

### 90. What is method overriding?

A child class can provide its own implementation of a parent method.

```python
class Animal:
    def sound(self):
        return "Some sound"

class Cat(Animal):
    def sound(self):
        return "Meow"

print(Cat().sound())
```

### 91. What is a dataclass?

A dataclass reduces boilerplate for classes that mainly store data.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

print(Point(2, 3))
```

## 8. Useful Python Tools and Practices

### 92. What are type hints?

Type hints describe the expected types and help editors and type checkers find mistakes.

```python
def multiply(first: int, second: int) -> int:
    return first * second
```

### 93. What is a generator?

A generator produces values one at a time using `yield`, which can save memory.

```python
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

for value in count_up_to(3):
    print(value)
```

### 94. What is the difference between `map()` and a list comprehension?

Both can transform items. List comprehensions are often easier to read for simple transformations.

```python
numbers = [1, 2, 3]
doubled = [number * 2 for number in numbers]
print(doubled)
```

### 95. What does `filter()` do?

`filter()` keeps items for which a condition is true.

```python
numbers = [1, 2, 3, 4]
even = list(filter(lambda number: number % 2 == 0, numbers))
print(even)
```

### 96. How do you test a function with `assert`?

`assert` checks that an expression is true and raises an error otherwise.

```python
def add(first, second):
    return first + second

assert add(2, 3) == 5
```

### 97. What is unit testing?

Unit testing checks small pieces of code independently. Python includes the `unittest` module.

```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5)

# Run with: python -m unittest
```

### 98. How do you inspect the current working directory?

Use the `pathlib` module for modern, readable path handling.

```python
from pathlib import Path

current_folder = Path.cwd()
print(current_folder)
```

### 99. How do you work with JSON data?

Use the built-in `json` module to convert between Python objects and JSON text.

```python
import json

user = {"name": "Kai", "active": True}
json_text = json.dumps(user)
restored_user = json.loads(json_text)
print(restored_user["name"])
```

### 100. How do you organize a small Python program?

Separate reusable functions from the program entry point, use clear names, handle errors, and keep related code in modules.

```python
def calculate_total(prices):
    return sum(prices)


def main():
    prices = [10, 5, 3]
    print(f"Total: {calculate_total(prices)}")


if __name__ == "__main__":
    main()
```

## Practice Suggestions

1. Type each example instead of only reading it.
2. Change the values and predict the output before running it.
3. Turn questions 1-40 into a small command-line calculator.
4. Use questions 41-55 to build a shopping cart program.
5. Use questions 71-84 to build a program that saves and loads notes.
6. Use questions 85-100 to model a small library, inventory, or bank account system.
