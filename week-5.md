---
title: 'Week 5: Object-oriented programming'
teaching: 119
exercises: 166
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 5, and how should I spend my 6 hours?
- How do I create my own data types?
- What does "everything is an object" mean?
- What is a dunder method?
- Can I model real things with classes?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Define a class with __init__ and methods.
- Create objects and use inheritance and method overriding.
- Use type(), id() and dunder methods to inspect objects.
- Explain duck typing.
- Write an Animal class, then start a library-loan manager with Book and Library classes.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 5 overview {#week-5-overview}

**Theme:** build your own types with classes, and group data and actions together in objects.

By the end of this week you will be able to:

- Write a **class** and create several **objects** (instances) from it.
- Use **inheritance** so one class can build on another.
- Explain in plain words that "everything is an object" in Python, and what a dunder method is.

### Time plan (under 6 hours)

| Block | What | Time |
|---|---|---|
| Watch | 6 short videos (below) | 45 min |
| Read & practise | Section 5.1 Classes and objects, with Level 1 exercises | 1 h 30 m |
| Concepts Bridge | [Everything is an object](#week-5-bridge) | 30 min |
| Build | [Animal class and library mini project, part 1](#week-5-practice), your portfolio item for this week | 2 h |
| Quiz | Canvas quiz, 6 questions | 15 min |
| **Total** | | **5 h 0 m** |

The remaining time is a buffer. Use it for the optional Dog step in the Animal task or for the optional material below.

### Watch (45 min)

Watch these in order. They start with objects, then cover inheritance. Pause and run the code yourself in PyCharm.

| # | Video | Length | What to look for |
|---|---|---|---|
| 1 | [T#48 Object Oriented Programming Intro](https://www.youtube.com/watch?v=gZwPdqC2Os0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 7:02 | Why programmers group data and actions together. |
| 2 | [T#49 Class and Object](https://www.youtube.com/watch?v=8O5kX73OkIY&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:01 | The difference between a class (blueprint) and an object (the thing built from it). |
| 3 | [T#50 `__init__` Method](https://www.youtube.com/watch?v=WIP3-woodlU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:46 | How `__init__` sets up a new object's data. |
| 4 | [T#51 Constructor, Self, Comparing Objects](https://www.youtube.com/watch?v=ic6wdPxcHc0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:04 | What `self` means, and why two objects with the same data are still different objects. |
| 5 | [T#55 Inheritance](https://www.youtube.com/watch?v=Cn7AkDb4pIU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:51 | How a child class reuses its parent's methods. You need this for the Animal task. |
| 6 | [T#57 Introduction to Polymorphism](https://www.youtube.com/watch?v=P1vH3Pfw6BI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 1:46 | One name, many forms. The Bridge builds on this idea. |

**Total: 44 min 30 s, shown as 45 min.**

### Read & practise (1 h 30 m)

Read the lesson with PyCharm open. Type the examples yourself and run them.

#### Section 5.1: Classes and objects (about 1 h 30 m)

Lesson: [Section 5.1: Classes and Objects](#section-5-1)

- **Read:** Creating a Class, Creating an Object, Class Constructor, Object Methods, Object Default Methods, Method to Modify Class Default Values, Inheritance, Overriding parent method.
- **Do:** Exercises Level 1. This is the `Statistics` class. Start with `count`, `sum`, `min`, `max`, `range` and `mean`, and stop there if time is short. Add the rest only if you have time.
- The lesson uses `super().__init__(...)` in the Inheritance section. Compare it with the `Dog` class you will write in the Build block.

**PyCharm note:** the lessons were written with VS Code in mind. In PyCharm, right-click your file and choose **Run**, or press the green arrow. Nothing else changes.

Files and saving are not part of this week. You will learn them in Part 2.

### Concepts Bridge (30 m)

[Everything is an object](#week-5-bridge): how `type()`, `id()` and dunder methods work, and how duck typing links them. It connects to the T#57 video you watched in the Watch block.

### Build (2 h)

[Practice tasks](#week-5-practice). This is your portfolio item for Week 5.

1. **Animal class** (about 30 minutes): a class and several objects. The `Dog` subclass is an optional stretch (about 15 more minutes).
2. **Library mini project, part 1** (about 90 minutes): a [library loan manager](#week-5-mini-project) using classes and a dictionary. It runs in memory. You finish it in Week 6.

### Quiz (15 min)

Take the Canvas quiz for Week 5 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `animal_starter.py` (your Animal class, with the test code in the `if __name__ == "__main__":` block)
- `library_starter.py` (your Book and Library classes from the mini project, part 1)

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Only do these if you have time left. Nothing here is required.

**Videos**

- T#52 Types of Variables
- T#53 Types of Methods
- T#54 Inner Class
- T#56 Constructor in Inheritance
- T#58 Duck Typing
- T#59 Operator Overloading
- T#60 Method Overloading and Overriding
- Abstract classes

**Extra practice**

- A `Cat` subclass of `Animal`, then a list holding an `Animal`, a `Dog` and a `Cat`, calling `speak()` on each.

**Reading**

- Driscoll, M. (2017) *Python 101*, Chapters 11 and 13. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Accessed: 2 November 2026).

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

## Concepts Bridge: Everything Is an Object {#week-5-bridge}

**Time: 30 minutes.** Part 1: 15 minutes. Part 2: 10 minutes. Activity: 5 minutes.

### Why this matters

Object-oriented programming in Python starts from one idea: "everything is an object". Knowing this helps you read the code you will write for the library and the animals, and the code in your next course. It supports LO 2 (apply object-oriented techniques).

### Part 1: Everything is an object (about 15 minutes)

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

### Part 2: Dunder methods and duck typing (about 10 minutes)

In T#57 you met the idea of one name with many forms. Python uses it in two ways.

**Duck typing:** if an object has the method you need, Python does not care what class it is. The saying is "if it walks like a duck and quacks like a duck, it is a duck".

**Dunder methods:** "dunder" is short for "double underscore", such as `__init__` or `__add__`. Python calls these special methods behind the scenes:

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

### Activity (5 minutes)

1. Without running it, predict the output of each line. Then run it and check. Run the lines after the `Basket` example, so `Basket` exists.

   ```python
   print(type(3))
   print(type(3.0))
   print(3 == 3.0)
   print(type(Basket))
   ```

2. In two sentences, explain why `len("abc")` and `len([1, 2])` both work. Use the words "object" and "dunder method".

#### Model answer

1. `<class 'int'>`, `<class 'float'>`, `True`, `<class 'type'>`. The last line shows that a class is itself an object, made from the `type` class.
2. Strings and lists are both objects, and each of their classes defines a `__len__` dunder method. `len()` calls `__len__` on whatever object it is given, which is duck typing.

### Further reading

- Driscoll, M. (2017) *Python 101*, Chapter 11, "Classes". Available at: https://web.archive.org/web/20260308142225/https://python101.pythonlibrary.org/chapter11_classes.html (Accessed: 2 November 2026).

## Practice task: Animal Class and Library Mini Project (Part 1) {#week-5-practice}

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

**Build block: 2 hours.** This is your portfolio item for Week 5. Your tutor marks it at the end of the week. Use the tests to check yourself as you go.

| Part | Task | Time |
|---|---|---|
| 1 | Animal class (steps 1 to 4 and 6; step 5 is an optional stretch) | about 30 minutes |
| 2 | Library mini project, part 1: classes and loans (in memory) | about 90 minutes |
| | **Total** | **2 hours** |

The mini project is the bigger task, so it gets most of the time. If the Animal class runs over, skip step 5 and move on.

You will need Section 5.1 (classes) and Section 4.4 (try/except, from Week 4).

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

Tests for `Dog` are skipped until you write it. Further stretch (optional): add a `Cat` subclass whose `speak()` is different, then loop over a list holding an `Animal`, a `Dog` and a `Cat` and call `speak()` on each.

---

### Part 2: Library mini project, part 1 (about 90 minutes)

Go to [mini_project/README.md](#week-5-mini-project). You will build a library loan manager with a `Book` class and a `Library` class. It works in memory for now: the books are kept while the program runs. Saving to a file comes in Part 2, Week 8.

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

### Mini project, part 1: library loan manager {#week-5-mini-project}

**Time: about 90 minutes.** This is your portfolio item for Week 5. Your tutor marks it at the end of the week.

#### What you are building

A small library system. It keeps track of books, and lets you lend and return them. This week it works in memory, so the books are kept while the program runs. Week 6 adds a menu, and Week 8 adds saving to a file.

You will use ideas from this week: classes, a dictionary of objects, and try/except (Week 4).

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
- `__str__(self)` returns text like:
  ```
  Dune by Frank Herbert (111) - available
  Dune by Frank Herbert (111) - on loan
  ```

##### 2. The `Library` class (about 50 minutes)

- `__init__` creates `self.books = {}`. The **key** is each book's `isbn` and the **value** is the `Book` object. (An ISBN is a book's unique number. We use short text codes like `"111"`.)
- `add_book(book)` stores the book under its isbn.
- `lend(isbn)` sets `on_loan` to `True`.
  - Unknown isbn: Python raises `KeyError` for you if you write `self.books[isbn]`.
  - Book already on loan: `raise ValueError("...")` with a helpful message (see the `raise` hint below).
- `return_book(isbn)` sets `on_loan` to `False`.
  - Unknown isbn: `KeyError`.
  - Book not on loan: `ValueError`.
- `available_books()` returns a **list** of the `Book` objects that are not on loan.

#### Try it yourself

After the tests pass, add a short block at the bottom of `library_starter.py`:

```python
if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Dune", "Frank Herbert", "111"))
    library.add_book(Book("Emma", "Jane Austen", "222"))
    library.lend("111")
    for book in library.available_books():
        print(book)
```

Leave the line `if __name__ == "__main__":` as it is and put your test code inside that block. Week 6 explains why it is there. Only Emma should print, because Dune is on loan.

#### Hints

- **`raise`** means "stop here and signal an error on purpose". You choose the error type and the message:
  ```python
  if book.on_loan:
      raise ValueError("Dune is already on loan")
  ```
  Python stops the method at that line, and the error message appears unless some other code catches it with `try/except`. The tests check that the right error is raised.

- Keep the attribute names `title`, `author`, `isbn` and `on_loan` exactly as written. Week 6 and Week 8 depend on these names.
- Write `__str__` first and test it, then move on.
- `"on loan" if book.on_loan else "available"` is a handy one-line way to choose between two words.

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
- [ ] All tests in `test_library.py` pass.

#### Coming in Week 6

In Week 6 you will finish this project. You will move the classes into a proper **module** (a reusable `.py` file), and write a separate program file with a text **menu** so a person can add, lend and return books without writing code. You will add a **search** feature and **docstrings** (short notes that explain each method). Keep the names in this Part 1 exactly as they are: Week 6 builds on them.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- A class is a blueprint; an object is one thing made from it.
- self refers to the current object.
- A child class inherits from its parent and can override its methods.
- Every value in Python is an object with a type and methods.
- Dunder methods such as __len__ and __add__ let Python call your objects with len() and +.
- Classes keep data and behaviour together.

::::::::::::::::::::::::::::::::::::::::::::::::
