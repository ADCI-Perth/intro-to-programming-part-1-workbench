---
title: '6.1 Modules'
teaching: 18
exercises: 12
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I split code into files and use code others have written?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Create and import your own module.
- Use built-in modules such as math, random, os and statistics.

::::::::::::::::::::::::::::::::::::::::::::::::

## Modules

### What is a Module

A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.

### Creating a Module

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

### Importing a Module

To import the file we use the _import_ keyword and the name of the file only.

```python
# main.py file
import mymodule
print(mymodule.generate_full_name('Jack', 'Wilson')) # Jack Wilson
```

### Import Functions from a Module

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

### Import Functions from a Module and Renaming

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

## Import Built-in Modules

Like other programming languages we can also import modules by importing the file/function using the key word _import_. Let's import the common module we will use most of the time. Some of the common built-in modules: _math_, _datetime_, _os_,_sys_, _random_, _statistics_, _collections_, _json_,_re_

### OS Module

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

### Sys Module

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

### Statistics Module

The statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: _mean_, _median_, _mode_, _stdev_ etc.

```python
from statistics import * # importing all the statistics modules
ages = [20, 20, 24, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Math Module

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

### String Module

A string module is a useful module for many purposes. The example below shows some use of the string module.

```python
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Random Module

By now you are familiar with importing modules. Let us do one more import to get very familiar with it. Let us import _random_ module which gives us a random number between 0 and 0.9999.... The _random_ module has lots of functions but in this section we will only use _random_ and _randint_.

```python
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999, e.g. 0.6394
print(randint(5, 20)) # it returns a random integer between 5 and 20 inclusive, e.g. 13
```

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 1

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

## Exercises: Level 2

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

## Exercises: Level 3

1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
1. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- A module is a .py file you can import.
- from module import name imports just what you need.
- Python ships with many useful built-in modules.

::::::::::::::::::::::::::::::::::::::::::::::::
