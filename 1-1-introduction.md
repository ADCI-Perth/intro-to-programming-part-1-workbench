---
title: '1.1 Introduction to Python'
teaching: 25
exercises: 16
---

:::::::::::::::::::::::::::::::::::::: questions

- What is Python and why is it a good first language?
- How do I run Python code in the shell and in a file?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Install Python and PyCharm and run a first program.
- Use the Python shell for quick calculations.
- Recognise the main Python data types.

::::::::::::::::::::::::::::::::::::::::::::::::

## Welcome

Welcome to **Intro to Programming**, a six-week beginner Python course. Each week has a week page that tells you what to watch, which sections to read, a short Concepts Bridge note and a practice task. This is Section 1.1, the first section of Week 1.

## Introduction

Python is a high-level programming language for general-purpose programming. It is an open source, interpreted, object-oriented programming language. Python was created by a Dutch programmer, Guido van Rossum. The name of the Python programming language was derived from a British sketch comedy series, *Monty Python's Flying Circus*.  The first version was released on February 20, 1991. In this course you will learn Python 3 step by step, with easy-to-understand explanations, real-world examples and hands-on exercises.

The course is designed for complete beginners. Plan to spend up to 6 hours each week, following the time plan on each week page.

## Why Python ?

It is a programming language which is very close to human language and because of that, it is easy to learn and use.
Python is used by various industries and companies (including Google). It has been used to develop web applications, desktop applications, system administration, and machine learning libraries. Python is a highly embraced language in the data science and machine learning community. I hope this is enough to convince you to start learning Python. Python is eating the world and you are killing it before it eats you.

## Environment Setup

### Installing Python

To run a python script you need to install python. Let's [download](https://www.python.org/) python.
If your are a windows user, click the button encircled in red.

> 📷 **Image placeholder:** python.org download page with the Windows download button highlighted  
> Add your screenshot as `episodes/fig/1.1-install-windows.png` and replace this note with `![python.org download page with the Windows download button highlighted](fig/1.1-install-windows.png)`.

If you are a macOS user, click the button encircled in red.

> 📷 **Image placeholder:** python.org download page with the macOS download button highlighted  
> Add your screenshot as `episodes/fig/1.1-install-macos.png` and replace this note with `![python.org download page with the macOS download button highlighted](fig/1.1-install-macos.png)`.

To check if python is installed write the following command on your device terminal.

```bash
python3 --version
```

You should see something like this (any version 3.12 or newer is fine):

```output
Python 3.12.10
```

As you can see from the terminal, I am using _Python 3.7.5_ version at the moment. Your version of Python might be different from mine by but it should be 3.6 or above. If you manage to see the python version, well done. Python has been installed on your machine. Continue to the next section.

### Python Shell

Python is an interpreted scripting language, so it does not need to be compiled. It means it executes the code line by line. Python comes with a _Python Shell (Python Interactive Shell)_. It is used to execute a single python command and get the result.

Python Shell waits for the Python code from the user. When you enter the code, it interprets the code and shows the result in the next line.
Open your terminal or command prompt(cmd) and write:

```bash
python
```

```output
Python 3.12.10 (...) on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The Python interactive shell is opened and it is waiting for you to write Python code(Python script). You will write your Python script next to this symbol >>> and then click Enter.
Let us write our very first script on the Python scripting shell.

```python
>>> 2 + 3
5
>>>
```

Well done, you wrote your first Python script on Python interactive shell. How do we close the Python interactive shell ?
To close the shell, next to this symbol >>> write **exit()** command and press Enter.

```python
>>> 2 + 3
5
>>> exit()
```

Now, you know how to open the Python interactive shell and how to exit from it.

Python will give you results if you write scripts that Python understands, if not it returns errors. Let's make a deliberate mistake and see what Python will return.

```python
>>> 2 + 3
5
>>> 2 x 3
  File "<stdin>", line 1
    2 x 3
      ^
SyntaxError: invalid syntax
```

As you can see from the returned error, Python is so clever that it knows the mistake we made and which was _Syntax Error: invalid syntax_. Using x as multiplication in Python is a syntax error because (x) is not a valid syntax in Python. Instead of (**x**) we use asterisk (*) for multiplication. The returned error clearly shows what to fix.

The process of identifying and removing errors from a program is called _debugging_. Let us debug it by putting * in place of **x**.

```python
>>> 2 x 3
  File "<stdin>", line 1
    2 x 3
      ^
SyntaxError: invalid syntax
>>> 2 * 3
6
```

Our bug was fixed, the code ran and we got a result we were expecting. As a programmer you will see such kind of errors on daily basis. It is good to know how to debug. To be good at debugging you should understand what kind of errors you are facing. Some of the Python errors you may encounter are _SyntaxError_, _IndexError_, _NameError_, _ModuleNotFoundError_, _KeyError_, _ImportError_, _AttributeError_, _TypeError_, _ValueError_, _ZeroDivisionError_ etc. We will see more about different Python **_error types_** in later sections.

Let us practice more how to use Python interactive shell. Go to your terminal or command prompt and write the word **python**.

```output
Python 3.12.10 (...) on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The Python interactive shell is opened. Let us do some basic mathematical operations (addition, subtraction, multiplication, division, modulus,  exponentiation).

Let us do some maths first before we write any Python code:

- 2 + 3 = 5
- 3 - 2 = 1
- 3 \* 2 = 6
- 3 / 2 = 1.5
- 3 \*\* 2 = 3 x 3 = 9

In python, we have the following additional operations:

- 3 % 2 = 1 => which means finding the remainder
- 3 // 2 = 1 => which means removing the remainder

Let us change the above mathematical expressions to Python code. The Python shell has been opened and let us write a comment at the very beginning of the shell.

A _comment_ is a part of the code which is not executed by python. So we can leave some text in our code to make our code more readable. Python does not run the comment part. A comment in python starts with hash(#) symbol.
This is how you write a comment in python

```bash
 # comment starts with hash
 # this is a python comment, because it starts with a (#) symbol
```

```python
>>> 2 + 3    # addition (+)
5
>>> 3 - 2    # subtraction (-)
1
>>> 2 * 3    # multiplication (*), not x
6
>>> 3 / 2    # division (/)
1.5
>>> 3 % 2    # modulus (%) - the remainder
1
>>> 2 % 3    # why is this 2?
2
>>> 3 // 2   # floor division (//) - drops the remainder
1
>>> 3 ** 2   # exponent (**) - 3 * 3
9
```

Before we move on to the next section, let us practice more on the Python interactive shell. Close the opened shell by writing _exit()_ on the shell and open it again and let us practice how to write text on the Python shell.

```python
>>> 'Jack'    # a string in single quotes
'Jack'
>>> "Jack"    # a string in double quotes
'Jack'
>>> 'Welcome to Intro to Programming'
'Welcome to Intro to Programming'
>>> '''We use triple quote if the text is more than one line'''
'We use triple quote if the text is more than one line'
>>> exit()
```

### Installing Visual Studio Code

The Python interactive shell is good to try and test small script codes but it will not be for a big project. In real work environment, developers use different code editors to write codes. This course uses PyCharm, but many developers also use Visual Studio Code. Visual Studio Code is a very popular open source text editor. I am a fan of vscode and I would recommend to [download](https://code.visualstudio.com/) visual studio code, but if you are in favor of other editors, feel free to follow with what you have.

> 📷 **Image placeholder:** PyCharm download page (this course uses PyCharm instead of Visual Studio Code)  
> Add your screenshot as `episodes/fig/1.1-pycharm-download.png` and replace this note with `![PyCharm download page (this course uses PyCharm instead of Visual Studio Code)](fig/1.1-pycharm-download.png)`.

If you installed visual studio code, let us see how to use it.
If you prefer a video, you can follow this Visual Studio Code for Python [Video tutorial](https://www.youtube.com/watch?v=bn7Cx4z-vSo)

#### How to use visual studio code

Open the visual studio code by double clicking the visual studio icon. When you open it you will get this kind of interface. Try to interact with the labeled icons.

> 📷 **Image placeholder:** PyCharm window with the main areas labelled (project files, editor, Run button, terminal)  
> Add your screenshot as `episodes/fig/1.1-pycharm-ui.png` and replace this note with `![PyCharm window with the main areas labelled (project files, editor, Run button, terminal)](fig/1.1-pycharm-ui.png)`.

Create a folder named IntroToProgramming on your desktop. Then open it using visual studio code.

> 📷 **Image placeholder:** opening a project folder in PyCharm (File > Open)  
> Add your screenshot as `episodes/fig/1.1-pycharm-open-project.png` and replace this note with `![opening a project folder in PyCharm (File > Open)](fig/1.1-pycharm-open-project.png)`.

> 📷 **Image placeholder:** the project folder open in PyCharm  
> Add your screenshot as `episodes/fig/1.1-pycharm-project-open.png` and replace this note with `![the project folder open in PyCharm](fig/1.1-pycharm-project-open.png)`.

After opening it, you will see shortcuts for creating files and folders inside of IntroToProgramming project's directory. As you can see below, I have created the very first file, `helloworld.py`. You can do the same.

> 📷 **Image placeholder:** a new file helloworld.py created in the PyCharm project  
> Add your screenshot as `episodes/fig/1.1-pycharm-helloworld.png` and replace this note with `![a new file helloworld.py created in the PyCharm project](fig/1.1-pycharm-helloworld.png)`.

After a long day of coding, you want to close your code editor, right? This is how you will close the opened project.

> 📷 **Image placeholder:** closing a project in PyCharm (File > Close Project)  
> Add your screenshot as `episodes/fig/1.1-pycharm-close-project.png` and replace this note with `![closing a project in PyCharm (File > Close Project)](fig/1.1-pycharm-close-project.png)`.

You have now finished setting up the development environment. Let us start coding.

## Basic Python

### Python Syntax

A Python script can be written in Python interactive shell or in the code editor. A Python file has an extension .py.

### Python Indentation

An indentation is a white space in a text. Indentation in many languages is used to increase code readability; however, Python uses indentation to create blocks of code. In other programming languages, curly brackets are used to create code blocks instead of indentation. One of the common bugs when writing Python code is incorrect indentation.

```python
>>>     "Hello, World!"  # the spaces before the text cause an indentation error
  File "<stdin>", line 1
    "Hello, World!"  # the spaces before the text cause an indentation error
IndentationError: unexpected indent
>>> "Hello, World!"  # this runs without an error
'Hello, World!'
```

### Comments

Comments play a crucial role in enhancing code readability and allowing developers to leave notes within their code. In Python, any text preceded by a hash (#) symbol is considered a comment and is not executed when the code runs.

**Example: Single Line Comment**

```bash
    # This is the first comment
    # This is the second comment
    # Python is eating the world
```

**Example: Multiline Comment**

Triple quote can be used for multiline comment if it is not assigned to a variable

```bash
"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""
```

### Data types

In Python there are several types of data types. Let us get started with the most common ones. Different data types will be covered in detail in other sections. For the time being, let us just go through the different data types and get familiar with them. You do not have to have a clear understanding now.

#### Number

- Integer: Integer(negative, zero and positive) numbers
    Example:
    ... -3, -2, -1, 0, 1, 2, 3 ...
- Float: Decimal number
    Example
    ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
- Complex
    Example
    1 + j, 2 + 4j

#### String

A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

**Example:**

```python
'Jack'
'Australia'
'Python'
'I love coding'
'I hope you are enjoying the first week of Intro to Programming'
```

#### Booleans

A boolean data type is either a True or False value. T and F should be always uppercase.

**Example:**

```python
True   # Is the light on? If it is on, then the value is True
False  # Is the light on? If it is off, then the value is False
```

#### List

Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.

**Example:**

```python
[0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
['Australia', 'New Zealand', 'Canada', 'United Kingdom'] # all the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float
```

#### Dictionary

A Python dictionary object is an unordered collection of data in a key value pair format.

**Example:**

```python
{
'first_name': 'Jack',
'last_name': 'Wilson',
'country': 'Australia',
'age': 25,
'is_student': True,
'skills': ['Python', 'Excel', 'SQL']
}
```

#### Tuple

A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

**Example:**

```python
('Jack', 'Olivia', 'Liam', 'Emma', 'Noah') # names
```

```python
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets
```

#### Set

A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

In later sections, we will go in detail about each and every Python data type.

**Example:**

```python
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set
```

### Checking Data types

To check the data type of certain data/variable we use the **type** function. In the following terminal you will see different python data types:

```python
>>> type(10)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type(1 + 3j)
<class 'complex'>
>>> type('Jack')
<class 'str'>
>>> type([1, 2, 3])
<class 'list'>
>>> type({'name': 'Jack'})
<class 'dict'>
>>> type((2, 3, 4, 5))
<class 'tuple'>
>>> type({9.8, 3.14, 2.7})
<class 'set'>
>>> exit()
```

### Python File

First open your project folder, IntroToProgramming. If you don't have this folder, create a folder name called IntroToProgramming. Inside this folder, create a file called helloworld.py. Now, let's do what we did on python interactive shell using visual studio code.

The Python interactive shell was printing without using **print** but on visual studio code to see our result we should use a built in function _print()_. The _print()_ built-in function takes one or more arguments as follows _print('arument1', 'argument2', 'argument3')_. See the examples below.

**Example:**

The file name is `helloworld.py`

```python
# Section 1.1 - Intro to Programming

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Jack'))      # String
print(type([1, 2, 3]))   # List
print(type({'name': 'Jack'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
```

To run the python file check the image below. You can run the python file either by running the green button on Visual Studio Code or by typing _python helloworld.py_ in the terminal .

> 📷 **Image placeholder:** helloworld.py running in PyCharm (green Run button) with the output in the Run window  
> Add your screenshot as `episodes/fig/1.1-pycharm-run.png` and replace this note with `![helloworld.py running in PyCharm (green Run button) with the output in the Run window](fig/1.1-pycharm-run.png)`.

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 1

1. Check the python version you are using
2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
   - addition(+)
   - subtraction(-)
   - multiplication(\*)
   - modulus(%)
   - division(/)
   - exponential(\*\*)
   - floor division operator(//)
3. Write strings on the python interactive shell. The strings are the following:
   - Your name
   - Your family name
   - Your country
   - I am enjoying Intro to Programming
4. Check the data types of the following data:
   - 10
   - 9.8
   - 3.14
   - 4 - 4j
   - ['Jack', 'Python', 'Australia']
   - Your name
   - Your family name
   - Your country

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 2

1. Create a folder named section_1_1 inside IntroToProgramming folder. Inside section_1_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use _print()_ when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 3

1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
2. Find an [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between (2, 3) and (10, 8)

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- Python is a free, readable, general-purpose language.
- The shell runs one line at a time; a .py file runs a whole program.
- Use print() to see results when you run a file.
- type() tells you the data type of a value.

::::::::::::::::::::::::::::::::::::::::::::::::
