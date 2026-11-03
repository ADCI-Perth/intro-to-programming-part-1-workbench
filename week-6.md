---
title: 'Week 6: Modules, libraries and choosing a paradigm'
teaching: 105
exercises: 214
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 6, and how should I spend my 6 hours?
- How do I split code into files and use code others have written?
- How do I install and use third-party packages?
- How do I use packages safely?
- How do I choose a paradigm for a problem?
- Can I finish a complete program and justify its design?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Create and import your own module.
- Use built-in modules such as math, random, os and statistics.
- Install, list and remove packages with pip.
- Fetch data from the web with requests.
- Create a simple package of your own.
- Add type hints to a function.
- Describe the risks of third-party libraries.
- Compare paradigms using a set of criteria.
- Finish the library-loan manager across modules, and compare two paradigms in it.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 6 overview {#week-6-overview}

**Theme:** split your code into modules, use other people's code safely, and decide which programming style suits a problem.

This is the last week. You also finish the mini project you started in Week 5.

### Learning goals

By the end of this week you can:

1. Write your own module and import it, and explain what `if __name__ == "__main__":` does.
2. Use built-in modules such as `random` and `math`.
3. Install a third-party package with `pip` inside a virtual environment, and say why pinning versions matters.
4. Explain, in a few sentences, which programming paradigm (style) suits a problem and why.

### Time plan (5 h 19 min)

| Block | Time | What you do |
|---|---|---|
| Watch | 49 min | Six videos (below) |
| Read & practise | 1 h | Section 6.1 and Section 6.2 notes, install practice, plus Level 1 exercises |
| Concepts Bridge | 30 min | [bridge.md](#week-6-bridge): type safety, library risk, choosing a paradigm |
| Build | 3 h | [Mini project, Part 2](#week-6-practice) |
| **Total** | **5 h 19 min** | Under the 6 h cap, so there is spare time for catching up |

Optional material is not counted in the total.

### Watch (49 min)

Watch in this order. Pause and try things in PyCharm as you go.

| # | Video | Length | Look out for |
|---|---|---|---|
| 1 | **T#45** Modules | 7:20 | How `import` finds a file and runs it. https://www.youtube.com/watch?v=1RuMJ53CKds&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 |
| 2 | **T#46** Special Variable `__name__` | 5:43 | Why code under `if __name__ == "__main__":` runs only when you run the file directly. https://www.youtube.com/watch?v=pzNISmtmzcY&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 |
| 3 | **[Corey Schafer]** pip: An In-Depth Look at the Package Management System | 9:06 | The main pip commands: install, uninstall, list, freeze. https://www.youtube.com/watch?v=U2ZN104hIcc |
| 4 | **[Tech With Tim]** Python Virtual Environments: Full Tutorial for Beginners | 9:05 | Why each project gets its own "box" of packages. https://www.youtube.com/watch?v=Y21OR1OPC9A |
| 5 | **T#28** Why NumPy? Installing NumPy | 6:58 | How PyCharm installs a package for you. https://www.youtube.com/watch?v=8LlXhtfNZEQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 |
| 6 | **[Computerphile]** Programming Paradigms | 10:44 | The names of the styles and what each is good at. You will use this for your paradigm note. https://www.youtube.com/watch?v=sqV3pL5x8PI |

### Read & practise (1 h)

Open each lesson, read it, type out the examples and run them. Do not just copy and paste.

#### Section 6.1: Modules (about 22 min)

Lesson: [Section 6.1: Modules](#section-6-1). Code: [lessons/6.1_code/](files/code/6.1/).

- Read: What is a Module, Creating a Module, Importing a Module, the two "Import Functions" sections, and the built-in modules **Math** and **Random**.
- Skim: OS, Sys, Statistics and String modules. Just know they exist.
- Do the **Level 1** exercises (1 to 3). They use `random`.

#### Section 6.2: pip and packages (about 28 min)

Lesson: [Section 6.2: pip and Packages](#section-6-2). Code: [lessons/6.2_code/mypackage/](files/code/6.2/mypackage).

- Read: What is PIP, Installing packages using pip, Uninstalling, List of Packages, Show Package, PIP Freeze, Creating a Package.
- Skim: Reading from URL. You need an internet connection and the `requests` package.
- Section 6.2's exercises read web data and use statistics, so they are too big for this block. Instead, create a small package of your own (a folder with `__init__.py` and one module), then import it from a separate file.

#### Installing packages: command line and PyCharm (about 10 min hands-on)

The lessons show the command line (Mac or Linux style). On Windows, use PowerShell or the **Terminal** tab inside PyCharm. If `pip` is not found, type `python -m pip` instead.

**Command line way**

```
python -m venv .venv
.venv\Scripts\activate
python -m pip install requests
python -m pip freeze
```

- On Mac or Linux, activate with `source .venv/bin/activate`.
- A **virtual environment** is a private folder of packages for one project. It stops projects from clashing.

**PyCharm way**

- Make a virtual environment: *File > Settings > Project > Python Interpreter > Add Interpreter > Add Local Interpreter > Virtualenv Environment > New*. (On Mac: *PyCharm > Settings*.) New projects usually do this for you.
- Install a package: in the same *Python Interpreter* page, click the **+** button, search for the package (for example `requests`), then click **Install Package**. This is what T#28 shows with NumPy.
- You can also open the **Terminal** tab at the bottom of PyCharm. It starts with your virtual environment already active.

#### Data files

Some optional lessons open files such as `data/weight-height.csv`. Those files live in [`assets/data/`](data/course-data.zip) at the top of this repository. Point your code at that folder.

### Concepts Bridge (30 min)

Go to [bridge.md](#week-6-bridge). It covers type hints, risks of third-party libraries, and a criteria table for choosing a paradigm (LO 4).

### Build (3 h)

Go to [practice/README.md](#week-6-practice). You finish the Week 5 mini project (a library-loan manager): add search, type hints, a menu program, and a short note on paradigms.

This is practice only. Nothing here is marked.

### Optional

Only if you have time and are curious.

**Videos**

- **T#47** `__name__` part 2 (Telusko playlist)
- **T#29 to T#31** NumPy arrays and matrices (Telusko playlist)
- **T#77** Jupyter Notebook (Telusko playlist)
- **T#74** Git and GitHub with Python (Telusko playlist)
- **[Low Level]** How Can Memory-Safe Code Stop Hackers? (7:43): https://www.youtube.com/watch?v=lxUYZVX_FjQ

**Lessons**

- [Section 6.4: Virtual environments](../learners/6-4-virtual-environments.md)
- [Section 6.3: Web scraping](../learners/6-3-web-scraping.md)
- [Section 6.5: Statistics (NumPy)](../learners/6-5-statistics-numpy.md)
- [Section 6.6: Pandas](../learners/6-6-pandas.md)

**Other**

- Unix time and time-related bugs: https://www.youtube.com/watch?v=-5wpm-gesOY
- Driscoll, M. (2017) *Python 101*, chapters 27, 29 and 33. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/
- Romano, F. (2018) *Learn Python Programming*, 2nd edn, chapter 5. Packt.

## 6.1 Modules {#section-6-1}

### Modules

#### What is a Module

A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.

#### Creating a Module

To create a module we write our codes in a python script and we save it as a .py file. Create a file named mymodule.py inside your project folder. Let us write some code in this file.

```python
# mymodule.py file
def generate_full_name(firstname, lastname):
    space = ' '
    fullname = firstname + space + lastname
    return fullname


def sum_two_nums(num1, num2):
    return num1 + num2


gravity = 9.81
person = {
    "firstname": "Jack",
    "age": 25,
    "country": "Australia",
    "city": "Perth"
}
```

Create main.py file in your project directory and import the mymodule.py file.

#### Importing a Module

To import the file we use the _import_ keyword and the name of the file only.

```python
# main.py file
import mymodule
print(mymodule.generate_full_name('Jack', 'Wilson')) # Jack Wilson
```

#### Import Functions from a Module

We can have many functions in a file and we can import all the functions differently.

```python
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Jack','Wilson'))  # Jack Wilson
print(sum_two_nums(1,9))                     # 10
mass = 100
weight = mass * gravity
print(weight)                                # 981.0
print(person['firstname'])                   # Jack
```

#### Import Functions from a Module and Renaming

During importing we can rename the name of the module.

```python
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Jack','Wilson'))  # Jack Wilson
print(total(1, 9))                # 10
mass = 100
weight = mass * g
print(weight)                     # 981.0
print(p)                          # {'firstname': 'Jack', 'age': 25, 'country': 'Australia', 'city': 'Perth'}
print(p['firstname'])             # Jack
```

### Import Built-in Modules

Like other programming languages we can also import modules by importing the file/function using the key word _import_. Let's import the common module we will use most of the time. Some of the common built-in modules: _math_, _datetime_, _os_,_sys_, _random_, _statistics_, _collections_, _json_,_re_

#### OS Module

Using python _os_ module it is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.

```python
# import the module
import os
# Getting the current working directory (the folder Python is working in)
print(os.getcwd())                         # e.g. C:\Users\jack\IntroToProgramming
# Creating a directory
os.mkdir('practice_folder')
print(os.path.exists('practice_folder'))   # True
# Removing a directory (it must be empty)
os.rmdir('practice_folder')
print(os.path.exists('practice_folder'))   # False
# os.chdir('some_folder') changes the current directory to some_folder
```

#### Sys Module

The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

Example of a script.py file:

```python
import sys
# print(sys.argv[0], sys.argv[1], sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy {}!'.format(sys.argv[1], sys.argv[2]))
```

To check how this script works, run this in the terminal (the quotes keep "Intro to Programming" as one argument):

```bash
python script.py Jack "Intro to Programming"
```

The result:

```bash
Welcome Jack. Enjoy Intro to Programming!
```

Some useful sys commands:

```python
import sys
# To know the largest integer variable it takes
print(sys.maxsize)   # 9223372036854775807 on a 64-bit computer
# To know the folders Python searches for modules
print(sys.path)
# To know the version of python you are using
print(sys.version)   # e.g. 3.12.10 (...)
# To stop the program straight away
sys.exit()
```

#### Statistics Module

The statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: _mean_, _median_, _mode_, _stdev_ etc.

```python
from statistics import * # importing all the statistics modules
ages = [20, 20, 24, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

#### Math Module

Module containing many mathematical operations and constants.

```python
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2.0, logarithm with 10 as base
```

Now, we have imported the *math* module which contains lots of function which can help us to perform mathematical calculations. To check what functions the module has got, we can use _help(math)_, or _dir(math)_. This will display the available functions in the module. If we want to import only a specific function from the module we import it as follows:

```python
from math import pi
print(pi)  # 3.141592653589793
```

It is also possible to import multiple functions at once

```python
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(log10(100))         # 2.0

```

But if we want to import all the function in math module we can use \* .

```python
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(log10(100))          # 2.0
```

When we import we can also rename the name of the function.

```python
from math import pi as  PI
print(PI) # 3.141592653589793
```

#### String Module

A string module is a useful module for many purposes. The example below shows some use of the string module.

```python
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

#### Random Module

By now you are familiar with importing modules. Let us do one more import to get very familiar with it. Let us import _random_ module which gives us a random number between 0 and 0.9999.... The _random_ module has lots of functions but in this section we will only use _random_ and _randint_.

```python
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999, e.g. 0.6394
print(randint(5, 20)) # it returns a random integer between 5 and 20 inclusive, e.g. 13
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Write a function which generates a six digit/character random_user_id. 
   ```output
     print(random_user_id()) 
     '1ee33d'
   ```
2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
   
```output
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
   
```output
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
1. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
1. Write a function generate_colors which can generate any number of hexa or rgb colors.

```output
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
   ```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 3

1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
1. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

::::::::::::::::::::::::::::::::::::::::::::::::

## 6.2 pip and Packages {#section-6-2}

### Python PIP - Python Package Manager

#### What is PIP ?

PIP stands for Preferred installer program. We use _pip_ to install different Python packages.
Package is a Python module that can contain one or more modules or other packages. A module or modules that we can install to our application is a package.
In programming, we do not have to write every utility program, instead we install packages and import them to our applications.

#### Installing PIP

pip comes with Python, so you normally already have it. Open a terminal (in PyCharm: **View > Tool Windows > Terminal**) and check it:

```bash
python -m pip --version
```

```output
pip 25.0.1 from C:\...\site-packages\pip (python 3.12)
```

If you see a version number, pip is installed. Your number may be a little higher or lower. To upgrade pip to the newest version, run:

```bash
python -m pip install --upgrade pip
```

We write `python -m pip` rather than just `pip`, because it makes sure pip installs packages for the same Python that runs your code.

Let us check some of the packages used in the Python community for different purposes. Just to let you know that there are lots of packages available for use with different applications.

#### Installing packages using pip

Let us try to install _numpy_, called numeric python. It is one of the most popular packages in machine learning and data science community.

- NumPy is the fundamental package for scientific computing with Python. It contains among other things:
  - a powerful N-dimensional array object
  - sophisticated (broadcasting) functions
  - tools for integrating C/C++ and Fortran code
  - useful linear algebra, Fourier transform, and random number capabilities

```bash
python -m pip install numpy
```

Let us start using numpy. Open the Python interactive shell (type `python` in the terminal, or use PyCharm's **Python Console**) and import numpy as follows:

```python
>>> import numpy
>>> numpy.__version__
'2.5.3'
>>> lst = [1, 2, 3, 4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr + 2
array([3, 4, 5, 6, 7])
>>>
```

Your numpy version may be different; that is fine.

Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Let us install the big brother of numpy, _pandas_:

```bash
python -m pip install pandas
```

```python
>>> import pandas
>>>
```

If the import gives no error, pandas is installed.

This section is not about numpy nor pandas, here we are trying to learn how to install packages and how to import them. If it is needed, we will talk about different packages in other sections.

Let us import a web browser module, which can help us to open any website. We do not need to install this module, it is already installed by default with Python 3. For instance if you like to open any number of websites at any time or if you like to schedule something, this _webbrowser_ module can be used.

```python
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'https://www.python.org',
    'https://adci.edu.au',
    'https://docs.python.org/3/',
    'https://pypi.org',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)
```

#### Uninstalling Packages

If you do not like to keep the installed packages, you can remove them using the following command.

```bash
python -m pip uninstall packagename
```

#### List of Packages

To see the installed packages on our machine. We can use pip followed by list.

```bash
python -m pip list
```

#### Show Package

To show information about a package

```bash
python -m pip show packagename
```

```bash
python -m pip show requests
```

```output
Name: requests
Version: 2.34.2
Summary: Python HTTP for Humans.
Home-page:
Author:
Author-email: Kenneth Reitz <me@kennethreitz.org>
License: Apache-2.0
Location: C:\...\site-packages
Requires: certifi, charset_normalizer, idna, urllib3
Required-by:
```

If we want even more details, just add --verbose

```bash
python -m pip show --verbose requests
```

#### PIP Freeze

Generate installed Python packages with their version and the output is suitable to use it in a requirements file. A requirements.txt file is a file that should contain all the installed Python packages in a Python project.

```bash
python -m pip freeze
```

```output
certifi==2026.7.22
idna==3.20
numpy==2.5.3
pandas==3.0.6
requests==2.34.2
urllib3==2.8.0
```

Your list and version numbers will differ. The pip freeze gave us the packages used, installed and their version. We use it with requirements.txt file for deployment.

#### Reading from URL

By now you are familiar with how to read or write on a file located on your local machine. Sometimes, we would like to read from a website using url or from an API.
API stands for Application Program Interface. It is a means to exchange structured data between servers primarily as json data. To open a network connection, we need a package called _requests_ - it allows to open a network connection and to implement CRUD(create, read, update and delete) operations. In this section, we will cover only reading or getting part of a CRUD.

Let us install _requests_:

```bash
python -m pip install requests
```

We will see _get_, _status_code_, _headers_, _text_ and _json_ methods in _requests_ module:
  - _get()_: to open a network and fetch data from url - it returns a response object
  - _status_code_: After we fetched data, we can check the status of the operation (success, error, etc)
  - _headers_: To check the header types
  - _text_: to extract the text from the fetched response object
  - _json_: to extract json data

Let's read a text file from Project Gutenberg: the play *Romeo and Juliet*.

```python
import requests # importing the request module

url = 'https://www.gutenberg.org/cache/epub/1112/pg1112.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)                          # <Response [200]>
print(response.status_code)              # 200 - status code, success
print(response.headers['Content-Type'])  # text/plain; charset=utf-8
print(response.text[:47])                # The Project Gutenberg eBook of Romeo and Juliet
```

- Let us read from an API. PyPI, the website pip installs packages from, has a JSON API that describes every package: https://pypi.org/pypi/requests/json

```python
import requests

url = 'https://pypi.org/pypi/requests/json'  # information about the requests package
response = requests.get(url)  # opening a network and fetching a data
print(response)              # <Response [200]>
print(response.status_code)  # 200
package = response.json()    # change the JSON into a Python dictionary
print(package['info']['name'])     # requests
print(package['info']['version'])  # e.g. 2.34.2 - the newest version when you run it
print(package['info']['summary'])  # Python HTTP for Humans.
```

We use _json()_ method from response object, if the we are fetching JSON data. For txt, html, xml and other file formats we can use _text_.

#### Creating a Package

We organize a large number of files in different folders and sub-folders based on some criteria, so that we can find and manage them easily. As you know, a module can contain multiple objects, such as classes, functions, etc. A package can contain one or more relevant modules. A package is actually a folder containing one or more module files. Let us create a package named mypackage, using the following steps:

Create a new folder named mypackage inside IntroToProgramming folder
Create an empty **__init__**.py file in the mypackage folder.
Create modules arithmetics.py and greet.py with following code:

```python
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(a, b):
    return (a - b)

def multiple(a, b):
    return a * b

def division(a, b):
    return a / b

def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b
```

```python
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to Intro to Programming!'
```

The folder structure of your package should look like this:

```output
─ mypackage
    ├── __init__.py
    ├── arithmetics.py
    └── greet.py
```

Now let's open the python interactive shell and try the package we have created:

Open the Python interactive shell from your IntroToProgramming folder (the folder that contains mypackage):

```python
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1, 2, 3, 5)
11
>>> arithmetics.subtract(5, 3)
2
>>> arithmetics.multiple(5, 3)
15
>>> arithmetics.division(5, 3)
1.6666666666666667
>>> arithmetics.remainder(5, 3)
2
>>> arithmetics.power(5, 3)
125
>>> from mypackage import greet
>>> greet.greet_person('Jack', 'Wilson')
'Jack Wilson, welcome to Intro to Programming!'
>>>
```

As you can see our package works perfectly. The package folder contains a special file called **__init__**.py - it stores the package's content. If we put **__init__**.py in the package folder, python start recognizes it as a package.
The **__init__**.py exposes specified resources from its modules to be imported to other python files. An empty **__init__**.py file makes all functions available when a package is imported. The **__init__**.py is essential for the folder to be recognized by Python as a package.

#### Further Information About Packages

- Database
  - SQLAlchemy or SQLObject - Object oriented access to several different database systems
    - _pip install SQLAlchemy_
- Web Development
  - Django - High-level web framework.
    - _pip install django_
  - Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
    - _pip install flask_
- HTML Parser
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
    - _pip install beautifulsoup4_
  - PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.

- XML Processing
  - ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library
- GUI
  - PyQt - Bindings for the cross-platform Qt framework.
  - TkInter - The traditional Python user interface toolkit.
- Data Analysis, Data Science and Machine learning
  - Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
  - Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
  - SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
  - Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
  - TensorFlow: is a machine learning library built by Google.
  - Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
- Network:
  - requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
    - _pip install requests_

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1112/pg1112.txt'
2. Read the cat breeds API, cat_breeds_api = 'https://catfact.ninja/breeds?limit=100', and create a frequency table of the country each breed comes from (the data is in the 'data' key).
3. Use the PyPI JSON API (https://pypi.org/pypi/PACKAGE_NAME/json) to print the newest version and the summary of numpy, pandas and requests.
4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCI (https://archive.ics.uci.edu/datasets). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Type Safety, Library Risk and Choosing a Paradigm {#week-6-bridge}

**Time: 30 minutes.** Video 11 min (Indently, 11:25), reading 10 min, activity 9 min.

### Why this matters

Choosing approaches and tools means knowing the risks of third-party libraries, and understanding type safety and memory safety. The lessons this week show how to *use* packages. This note shows how to use them *safely*, then gives you a table of criteria for LO 4: judging which paradigm best suits a problem.

### 1. Type safety

A **type** says what kind of value you have: a whole number (`int`), text (`str`) and so on. **Type safety** means the language or its tools stop you using a value the wrong way.

Python checks types only while the program runs. This is called **dynamic typing**. A mistake can hide until the exact line runs:

```python
def double(x):
    return x * 2

print(double(4))
print(double("ha"))
```

Both lines work, but the second gives `haha`, which you may not have wanted. A **type hint** (or type annotation) tells readers, and checking tools, what you expect:

```python
def double(x: int) -> int:
    return x * 2

print(double(4))
```

`x: int` means "x should be an int". `-> int` means "this function returns an int". Python itself ignores hints when it runs. They are notes for people and tools.

A tool called **mypy** reads the hints and warns you *before* you run the code. This is **static type checking**. It is a third-party package, so install it with pip first (inside your virtual environment):

```
python -m pip install mypy
```

Now save this as `bad_types.py`:

```python
def double(x: int) -> int:
    return x * 2

double("ha")
```

Then run mypy:

```
python -m mypy bad_types.py
```

Mypy reports an error like `Argument 1 to "double" has incompatible type "str"; expected "int"`. The code still runs in plain Python, but mypy caught the likely mistake early. You do not need mypy to finish this course. The commands are here so you know what it does.

#### Watch

**[Indently]** A Quick Guide to Type Annotations (ft. Mypy) (11:25): https://www.youtube.com/watch?v=Y9fT4HVdCuQ

Look for: how to hint a function, a list (`list[int]`) and a value that might be `None`.

### 2. Third-party library risk

Every package you install is code written by a stranger. It runs with your permissions. Two simple habits lower the risk.

**Pin versions.** A **version** is a number such as `2.34.2`. If you ask for "the latest" `requests`, you may get a different version next month, and it might break your program or contain a new bug. **Pinning** means asking for one exact version. Record pins in a file called `requirements.txt`:

```
requests==2.34.2
```

`==` means "exactly this version". Anyone can then rebuild your setup with:

```
python -m pip install -r requirements.txt
```

You can create the file from your current environment with `python -m pip freeze > requirements.txt`. Pinning also gives you a calm moment to read what changed before you update. Pinning an old version is not automatically safe: `requests` 2.32.5, for example, has a known security advisory (CVE-2026-25645) fixed in 2.33.0. Check for security advisories before you pin (run `python -m pip install pip-audit` then `python -m pip_audit`, or read the package's GitHub "Security" page), and update your pins regularly.

**Watch out for look-alike packages.** Attackers upload packages with names close to popular ones. This is **typosquatting**: they rely on a typing slip. For example, `reqeusts` or `python-requests` instead of `requests`. Such a package may steal passwords or files when you install or import it. Before you install:

- Copy the exact name from the official documentation. Do not type it from memory.
- Check the package page on pypi.org: its age, download numbers, and project links.
- Be wary of tiny, brand-new packages with names that nearly match a famous one.
- Install only what you need.

### 3. Memory safety

A **memory-safe** language stops code from reading or writing memory it does not own. Python checks every list position and frees unused memory for you, while C leaves that work to the programmer, which is faster but allows bugs such as buffer overflows. (Optional: **[Low Level]** How Can Memory-Safe Code Stop Hackers? 7:43, https://www.youtube.com/watch?v=lxUYZVX_FjQ.)

### 4. Choosing a paradigm (LO 4)

A **paradigm** is a style of programming. Python supports the four you have met in this course. No style is best everywhere. Judge a problem against the same criteria each time:

| Criterion | Imperative | Object-oriented | Functional | Logic |
|---|---|---|---|---|
| **State and data flow** | Step-by-step commands change variables. | Data and the methods that change it live together in objects. | Functions take values in and return new values. Data is not changed. | You state facts and rules. The system works out the answers. |
| **Fits when** | The job is a short, clear sequence of steps. | You model many things that each have their own changing state. | You transform data through stages (filter, map, calculate). | The problem is about relationships and rules, such as "who is related to whom". |
| **Testability** | Fair: tests must set up and check shared variables. | Good if each object is small. Tests must build objects in the right state first. | Best: same input always gives the same output, with nothing to set up. | Good for the rules themselves. Tracing why an answer appeared can be hard. |
| **Example in this course** | Week 3 grade calculator (loops and if statements). | Week 5 library (`Book` and `Library` classes). | Week 4 rewrite of the grade calculator (`map`, `filter`, small functions). | Week 4 family tree (facts and rules about parents). |

Real programs mix styles. The Week 6 library is object-oriented overall, but its `search` is a functional list comprehension. When you judge a problem, ask: where does the state live, how easy is each part to test, and does the problem look like steps, things, transformations or rules?

::::::::::::::::::::::::::::::::::::: challenge

### Activity (about 8 minutes)

1. Take this function and add type hints to the parameters and the return value:

   ```python
   def full_name(first, last):
       return first + " " + last
   ```

2. Add a `requirements.txt` line that pins `requests` to version `2.34.2`.
3. Write one sentence: which of the names `requests`, `reqeusts`, `request` would you check carefully on pypi.org before installing, and why?
4. Using the table in section 4, name the paradigm you would pick for a program that works out "who is a grandparent of whom" from a list of parent facts, and give one reason.

:::::::::::::::: solution

### Model answer

1. ```python
   def full_name(first: str, last: str) -> str:
       return first + " " + last

   print(full_name("Ada", "Lovelace"))
   ```
2. `requests==2.34.2`
3. All three need checking, but `reqeusts` (a typo) and `request` (a different, similar package) are the risky ones. Copying the name from the official docs avoids typosquatting.
4. Logic programming, as in the Week 4 family tree: you state parent facts and one grandparent rule, and the system finds every answer. An imperative version would need nested loops that are harder to read and extend.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Further reading

- Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (accessed 2 November 2026).
- Romano, F. (2018) *Learn Python Programming*, 2nd edn. Birmingham: Packt Publishing.
- Indently (no date) *A quick guide to type annotations (ft. Mypy)* [Video]. Available at: https://www.youtube.com/watch?v=Y9fT4HVdCuQ (accessed 2 November 2026).

## Practice task: Mini Project (Part 2) {#week-6-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [library.py](files/week-6/solution/library.py)
- [main.py](files/week-6/solution/main.py)
- [test_library.py](files/week-6/test_library.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time guide: 3 hours.** This is practice, not a graded task. You finish the project you started in Week 5.

### Goal

Turn your Week 5 `library.py` into a small program with a text menu. You will add a search, type hints, error handling and a short written note.

New words this week:

- **Type hint:** a note in the code saying what type a value should be, such as `title: str`.
- **Module:** a `.py` file whose code another file can `import`.
- **Paradigm:** a style of programming (for example object-oriented, functional or imperative).

### What you start with

Your Week 5 `Library` and `Book` classes:

- `Book(title, author, isbn)` with `on_loan` (starts as `False`), `to_dict()`, `from_dict(data)` and `__str__`.
- `Library` with `books` (a dictionary keyed by ISBN), `add_book`, `lend`, `return_book`, `available_books`, `save(path)` and `load(path)`.

If your Part 1 is not finished, finish the [Week 5 mini project](week-5.md#week-5-mini-project) first, or look at `solution/library.py` after a real attempt.

### Steps

#### Step 1: Set up the Week 6 folder (10 min)

1. Make a new folder for Week 6, for example `mini_project_part2`.
2. Copy your Week 5 `library.py` into it. It is in your own Week 5 project folder; the course version is [`weeks/week-5/practice/mini_project/library.py`](files/week-5/mini_project/library.py).
3. Open the folder as a project in PyCharm.

#### Step 2: Add `search` (30 min)

Add this method to `Library`:

```python
def search(self, text):
    ...
```

- It returns a list of `Book` objects whose title **or** author contains `text`.
- Ignore upper and lower case: searching `"austen"` finds `"Jane Austen"`.
- Use a **list comprehension** (`[... for ... in ... if ...]`) or `filter`.

Hint: `text.lower() in book.title.lower()`.

#### Step 3: Add type hints (20 min)

Add hints to every method in `Book` and `Library`, including the return type. For example:

```python
def add_book(self, book: Book) -> None:
def available_books(self) -> list[Book]:
```

Hints:

- Methods that return nothing use `-> None`.
- Inside `Book`, a method that returns a `Book` writes the type in quotes: `-> "Book"`.
- A file path can be `str | Path` (add `from pathlib import Path`).
- Optional: if you have installed mypy (`python -m pip install mypy`), run `python -m mypy library.py`. See the Bridge note.

#### Step 4: Write `main.py` (60 min)

Create `main.py` next to `library.py`. Start with `from library import Book, Library`.

Show this menu in a loop:

```
1. Add a book
2. List available books
3. Lend a book
4. Return a book
5. Search
6. Save and quit
```

- Load the library from `library.json` when the program starts (a missing file is fine: it gives an empty library).
- Option 6 saves to `library.json` and stops the loop.
- Put the menu loop in a function called `main()`, and finish the file with:

```python
if __name__ == "__main__":
    main()
```

This means the menu runs only when you run `main.py` directly, not when another file imports it (see T#46).

#### Step 5: Handle bad input (30 min)

Use `try` and `except` so the program never crashes:

- Lending or returning an unknown ISBN raises `KeyError`. Print a friendly message.
- Lending a book already on loan (or returning one that is not) raises `ValueError`. Print the message.
- A menu choice that is not 1 to 6 should print a hint and show the menu again.
- Empty title, author or ISBN when adding a book should be refused.

#### Step 6: Write the paradigm note (20 min)

Write 5 to 6 sentences in a file called `note.txt` (or a comment at the top of `main.py`). Compare **at least two named paradigms** (object-oriented, imperative, functional or logic) using the criteria table in ["Choosing a paradigm" in the Bridge](#week-6-bridge): how each handles state, when it fits, and how easy it is to test.

1. Name the paradigms you are comparing (at least two).
2. Which parts of your library project are object-oriented? Point to one example, such as `Library.lend`.
3. Which parts are functional? Point to one example, such as the `search` list comprehension.
4. Would a purely imperative version (no classes, just functions and a dictionary) be better or worse? Why?
5. Say which style is easier to test, and why.
6. Say what you would change if the library had a million books.

Use the Bridge table, the [Computerphile] paradigms video and your Week 4 notes. There is no single right answer. Explain your reasoning.

#### Step 7: Test and tidy (10 min)

Run the checks below, then fix anything that fails.

### Example session

```
1. Add a book
2. List available books
...
Choose 1-6: 1
Title: Dune
Author: Frank Herbert
ISBN: 111
Book added.
Choose 1-6: 3
ISBN to lend: 999
No book with that ISBN.
Choose 1-6: 5
Search for: herbert
Dune by Frank Herbert (111) - available
```

### Check your work

- [ ] `search("AUSTEN")` and `search("austen")` give the same result.
- [ ] Every method has type hints.
- [ ] `main.py` imports `library` and uses `if __name__ == "__main__":`.
- [ ] Bad ISBNs and bad menu choices print a message and do not crash.
- [ ] Quitting with option 6 saves, and starting again shows your books.
- [ ] Your 5 to 6 sentence paradigm note compares at least two paradigms.

### Run the tests

From the top folder of the course repository, test your own folder by setting `MINI_PROJECT_DIR` to it.

PowerShell:

```
$env:MINI_PROJECT_DIR = "C:\path\to\mini_project_part2"
python -m pytest weeks/week-6/practice
```

Mac or Linux:

```
MINI_PROJECT_DIR=/path/to/mini_project_part2 python -m pytest weeks/week-6/practice
```

If pytest is missing, run `python -m pip install pytest`. Without `MINI_PROJECT_DIR`, the tests run against the model solution in `solution/`.

Run `main.py` from PyCharm (right-click, **Run**) or with `python main.py` from inside your folder.

### Model solution

Try it yourself first. Then compare with [solution/library.py](files/week-6/solution/library.py) and [solution/main.py](files/week-6/solution/main.py).

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- A module is a .py file you can import.
- from module import name imports just what you need.
- Python ships with many useful built-in modules.
- Use python -m pip so packages install for the Python you run.
- pip freeze lists installed packages for a requirements.txt file.
- A folder with an __init__.py file is a package.
- Type hints document intent and let tools find mistakes.
- Pin versions and check package names before installing.
- No paradigm is best everywhere: judge each problem against the same criteria.
- Splitting code into modules keeps programs manageable.
- Explain design choices using clear criteria.

::::::::::::::::::::::::::::::::::::::::::::::::
