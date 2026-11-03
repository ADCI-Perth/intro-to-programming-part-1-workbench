---
title: 'Week 5: Object-oriented programming and files'
teaching: 164
exercises: 170
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 5, and how should I spend my 6 hours?
- How do I create my own data types?
- How do I save data and read it back later?
- What does "everything is an object" mean?
- Why is 0.1 + 0.2 not exactly 0.3?
- Can I model real things with classes and save them to a file?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Define a class with __init__ and methods.
- Create objects and use inheritance and method overriding.
- Read and write text files with open() and with.
- Read and write JSON and CSV files.
- Use type(), id() and dunder methods to inspect objects.
- Explain floating-point error and use Decimal for money.
- Write an Animal class, then start a library-loan manager that saves to JSON.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 5 overview {#week-5-overview}

**Theme:** build your own types with classes, then save data to files.

By the end of this week you will be able to:

- Write a **class** and create several **objects** (instances) from it.
- Use **inheritance** so one class can build on another.
- Read and write text files and JSON files, and handle a missing file with `try/except`.
- Explain in plain words that "everything is an object" in Python, and why `0.1 + 0.2` is not exactly `0.3`.

### Time plan (about 5 h 35 m, within the 6 h cap)

| Block | What | Time |
|---|---|---|
| Watch | 10 videos (below) | 1 h 24 m |
| Read & practise | Section 5.1 Classes and objects; Section 5.2 File handling | 1 h 40 m |
| Concepts Bridge | [Everything is an object, and floating-point risk](#week-5-bridge) | 30 m |
| Build | [Animal class and mini project Part 1](#week-5-practice) | 2 h |
| **Total** | | **5 h 34 m** |

The remaining time is a buffer. Use it for the optional Dog step in the Animal task or for the optional material below.

### Watch (1 h 24 m)

Watch these in order. They start with objects, then cover inheritance and operators, then files. Pause and run the code yourself in PyCharm.

| # | Video | Length | What to look for |
|---|---|---|---|
| 1 | [T#48 Object Oriented Programming Intro](https://www.youtube.com/watch?v=gZwPdqC2Os0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 7:02 | Why programmers group data and actions together. |
| 2 | [T#49 Class and Object](https://www.youtube.com/watch?v=8O5kX73OkIY&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:01 | The difference between a class (blueprint) and an object (the thing built from it). |
| 3 | [T#50 `__init__` Method](https://www.youtube.com/watch?v=WIP3-woodlU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:46 | How `__init__` sets up a new object's data. |
| 4 | [T#51 Constructor, Self, Comparing Objects](https://www.youtube.com/watch?v=ic6wdPxcHc0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:04 | What `self` means, and why two objects with the same data are still different objects. |
| 5 | [T#55 Inheritance](https://www.youtube.com/watch?v=Cn7AkDb4pIU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:51 | How a child class reuses its parent's methods. You need this for the Animal task. |
| 6 | [T#57 Introduction to Polymorphism](https://www.youtube.com/watch?v=P1vH3Pfw6BI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 1:46 | One name, many forms. A short idea you will meet again in T#58 and T#59. |
| 7 | [T#58 Duck Typing](https://www.youtube.com/watch?v=CuK0g8OFzwo&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:17 | Python cares what an object can do, not what class it is. |
| 8 | [T#59 Operator Overloading](https://www.youtube.com/watch?v=9wd50TKv_OQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 14:29 | How methods such as `__add__` make `+` work on your own objects. The Bridge builds on this. |
| 9 | [T#65 File Handling](https://www.youtube.com/watch?v=aequTxAvQq4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 12:14 | Opening, reading and writing a file, and closing it safely. |
| 10 | [[Tech With Tim] How To Use JSON In Python](https://www.youtube.com/watch?v=-51jxlQaxyA) | 6:11 | Turning a dictionary into JSON text and back again. You need this for the mini project. |

### Read & practise (1 h 40 m)

Read each lesson with PyCharm open. Type the examples yourself and run them.

#### Section 5.1: Classes and objects (about 55 m)

Lesson: [Section 5.1: Classes and Objects](#section-5-1)

- **Read:** Creating a Class, Creating an Object, Class Constructor, Object Methods, Object Default Methods, Method to Modify Class Default Values, Inheritance, Overriding parent method.
- **Do:** Exercises Level 1. This is the `Statistics` class. Start with `count`, `sum`, `min`, `max`, `range` and `mean`, and stop there if time is short. Add the rest only if you have time.
- The lesson uses `super().__init__(...)` in the Inheritance section. Compare it with the `Dog` class you will write in the Build block.

#### Section 5.2: File handling (about 45 m)

Lesson: [Section 5.2: File Handling](#section-5-2)

- **Read:** Opening Files for Reading, Opening Files for Writing and Updating, Deleting Files, File with txt Extension, and the JSON sections (File with json Extension, Changing JSON to Dictionary, Changing Dictionary to JSON, Saving as JSON File).
- **Skip:** the csv, xlsx and xml sections. You do not need them this week.
- **Do:** Exercises Level 1 (count lines and words in the speeches; find the most spoken languages). Do the first speeches exercise fully and attempt the rest if time allows.

**Where are the files?** The lesson opens files such as `./data/obama_speech.txt` and `./files/reading_file_example.txt`. In this repository they live in [`assets/data/`](data/course-data.zip) and [`assets/files/`](data/course-data.zip) at the top level. If your script sits in `weeks/week-5/`, use paths like `../../assets/data/obama_speech.txt`. Alternatively, copy the file you need next to your script. PyCharm runs a script with its own folder as the working directory, so a copy beside the script is found by just its name.

**PyCharm note:** the lessons were written with VS Code in mind. In PyCharm, right-click your file and choose **Run**, or press the green arrow. Nothing else changes.

### Concepts Bridge (30 m)

[Everything is an object, and floating-point risk](#week-5-bridge): Part 1 7 m, Part 2 15 m (including the video), activity 8 m. It connects duck typing and operator overloading (T#58, T#59) to `type()`, `id()` and dunder methods. It also explains why `0.1 + 0.2 != 0.3`, and introduces `Decimal`. It includes the [Computerphile] Floating Point Numbers video (9:16).

### Build (2 h)

[Practice tasks](#week-5-practice):

1. **Animal class** (about 30 minutes): a class and several objects. The `Dog` subclass is an optional stretch (about 15 more minutes).
2. **Mini project, Part 1** (about 90 minutes): a [library loan manager](#week-5-mini-project) using classes, a dictionary, try/except and JSON. You finish it in Week 6.

These are practice tasks. They are not graded.

### Optional

Only do these if you have time left. Nothing here is required.

**Videos**

- T#52 Types of Variables
- T#53 Types of Methods
- T#54 Inner Class
- T#56 Constructor in Inheritance
- T#60 Method Overloading and Overriding
- Abstract classes
- [Bro Code] [Learn Python Dates & Times in 6 Minutes](https://www.youtube.com/watch?v=DwBDHsdX6XQ) (6:18), to go with Section 5.3
- [Socratica] [Regular Expressions in Python](https://www.youtube.com/watch?v=nxjwB8up2gI) (13:23), to go with Section 5.4

**Optional lessons**

- [Section 5.3: Python datetime](../learners/5-3-date-time.md)
- [Section 5.4: Regular expressions](../learners/5-4-regular-expressions.md)

**Extra practice**

- A **Currency class using `Decimal`** (working with money safely). Follow on from the Bridge.
- A string-shuffle program (text processing).

**Reading**

- Driscoll, M. (2017) *Python 101*, Chapters 11, 13, 15, 16 and 22. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Accessed: 2 November 2026).

## 5.1 Classes and Objects {#section-5-1}

### Classes and Objects

Python is an object oriented programming language. Everything in Python is an object, with its properties and methods. A number, string, list, dictionary, tuple, set etc. used in a program is an object of a corresponding built-in class. We create class to create an object. A class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class to create an object. The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.

We have been working with classes and objects right from the beginning of this challenge unknowingly. Every element in a Python program is an object of a class.
Let us check if everything in python is a class:

```python
student@adci:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

#### Creating a Class

To create a class we need the key word **class** followed by the name and colon. Class name should be **CamelCase**.

```python
# syntax
class ClassName:
    code goes here
```

**Example:**

```python
class Person:
    pass

print(Person)
```

```output
<class '__main__.Person'>
```

#### Creating an Object

We can create an object by calling the class.

```python
p = Person()
print(p)
```

```output
<__main__.Person object at 0x10804e510>
```

The number at the end is the object's address in memory, so yours will be different.

#### Class Constructor

In the examples above, we have created an object from the Person class. However, a class without a constructor is not really useful in real applications. Let us use constructor function to make our class more useful. Like the constructor function in Java or JavaScript, Python has also a built-in **__init__**() constructor function. The **__init__** constructor function has self parameter which is a reference to the current instance of the class

**Examples:**

```python
class Person:
    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name

p = Person('Jack')
print(p.name)
print(p)
```

```output
Jack
<__main__.Person object at 0x2abf46907e80>
```

Let us add more parameters to the constructor function.

```python
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Person('Jack', 'Wilson', 25, 'Australia', 'Perth')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
```

```output
Jack
Wilson
25
Australia
Perth
```

#### Object Methods

Objects can have methods. The methods are functions which belong to the object.

**Example:**

```python
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p = Person('Jack', 'Wilson', 25, 'Australia', 'Perth')
print(p.person_info())
```

```output
Jack Wilson is 25 years old. He lives in Perth, Australia.
```

#### Object Default Methods

Sometimes, you may want to have default values for your object methods. If we give default values for the parameters in the constructor, we can avoid errors when we call or instantiate our class without parameters. Let's see how it looks:

**Example:**

```python
class Person:
    def __init__(self, firstname='Jack', lastname='Wilson', age=25, country='Australia', city='Perth'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('Noah', 'Brown', 30, 'New Zealand', 'Auckland')
print(p2.person_info())
```

```output
Jack Wilson is 25 years old. He lives in Perth, Australia.
Noah Brown is 30 years old. He lives in Auckland, New Zealand.
```

#### Method to Modify Class Default Values

In the example below, the person class, all the constructor parameters have default values. In addition to that, we have skills parameter, which we can access using a method. Let us create add_skill method to add skills to the skills list.

```python
class Person:
    def __init__(self, firstname='Jack', lastname='Wilson', age=25, country='Australia', city='Perth'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('Python')
p1.add_skill('Excel')
p1.add_skill('SQL')
p2 = Person('Noah', 'Brown', 30, 'New Zealand', 'Auckland')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```

```output
Jack Wilson is 25 years old. He lives in Perth, Australia.
Noah Brown is 30 years old. He lives in Auckland, New Zealand.
['Python', 'Excel', 'SQL']
[]
```

#### Inheritance

Using inheritance we can reuse parent class code. Inheritance allows us to define a class that inherits all the methods and properties from parent class. The parent class or super or base class is the class which gives all the methods and properties. Child class is the class that inherits from another or parent class.
Let us create a student class by inheriting from person class.

```python
class Student(Person):
    pass


s1 = Student('Liam', 'Taylor', 20, 'Australia', 'Perth')
s2 = Student('Olivia', 'Thompson', 19, 'Australia', 'Fremantle')
print(s1.person_info())
s1.add_skill('Python')
s1.add_skill('SQL')
s1.add_skill('Excel')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organising')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```output
Liam Taylor is 20 years old. He lives in Perth, Australia.
['Python', 'SQL', 'Excel']
Olivia Thompson is 19 years old. He lives in Fremantle, Australia.
['Organising', 'Marketing', 'Digital Marketing']
```

Notice that the output says "He" for Olivia too, because `person_info()` always uses "He". We fix this below by overriding the method.

We did not call the **__init__**() constructor in the child class. If we didn't call it then we can still access all the properties from the parent. But if we do call the constructor we can access the parent properties by calling _super_.
We can add a new method to the child or we can override the parent class methods by creating the same method name in the child class. When we add the **__init__**() function, the child class will no longer inherit the parent's **__init__**() function.

#### Overriding parent method

```python
class Student(Person):
    def __init__(self, firstname='Jack', lastname='Wilson', age=25, country='Australia', city='Perth', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        pronoun = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {pronoun} lives in {self.city}, {self.country}.'

s1 = Student('Liam', 'Taylor', 20, 'Australia', 'Perth', 'male')
s2 = Student('Olivia', 'Thompson', 19, 'Australia', 'Fremantle', 'female')
print(s1.person_info())
s1.add_skill('Python')
s1.add_skill('SQL')
s1.add_skill('Excel')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organising')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```output
Liam Taylor is 20 years old. He lives in Perth, Australia.
['Python', 'SQL', 'Excel']
Olivia Thompson is 19 years old. She lives in Fremantle, Australia.
['Organising', 'Marketing', 'Digital Marketing']
```

We can use super() built-in function or the parent name Person to automatically inherit the methods and properties from its parent. In the example above we override the parent method. The child method has a different feature, it can identify, if the gender is male or female and assign the proper pronoun(He/She).

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Python has the module called _statistics_ and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

```output
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

```output
# your output should look like this
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

::::::::::::::::::::::::::::::::::::::::::::::::

## 5.2 File Handling {#section-5-2}

### File Handling

So far we have seen different Python data types. We usually store our data in different file formats. In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section. First, let us get familiar with handling files with common file format(.txt).

File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use _open()_ built-in function.

```python
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
```

- "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
- "a" - Append - Opens a file for appending, creates the file if it does not exist
- "w" - Write - Opens a file for writing, creates the file if it does not exist
- "x" - Create - Creates the specified file, returns an error if the file exists
- "t" - Text - Default value. Text mode
- "b" - Binary - Binary mode (e.g. images)

#### Opening Files for Reading

The default mode of _open_ is reading, so we do not have to specify 'r' or 'rt'. I have created and saved a file named reading_file_example.txt in the files directory. Let us see how it is done:

```python
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'> - the encoding may differ on your computer
f.close()
```

As you can see in the example above, I printed the opened file and it gave  some information about it. Opened file has different reading methods: _read()_, _readline_, _readlines_. An opened file has to be closed with _close()_ method.

- _read()_: read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the *read(number)* method.

```python
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```output
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

Instead of printing all the text, let us print the first 10 characters of the text file.

```python
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```output
<class 'str'>
This is an
```

- _readline()_: read only the first line

```python
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```output
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_: read all the text line by line and returns a list of lines

```python
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```output
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

Another way to get all the lines as a list is using _splitlines()_:

```python
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

After we open a file, we should close it. There is a high tendency of forgetting to close them. There is a new way of opening files using _with_ - closes the files by itself. Let us rewrite the previous example with the _with_ method:

```python
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

#### Opening Files for Writing and Updating

To write to an existing file, we must add a mode as parameter to the _open()_ function:

- "a" - append - will append to the end of the file, if the file does not exist it creates a new file.
- "w" - write - will overwrite any existing content, if the file does not exist it creates.

The code below creates a new file, if the file does not exist:

```python
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file.\n')
```

Now let us append some text to the end of that file. Running this again adds the line again, because "a" never removes what is already there:

```python
with open('./files/writing_file_example.txt','a') as f:
    f.write('This text has to be appended at the end.\n')

with open('./files/writing_file_example.txt') as f:
    print(f.read())
```

```output
This text will be written in a newly created file.
This text has to be appended at the end.
```

#### Deleting Files

To remove a file we use the _os_ module. Modules are explained in Week 6, so for now leave the `import os` line as is.

```python
import os
os.remove('./files/writing_file_example.txt')
```

If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:

```python
import os
if os.path.exists('./files/writing_file_example.txt'):
    os.remove('./files/writing_file_example.txt')
else:
    print('The file does not exist')
# The file does not exist - we already removed it above
```

### File Types

#### File with txt Extension

File with _txt_ extension is a very common form of data and we have covered it in the previous section. Let us move to the JSON file

#### File with json Extension

JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.

_Example:_

```python
# dictionary
person_dct = {
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": ["Python", "Excel", "SQL"]
}

# JSON: the same data as a string. JSON always uses double quotes
person_json = '{"name": "Jack", "country": "Australia", "city": "Perth", "skills": ["Python", "Excel", "SQL"]}'

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": ["Python", "Excel", "SQL"]
}'''
```

#### Changing JSON to Dictionary

To change a JSON to a dictionary, first we import the json module and then we use _loads_ method.

```python
import json
# JSON
person_json = '''{
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": ["Python", "Excel", "SQL"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

```output
<class 'dict'>
{'name': 'Jack', 'country': 'Australia', 'city': 'Perth', 'skills': ['Python', 'Excel', 'SQL']}
Jack
```

#### Changing Dictionary to JSON

To change a dictionary to a JSON we use _dumps_ method from the json module.

```python
import json
# python dictionary
person = {
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": ["Python", "Excel", "SQL"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)
```

When you print it, it does not have the quotes, but it is a string. JSON does not have its own type in Python: it is a string.

```output
<class 'str'>
{
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": [
        "Python",
        "Excel",
        "SQL"
    ]
}
```

#### Saving as JSON File

We can also save our data as a json file. Let us save it as a json file using the following steps. For writing a json file, we use the json.dump() method, it can take dictionary, output file, ensure_ascii and indent.

```python
import json
# python dictionary
person = {
    "name": "Jack",
    "country": "Australia",
    "city": "Perth",
    "skills": ["Python", "Excel", "SQL"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

In the code above, we use encoding and indentation. Indentation makes the json file easy to read.

#### File with csv Extension

CSV stands for comma separated values. CSV is a simple file format used to store tabular data, such as a spreadsheet or database. CSV is a very common data format in data science.

**Example:**

```csv
"name","country","city","skills"
"Jack","Australia","Perth","Python"
```

**Example:**

```python
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a student. He lives in {row[2]}, {row[1]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
```

```output
Column names are :name, country, city, skills
        Jack is a student. He lives in Perth, Australia.
Number of lines:  2
```

#### File with xlsx Extension

To read Excel files we need to install the _openpyxl_ package. Installing packages with pip is covered in Week 6, so for now just read this example; it will not run until openpyxl is installed.

```python
import openpyxl
workbook = openpyxl.load_workbook('sample.xlsx')
print(workbook.sheetnames)   # the names of the sheets, e.g. ['Sheet1']
```

#### File with xml Extension

XML is another structured data format which looks like HTML. In XML the tags are not predefined. The first line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute.
**Example: XML**

```xml
<?xml version="1.0"?>
<person gender="male">
  <name>Jack</name>
  <country>Australia</country>
  <city>Perth</city>
  <skills>
    <skill>Python</skill>
    <skill>Excel</skill>
    <skill>SQL</skill>
  </skills>
</person>
```

For more information on how to read an XML file check the [documentation](https://docs.python.org/3/library/xml.etree.elementtree.html)

```python
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field:', child.tag)
```

```output
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
   1) Read obama_speech.txt file and count number of lines and words
   2) Read michelle_obama_speech.txt file and count number of lines and words
   3) Read donald_speech.txt file and count number of lines and words
   4) Read melina_trump_speech.txt file and count number of lines and words
2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

   ```output
   # Your output should look like this
   print(most_spoken_languages('./data/countries_data.json', 10))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic'),
   (24, 'Spanish'),
   (9, 'Russian'),
   (9, 'Portuguese'),
   (8, 'Dutch'),
   (7, 'German'),
   (5, 'Chinese'),
   (4, 'Swahili'),
   (4, 'Serbian')]

   # Your output should look like this
   print(most_spoken_languages('./data/countries_data.json', 3))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic')]
   ```

3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

   ```output
   # Your output should look like this
   print(most_populated_countries('./data/countries_data.json', 10))

   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000},
   {'country': 'Indonesia', 'population': 258705000},
   {'country': 'Brazil', 'population': 206135893},
   {'country': 'Pakistan', 'population': 194125062},
   {'country': 'Nigeria', 'population': 186988000},
   {'country': 'Bangladesh', 'population': 161006790},
   {'country': 'Russian Federation', 'population': 146599183},
   {'country': 'Japan', 'population': 126960000}
   ]

   # Your output should look like this

   print(most_populated_countries('./data/countries_data.json', 3))
   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000}
   ]
   ```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
2. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

```output
    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

3. Use the function, find_most_frequent_words to find:
   1) The ten most frequent words used in [Obama's speech](data/obama_speech.txt)
   2) The ten most frequent words used in [Michelle's speech](data/michelle_obama_speech.txt)
   3) The ten most frequent words used in [Trump's speech](data/donald_speech.txt)
   4) The ten most frequent words used in [Melina's speech](data/melina_trump_speech.txt)
4. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of [Michelle's](data/michelle_obama_speech.txt) and [Melina's](data/melina_trump_speech.txt) speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of [stop words](data/stop_words.py) are in the data directory
5. Find the 10 most repeated words in the romeo_and_juliet.txt
6. Read the [hacker news csv](data/hacker_news.csv) file and find out:
   1) Count the number of lines containing python or Python
   2) Count the number lines containing JavaScript, javascript or Javascript
   3) Count the number lines containing Java and not JavaScript

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Everything Is an Object, and Floating-Point Risk {#week-5-bridge}

**Time: 30 minutes.** Part 1: 7 minutes. Part 2: 15 minutes (the 9:16 video plus about 5 minutes of reading and running the code). Activity: 8 minutes.

### Why this matters

Object-oriented programming in Python starts from one idea: "everything is an object". Working with numbers safely means knowing about floating-point problems such as the Ariane 5 failure. Both support LO 2 (apply object-oriented techniques) and LO 3 (build to a specification, which includes knowing where your numbers can go wrong).

### Part 1: Everything is an object (about 7 minutes)

An **object** is a piece of data bundled with the actions (methods) that work on it. This week you built your own objects with `class`. Here is the surprise: Python's built-in values are objects too. Whole numbers, strings, lists and even functions are all objects.

Two built-in functions let you look inside:

- `type(x)` tells you which class an object was made from.
- `id(x)` gives a number that identifies that one object while the program runs. Two different objects never share an id at the same time.

```python
print(type(42))
print(type("hello"))
print(type([1, 2, 3]))
print(type(len))

class Dog:
    pass

rex = Dog()
print(type(rex))
print(type(Dog))          # even a class is an object

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)             # same contents?
print(a is b)             # same object?
print(a is c)             # c is just another name for a
print(id(a) == id(c))
print((42).bit_length())  # a whole number has methods
```

Run it and read the output. A list has methods like `.append()` because it is an object of the `list` class. A whole number has methods such as `.bit_length()` for the same reason.

#### Duck typing and dunder methods

In T#58 you met **duck typing**: if an object has the method you need, Python does not care what class it is. The saying is "if it walks like a duck and quacks like a duck, it is a duck".

In T#59 you met **operator overloading**. The link between the two is the **dunder method**. "Dunder" is short for "double underscore", such as `__init__` or `__add__`. Python calls these special methods behind the scenes:

| You write | Python actually calls |
|---|---|
| `len(x)` | `x.__len__()` |
| `a + b` | `a.__add__(b)` |
| `str(x)` and `print(x)` | `x.__str__()` |
| `a == b` | `a.__eq__(b)` |

That is why `+` works on numbers, strings and lists: each class defines its own `__add__`. It is also why your own class can use `len()` or `+` once you define the right dunder method.

```python
print(3 + 4)
print("3" + "4")
print([3] + [4])
print((3).__add__(4))       # exactly what 3 + 4 does

class Basket:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return Basket(self.items + other.items)

    def __str__(self):
        return "Basket with " + ", ".join(self.items)

mine = Basket(["apple", "pear"])
yours = Basket(["plum"])
print(len(mine))            # works because of __len__
print(mine + yours)         # works because of __add__ and __str__
```

`Basket` and `list` are different classes, yet `len()` works on both. That is duck typing again: `len()` only asks "do you have `__len__`?".

**Optional, if you have time later:** Driscoll (2017) Chapter 11, "Classes" (<https://web.archive.org/web/20260308142225/https://python101.pythonlibrary.org/chapter11_classes.html>). It is not part of the 30 minutes.

### Part 2: Floating-point risk (about 15 minutes)

#### Watch first (9:16, about 10 minutes with pauses)

**[Computerphile] Floating Point Numbers (9:16)** — <https://www.youtube.com/watch?v=PZRI1IfStY0>

Look for how a computer stores a number using a fixed number of binary digits, and why some decimal numbers cannot be stored exactly.

#### Why `0.1 + 0.2 != 0.3`

Computers store numbers in binary (base 2). In the decimal system you cannot write one third exactly (0.3333...). In binary, you cannot write one tenth exactly. Python's `float` type stores the closest value it can fit, so tiny errors creep in.

```python
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")       # see the real stored value of 0.1
print(round(0.1 + 0.2, 2) == 0.3)
```

The first line prints `0.30000000000000004`. The comparison is `False`. This is not a Python bug. Almost every language that uses standard floating-point numbers behaves this way.

Two safe habits:

1. Never compare floats with `==`. Compare with a tolerance, such as `math.isclose(a, b)`.
2. For money, use whole cents (integers) or the `Decimal` type.

```python
import math
print(math.isclose(0.1 + 0.2, 0.3))
```

#### The `Decimal` type

`decimal.Decimal` stores numbers as decimal digits, so 0.1 really is 0.1. It is slower than `float`, but exact for the sums people do by hand. Always create a `Decimal` from a **string**. If you pass a float, the float's error comes along too.

```python
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal(0.1))        # the float's error is copied in
print(Decimal("19.95") * 3)
```

#### Case study: Ariane 5 (1996)

On 4 June 1996 the first Ariane 5 rocket broke up about 37 seconds after launch. Software reused from Ariane 4 tried to convert a 64-bit floating-point value into a 16-bit signed whole number. The faster Ariane 5 produced a value too big to fit, the overflow stopped the inertial reference system computers (both the primary and the backup), and the rocket lost its guidance data. Number types have limits, so check that a value fits before you convert it (Lions, 1996).

### Activity (about 8 minutes)

1. Without running it, predict the output of each line:
   ```python
   print(0.1 * 3)
   print(0.1 * 3 == 0.3)
   print(type(0.1 * 3))
   print(type(Decimal("0.1") * 3))
   ```
   Then run it (add `from decimal import Decimal` at the top) and check your predictions.
2. A shop sells an item for 0.10 dollars. Add up the price 10 times in a loop using a `float`, then using a `Decimal`. Compare each total with `1`. What do you notice?
3. In two sentences, explain to a classmate why `len("abc")` and `len([1, 2])` both work. Use the words "object" and "dunder method".

#### Model answer

1. Predictions: `0.30000000000000004`, `False`, `<class 'float'>`, `<class 'decimal.Decimal'>`.
2. The `float` total is `0.9999999999999999`, so `total == 1` is `False`. The `Decimal` total is exactly `1.0`, so the comparison is `True`.
3. Strings and lists are both objects, and each of their classes defines a `__len__` dunder method. `len()` simply calls `__len__` on whatever object it is given, which is duck typing.

Working code for questions 1 and 2:

```python
from decimal import Decimal

print(0.1 * 3)
print(0.1 * 3 == 0.3)
print(type(0.1 * 3))
print(type(Decimal("0.1") * 3))

float_total = 0.0
decimal_total = Decimal("0")
for _ in range(10):
    float_total += 0.1
    decimal_total += Decimal("0.1")

print(float_total, float_total == 1)
print(decimal_total, decimal_total == 1)
```

### Reference

- Lions, J.L. (1996) *Ariane 5 Flight 501 Failure: Report by the Inquiry Board*. Paris: European Space Agency.

## Practice task: Animal Class and Mini Project (Part 1) {#week-5-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [animal_starter.py](files/week-5/animal_starter.py)
- [animal_solution.py](files/week-5/animal_solution.py)
- [test_animal.py](files/week-5/test_animal.py)
- [library_starter.py](files/week-5/mini_project/library_starter.py)
- [library.py](files/week-5/mini_project/library.py)
- [test_library.py](files/week-5/mini_project/test_library.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Build block: 2 hours.** This is practice, not an assessment. There are no marks. Use the tests to check yourself.

| Part | Task | Time |
|---|---|---|
| 1 | Animal class (steps 1 to 4 and 6; step 5 is an optional stretch) | about 30 minutes |
| 2 | Mini project, Part 1: library loan manager | about 90 minutes |
| | **Total** | **2 hours** |

The mini project is the bigger task, so it gets most of the time. If the Animal class runs over, skip step 5 and move on.

You will need Section 5.1 (classes), Section 5.2 (files and JSON) and Section 4.4 (try/except, from Week 4).

---

### Part 1: Animal class (about 30 minutes, plus about 15 for the optional step 5)

#### Goal

Write a class, make several objects from it, then write a **subclass** (a class that inherits from another). This is a classic first OOP exercise: one class, many objects.

Key terms:

- **Class:** a blueprint for objects.
- **Object (or instance):** one thing built from the blueprint. `Animal("Mittens", ...)` and `Animal("Daisy", ...)` are two instances.
- **Attribute:** a variable that belongs to an object, such as `self.name`.
- **Subclass:** a class that inherits the attributes and methods of a parent class and can add or replace some.

#### Steps

Open `animal_starter.py` and work through TODO 1 to 6. Step 5 is an optional stretch.

1. **`Animal`** takes `name`, `species`, `sound` and `age` (age defaults to `0`). Store all four on `self`.
2. **`speak()`** returns (does not print) text such as `"Mittens says Meow"`.
3. **`have_birthday()`** adds 1 to the animal's age.
4. **`__str__()`** returns text such as `"Mittens the cat (age 3)"`. Python uses it when you `print()` the object.
5. **Optional stretch: `Dog`** inherits from `Animal`. Its `__init__` takes only `name` and `age=0` and calls `super().__init__(...)` with species `"dog"` and sound `"Woof"`. It **overrides** `speak()` (replaces the parent's version) to return `"Rex says Woof! Woof!"`, and adds a new method `fetch(item)` returning `"Rex fetches the ball"`.
6. In the `if __name__ == "__main__":` block, create at least two `Animal` objects. Print each, call `speak()`, give one a birthday, and print it again. If you did step 5, add a `Dog` too and call `fetch()`.

   Leave the line `if __name__ == "__main__":` exactly as it is in the starter and put your test code inside that block. Week 6 explains why it is there; for now, just treat it as "run this part when I press Run".

#### Example output

```
Mittens the cat (age 3)
Mittens says Meow
Daisy the cow (age 0)
Daisy says Moo
Rex the dog (age 2)
Rex says Woof! Woof!
Rex the dog (age 3)
Rex fetches the ball
```

#### Hints

- Inside a method, `self` means "this object". Every method's first parameter is `self`.
- Use `return` in `speak()`, not `print()`. Returned text is easier to test.
- Changing one object's age must not change another's. If it does, check that you used `self.age`.
- Stuck on `super()`? Compare with the `Student(Person)` example in Section 5.1 (Inheritance).

#### Check your work

- [ ] Two `Animal` objects keep separate names and ages.
- [ ] `print(...)` of an animal shows the `__str__` text, not something like `<__main__.Dog object at 0x...>`.
- [ ] (Step 5 only) `Dog("Rex")` works without giving a species or sound.
- [ ] (Step 5 only) `isinstance(rex, Animal)` is `True`.
- [ ] `test_animal.py` passes (see "Running the tests" below).

Tests for `Dog` are skipped until you write it. Further stretch (optional): add a `Cat` subclass whose `speak()` is different, then loop over a list holding an `Animal`, a `Dog` and a `Cat` and call `speak()` on each. That is polymorphism and duck typing (T#57 and T#58) in action.

---

### Part 2: Mini project, Part 1 (about 90 minutes)

Go to [mini_project/README.md](#week-5-mini-project). You will build a library loan manager with a `Book` class, a `Library` class and JSON saving. Week 6 finishes it.

---

### Running the tests

Tests are small programs that check your code. We use **pytest**.

1. Open `test_animal.py`. Near the top, change `MODULE_NAME = "animal_solution"` to `MODULE_NAME = "animal_starter"`. Now the tests check your code.
2. In PyCharm, right-click `test_animal.py` and choose **Run 'pytest in test_animal.py'**. Or, in the Terminal tab, from the repository root:
   ```
   python -m pytest weeks/week-5/practice/test_animal.py
   ```
3. Read any failure message from the top. It names the test and shows what it expected.

Peek at `animal_solution.py` only after you have tried each step yourself. The same method works for the mini project with `test_library.py`.

If `pytest` is missing, run `python -m pip install pytest` in the Terminal tab.

### Mini Project, Part 1: Library Loan Manager {#week-5-mini-project}

**Time: about 90 minutes.** This is practice, not an assessment. There are no marks.

#### What you are building

A small library system. It keeps track of books, lets you lend and return them, and saves everything to a JSON file so nothing is lost when the program stops.

You will use ideas from this week: classes (Section 5.1), a dictionary of objects, try/except (Week 4), and saving to JSON (Section 5.2).

#### Files

| File | What it is |
|---|---|
| `library_starter.py` | Your work. It has TODOs to fill in. |
| `test_library.py` | Tests that check your work. |
| `library.py` | The model solution. Look only after you have tried. |

#### Steps

Open `library_starter.py` and work through the TODOs in order.

##### 1. The `Book` class (about 30 minutes)

- `__init__(self, title, author, isbn)` stores the three values. It also sets `self.on_loan = False`.
- `to_dict(self)` returns a dictionary: `{"title": ..., "author": ..., "isbn": ..., "on_loan": ...}`.
- `__str__(self)` returns text like:
  ```
  Dune by Frank Herbert (111) - available
  Dune by Frank Herbert (111) - on loan
  ```
- `from_dict` is already written for you. It uses `@classmethod`. A **class method** belongs to the class instead of one object, and its first parameter is `cls` (the class itself). That lets `Book.from_dict(data)` build a new `Book` from a dictionary, which is how a book comes back from the saved file. Read it, but you do not need to change it.

##### 2. The `Library` class (about 35 minutes)

- `__init__` creates `self.books = {}`. The **key** is each book's `isbn` and the **value** is the `Book` object. (An ISBN is a book's unique number. We use short text codes like `"111"`.)
- `add_book(book)` stores the book under its isbn.
- `lend(isbn)` sets `on_loan` to `True`.
  - Unknown isbn: Python raises `KeyError` for you if you write `self.books[isbn]`.
  - Book already on loan: `raise ValueError("...")` with a helpful message (see the `raise` hint below).
- `return_book(isbn)` sets `on_loan` to `False`.
  - Unknown isbn: `KeyError`.
  - Book not on loan: `ValueError`.
- `available_books()` returns a **list** of the `Book` objects that are not on loan.

##### 3. Saving and loading (about 15 minutes, then 10 to run it and check)

- `save(path)` is already written for you. Read it: it turns each book into a dictionary with `to_dict()`, puts them in a list, and uses `json.dump(data, file, indent=2)`.
- `load(path)` is yours to write. It reads the file, turns each dictionary back into a `Book` with `Book.from_dict(...)`, and **replaces** `self.books`. Wrap the file reading in `try/except FileNotFoundError`. If the file does not exist yet, leave the library empty and do not crash.

#### Try it yourself

After the tests pass, add a short block at the bottom of `library_starter.py`:

```python
if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Dune", "Frank Herbert", "111"))
    library.add_book(Book("Emma", "Jane Austen", "222"))
    library.lend("111")
    for book in library.books.values():
        print(book)
    library.save("library.json")
```

Leave the line `if __name__ == "__main__":` as it is and put your test code inside that block. Week 6 explains why it is there.

Open `library.json` and look at the saved text.

#### Hints

- **`raise`** means "stop here and signal an error on purpose". You choose the error type and the message:
  ```python
  if book.on_loan:
      raise ValueError("Dune is already on loan")
  ```
  Python stops the method at that line, and the error message appears unless some other code catches it with `try/except`. The tests check that the right error is raised.

- Use the keys `"title"`, `"author"`, `"isbn"` and `"on_loan"` exactly. Other code (and Week 6) depends on these names.
- Write the `to_dict` and `__str__` code first and test it, then move on.
- `"on loan" if book.on_loan else "available"` is a handy one-line way to choose between two words.
- `with open(path, "w", encoding="utf-8") as file:` closes the file for you.
- In PyCharm, the `tmp_path` in the tests is a temporary folder that pytest creates and cleans up. Your real files are never touched.

#### Running the tests

1. Open `test_library.py`. Change `MODULE_NAME = "library"` to `MODULE_NAME = "library_starter"` so the tests check your code.
2. Right-click the file in PyCharm and choose **Run 'pytest in test_library.py'**, or run this in the Terminal from the repository root:
   ```
   python -m pytest weeks/week-5/practice/mini_project
   ```

#### Check your work

- [ ] A new `Book` is not on loan.
- [ ] `print(book)` gives text in the exact format above.
- [ ] Lending the same book twice raises `ValueError`.
- [ ] Lending or returning an unknown isbn raises `KeyError`.
- [ ] `available_books()` leaves out books that are on loan.
- [ ] Save, then load into a new `Library`, gives the same books and loan status.
- [ ] Loading a file that does not exist leaves the library empty without an error.
- [ ] All tests in `test_library.py` pass.

#### Coming in Week 6 (Part 2)

In Week 6 you will finish this project. You will move the classes into a proper **module** (a reusable `.py` file) and write a separate program file with a text **menu** so a person can add, lend and return books without writing code. You will add a **search** feature (for example, finding books by title or author) and add **type hints** (notes that say what type each value should be) so your code is easier to read and check. Keep the names in this Part 1 exactly as they are: Week 6 builds on them.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- A class is a blueprint; an object is one thing made from it.
- self refers to the current object.
- A child class inherits from its parent and can override its methods.
- Use with open(...) so the file closes itself.
- Mode "w" overwrites, "a" appends, "r" reads.
- json.dump() and json.load() save and load Python data.
- Every value in Python is an object with a type and methods.
- Floats are approximations; use Decimal when exact values matter.
- Classes keep data and behaviour together.
- JSON files let a program remember data between runs.

::::::::::::::::::::::::::::::::::::::::::::::::
