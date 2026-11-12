---
title: 'Week 6: Modules and choosing a paradigm'
teaching: 80
exercises: 214
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 6, and how should I spend my 6 hours?
- How do I split code into files and use code others have written?
- How do I choose a paradigm for a problem?
- Can I finish a complete program and justify its design?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Create and import your own module.
- Use built-in modules such as math and random.
- Compare paradigms using a set of criteria.
- Write a short note that justifies a choice.
- Finish the library-loan manager with a menu and search, and compare two paradigms in it.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 6 overview {#week-6-overview}

**Theme:** split your code into modules, use the built-in modules that come with Python, and decide which programming style suits a problem.

This is the last week of Part 1. You also finish the library mini project you started in Week 5.

### Learning goals

By the end of this week you can:

1. Write your own module and import it, and explain what `if __name__ == "__main__":` does.
2. Use built-in modules such as `random` and `math`.
3. Add a search feature and a text menu to a small program, and handle bad input without crashing.
4. Explain, in a few sentences, which programming paradigm (style) suits a problem and why (LO 4).

### Time plan (under 6 hours)

| Block | Time | What you do |
|---|---|---|
| Watch | 24 min | Three videos (below) |
| Read & practise | 1 h 0 m | Section 6.1 (modules), with Level 1 exercises |
| Concepts Bridge | 30 min | [Choosing a paradigm](#week-6-bridge) |
| Build | 3 h | [Mini project, part 2](#week-6-practice), your portfolio item for this week |
| Quiz | 15 min | Canvas quiz, 6 questions |
| **Total** | **5 h 9 min** | Under the 6 h cap |

### Watch (24 min)

Watch in this order. Pause and try things in PyCharm as you go.

| # | Video | Length | Look out for |
|---|---|---|---|
| 1 | **T#45** Modules | 7:20 | How `import` finds a file and runs it. https://www.youtube.com/watch?v=1RuMJ53CKds&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 |
| 2 | **T#46** Special Variable `__name__` | 5:43 | Why code under `if __name__ == "__main__":` runs only when you run the file directly. https://www.youtube.com/watch?v=pzNISmtmzcY&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 |
| 3 | **[Computerphile]** Programming Paradigms | 10:44 | The names of the styles and what each is good at. You will use this for your paradigm note. https://www.youtube.com/watch?v=sqV3pL5x8PI |

### Read & practise (1 h 0 m)

Open the lesson, read it, type out the examples and run them. Do not just copy and paste.

#### Section 6.1: Modules (about 1 h)

Lesson: [Section 6.1: Modules](#section-6-1). Code: [main.py](files/code/6.1/main.py), [mymodule.py](files/code/6.1/mymodule.py).

- Read: What is a Module, Creating a Module, Importing a Module, the two "Import Functions" sections, and the built-in modules **Math** and **Random**.
- Skim: OS, Sys, Statistics and String modules. Just know they exist.
- Do the **Level 1** exercises (1 to 3). They use `random`.

**PyCharm note:** create `mymodule.py` and `main.py` in the same PyCharm project. Right-click `main.py` and choose **Run**.

### Concepts Bridge (30 min)

Go to [the Concepts Bridge](#week-6-bridge). It gives you a criteria table for choosing a paradigm (LO 4), and two short activities.

### Build (3 h)

Go to [the practice task](#week-6-practice). You finish the Week 5 mini project (a library-loan manager). You add search, a text menu program, and a short note on paradigms. This is your portfolio item for Week 6.

### Quiz (15 min)

Take the Canvas quiz for Week 6 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `library.py` (your finished library classes, including `search`)
- `main.py` (your menu program)
- `note.txt` (five or six sentences comparing two paradigms, see the practice task)

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Only if you have time and are curious.

- **T#47** `__name__` part 2 (Telusko playlist)
- Section 6.1 Level 2 exercises (they use `random` and lists).
- Driscoll, M. (2017) *Python 101*, chapter 27, 29 and 33. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/

---

### What comes next

Part 2 starts with its own Week 1, on text and encoding. It covers files, data, libraries (pip, virtual environments, NumPy, Pandas and Matplotlib) and security basics. Saving the library to a file is added in Part 2 Week 2.

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

## Concepts Bridge: Choosing a Paradigm {#week-6-bridge}

**Time: 30 minutes.** Reading 15 minutes, activity 10 minutes, checking the model answer 5 minutes.

### Why this matters

A **paradigm** is a style of programming. This course has taught four: imperative, object-oriented, functional and logic. Python supports all four, but no style is best everywhere. Choosing well is LO 4: you must judge which paradigm best suits a particular problem, and say why.

### The four paradigms

Judge a problem against the same criteria each time:

| Criterion | Imperative | Object-oriented | Functional | Logic |
|---|---|---|---|---|
| **State and data flow** | Step-by-step commands change variables. | Data and the methods that change it live together in objects. | Functions take values in and return new values. Data is not changed. | You state facts and rules. The system works out the answers. |
| **Fits when** | The job is a short, clear sequence of steps. | You model many things that each have their own changing state. | You transform data through stages (filter, map, calculate). | The problem is about relationships and rules, such as "who is related to whom". |
| **Testability** | Fair: tests must set up and check shared variables. | Good if each object is small. Tests must build objects in the right state first. | Best: same input always gives the same output, with nothing to set up. | Good for the rules themselves. Tracing why an answer appeared can be hard. |
| **Example in this course** | Week 3 grade calculator (loops and if statements). | Week 5 library (`Book` and `Library` classes). | Week 4 rewrite of the grade calculator (`map`, `filter`, small functions). | Week 4 family tree (facts and rules about parents). |

Real programs mix styles. The library is object-oriented overall, but its `search` is a functional list comprehension. When you judge a problem, ask three questions:

1. Where does the state live?
2. How easy is each part to test?
3. Does the problem look like steps, things, transformations or rules?

### Writing a paradigm note

Your portfolio note compares **at least two** paradigms, using the table above. A good note:

- names the paradigms it compares,
- points to one real example in your library project for each,
- says which is easier to test, and why,
- says what would change for a much larger library.

Use the table as your checklist. There is no single right answer. The reasons matter most.

::::::::::::::::::::::::::::::::::::: challenge

### Activity 1: name the paradigm (5 minutes)

A program must work out "who is a grandparent of whom" from a list of parent facts. Using the table, name the paradigm you would pick, and give one reason in one sentence.

### Activity 2: spot the style (5 minutes)

Look at this code. Which paradigm is it mostly written in? Give one reason.

```python
def double_all(numbers):
    return [n * 2 for n in numbers]
```

:::::::::::::::: solution

### Model answer

1. **Logic programming.** The problem is about relationships (parent facts and a grandparent rule), and it is shorter and clearer to state the rule than to write nested loops. This matches the Week 4 family tree. An imperative version would need loops that are harder to read and extend.
2. **Functional.** The function takes values in and returns a new list. It does not change `numbers`, and the same input always gives the same output, so it is easy to test.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

### Further reading

- Computerphile (n.d.) *Programming Paradigms* [Video]. YouTube. Available at: https://www.youtube.com/watch?v=sqV3pL5x8PI (Accessed: 2 November 2026).
- Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Accessed: 2 November 2026).

## Practice task: Library Menu Program (Part 2 of the mini project) {#week-6-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

The easiest way to get every file is the [course zip file](data/course-data.zip) from the Setup page. Unzip it and open the folder in PyCharm. The test commands on this page are run from the top of that folder, so keep the folder layout. You can also download single files here:

- [library.py](files/week-6/solution/library.py)
- [main.py](files/week-6/solution/main.py)
- [test_library.py](files/week-6/test_library.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time guide: 3 hours.** This is your portfolio item for Week 6. Your tutor marks it at the end of the week. You finish the project you started in Week 5.

### Goal

Turn your Week 5 `library.py` into a small program with a text menu. You will add a search, error handling and a short paradigm note.

New words this week:

- **Module:** a `.py` file whose code another file can `import`.
- **Docstring:** a short piece of text, in triple quotes, that explains what a function or class does. Python keeps it, and it is shown by `help()`.
- **Paradigm:** a style of programming (for example object-oriented, functional or imperative).

### What you start with

Your Week 5 `Book` and `Library` classes:

- `Book(title, author, isbn)` with `on_loan` (starts as `False`) and `__str__`.
- `Library` with `books` (a dictionary keyed by ISBN), `add_book`, `lend`, `return_book` and `available_books`.

If your Week 5 mini project is not finished, finish it first, or look at `solution/library.py` after a real attempt.

The library works in memory in this week: books are kept while the program runs. Saving to a file comes in Part 2 Week 2.

### Steps

#### Step 1: Set up the Week 6 folder (10 min)

1. Make a new folder for Week 6, for example `mini_project_part2`.
2. Copy your Week 5 mini project file `library_starter.py` into it, and rename the copy `library.py`.
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

#### Step 3: Add docstrings (20 min)

Add a one-line docstring under the `class` line and under every method in `Book` and `Library`. Say what the method does in plain words. For example:

```python
def add_book(self, book):
    """Store a book under its isbn."""
    self.books[book.isbn] = book
```

#### Step 4: Write `main.py` (60 min)

Create `main.py` next to `library.py`. Start with `from library import Book, Library`.

Show this menu in a loop:

```
1. Add a book
2. List available books
3. Lend a book
4. Return a book
5. Search
6. Quit
```

- Put the menu loop in a function called `main()`, and finish the file with:

```python
if __name__ == "__main__":
    main()
```

This means the menu runs only when you run `main.py` directly, not when another file imports it (see T#46).

- Option 6 quits. The books are not saved yet, so the program should say so, for example: `Goodbye. Books are not saved yet.`

#### Step 5: Handle bad input (30 min)

Use `try` and `except` so the program never crashes:

- Lending or returning an unknown ISBN raises `KeyError`. Print a friendly message.
- Lending a book already on loan (or returning one that is not) raises `ValueError`. Print the message.
- A menu choice that is not 1 to 6 should print a hint and show the menu again.
- Empty title, author or ISBN when adding a book should be refused.

#### Step 6: Write the paradigm note (20 min)

Write 5 to 6 sentences in a file called `note.txt`. Compare **at least two named paradigms** (object-oriented, imperative, functional or logic) using the criteria table in ["Choosing a paradigm" in the Bridge](#week-6-bridge): how each handles state, when it fits, and how easy it is to test.

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
Choose 1-6: 6
Goodbye. Books are not saved yet.
```

### Check your work

- [ ] `search("AUSTEN")` and `search("austen")` give the same result.
- [ ] Every method in `Book` and `Library` has a docstring.
- [ ] `main.py` imports `library` and uses `if __name__ == "__main__":`.
- [ ] Bad ISBNs and bad menu choices print a message and do not crash.
- [ ] Adding a book with an empty field is refused.
- [ ] Your paradigm note compares at least two paradigms.

### Run the tests

From the top of the course folder, test your own folder by setting `MINI_PROJECT_DIR` to it. Your folder must contain `library.py` and `main.py`.

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
- No paradigm is best everywhere: judge each problem against the same criteria.
- Splitting code into modules keeps programs manageable.
- Explain design choices using clear criteria.

::::::::::::::::::::::::::::::::::::::::::::::::
