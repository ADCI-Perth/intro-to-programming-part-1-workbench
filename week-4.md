---
title: 'Week 4: Recursion, functional programming and errors'
teaching: 145
exercises: 178
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 4, and how should I spend my 6 hours?
- How can I build lists in one line?
- What is a lambda function?
- How can functions work with other functions?
- What do Python error messages mean?
- How can my program keep going when something goes wrong?
- What are programming paradigms?
- How do functional and logic programming differ from what I have done so far?
- How does a functional version of a program compare with an imperative one?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Write list comprehensions with and without a condition.
- Write small lambda functions.
- Pass functions as arguments and return them from functions.
- Use map() and filter().
- Read a traceback and find the line that failed.
- Recognise common error types and fix them.
- Use try and except.
- Catch the specific error type you expect.
- Explain pure functions, side effects and recursion.
- Run a small logic program and predict the answers of a Python version.
- Rewrite a grade calculator with comprehensions, map/filter and try/except.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 4 overview {#week-4-overview}

**Theme:** write smaller, cleaner code with functions and comprehensions, and stop your programs from crashing when something goes wrong.

### What you will be able to do by the end of this week

- Explain recursion (a function that calls itself) and read a simple recursive function.
- Use list comprehensions, `lambda`, `map()` and `filter()` to transform and select data.
- Read a Python error message and name the type of error.
- Use `try` / `except` to handle bad input without crashing.

### Time plan (under 6 hours)

| Block | What you do | Time |
|---|---|---|
| Watch | 6 short videos | 53 min |
| Read & practise | Sections 4.1, 4.2, 4.3 and 4.4, plus exercises | 2 h 0 m |
| Concepts Bridge | Pure functions, recursion and logic programming (Prolog run in SWISH) | 30 min |
| Build | Practice task: error handling and a functional rewrite of a grade calculator | 2 h |
| Quiz | Canvas quiz, 6 questions | 15 min |
| **Total** | | **5 h 38 min** |

Suggested split for Read & practise: Section 4.1 (35 min), Section 4.2 (40 min), Section 4.3 (30 min), Section 4.4 (15 min).

The week totals less than 6 h on purpose. Use any spare time to repeat exercises you found hard, or try the optional material.

If your teacher runs an optional one-hour online drop-in or Q&A, it counts inside the Read & practise time.

---

### 1. Watch (53 min)

Watch these in order. Pause and try the code yourself in PyCharm. "T#" videos come from the Telusko *Python for Beginners (Full Course)* playlist.

| # | Video | Length | Link | Look for |
|---|---|---|---|---|
| 1 | T#40 Recursion | 5:43 | https://www.youtube.com/watch?v=XkL3SUioNvo&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 | What a function does when it calls itself. |
| 2 | T#41 Factorial using Recursion | 4:57 | https://www.youtube.com/watch?v=TqqQld6m6A0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 | The "stop" case (base case) that ends the calls. |
| 3 | T#42 Anonymous Functions, Lambda | 4:38 | https://www.youtube.com/watch?v=hYzwCsKGRrg&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 | How a one-line `lambda` replaces a short `def`. |
| 4 | T#43 Filter Map Reduce | 11:34 | https://www.youtube.com/watch?v=kj850Y8y8FI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 | What `map` (change every item) and `filter` (keep some items) each give back. |
| 5 | [Bro Code] Learn Python List Comprehensions in 10 Minutes | 10:20 | https://www.youtube.com/watch?v=YlY2g2xrl6Q | The pattern `[expression for item in list if condition]`. |
| 6 | T#63 Exception Handling | 15:59 | https://www.youtube.com/watch?v=6SPDvPK38tw&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 | Which code goes in `try` and which in `except`. |

**Total: about 53 min.**

---

### 2. Read & practise (2 h 0 m)

Open each lesson, read it, type the examples into PyCharm and run them. Then do the exercises.

#### Section 4.1: List comprehension and lambda (about 35 min)

- Lesson: [Section 4.1](#section-4-1)
- Read all of it: list comprehension first, then lambda functions.
- This lesson has no levels. Do exercises 1 to 6 at the end. Exercises 1, 2 and 5 are the easiest, so start there.

#### Section 4.2: Higher-order functions (about 40 min)

- Lesson: [Section 4.2](#section-4-2)
- Read "Higher Order Functions" (functions as parameters and return values) and "Built-in Higher Order Functions" (map, filter, reduce).
- **Skip** "Python Closures" and "Python Decorators". They are optional (see below).
- Do the Level 1 exercises.
- Some Level 2 and 3 exercises use country data. The data files are in [assets/data](data/course-data.zip) (see `countries.py` and `countries-data.py`). The lesson's `data/...` paths mean this folder.

#### Section 4.3: Error types (about 30 min)

- Lesson: [Section 4.3](#section-4-3)
- Read all of it. Each section shows one kind of error, such as `NameError` or `ValueError`.
- The one exercise is to try every example yourself. In PyCharm, use the **Python Console** tab at the bottom. Note the name of each error you see.

#### Section 4.4: Exception handling (about 15 min)

- Lesson: [Section 4.4](#section-4-4)
- Core: read **only the "Exception Handling" section** (the `try` / `except` part).
- **Skip** packing and unpacking, spreading, enumerate and zip for now. They are optional.
- The lesson's exercise is about unpacking, so skip it. Write your own instead. Ask for a number with `input()`, convert it with `int()`, and print a friendly message in an `except ValueError` block if the text is not a number.

> **PyCharm note:** the lessons were written with VS Code in mind. In PyCharm, right-click a file and choose **Run**, or use the Python Console for short tests.

---

### 3. Concepts Bridge (30 min)

Pure functions, recursion, and a first look at logic programming with a short Prolog video. You run one Prolog program and predict some Python outputs. You do not need to write Prolog.

- [Open the Week 4 Bridge](#week-4-bridge)

---

### 4. Build (2 h)

Rewrite part of a grade calculator in a functional style, and add `try` / `except` checks for bad input. This is your portfolio item for this week.

- [Open the Week 4 practice task](#week-4-practice)

---

### 5. Quiz (15 min)

Take the Canvas quiz for Week 4 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `starter.py` (your completed Part B functions and `main()`)
- `comparison_note.txt` (five sentences comparing the loop version with your functional version)

Your tutor marks the portfolio. The quiz is marked automatically.

---

### Optional (not required)

Only do these if you have time left after the core work.

**Videos**
- T#44 Decorators (Telusko)
- Zip function (Telusko)
- T#61 Iterators (Telusko)
- T#62 Generators (Telusko)

**Lesson sections**
- Section 4.2: Python closures and decorators.
- Section 4.4: packing and unpacking, spreading, enumerate and zip.

**Reading**
- Driscoll, M. (2017) *Python 101*, chapters 7, 25 and 26. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/

---

## 4.1 List Comprehension and Lambda {#section-4-1}

### List Comprehension

List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the _for_ loop.

```python
# syntax
[expression for i in iterable if condition]
```

**Example: 1**

For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:

```python
# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

```

**Example: 2**

For instance if you want to generate a list of numbers

```python
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(6)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

```

**Example: 3**

List comprehension can be combined with if expression

```python
# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [4, 6, 8, 10]

# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Lambda Function

Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. Lambda function is similar to anonymous functions in JavaScript. We need it when we want to write an anonymous function inside another function.

#### Creating a Lambda Function

To create a lambda function we use _lambda_ keyword followed by a parameter(s), followed by an expression. See the syntax and the example below. Lambda function does not use return but it explicitly returns the expression.

```python
# syntax
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```

**Example:**

```python
# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
print((lambda a, b: a + b)(2,3)) # 5 - wrapped in print() to see the result

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

#### Lambda Function Inside Another Function

Using a lambda function inside another function.

```python
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

1. Filter only negative and zero in the list using list comprehension
   ```python
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
2. Flatten the following list of lists of lists to a one dimensional list :

   ```output
   list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

   output
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

3. Using list comprehension create the following list of tuples:
   ```output
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
4. Flatten the following list to a new list:
   ```output
   countries = [[('Australia', 'Canberra')], [('New Zealand', 'Wellington')], [('Fiji', 'Suva')]]
   output:
   [['AUSTRALIA', 'AUS', 'CANBERRA'], ['NEW ZEALAND', 'NEW', 'WELLINGTON'], ['FIJI', 'FIJ', 'SUVA']]
   ```
5. Change the following list to a list of dictionaries:
   ```output
   countries = [[('Australia', 'Canberra')], [('New Zealand', 'Wellington')], [('Fiji', 'Suva')]]
   output:
   [{'country': 'AUSTRALIA', 'city': 'CANBERRA'},
   {'country': 'NEW ZEALAND', 'city': 'WELLINGTON'},
   {'country': 'FIJI', 'city': 'SUVA'}]
   ```
6. Change the following list of lists to a list of concatenated strings:
   ```output
   names = [[('Jack', 'Wilson')], [('David', 'Smith')], [('Emma', 'Brown')], [('Noah', 'Taylor')]]
   output
   ['Jack Wilson', 'David Smith', 'Emma Brown', 'Noah Taylor']
   ```
7. Write a lambda function which can solve a slope or y-intercept of linear functions.

::::::::::::::::::::::::::::::::::::::::::::::::

## 4.2 Higher-Order Functions {#section-4-2}

### Higher Order Functions

In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

- A function can take one or more functions as parameters
- A function can be returned as a result of another function
- A function can be modified
- A function can be assigned to a variable

In this section, we will cover:

1. Handling functions as parameters
2. Returning functions as return value from another functions
3. Using Python closures and decorators

#### Function as a Parameter

```python
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

#### Function as a Return Value

```python
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

You can see from the above example that the higher order function is returning different functions depending on the passed parameter

### Python Closures

Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let us have a look at how closures work in Python. In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below.

**Example:**

```python
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

### Python Decorators

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

#### Creating Decorators

To create a decorator function, we need an outer function with an inner wrapper function.

**Example:**

```python
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

```

#### Applying Multiple Decorators to a Single Function

```python
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

#### Accepting Parameters in Decorator Functions

Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters.

```python
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I am learning Python.".format(
        first_name, last_name))

print_full_name("Jack", "Wilson", 'Australia')
# I am Jack Wilson. I am learning Python.
# I live in Australia
```

### Built-in Higher Order Functions

Some of the built-in higher order functions that we cover in this part are _map()_, _filter_, and _reduce_.
Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.

#### Python - Map Function

The map() function is a built-in function that takes a function and iterable as parameters.

```python
    # syntax
    map(function, iterable)
```

**Example: 1**

```python
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**Example: 2**

```python
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**Example: 3**

```python
names = ['Jack', 'Olivia', 'Thomas', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['JACK', 'OLIVIA', 'THOMAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['JACK', 'OLIVIA', 'THOMAS', 'ABRAHAM']
```

What actually map does is iterating over a list. For instance, it changes the names to upper case and returns a new list.

#### Python - Filter Function

The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.

```python
    # syntax
    filter(function, iterable)
```

**Example: 1**

```python
# Let's filter only even numbers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**Example: 2**

```python
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

```python
# Filter long name
names = ['Jack', 'Olivia', 'Thomas', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 6:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Abraham']
```

#### Python - Reduce Function

The _reduce()_ function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value.
**Example: 1**

```python
from functools import reduce  # reduce lives in the functools module - leave this line as is; Week 6 explains importing

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

```python
countries = ['Australia', 'New Zealand', 'Fiji', 'England', 'Tuvalu', 'Ireland']
names = ['Jack', 'Olivia', 'Thomas', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Explain the difference between map, filter, and reduce.
2. Explain the difference between higher order function, closure and decorator
3. Define a call function before map, filter or reduce, see examples.
4. Use for loop to print each country in the countries list.
5. Use for to print each name in the names list.
6. Use for to print each number in the numbers list.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Use map to create a new list by changing each country to uppercase in the countries list
1. Use map to create a new list by changing each number to its square in the numbers list
1. Use map to change each name to uppercase in the names list
1. Use filter to filter out countries containing 'land'.
1. Use filter to filter out countries having exactly six characters.
1. Use filter to filter out countries containing six letters and more in the country list.
1. Use filter to filter out countries starting with an 'F'
1. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
1. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
1. Use reduce to sum all the numbers in the numbers list.
1. Use reduce to concatenate all the countries and to produce this sentence: Australia, New Zealand, Fiji, England, Tuvalu, and Ireland are English-speaking countries
1. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](data/countries.py) in this repository as countries.py (e.g. 'land', 'ia', 'island', 'stan')).
1. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
1. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.py list in the data folder.
1. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 3

1. Use the countries_data.py (`assets/data/countries-data.py`) file and follow the tasks below:
   - Sort countries by name, by capital, by population
   - Sort out the ten most spoken languages by location.
   - Sort out the ten most populated countries.

::::::::::::::::::::::::::::::::::::::::::::::::

## 4.3 Python Error Types {#section-4-3}

### Python Error Types

When we write code it is common that we make a typo or some other common error. If our code fails to run, the Python interpreter will display a message, containing feedback with information on where the problem occurs and the type of an error. It will also sometimes gives us suggestions on a possible fix. Understanding different types of errors in programming languages will help us to debug our code quickly and also it makes us better at what we do.

Let us see the most common error types one by one. First let us open our Python interactive shell. Go to your computer terminal (or the Python Console in PyCharm) and type 'python'. The python interactive shell will be opened.

#### SyntaxError

**Example 1: SyntaxError**

```python
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>>
```

As you can see we made a syntax error because we forgot to enclose the string with parenthesis and Python already suggests the solution. Let us fix it.

```python
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print('hello world')
hello world
>>>
```

The error was a _SyntaxError_. After the fix our code was executed without a hitch. Let see more error types.

#### NameError

**Example 1: NameError**

```python
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

As you can see from the message above, name age is not defined. Yes, it is true that we did not define an age variable but we were trying to print it out as if we had had declared it. Now, lets fix this by declaring it and assigning with a value.

```python
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>
```

The type of error was a _NameError_. We debugged the error by defining the variable name.

#### IndexError

**Example 1: IndexError**

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

In the example above, Python raised an _IndexError_, because the list has only indexes from 0 to 4 , so it was out of range.

#### ModuleNotFoundError

**Example 1: ModuleNotFoundError**

```python
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

In the example above, I added an extra s to math deliberately and _ModuleNotFoundError_ was raised. Lets fix it by removing the extra s from math.

```python
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

We fixed it, so let's use some of the functions from the math module.

#### AttributeError

**Example 1: AttributeError**

```python
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>>
```

As you can see, I made a mistake again! Instead of pi, I tried to call a PI constant from the math module. It raised an attribute error, it means, that the attribute does not exist in the module. Lets fix it by changing from PI to pi.

```python
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>> math.pi
3.141592653589793
>>>
```

Now, when we call pi from the math module we got the result.

#### KeyError

**Example 1: KeyError**

```python
>>> users = {'name':'Sam', 'age':25, 'country':'Australia'}
>>> users['name']
'Sam'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

As you can see, there was a typo in the key used to get the dictionary value. so, this is a key error and the fix is quite straight forward. Let's do this!

```python
>>> user = {'name':'Sam', 'age':25, 'country':'Australia'}
>>> user['name']
'Sam'
>>> user['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> user['country']
'Australia'
>>>
```

We debugged the error, our code ran and we got the value.

#### TypeError

**Example 1: TypeError**

```python
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

In the example above, a TypeError is raised because we cannot add a number to a string. First solution would be to convert the string to int or float. Another solution would be converting the number to a string (the result then would be '43'). Let us follow the first fix.

```python
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>
```

Error removed and we got the result we expected.

#### ImportError

**Example 1: ImportError**

```python
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math' (unknown location)
>>>
```

There is no function called power in the math module, it goes with a different name: _pow_. Let's correct it:

```python
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math' (unknown location)
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

#### ValueError

```python
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

In this case we cannot change the given string to a number, because of the 'a' letter in it.

#### ZeroDivisionError

```python
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

We cannot divide a number by zero.

We have covered some of the python error types, if you want to check more about it check the python documentation about python error types.
If you are good at reading the error types, then you will be able to fix your bugs fast and you will also become a better programmer.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

1. Open your Python interactive shell and try all the examples covered in this section.

::::::::::::::::::::::::::::::::::::::::::::::::

## 4.4 Exception Handling {#section-4-4}

### Exception Handling

Python uses _try_ and _except_ to handle errors gracefully. A graceful exit (or graceful handling) of errors is a simple programming idiom - a program detects a serious error condition and "exits gracefully", in a controlled manner as a result. Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this makes our application more robust. The cause of an exception is often external to the program itself. An example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device. Graceful handling of errors prevents our applications from crashing.

We have covered the different Python _error_ types in the previous section. If we use _try_ and _except_ in our program, then it will not raise errors in those blocks.

```python
try:
    ...  # Run this code
except ValueError:  # the exception name is optional
    ...  # Run this code when there is an exception
else:
    ...  # No exception? Run this code
finally:
    ...  # Always run this code
```

```python
# syntax
try:
    code in this block runs if things go well
except:
    code in this block runs if things go wrong
```

**Example:**

```python
try:
    print(10 + '5')
except:
    print('Something went wrong')
# Something went wrong
```

In the example above the second operand is a string. We could change it to float or int to add it with the number to make it work. But without any changes, the second block, _except_, will be executed.

**Example:**

```python
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2026 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
```

```output
Enter your name:Jack
Year you were born:2001
Something went wrong
```

In the above example, the exception block will run and we do not know exactly the problem. To analyze the problem, we can use the different error types with except.

In the following example, it will handle the error and will also tell us the kind of error raised.

```python
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2026 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occurred')
except ValueError:
    print('Value error occurred')
except ZeroDivisionError:
    print('Zero division error occurred')
```

```output
Enter your name:Jack
Year you were born:2001
Type error occurred
```

In the code above the output is going to be _TypeError_.
Now, let's add an additional block:

```python
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occurred')
except ValueError:
    print('Value error occurred')
except ZeroDivisionError:
    print('Zero division error occurred')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')
```

```output
Enter your name:Jack
Year you were born:2001
You are Jack. And your age is 25.
I usually run with the try block
I always run.
```

We can also shorten the above code as follows:

```python
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

```

### Packing and Unpacking Arguments in Python

We use two operators:

- \* for tuples
- \*\* for dictionaries

Let us take as an example below. It takes only arguments but we have list. We can unpack the list and changes to argument.

#### Unpacking

##### Unpacking Lists

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst))  # this would give: TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

If we ran this code, it would raise an error, because this function takes numbers (not a list) as arguments. Let us unpack/destructure the list.

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

We can also use unpacking in the range built-in function that expects a start and an end.

```python
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(list(numbers))  # [2, 3, 4, 5, 6]

```

A list or a tuple can also be unpacked like this:

```python
countries = ['Australia', 'New Zealand', 'Fiji', 'Samoa', 'Tonga']
aus, nz, fiji, *rest = countries
print(aus, nz, fiji, rest)   # Australia New Zealand Fiji ['Samoa', 'Tonga']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      # 1 [2, 3, 4, 5, 6] 7
```

##### Unpacking Dictionaries

```python
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {city}, {country}. He is {age} years old.'
dct = {'name':'Jack', 'country':'Australia', 'city':'Perth', 'age':25}
print(unpacking_person_info(**dct)) # Jack lives in Perth, Australia. He is 25 years old.
```

#### Packing

Sometimes we never know how many arguments need to be passed to a python function. We can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.

#### Packing Lists

```python
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

##### Packing Dictionaries

```python
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Jack",
      country="Australia", city="Perth", age=25))
```

```output
name = Jack
country = Australia
city = Perth
age = 25
{'name': 'Jack', 'country': 'Australia', 'city': 'Perth', 'age': 25}
```

### Spreading in Python

Like in JavaScript, spreading is possible in Python. Let us check it in an example below:

```python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Australia', 'New Zealand']
country_lst_two = ['Fiji', 'Samoa', 'Tonga']
oceania_countries = [*country_lst_one, *country_lst_two]
print(oceania_countries)  # ['Australia', 'New Zealand', 'Fiji', 'Samoa', 'Tonga']
```

### Enumerate

If we are interested in an index of a list, we use _enumerate_ built-in function to get the index of each item in the list.

```python
for index, item in enumerate([20, 30, 40]):
    print(index, item)
# 0 20
# 1 30
# 2 40
```

```python
countries = ['Australia', 'New Zealand', 'Fiji', 'Samoa', 'Tonga']
for index, i in enumerate(countries):
    if i == 'Fiji':
        print(f'The country {i} has been found at index {index}')
```

```output
The country Fiji has been found at index 2
```

### Zip

Sometimes we would like to combine lists when looping through them. See the example below:

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```output
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

1. names = ['Australia', 'New Zealand', 'Fiji', 'Samoa', 'Tonga', 'Japan', 'China']. Unpack the first five countries and store them in a variable oceania_countries, store Japan and China in jp and cn respectively.

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Functional and Logic Programming {#week-4-bridge}

**Time: 30 minutes** (5 min functional ideas, 8 min video, 4 min SWISH, 3 min Python version, 10 min activity)

### Why this matters

Python can be used in a functional way, even though it is also object-oriented. This supports LO 2 (apply object-oriented, imperative, functional and logic programming techniques). Today you meet two **paradigms** (styles of programming): functional and logic.

### Functional ideas (5 min)

A **side effect** is anything a function does besides returning a value, such as printing or changing a list outside the function. A **pure function** has no side effects: the same input always gives the same answer.

```python
def add_gst_pure(price):
    return round(price * 1.1, 2)      # pure: only uses its input


def add_gst_impure(price, log):
    total = round(price * 1.1, 2)
    log.append(total)                 # side effect: changes a list outside
    return total


history = []
print(add_gst_pure(100))              # 110.0
print(add_gst_impure(100, history))   # 110.0
print(add_gst_impure(50, history))    # 55.0
print(history)                        # [110.0, 55.0] (the outside list changed)
```

Pure functions are easy to test, because you only check input and output.

**Recursion** means a function calls itself on a smaller problem. It needs a **base case**, the simple answer that stops the calls.

```python
def add_up(items):
    if not items:                          # base case: empty list
        return 0
    return items[0] + add_up(items[1:])    # smaller problem


print(add_up([4, 5, 6]))  # 15
```

Each call works on a shorter list, until the base case is reached. Then the answers are added back up.

### Logic programming (LO 2)

In **logic programming** you do not write steps. You state **facts** (things that are true) and **rules** (how new facts follow from old ones). Then you ask **queries** (questions) and the system searches for answers. Prolog is the best-known logic language.

#### Video (8 min)

**[Programming Epitome] Prolog Programming Basics: Facts, Rules and Queries** (7:57)
https://www.youtube.com/watch?v=4F2FLNQ6yms

Watch for: how a fact, a rule and a query look, and how Prolog finds the answers by itself.

#### Run it: a family tree in Prolog (4 min)

1. Open SWISH: https://swish.swi-prolog.org/ (free, runs in your browser, no account needed to run queries). If it shows a welcome page, choose to create a new Prolog program.
2. Paste this program into the editor (the main text area).

```prolog
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

ancestor(X, Z) :- parent(X, Z).
ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).
```

`:-` means "is true if". Names starting with a capital letter (X, Y, Z) are variables. Every line ends with a full stop.

3. In the query box at the bottom right, type `grandparent(tom, Who).` and click **Run!**. You should see `Who = ann`, then use **Next** to see `Who = pat`.
4. Now run `ancestor(tom, Who).` and click **Next** to see every answer. Notice you did not write any search steps. Prolog found the answers itself.

#### The same idea in Python (3 min)

Facts are a set of tuples. Rules are functions. Queries are function calls. Run this in PyCharm. Before you run it, predict each printed answer.

```python
# Facts: (parent, child)
parent_facts = {
    ("tom", "bob"),
    ("tom", "liz"),
    ("bob", "ann"),
    ("bob", "pat"),
}


# Rules
def is_parent(x, y):
    return (x, y) in parent_facts


def children(x):
    return sorted([c for (p, c) in parent_facts if p == x])


def is_sibling(a, b):
    if a == b:
        return False
    for (p, child) in parent_facts:
        if child == a and is_parent(p, b):
            return True
    return False


# Queries
print(is_parent("tom", "bob"))    # True
print(children("tom"))            # ['bob', 'liz']
print(is_sibling("ann", "pat"))   # True
print(is_sibling("ann", "liz"))   # False
```

In Prolog you write the rule once and the system does the searching. In Python you write the search yourself with a `for` loop. Python is not a logic language, but you can copy the idea.

::::::::::::::::::::::::::::::::::::: challenge

### Activity (10 min)

Use the Python code above as your starting point.

1. Add the fact that `liz` is the parent of `joe`: add `("liz", "joe")` to `parent_facts`.
2. Add this rule below the others, then run the query:

```python
def is_grandparent(x, z):
    for (p, y) in parent_facts:
        if p == x and is_parent(y, z):
            return True
    return False


print(is_grandparent("tom", "joe"))   # True
```

3. Change one value in the last query so you can predict a different answer. Run it, then check your prediction.
4. In one or two sentences: which parts of this code are pure, and which part is logic-style? Keep your answer. You will use it in the portfolio note.

> **Stretch (optional, after the core work):** write a recursive `is_ancestor(x, z)`. It returns `True` if `x` is a parent of `z`. Otherwise, for each child `y` of `x`, it asks `is_ancestor(y, z)`. Test it with `tom` and `joe`, and with `ann` and `tom`.

:::::::::::::::: solution

### Model answer

Step 1 adds `("liz", "joe")` to the set. Step 2 prints `True`. Step 3 depends on the value you change. For example, `is_grandparent("bob", "joe")` prints `False`, because bob's children are ann and pat.

For step 4, a good answer says that `is_parent` and `is_grandparent` are pure, because they only read `parent_facts` and return a value. The facts and rules layout is logic-style, but Python makes you write the search loop yourself. Prolog does the searching for you.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

### Further reading

- Programming Epitome (n.d.) *Prolog Programming Basics: Facts, Rules and Queries* [Video]. YouTube. Available at: https://www.youtube.com/watch?v=4F2FLNQ6yms (Accessed: 2 November 2026).
- Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Accessed: 2 November 2026).

## Practice task: Functional Grade Calculator {#week-4-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [starter.py](files/week-4/starter.py)
- [solution.py](files/week-4/solution.py)
- [test_solution.py](files/week-4/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time: about 2 hours.** This is your portfolio item for Week 4. Your tutor marks it at the end of the week.

### Goal

Take a short grade calculator written with loops and rewrite it in a **functional style**. Then make it safe against bad input with `try` / `except`.

You do not need your Week 3 files. The Week 3 version is already inside `starter.py` (Part A).

### Files

| File | What it is |
|---|---|
| `starter.py` | Part A: the loop version (given). Part B: your functions to fill in. |
| `test_solution.py` | Tests for the functions. |
| `solution.py` | A model answer. Try the task yourself before you look. |

### Steps

1. Read Part A in `starter.py`. To try it, scroll to the last line of the file and **temporarily** change `main()` to `main_loop()`. Run the file, then type `abc` when it asks for a mark. It crashes. That is the problem we will fix. Change the last line back to `main()` before you carry on.
   - Near the bottom you will see `if __name__ == "__main__":`. Leave those two lines as they are. They mean "run this when the file is run directly", and Week 6 explains how they work.
2. In Part B, write `parse_mark(text)`. Use `try` / `except ValueError`. Return `None` for text that is not a number, or a number outside 0 to 100. Otherwise return the mark as a float.
3. Write `valid_marks(texts)` with a **list comprehension**. Use `map(parse_mark, texts)` and drop the `None` values.
4. Write `average(marks)`. Use `try` / `except ZeroDivisionError` so an empty list gives `0.0`.
5. Write `grade(mark)`. Copy the if/elif logic from Part A.
6. Write `letter_grades(marks)` with `map()`.
7. Write `passing_marks(marks)` with `filter()` and a `lambda`.
8. Write `grade_counts(marks)` with a **dictionary comprehension** over `GRADE_ORDER`.
9. Write `main()`. Ask for marks until an empty line. Tell the user when a mark is not valid and carry on. Print the results.
10. Write your 5-sentence note in `comparison_note.txt` (see below). This is the second part of your portfolio item.

### Example run

```output
Enter marks from 0 to 100. Press Enter on an empty line to finish.
Mark: 90
Mark: abc
  Not a valid mark, ignoring it.
Mark: 55
Mark: 120
  Not a valid mark, ignoring it.
Mark: 
Average: 72.5
Grades: ['HD', 'P']
Passing marks: [90.0, 55.0]
Grade counts: {'HD': 1, 'D': 0, 'C': 0, 'P': 1, 'F': 0}
```

Your wording can differ.

### Hints

- `float("abc")` raises a `ValueError`. That is the error you catch.
- `[m for m in map(f, items) if m is not None]` keeps only the answers that are not `None`.
- `list(map(grade, marks))` and `list(filter(lambda m: m >= 50, marks))` need `list(...)` to give you a list.
- `grades.count("HD")` counts how many times `"HD"` appears in a list.
- A **dictionary comprehension** builds a dictionary in one line, like a list comprehension but with `key: value`. For example, `{g: grades.count(g) for g in GRADE_ORDER}` makes a dictionary with one entry per grade in `GRADE_ORDER`, where each value is how often that grade appears in `grades`. (Here `grades` is the list of letter grades you get from `letter_grades(marks)`.)
- Keep `input()` and `print()` inside `main()` only. Functions that only take input and return output are **pure** and easy to test.

### Your 5-sentence note

Write five sentences in a plain text file called `comparison_note.txt`, comparing the loop version (Part A) with your functional version (Part B). You could cover:

1. Which version is shorter?
2. Which is easier to read, and for whom?
3. Which is easier to test, and why?
4. What did `try` / `except` change for the user?
5. Which style would you choose for this problem, and why?

### Check your work

- [ ] Run the tests. In PyCharm, right-click `test_solution.py` and choose **Run pytest**, or in the terminal: `python -m pytest weeks/week-4/practice`.
- [ ] To test your own file, open `test_solution.py` and change `import solution as calc` to `import starter as calc`.
- [ ] Typing `abc`, `-5` or `150` does not crash the program.
- [ ] An empty list of marks does not crash `average`.
- [ ] `letter_grades`, `passing_marks` and `grade_counts` do not change the list you give them.
- [ ] `comparison_note.txt` has five sentences.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- [expression for item in iterable if condition] builds a new list.
- A lambda is a small function written in one expression.
- Functions are values: you can pass them around.
- map() changes every item; filter() keeps the items that pass a test.
- The last line of a traceback names the error type.
- Read error messages carefully: Python often suggests the fix.
- try runs risky code; except handles the error.
- Catch the specific error you expect, not every error.
- A pure function has no side effects.
- Recursion solves a problem by calling the function on a smaller problem.
- Logic programming states facts and rules, then asks questions.
- The same problem can be solved in more than one style.

::::::::::::::::::::::::::::::::::::::::::::::::
