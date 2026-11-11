---
title: 'Week 1: Getting started: how programs run, values and operators'
teaching: 164
exercises: 176
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 1, and how should I spend my 6 hours?
- What is Python and why is it a good first language?
- How do I run Python code in the shell and in a file?
- How do I store values so I can use them again?
- Which functions come built into Python?
- How does Python do arithmetic?
- How do I compare values and combine conditions?
- How does a program take in information, work on it and give a result?
- Can I combine input, variables and operators in a small program?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Install Python and PyCharm and run a first program.
- Use the Python shell for quick calculations.
- Recognise the main Python data types.
- Create variables with clear snake_case names.
- Use built-in functions such as print(), len(), type() and input().
- Convert between data types (casting).
- Use arithmetic, assignment, comparison and logical operators.
- Predict the result of an expression before running it.
- Describe a task as input, process and output.
- Write a short program that follows those three steps.
- Write a unit converter or calculator that runs in PyCharm.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 1 overview {#week-1-overview}

**Theme:** how a Python program runs, and the building blocks you use in every program: values, variables and operators.


### What you will be able to do this week

- Install Python and PyCharm, then write, run and debug a short script.
- Store values in variables and name the basic data types (numbers, text, true/false).
- Use arithmetic, comparison and logical operators.
- Read a short program and say, in plain words, what each line does.

### Time plan (under 6 hours)

| Block | What you do | Time |
|---|---|---|
| Watch | 7 short videos | 1 h 15 m |
| Read & practise | Sections 1.1, 1.2 and 1.3, with the assigned exercises | 1 h 55 m |
| Concepts Bridge | [Input, process, output](#week-1-bridge) | 0.5 h |
| Build | [Unit converter](#week-1-practice), your portfolio item for this week | 2 h |
| Quiz | Canvas quiz, 6 questions | 0.25 h |
| **Total** | | **5 h 55 m** |

Suggested order: watch a video, then read the matching lesson, then try the code yourself in PyCharm. Do the Bridge, Build and Quiz blocks last.

### Watch (1 h 15 m)

Watch in this order. Each link opens inside the Telusko playlist. **T#n** means "Telusko video number n".

| # | Video | Length | Look for |
|---|---|---|---|
| 1 | [T#1 Introduction to Python](https://www.youtube.com/watch?v=hEgO047GxaQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 4:13 | What Python is and what people use it for. |
| 2 | [T#2 Python Installation, PyCharm](https://www.youtube.com/watch?v=CScxy0294SE&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 9:33 | The steps to install Python and PyCharm. See the PyCharm note below. |
| 3 | [T#3 Getting Started with Python](https://www.youtube.com/watch?v=DWgzHbglNIo&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 14:49 | How to write and run your first line with `print()`. |
| 4 | [T#16 Working with PyCharm: Run, Debug, Trace](https://www.youtube.com/watch?v=akcEaEH91gI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 10:26 | How to run a file, and how to pause it line by line to see what happens. |
| 5 | [T#4 Variables in Python](https://www.youtube.com/watch?v=TqPzwenhMj0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 10:22 | A variable is a name that points to a value. |
| 6 | [T#10 Data Types in Python](https://www.youtube.com/watch?v=gCCVsvgR2KU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 14:35 | The main types: `int`, `float`, `str`, `bool`. |
| 7 | [T#11 Operators in Python](https://www.youtube.com/watch?v=v5MR5JnKcZI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:07 | What `+`, `-`, `*`, `/`, `//`, `%` and `**` each do. |

**Video total: 1 h 15 m.**

#### PyCharm note

T#2 was recorded before 2025. The PyCharm download page now looks different: there is **one** PyCharm download, with no "Community" or "Professional" choice. Install it and carry on with the free core features. This course uses PyCharm for everything.

### Read & practise (1 h 55 m)

Read each lesson, type the examples into PyCharm and run them. Then do the exercises in the table below (about 3 minutes each). Skip Level 2 and Level 3 unless you have time left over.

Each time includes reading the lesson plus about 3 minutes for each assigned exercise. Total: 35 + 35 + 45 = 115 minutes (1 h 55 m).

**Where is the data?** Some lessons open files such as `data/...` or `files/...`. These live in `assets/data/` and `assets/files/` at the root of this repository. You will not need them this week.

| Order | Lesson | Time | Read | Exercises |
|---|---|---|---|---|
| 1 | [Section 1.1: Introduction](#section-1-1) | about 35 min | All of it. | Level 1 |
| 2 | [Section 1.2: Variables and built-in functions](#section-1-2) | about 35 min | All of it. | Level 1, exercises 1 to 7. |
| 3 | [Section 1.3: Operators](#section-1-3) | about 45 min | All of it. | The Section 1.3 exercises (the page has one list, not levels). Do exercises 1 to 8. Exercises 9 to 11 are optional. |

#### Set up PyCharm

This course uses **PyCharm** only. Section 1.1 shows how to install and use PyCharm in the section called **"Installing PyCharm"**. A quick start:

1. Open PyCharm and choose **New Project**.
2. Name the project `IntroToProgramming` (or any name you like).
3. Right-click the project name, choose **New > Python File** and call it `helloworld`.
4. Type `print("Hello, World!")` and click the green **Run** arrow.

The Python shell, syntax, comments and data types in Section 1.1 all work in PyCharm too.

If a lesson asks you to make a folder such as `section_1_2`, make it inside your PyCharm project. Right-click the project name, then choose **New > Directory**.

### Concepts Bridge (0.5 h)

Open [bridge.md](#week-1-bridge). It shows how every program takes in information, works on it and gives a result. You practise this with everyday tasks before you write code. You will use the same steps in Week 3.

### Build (2 h)

Open the [practice task](#week-1-practice). You write a unit converter, then a short reflection about what your program does. Both go into your portfolio for this week.

### Quiz (0.25 h)

Take the Canvas quiz for Week 1 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `starter.py` (your converter)
- `reflection.txt` (five sentences, see the practice task)

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Nothing here is required. Try these if you want more.

**Videos**

- T#9 More on variables
- T#12 Number system conversion
- T#14 Bitwise operators
- T#15 Math functions
- T#17 Swap two variables
- T#67 Is Python Compiled or Interpreted? (6:48): https://www.youtube.com/watch?v=0BhSWyDEDC4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3
- [Max Rohowsky] [PyCharm Tutorial: Basics in 10 Minutes](https://www.youtube.com/watch?v=HHcZbXsZtm0) (10:00)

Find the Telusko videos by number in the [playlist](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3).

**More videos: Data with Baraa, Python Ultimate Course**

These lessons are from a different presenter. They are longer than the core videos, so treat them as extra explanation when you want more detail. Find them in the [playlist](https://www.youtube.com/playlist?list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn).

- [Data with Baraa] [What is Python (Visually Explained)](https://www.youtube.com/watch?v=GRNI9T9R8gQ&list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn) (10:47)
- [Data with Baraa] [Python Variables: Visually Explained](https://www.youtube.com/watch?v=YHgkADDCWJg&list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn) (13:39)
- [Data with Baraa] [Python Data Types: Visually Explained](https://www.youtube.com/watch?v=0uY2qNAsAWs&list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn) (30:23)
- [Data with Baraa] [Python Comparison Operators (Visually Explained)](https://www.youtube.com/watch?v=OZ7AinsDYVo&list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn) (7:08)
- [Data with Baraa] [Python Logical Operators (Visually Explained)](https://www.youtube.com/watch?v=yFaYylK1yCE&list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn) (17:55)
- [Data with Baraa] [Python Membership & Identity Operators (Visually Explained)](https://www.youtube.com/watch?v=qtTs03rI7W0&list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn) (12:32)

**Reading**

- Section 1.1, 1.2 and 1.3: the Level 2 and Level 3 exercises.
- Section 1.2, Level 1, exercises 8 to 13. These are six one-line variable declarations (age, year, true/false values and several variables on one line). Do them if you want extra practice.
- Driscoll, M. (2017) *Python 101*, chapters 1 and 3. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/
- Romano, F. (2018) *Learn Python Programming*, 2nd edn, chapter 1. Birmingham: Packt.

## 1.1 Introduction to Python {#section-1-1}

### Welcome

Welcome to **Intro to Programming**, a six-week beginner Python course. Each week has a week page that tells you what to watch, which sections to read, a short Concepts Bridge note and a practice task. This is Section 1.1, the first section of Week 1.

### Introduction

Python is a high-level programming language for general-purpose programming. It is an open source, interpreted, object-oriented programming language. Python was created by a Dutch programmer, Guido van Rossum. The name of the Python programming language was derived from a British sketch comedy series, *Monty Python's Flying Circus*.  The first version was released on February 20, 1991. In this course you will learn Python 3 step by step, with easy-to-understand explanations, real-world examples and hands-on exercises.

The course is designed for complete beginners: you do not need any programming or technical background. Many learners work in offices and want to move into programming or computing, so each week fits around a full-time job. Plan to spend up to 6 hours each week, following the time plan on each week page.

### Why Python ?

It is a programming language which is very close to human language and because of that, it is easy to learn and use.
Python is used by various industries and companies (including Google). It has been used to develop web applications, desktop applications, system administration, and machine learning libraries. Python is a highly embraced language in the data science and machine learning community. I hope this is enough to convince you to start learning Python. Python is eating the world and you are killing it before it eats you.

### Environment Setup

#### Installing Python

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

#### Python Shell

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

#### Installing PyCharm

Python shell is good for trying small pieces of code, but it is not good for a bigger project. Real developers write code in a code editor. This course uses **PyCharm** for every lesson, exercise and build, so you only need to install PyCharm.

If you prefer a video, watch [T#16 Working with PyCharm: Run, Debug, Trace](https://www.youtube.com/watch?v=akcEaEH91gI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) (10:26). It shows how to use PyCharm.

Download PyCharm from the [JetBrains website](https://www.jetbrains.com/pycharm/download/). There is one download, and the free core features are enough for this course.

> 📷 **Image placeholder:** PyCharm download page  
> Add your screenshot as `episodes/fig/1.1-pycharm-download.png` and replace this note with `![PyCharm download page](fig/1.1-pycharm-download.png)`.

##### How to use PyCharm

Open PyCharm. When you open it you will see the main window. Try to interact with the labelled icons.

> 📷 **Image placeholder:** PyCharm window with the main areas labelled (project files, editor, Run button, terminal)  
> Add your screenshot as `episodes/fig/1.1-pycharm-ui.png` and replace this note with `![PyCharm window with the main areas labelled (project files, editor, Run button, terminal)](fig/1.1-pycharm-ui.png)`.

Create a folder named IntroToProgramming on your desktop. Then open it in PyCharm using **File > Open**.

> 📷 **Image placeholder:** opening a project folder in PyCharm (File > Open)  
> Add your screenshot as `episodes/fig/1.1-pycharm-open-project.png` and replace this note with `![opening a project folder in PyCharm (File > Open)](fig/1.1-pycharm-open-project.png)`.

> 📷 **Image placeholder:** the project folder open in PyCharm  
> Add your screenshot as `episodes/fig/1.1-pycharm-project-open.png` and replace this note with `![the project folder open in PyCharm](fig/1.1-pycharm-project-open.png)`.

After the project opens, you will see shortcuts for creating files and folders inside the IntroToProgramming folder. The screenshot below shows the first file, `helloworld.py`. You can do the same.

> 📷 **Image placeholder:** a new file helloworld.py created in the PyCharm project  
> Add your screenshot as `episodes/fig/1.1-pycharm-helloworld.png` and replace this note with `![a new file helloworld.py created in the PyCharm project](fig/1.1-pycharm-helloworld.png)`.

When you finish for the day, close the project. This is how you do it.

> 📷 **Image placeholder:** closing a project in PyCharm (File > Close Project)  
> Add your screenshot as `episodes/fig/1.1-pycharm-close-project.png` and replace this note with `![closing a project in PyCharm (File > Close Project)](fig/1.1-pycharm-close-project.png)`.

You have now finished setting up the development environment. Let us start coding.

### Basic Python

#### Python Syntax

A Python script can be written in Python interactive shell or in the code editor. A Python file has an extension .py.

#### Python Indentation

An indentation is a white space in a text. Indentation in many languages is used to increase code readability; however, Python uses indentation to create blocks of code. In other programming languages, curly brackets are used to create code blocks instead of indentation. One of the common bugs when writing Python code is incorrect indentation.

```python
>>>     "Hello, World!"  # the spaces before the text cause an indentation error
  File "<stdin>", line 1
    "Hello, World!"  # the spaces before the text cause an indentation error
IndentationError: unexpected indent
>>> "Hello, World!"  # this runs without an error
'Hello, World!'
```

#### Comments

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

#### Data types

In Python there are several types of data types. Let us get started with the most common ones. Different data types will be covered in detail in other sections. For the time being, let us just go through the different data types and get familiar with them. You do not have to have a clear understanding now.

##### Number

- Integer: Integer(negative, zero and positive) numbers
    Example:
    ... -3, -2, -1, 0, 1, 2, 3 ...
- Float: Decimal number
    Example
    ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
- Complex
    Example
    1 + j, 2 + 4j

##### String

A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

**Example:**

```python
'Jack'
'Australia'
'Python'
'I love coding'
'I hope you are enjoying the first week of Intro to Programming'
```

##### Booleans

A boolean data type is either a True or False value. T and F should be always uppercase.

**Example:**

```python
True   # Is the light on? If it is on, then the value is True
False  # Is the light on? If it is off, then the value is False
```

##### List

Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.

**Example:**

```python
[0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
['Australia', 'New Zealand', 'Canada', 'United Kingdom'] # all the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float
```

##### Dictionary

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

##### Tuple

A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

**Example:**

```python
('Jack', 'Olivia', 'Liam', 'Emma', 'Noah') # names
```

```python
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets
```

##### Set

A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

In later sections, we will go in detail about each and every Python data type.

**Example:**

```python
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set
```

#### Checking Data types

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

#### Python File

First open your project folder, IntroToProgramming. If you don't have this folder, create a folder name called IntroToProgramming. Inside this folder, create a file called helloworld.py. Now, let's do what we did in the Python interactive shell, but in PyCharm.

The Python interactive shell was printing without using **print** but in PyCharm to see our result we should use a built in function _print()_. The _print()_ built-in function takes one or more arguments as follows _print('arument1', 'argument2', 'argument3')_. See the examples below.

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

To run the python file check the image below. You can run the Python file by clicking the green Run button in PyCharm, or by typing _python helloworld.py_ in the terminal .

> 📷 **Image placeholder:** helloworld.py running in PyCharm (green Run button) with the output in the Run window  
> Add your screenshot as `episodes/fig/1.1-pycharm-run.png` and replace this note with `![helloworld.py running in PyCharm (green Run button) with the output in the Run window](fig/1.1-pycharm-run.png)`.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

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

### Exercises: Level 2

1. Create a folder named section_1_1 inside IntroToProgramming folder. Inside section_1_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use _print()_ when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 3

1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
2. Find an [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between (2, 3) and (10, 8)

::::::::::::::::::::::::::::::::::::::::::::::::

## 1.2 Variables and Built-in Functions {#section-1-2}

### Built in functions

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

### Variables

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

#### Declaring Multiple Variable in a Line

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

### Data Types

There are several data types in Python. To identify the data type we use the _type_ built-in function. I would like to ask you to focus on understanding different data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.

### Checking Data types and Casting

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

### Numbers

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

### Exercises: Level 1

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

### Exercises: Level 2

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

## 1.3 Operators {#section-1-3}

### Boolean

A boolean data type represents one of the two values: _True_ or _False_. The use of these data types will be clear once we start using the comparison operator. The first letter **T** for True and **F** for False should be capital unlike JavaScript.
**Example: Boolean Values**

```python
print(True)
print(False)
```

### Operators

Python language supports several types of operators. In this section, we will focus on few of them.

#### Assignment Operators

Assignment operators are used to assign values to variables. Let us take = as an example. Equal sign in mathematics shows that two values are equal, however in Python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable. The table below shows the different types of python assignment operators, taken from [w3school](https://www.w3schools.com/python/python_operators.asp).

| Operator | Example | Same as |
|---|---|---|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
| `&=` | `x &= 3` | `x = x & 3` |
| `\|=` | `x \|= 3` | `x = x \| 3` |
| `^=` | `x ^= 3` | `x = x ^ 3` |
| `>>=` | `x >>= 3` | `x = x >> 3` |
| `<<=` | `x <<= 3` | `x = x << 3` |

#### Arithmetic Operators:

- Addition(+): a + b
- Subtraction(-): a - b
- Multiplication(*): a * b
- Division(/): a / b
- Modulus(%): a % b
- Floor division(//): a // b
- Exponentiation(**): a ** b

| Operator | Name | Example |
|---|---|---|
| `+` | Addition | `x + y` |
| `-` | Subtraction | `x - y` |
| `*` | Multiplication | `x * y` |
| `/` | Division | `x / y` |
| `%` | Modulus | `x % y` |
| `**` | Exponentiation | `x ** y` |
| `//` | Floor division | `x // y` |

**Example: Integers**

```python
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2
```

**Example: Floats**

```python
# Floating numbers
print('Floating Point Number, pi', 3.14)
print('Floating Point Number, gravity', 9.81)
```

**Example: Complex numbers**

```python
# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
```

Let's declare a variable and assign a number data type. I am going to use single character variable but remember do not develop a habit of declaring such types of variables. Variable names should be all the time mnemonic.

**Example:**

```python
# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 2 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
```

**Example:**

```python
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)
```

Let us start connecting the dots and start making use of what we already know to calculate (area, volume,density,  weight, perimeter, distance, force).

**Example:**

```python
# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)   # 314.0

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)   # 200

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # 735.75 N - adding the unit to the weight

# Calculate the density of a liquid
mass = 75 # in kg
volume = 0.075 # in cubic metres
density = mass / volume
print(density, 'kg/m^3') # 1000.0 kg/m^3 - adding the unit to the density

```

#### Comparison Operators

In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value. The following table shows Python comparison operators which was taken from [w3shool](https://www.w3schools.com/python/python_operators.asp).

| Operator | Name | Example |
|---|---|---|
| `==` | Equal | `x == y` |
| `!=` | Not equal | `x != y` |
| `>` | Greater than | `x > y` |
| `<` | Less than | `x < y` |
| `>=` | Greater than or equal to | `x >= y` |
| `<=` | Less than or equal to | `x <= y` |
**Example: Comparison Operators**

```python
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
```

In addition to the above comparison operator Python uses:

- _is_: Returns true if both variables are the same object(x is y)
- _is not_: Returns true if both variables are not the same object(x is not y)
- _in_: Returns True if the queried list contains a certain item(x in y)
- _not in_: Returns True if the queried list doesn't have a certain item(x not in y)

```python
first_list = [1, 2, 3]
same_list = first_list               # same_list points to the same list as first_list
copy_list = [1, 2, 3]                # a new list that looks the same
print('same_list is first_list:', same_list is first_list)          # True - the same object
print('copy_list is first_list:', copy_list is first_list)          # False - a different object
print('copy_list is not first_list:', copy_list is not first_list)  # True
print('copy_list == first_list:', copy_list == first_list)          # True - the values are equal
print("'P' in 'Perth':", 'P' in 'Perth')            # True - P is found in the string
print("'B' not in 'Perth':", 'B' not in 'Perth')    # True - there is no B in Perth
print('coding' in 'coding for all')                 # True - the sentence contains the word coding
print("'a' in 'an':", 'a' in 'an')                  # True
```

#### Logical Operators

Unlike other programming languages python uses keywords _and_, _or_ and _not_ for logical operators. Logical operators are used to combine conditional statements:

| Operator | Description | Example |
|---|---|---|
| `and` | Returns `True` if both statements are true | `x < 5 and x < 10` |
| `or` | Returns `True` if one of the statements is true | `x < 5 or x < 4` |
| `not` | Reverses the result: returns `False` if the result is true | `not(x < 5 and x < 10)` |

```python
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

```output
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100.0
```

5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

```output
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
```

6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10) 
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
15. Use _not in_ to check that _Java_ is not in the sentence from task 14
16. Find the length of the text _python_ and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int(float('9.8')) is equal to 10 (hint: int() cannot read '9.8' directly, so convert it to a float first)
21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

```output
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
```

22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

```output
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
```

23. Write a Python script that displays the following table

```output
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Input, Process, Output {#week-1-bridge}

**Time:** about 30 minutes (10 min reading, 10 min running the example, 10 min activity).

### Why this matters

Every program, however big, does three jobs:

1. **Input**: it gets information in.
2. **Process**: it works on that information.
3. **Output**: it gives a result back.

Thinking in these three steps before you type helps you solve problems (LO 1). You will use the same steps for the grade calculator in Week 3, and again when you design programs in Week 6.

### The big idea: everyday tasks have inputs, processes and outputs

You already do this at home and at work. Here are three examples:

| Everyday task | Input | Process | Output |
|---|---|---|---|
| Working out your pay | Hours worked, hourly rate | Multiply hours by rate | Gross pay |
| Making a cup of tea | Water, tea bag, milk | Heat the water, steep the tea bag | A cup of tea |
| Checking your change at a shop | Price, money given | Subtract price from money given | Change to hand back |

Notice that the process is the step that does the work. The input and output are what goes in and comes out.

### How Python runs your file

Python reads your file from top to bottom and carries out each line in order. When it reaches `input()`, it waits for the user to type something. When it reaches `print()`, it shows a result on the screen.

### Worked example

Here is the pay example as a program. Copy it into PyCharm and run it.

> **Just copy and run this.** You have not used every part of this yet. `input()` asks the user for text, and `float()` turns that text into a number. You will use both in the Build task.

```python
hours = float(input("Hours worked: "))   # input
rate = float(input("Hourly rate: "))     # input
pay = hours * rate                       # process
print("Gross pay:", pay)                 # output
```

Run it twice, with different numbers. Each time, notice:

- which lines take in information (input),
- which line does the work (process),
- which line shows the result (output).

### Activity (10 minutes)

1. Write the input, process and output for **two** everyday tasks from your own life or work. Use a table like the one above, on paper or in a text file.
2. Change the process line in the worked example so the pay has 10% tax taken off. Hint: `pay = hours * rate * 0.9` takes off 10%. Run the program again to check.
3. In two or three sentences, answer: *what would happen if the user typed "ten" instead of 10?* You will learn how to deal with this in Week 4.

#### Model answer

1. Answers will vary. A good answer names the inputs, one clear process, and one clear output.
2. The result is 90% of the gross pay. For example, 38 hours at $30 per hour is $1,140 before tax, and $1,026 after the 10% reduction.
3. The program stops with an error, because `float("ten")` cannot turn the word into a number. Good programs check input before using it.

### Further reading

- Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Introduction).
- Romano, F. (2018) *Learn Python Programming*, 2nd edn. Birmingham: Packt. Chapter 1.

## Practice task: Unit Converter {#week-1-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [starter.py](files/week-1/starter.py)
- [solution.py](files/week-1/solution.py)
- [test_solution.py](files/week-1/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time:** about 2 hours. This is your portfolio item for Week 1. Your tutor marks it at the end of the week.

### Goal

Write a small script that asks for a distance and a temperature, converts them and prints the answers. Then write five sentences about what your program does.

You only need what you learned this week: variables, `input()`, `float()`, arithmetic operators and `print()`.

### Part 1: the converter (about 1 h 15 min)

Work in `starter.py`. Follow the TODO comments.

1. Ask the user for a distance in **kilometres**. `input()` gives you text, so wrap it in `float()` to get a number.
2. Convert it to **miles**: `miles = kilometres * 0.621371`.
3. Ask for a temperature in **degrees Celsius** and convert it to **Fahrenheit**: `fahrenheit = celsius * 9 / 5 + 32`.
4. Round each answer to 2 decimal places with `round(value, 2)`.
5. Print both answers in exactly this form, so the checks can read them:

```
Enter a distance in kilometres: 10
Enter a temperature in Celsius: 25
10.0 km is 6.21 miles
25.0 C is 77.0 F
```

The `10` and `25` are typed by the user. Everything else is printed by your script.

#### Hints

- `float("10")` gives `10.0`. That is why the output says `10.0 km`.
- `input("Enter ...: ")` shows a message (a **prompt**) and waits for the user to type.
- Print with commas: `print(kilometres, "km is", miles, "miles")`. `print` puts a space between the items.
- `*` is multiply, `/` is divide. Python does multiplication and division before `+`.

#### Stretch (only if you have time)

Add a third conversion, such as kilograms to pounds (1 kg = 2.20462 lb). Keep the same style.

### Part 2: reflection (about 30 min)

Create a plain text file called `reflection.txt` (in PyCharm: **New > File**). Write **exactly five sentences** about your program:

1. What the program asks the user for.
2. What it calculates.
3. What it prints.
4. What happens if the user types a word, such as `ten`, instead of a number. Try it to check.
5. One change you would make to make the program easier to use.

Use the [Concepts Bridge](#week-1-bridge) to help you describe the input, process and output.

### Check your work

- [ ] `starter.py` runs with no errors.
- [ ] It asks for kilometres, then Celsius.
- [ ] 10 km prints `10.0 km is 6.21 miles`.
- [ ] 25 C prints `25.0 C is 77.0 F`.
- [ ] You used only variables, `input()`, `float()`, `round()`, arithmetic and `print()`.
- [ ] `reflection.txt` has five sentences, covering all five points above.

### Run the automatic checks (optional)

The file `test_solution.py` checks the model answer in `solution.py`. It runs the script the way a user would: it types the answers in for you, then checks what the script printed. You can point it at your own work. In a terminal, from the project folder:

**Windows (PowerShell):**

```
$env:CONVERTER_SCRIPT = "starter.py"; python -m pytest weeks/week-1/practice
```

**macOS or Linux:**

```
CONVERTER_SCRIPT=starter.py python -m pytest weeks/week-1/practice
```

If pytest is not installed, run `python -m pip install pytest` first. Try the task yourself before you look at `solution.py`.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- Python is a free, readable, general-purpose language.
- The shell runs one line at a time; a .py file runs a whole program.
- Use print() to see results when you run a file.
- type() tells you the data type of a value.
- A variable is a name that refers to a value.
- Variable names use snake_case and cannot start with a number.
- input() always gives a string; convert it with int() or float() before doing maths.
- / always gives a float; // drops the remainder; % gives the remainder.
- Comparison operators give True or False.
- and, or and not combine conditions.
- == checks equal values; is checks the same object.
- Every program takes in information, works on it and gives a result.
- input() waits for the user; print() shows the result.
- Python reads a file from top to bottom and carries out each line.
- Small programs are built from variables, input, operators and print.

::::::::::::::::::::::::::::::::::::::::::::::::
