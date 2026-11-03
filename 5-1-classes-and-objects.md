---
title: '5.1 Classes and Objects'
teaching: 30
exercises: 20
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I create my own data types?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Define a class with __init__ and methods.
- Create objects and use inheritance and method overriding.

::::::::::::::::::::::::::::::::::::::::::::::::

## Classes and Objects

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

### Creating a Class

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

### Creating an Object

We can create an object by calling the class.

```python
p = Person()
print(p)
```

```output
<__main__.Person object at 0x10804e510>
```

The number at the end is the object's address in memory, so yours will be different.

### Class Constructor

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

### Object Methods

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

### Object Default Methods

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

### Method to Modify Class Default Values

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

### Inheritance

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

### Overriding parent method

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

## Exercises: Level 1

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

## Exercises: Level 2

1. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- A class is a blueprint; an object is one thing made from it.
- self refers to the current object.
- A child class inherits from its parent and can override its methods.

::::::::::::::::::::::::::::::::::::::::::::::::
