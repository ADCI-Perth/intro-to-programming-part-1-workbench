---
title: '1.2 Variables and Built-in Functions'
teaching: 25
exercises: 16
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I store values so I can use them again?
- Which functions come built into Python?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Create variables with clear snake_case names.
- Use built-in functions such as print(), len(), type() and input().
- Convert between data types (casting).

::::::::::::::::::::::::::::::::::::::::::::::::

## Built in functions

In Python we have lots of built-in functions. Built-in functions are globally available for your use that mean you can make use of the built-in functions without importing or configuring. Some of the most commonly used Python built-in functions are the following: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, _open()_, _file()_, _help()_, and _dir()_. In the following table you will see an exhaustive list of Python built-in functions taken from [python documentation](https://docs.python.org/3/library/functions.html).

| | | | | |
|---|---|---|---|---|
| `abs()` | `delattr()` | `hash()` | `memoryview()` | `set()` |
| `all()` | `dict()` | `help()` | `min()` | `setattr()` |
| `any()` | `dir()` | `hex()` | `next()` | `slice()` |
| `ascii()` | `divmod()` | `id()` | `object()` | `sorted()` |
| `bin()` | `enumerate()` | `input()` | `oct()` | `staticmethod()` |
| `bool()` | `eval()` | `int()` | `open()` | `str()` |
| `breakpoint()` | `exec()` | `isinstance()` | `ord()` | `sum()` |
| `bytearray()` | `filter()` | `issubclass()` | `pow()` | `super()` |
| `bytes()` | `float()` | `iter()` | `print()` | `tuple()` |
| `callable()` | `format()` | `len()` | `property()` | `type()` |
| `chr()` | `frozenset()` | `list()` | `range()` | `vars()` |
| `classmethod()` | `getattr()` | `locals()` | `repr()` | `zip()` |
| `compile()` | `globals()` | `map()` | `reversed()` | `__import__()` |
| `complex()` | `hasattr()` | `max()` | `round()` |  |

Let us open the Python shell and start using some of the most common built-in functions.

```python
>>> print('Hello, World!')   # prints the text Hello, World!
Hello, World!
>>> len('Hello, World!')     # counts the characters, including the space
13
>>> type('Hello, World!')    # checks the data type
<class 'str'>
>>> str(10)                  # converts a number to a string
'10'
>>> int('10')                # converts a string to a number
10
>>> float(10)                # converts an integer to a decimal
10.0
>>> input('Enter your name: ')   # takes user input
Enter your name: Jack
'Jack'
>>> exit()
```

Let us practice more by using different built-in functions

```python
>>> help('keywords')   # prints all Python reserved words

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

>>> help(str)          # opens a long help page about strings; press q to close it
>>> dir(str)           # lists everything a string can do (shortened here)
['__add__', '__class__', '__contains__', ..., 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isupper', 'join', 'lower', 'lstrip', 'replace', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'upper', 'zfill']
```

As you can see from the terminal above, Python has got reserved words. We do not use reserved words to declare variables or functions. We will cover variables in the next section.

I believe, by now you are familiar with built-in functions. Let us do one more practice of built-in functions and we will move on to the next section.

```python
>>> min(20, 30, 40, 50)      # gives the minimum value
20
>>> max(20, 30, 40, 50)      # gives the maximum value
50
>>> min([20, 30, 40, 50])    # takes a list and returns the minimum
20
>>> max([20, 30, 40, 50])    # takes a list and returns the maximum
50
>>> sum([20, 30, 40, 50])    # takes a list and returns the sum
140
>>> exit()
```

## Variables

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored.
Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

Python Variable Name Rules

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

Here are some example of valid variable names:

```bash
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
```

Invalid variables names

```bash
first-name
first@name
first$name
num-1
1num
```

We will use standard Python variable naming style which has been adopted by many Python developers. Python developers use snake case(snake_case) variable naming convention. We use underscore character after each word for a variable containing more than one word(eg. first_name, last_name, engine_rotation_speed).  The example below is an example of standard naming of variables, underscore is required when the variable name is more than one word.

When we assign a certain data type to a variable, it is called variable declaration. For instance in the example below my first name is assigned to a variable first_name. The equal sign is an assignment operator. Assigning means storing data in the variable. The equal sign in Python is not equality as in Mathematics.

_Example:_

```python
# Variables in Python
first_name = 'Jack'
last_name = 'Wilson'
country = 'Australia'
city = 'Perth'
age = 25
is_student = True
skills = ['Python', 'Excel', 'SQL']
person_info = {
   'first_name': 'Jack',
   'last_name': 'Wilson',
   'country': 'Australia',
   'city': 'Perth'
   }
```

Let us use the _print()_ and _len()_ built-in functions. Print function takes unlimited number of arguments. An argument is a value which we can be passed or put inside the function parenthesis, see the example below.

**Example:**

```python
print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument
```

Let us print and also find the length of the variables declared at the top:

**Example:**

```python
# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Student: ', is_student)
print('Skills: ', skills)
print('Person information: ', person_info)
```

### Declaring Multiple Variable in a Line

Multiple variables can also be declared in one line:

**Example:**

```python
first_name, last_name, country, age, is_student = 'Jack', 'Wilson', 'Australia', 25, True

print(first_name, last_name, country, age, is_student)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Student: ', is_student)
```

Getting user input using the _input()_ built-in function. Let us assign the data we get from a user into first_name and age variables.
**Example:**

```python
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
```

## Data Types

There are several data types in Python. To identify the data type we use the _type_ built-in function. I would like to ask you to focus on understanding different data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.

## Checking Data types and Casting

- Check Data types: To check the data type of certain data/variable we use the _type_
  **Examples:**

```python
# Different python data types
# Let's declare variables with various data types

first_name = 'Jack'         # str
last_name = 'Wilson'        # str
country = 'Australia'       # str
city = 'Perth'              # str
age = 25                    # int

# Printing out types
print(type('Jack'))              # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name': 'Jack'}))    # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip
```

- Casting: Converting one data type to another data type. We use _int()_, _float()_, _str()_, _list_, _set_
  When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

  **Examples:**

```python
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_float', num_float)       # 10.6
print('num_int', num_int)           # 10
# int('10.6') would give an error: int() cannot read a decimal point in a string

# str to list
first_name = 'Jack'
print(first_name)                    # Jack
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['J', 'a', 'c', 'k']
```

## Numbers

Number data types in Python:

1. Integers: Integer(negative, zero and positive) numbers
   Example:
   ... -3, -2, -1, 0, 1, 2, 3 ...

2. Floating Point Numbers(Decimal numbers)
   Example:
   ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3. Complex Numbers
   Example:
   1 + j, 2 + 4j, 1 - 1j

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 1

1. Inside IntroToProgramming create a folder called section_1_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Section 1.2: Intro to Programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_student and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 2

1. Check the data type of all your variables using type() built-in function
2. Using the _len()_ built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
5. Add num_one and num_two and assign the value to a variable total
6. Subtract num_two from num_one and assign the value to a variable diff
7. Multiply num_two and num_one and assign the value to a variable product
8. Divide num_one by num_two and assign the value to a variable division
9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10. Calculate num_one to the power of num_two and assign the value to a variable exp
11. Find floor division of num_one by num_two and assign the value to a variable floor_division
12. The radius of a circle is 30 metres.
    1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
    2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
    3. Take radius as user input and calculate the area.
13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- A variable is a name that refers to a value.
- Variable names use snake_case and cannot start with a number.
- input() always gives a string; convert it with int() or float() before doing maths.

::::::::::::::::::::::::::::::::::::::::::::::::
