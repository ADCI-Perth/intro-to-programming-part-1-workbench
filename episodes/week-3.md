---
title: 'Week 3: Control flow and functions'
teaching: 164
exercises: 176
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 3, and how should I spend my 6 hours?
- How can a program choose what to do?
- How do I repeat steps without copying code?
- How do I write code once and reuse it?
- How do I plan a solution before I code it?
- Can I plan and build a program with functions and decisions?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Write if, elif and else statements.
- Combine conditions with and and or.
- Write while and for loops.
- Use range(), break and continue.
- Loop over lists, strings and dictionaries.
- Define functions with parameters and return values.
- Use default, keyword and arbitrary arguments.
- Use the understand, pseudocode, code, test process.
- Complete a bubble sort template and trace it in the debugger.
- Write pseudocode, then a grade calculator using functions and if/elif.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 3 overview {#week-3-overview}

This week your programs start to make decisions, repeat steps and reuse code. These ideas are the heart of programming.

### Learning goals

By the end of this week you can:

- make a program choose between actions with `if`, `elif` and `else`;
- repeat steps with `while` and `for` loops, and stop or skip with `break` and `continue`;
- write your own functions that take values and return a result;
- plan a solution in pseudocode, and trace a simple sorting method step by step in the PyCharm debugger.

### Time plan (under 6 hours)

| Block | Time | What you do |
|---|---|---|
| Watch | 1 h 15 m | 7 short videos |
| Read & practise | 1 h 55 m | Sections 3.1, 3.2 and 3.3, with Level 1 exercises |
| Concepts Bridge | 0.5 h | [Problem solving and sorting](#week-3-bridge), including one short video |
| Build | 2 h | [Grade calculator](#week-3-practice), your portfolio item for this week |
| Quiz | 0.25 h | Canvas quiz, 6 questions |
| **Total** | **5 h 55 m** | |

Do the Watch block first, then read, then bridge, then build, then the quiz. You can mix videos and reading by topic: for example, watch T#19 and then read Section 3.1.

### Watch (1 h 15 m)

All links open in the Telusko *Python for Beginners (Full Course)* playlist.

| # | Video | Length | Look for |
|---|---|---|---|
| T#19 | [If Elif Else Statement](https://www.youtube.com/watch?v=PqFKRqpHrjw&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 15:38 | How Python picks one branch, and why the indentation matters |
| T#20 | [While Loop](https://www.youtube.com/watch?v=HZARImviDxg&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 12:43 | The condition is checked before every repeat |
| T#21 | [For Loop](https://www.youtube.com/watch?v=0ZvaDa8eT5s&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 7:27 | Looping over a list and over `range()` |
| T#22 | [Break Continue Pass](https://www.youtube.com/watch?v=yCZBnjF4_tU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 10:20 | What each keyword does to a loop |
| T#32 | [Functions in Python](https://www.youtube.com/watch?v=BVfCWuca9nw&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:13 | How to define a function with `def` and call it |
| T#33 | [Function Arguments](https://www.youtube.com/watch?v=ijXMGpoMkhQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 7:52 | Passing values in, and getting a value back with `return` |
| T#34 | [Types of Arguments](https://www.youtube.com/watch?v=eci9iU_s6Ag&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 9:55 | Positional, keyword and default arguments |

The bubble sort video (T#70) is in the Concepts Bridge, not here.

### Read & practise (1 h 55 m)

Read each lesson, type and run every example in PyCharm, then do the Level 1 exercises. Create one `.py` file per section, such as `section_3_1.py`. In PyCharm, use **File > New > Python File**, then click the green arrow to run.

| Order | Lesson | About | Read | Level 1 exercises |
|---|---|---|---|---|
| 1 | [Conditionals](#section-3-1) | 35 min | All sections. Short Hand and Nested Conditions can be a quick skim. | 1 to 3 |
| 2 | [Loops](#section-3-2) | 45 min | While Loop, Break and Continue, For Loop, The Range Function, Nested For Loop. Skim For Else and Pass. | 1 to 8 |
| 3 | [Functions](#section-3-3) | 35 min | Everything down to "Function with Default Parameters". Skim the arbitrary-arguments and dictionary-unpacking sections. | 1, 2, 4, 5, 8, 9, 11, 13 |

Notes:

- Section 3.3 exercise 3 asks you to check types. Skip that part; just add up the numbers.
- Section 3.2 Level 2 and 3 use files from the `data` folder (`countries.py`, `countries-data.py`). In this course they are in [assets/data](data/course-data.zip). They are optional extras.
- Modules (Section 6.1) are taught in Week 6.

### Concepts Bridge (0.5 h)

[Bridge: solving problems and sorting](#week-3-bridge). Learn the understand, pseudocode, code, test process. Then watch the bubble sort video, fill in a bubble sort template, and trace it in the PyCharm debugger.

### Build (2 h)

[Practice task: grade calculator](#week-3-practice). Enter marks, store them, and report the average and a grade, using functions and `if`/`elif`. Write short pseudocode first. This is your portfolio item for this week.

### Quiz (0.25 h)

Take the Canvas quiz for Week 3 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `starter.py` (your grade calculator, with your pseudocode at the top)
- `bubble_sort_template.py` (the template from the Concepts Bridge, with the blanks filled in)

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Only if you have time. Nothing here is needed to finish the week.

**Videos (Telusko)**

- T#22.1 Break vs continue vs pass
- T#23 Printing patterns
- T#24 For-else
- T#25 Prime numbers
- T#35 `**kwargs`
- T#36 Global vs local
- T#37 Pass list to function
- T#38 Fibonacci
- T#39 Factorial
- T#68 Linear search
- T#69 Binary search
- T#71 Selection sort

Find these in the [playlist](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3).

**Reading**

- Driscoll, M. (2017) *Python 101*, Chapters 4 to 6 and 10. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/

## 3.1 Conditionals {#section-3-1}

### Conditionals

By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:

- Conditional execution: a block of one or more statements will be executed if a certain expression is true
- Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover _if_, _else_, _elif_ statements. The comparison and logical operators we learned in previous sections will be useful here.

#### If Condition

In python and other programming languages the key word _if_ is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.

```python
# syntax
if condition:
    this part of code runs for truthy conditions
```

**Example: 1**

```python
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

As you can see in the example above, 3 is greater than 0. The condition was true and the block code was executed. However, if the condition is false, we do not see the result. In order to see the result of the falsy condition, we should have another block, which is going to be _else_.

#### If Else

If condition is true the first block will be executed, if not the else condition will run.

```python
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

**Example:**

```python
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
# A is a positive number
```

The condition above proves false, therefore the else block was executed. How about if our condition is more than two? We could use _elif_.

#### If Elif Else

In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. As similar to life, programming is also full of conditions. We use _elif_ when we have multiple conditions.

```python
# syntax
if condition:
    code
elif condition:
    code
else:
    code

```

**Example:**

```python
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
# A is zero
```

#### Short Hand

```python
# syntax
code if condition else code
```

**Example:**

```python
a = 3
print('A is positive' if a > 0 else 'A is negative') # A is positive - the first condition is met
```

#### Nested Conditions

Conditions can be nested

```python
# syntax
if condition:
    code
    if condition:
    code
```

**Example:**

```python
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
# A is zero
```

We can avoid writing nested condition by using logical operator _and_.

#### If Condition and Logical Operators

```python
# syntax
if condition and condition:
    code
```

**Example:**

```python
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
# A is zero
```

#### If and Or Logical Operators

```python
# syntax
if condition or condition:
    code
```

**Example:**

```python
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')
# Access denied! - James is not admin and his access level is below 4
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Get user input using input("Enter your age: "). If the user is 16 or older, give feedback: You are old enough to learn to drive. If below 16, tell them how many more years they need to wait. Output:

    ```bash
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 14
    You need 2 more years to learn to drive.
    ```

2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input("Enter your age: ") to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

    ```bash
    Enter your age: 30
    You are 5 years older than me.
    ```

3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

```bash
Enter number one: 4
Enter number two: 3
4 is greater than 3
```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Write a code which gives grade to students according to theirs scores:

    ```bash
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```

   2. Get the month from user input then check if the season in Australia is Summer, Autumn, Winter or Spring. If the user input is:
    December, January or February, the season is Summer.
    March, April or May, the season is Autumn.
    June, July or August, the season is Winter.
    September, October or November, the season is Spring.
   3. The following list contains some fruits:

    ```bash
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 3

1. Here we have a person dictionary. Feel free to modify it!

```python
person = {
    'first_name': 'Jack',
    'last_name': 'Wilson',
    'age': 25,
    'country': 'Australia',
    'is_student': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': '12 Hay Street',
        'postcode': '6000'
    }
}
```

     * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
     * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
     * If a person skills has only JavaScript and React, print('This person is a front end developer'), if the person skills has Node, Python, MongoDB, print('This person is a backend developer'), if the person skills has React, Node and MongoDB, print('This person is a full stack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
     * If the person is a student and lives in Australia, print the information in the following format:

```output
    Jack Wilson lives in Australia. He is a student.
```

::::::::::::::::::::::::::::::::::::::::::::::::

## 3.2 Loops {#section-3-2}

### Loops

Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

1. while loop
2. for loop

#### While Loop

We use the reserved word _while_ to make a while loop. It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.

```python
  # syntax
while condition:
    code goes here
```

**Example:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
```

In the above while loop, the condition becomes false when count is 5. That is when the loop stops.
If we are interested to run block of code once the condition is no longer true, we can use _else_.

```python
  # syntax
while condition:
    code goes here
else:
    code goes here
```

**Example:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.

#### Break and Continue - Part 1

- Break: We use break when we like to get out of or stop the loop.

```python
# syntax
while condition:
    code goes here
    if another_condition:
        break
```

**Example:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.

- Continue: With the continue statement we can skip the current iteration, and continue with the next:

```python
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
```

**Example:**

```python
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
```

The above while loop only prints 0, 1, 2 and 4 (skips 3).

#### For Loop

A _for_ keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

- Using For loop on list

```python
# syntax
for iterator in lst:
    code goes here
```

**Example:**

```python
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
```

- Using For loop on string

```python
# syntax
for iterator in string:
    code goes here
```

**Example:**

```python
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])
```

- Using For loop on tuple

```python
# syntax
for iterator in tpl:
    code goes here
```

**Example:**

```python
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- For loop with dictionary
  Looping through a dictionary gives you the key of the dictionary.

```python
  # syntax
for iterator in dct:
    code goes here
```

**Example:**

```python
person = {
    'first_name': 'Jack',
    'last_name': 'Wilson',
    'age': 25,
    'country': 'Australia',
    'is_student': True,
    'skills': ['Python', 'Excel', 'SQL'],
    'address': {
        'street': '12 Hay Street',
        'postcode': '6000'
    }
}
for key in person:
    print(key)        # first_name, last_name, age, ... one key per line

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out, e.g. first_name Jack
```

- Using For Loop in set

```python
# syntax
for iterator in st:
    code goes here
```

**Example:**

```python
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

#### Break and Continue - Part 2

Short reminder:
_Break_: We use break when we want to stop our loop before it is completed.

```python
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
```

**Example:**

```python
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
# prints 0, 1, 2 and 3, then stops
```

In the above example, the loop stops when it reaches 3.

Continue: We use continue when we want to skip some of the steps in the iteration of the loop.

```python
  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
```

**Example:**

```python
numbers = (0,1,2,3,4,5)
for number in numbers:
    if number == 3:
        continue      # skip the rest of this step and go to the next number
    print(number)
print('outside the loop')
# prints 0, 1, 2, 4, 5 (3 is skipped) and then 'outside the loop'
```

In the example above, if the number equals 3, the code _after_ the condition (but inside the loop) is skipped, so 3 is not printed, and the execution of the loop continues if there are any iterations left.

#### The Range Function

The _range()_ function is used to return a list of numbers. The _range(start, end, step)_ takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end).
Creating sequences using range

```python
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11, 9, 7, 5, 3, 1]
```

```python
# syntax
for iterator in range(start, end, step):
```

**Example:**

```python
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
```

#### Nested For Loop

We can write loops inside a loop.

```python
# syntax
for x in y:
    for t in x:
        print(t)
```

**Example:**

```python
person = {
    'first_name': 'Jack',
    'last_name': 'Wilson',
    'age': 25,
    'country': 'Australia',
    'is_student': True,
    'skills': ['Python', 'Excel', 'SQL'],
    'address': {
        'street': '12 Hay Street',
        'postcode': '6000'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
# Python
# Excel
# SQL
```

#### For Else

If we want to execute some message when the loop ends, we use else.

```python
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

**Example:**

```python
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```

#### Pass

In Python, when a statement is required (after a colon), but we don't like to execute any code there, we can write the word _pass_ to avoid errors. Also we can use it as a placeholder, for future statements.

**Example:**

```python
for number in range(6):
    pass
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Iterate 0 to 10 using for loop, do the same using while loop.
2. Iterate 10 to 0 using for loop, do the same using while loop.
3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

   ```output
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. Use nested loops to create the following:

   ```bash
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```

5. Print the following pattern:

   ```bash
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```

6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
7. Use for loop to iterate from 0 to 100 and print only even numbers
8. Use for loop to iterate from 0 to 100 and print only odd numbers

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.

```bash
The sum of all numbers is 5050.
```

2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

   ```bash
   The sum of all evens is 2550. And the sum of all odds is 2500.
   ```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 3

1. Go to the data folder and use the [countries.py](data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
1. Go to the data folder and use the [countries_data.py](data/countries-data.py) file.
   1. What are the total number of languages in the data
   2. Find the ten most spoken languages from the data
   3. Find the 10 most populated countries in the world

::::::::::::::::::::::::::::::::::::::::::::::::

## 3.3 Functions {#section-3-3}

### Functions

So far we have seen many built-in Python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, let us learn what a function is and why we need them?

#### Defining a Function

A function is a reusable block of code or programming statements designed to perform a certain task. To define or declare a function, Python provides the _def_ keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.

#### Declaring and Calling a Function

When we make a function, we call it declaring a function. When we start using the it,  we call it _calling_ or _invoking_ a function. Functions can be declared with or without parameters.

```python
# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()
```

#### Function without Parameters

Function can be declared without parameters.

**Example:**

```python
def generate_full_name ():
    first_name = 'Jack'
    last_name = 'Wilson'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function - prints Jack Wilson

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()  # 5
```

#### Function Returning a Value - Part 1

Functions return values using the _return_ statement. If a function has no return statement, it returns None. Let us rewrite the above functions using return. From now on, we get a value from a function when we call the function and print it.

```python
def generate_full_name ():
    first_name = 'Jack'
    last_name = 'Wilson'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())  # Jack Wilson

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())  # 5
```

#### Function with Parameters

In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as parameters.

- Single Parameter: If our function takes a parameter we should call our function with an argument

```python
  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))
```

**Example:**

```python
def greetings (name):
    message = name + ', welcome to Intro to Programming!'
    return message

print(greetings('Jack'))  # Jack, welcome to Intro to Programming!

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))  # 100

def square_number(x):
    return x * x
print(square_number(2))  # 4

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))  # 314.0

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- Two Parameter: A function may or may not have a parameter or parameters. A function may also have two or more parameters. If our function takes parameters we should call it with arguments. Let us check a function with two parameters:

```python
  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))
```

**Example:**

```python
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Jack','Wilson'))  # Full Name:  Jack Wilson

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))  # Sum of two numbers:  10

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age 

print('Age: ', calculate_age(2026, 2001))  # Age:  25

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))  # 981.0 N
```

#### Passing Arguments with Key and Value

If we pass the arguments with key and value, the order of the arguments does not matter.

```python
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here
```

**Example:**

```python
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Jack', lastname = 'Wilson')  # Jack Wilson

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # 5 - order does not matter
```

#### Function Returning a Value - Part 2

If we do not return a value with a function, then our function is returning _None_ by default. To return a value with a function we use the keyword _return_ followed by the variable we are returning. We can return any kind of data types from a function.

- Returning a string:
**Example:**

```python
def print_name(firstname):
    return firstname
print(print_name('Jack')) # Jack

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_full_name(firstname='Jack', lastname='Wilson'))  # Jack Wilson
```

- Returning a number:

**Example:**

```python
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))  # 5

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2026, 2001))  # Age:  25
```

- Returning a boolean:
  **Example:**

```python
def is_even (n):
    if n % 2 == 0:
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- Returning a list:
  **Example:**

```python
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))  # [0, 2, 4, 6, 8, 10]
```

#### Function with Default Parameters

Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.

```python
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

**Example:**

```python
def greetings (name = 'Peter'):
    message = name + ', welcome to Intro to Programming!'
    return message
print(greetings())        # Peter, welcome to Intro to Programming!
print(greetings('Jack'))  # Jack, welcome to Intro to Programming!

def generate_full_name (first_name = 'Jack', last_name = 'Wilson'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())                # Jack Wilson
print(generate_full_name('David','Smith'))  # David Smith

def calculate_age (birth_year, current_year = 2026):
    age = current_year - birth_year
    return age 
print('Age: ', calculate_age(2001))  # Age:  25

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 981.0 N - uses 9.81, the average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # 162.0 N - gravity on the surface of the Moon
```

#### Arbitrary Number of Arguments

If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding \* before the parameter name.

```python
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
```

**Example:**

```python
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

#### Default and Arbitrary Number of Parameters in Functions

```python
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Jack','Olivia','Liam','Emma')
# Team-1
# Jack
# Olivia
# Liam
# Emma
```
#### Dictionary unpacking

You can call a function which has named arguments using a dictionary with matching key names. You do so using ``**``.

```python
# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="Perth")  
# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "Perth"}

# Call the function using dictionary unpacking
greet(**my_dict)  
# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York
```

#### Arbitrary Number of Named Arguments

You can also define a function to accept an arbitrary number of named arguments.

```python
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)

arbitrary_named_args(name="Jack", city="Perth")
# I received an arbitrary number of arguments, totaling 2
# They are provided as a dictionary in my function: <class 'dict'>
# Let's print them:
#  * key: name value: Jack
#  * key: city value: Perth
```

Generally avoid this unless required as it makes it harder to understand what the function accepts and does.

#### Function as a Parameter of Another Function

```python
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 9
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to_fahrenheit_.
5. Write a function called check_season, it takes a month parameter and returns the season in Australia: Summer, Autumn, Winter or Spring.
6. Write a function called calculate_slope which return the slope of a linear equation
7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

```output
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ['C', 'B', 'A']
```

10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

```output
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

```

12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

```output
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

```output
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

```output
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```

1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
1. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
1. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
1. Write a function called _greet_ which takes a default argument, _name_. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.

```output
    greet()
    # Hello, Guest!
    greet("Alice")
    # Hello, Alice!
```
1. Create a function called _show_args_ to take an arbitrary number of named arguments and print their names and values.
   ```output
   show_args(name="Alice", age=30, city="Sydney")
   # Received: name: Alice, age: 30, city: Sydney
   show_args(name="Bob", pet="Fluffy, the bunny")
   # Received: name: Bob, pet: Fluffy, the bunny
   ```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 3

1. Write a function called is_prime, which checks if a number is prime.
1. Write a functions which checks if all items are unique in the list.
1. Write a function which checks if all the items of the list are of the same data type.
1. Write a function which check if provided variable is a valid python variable
1. Go to the data folder and access the countries-data.py file.

- Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
- Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Solving Problems and Sorting {#week-3-bridge}

**Time: 30 minutes.**

| Part | Minutes |
|---|---|
| Watch: T#70 Bubble Sort | 7 |
| Read: the problem-solving process | 5 |
| Read: bubble sort pseudocode | 3 |
| Activity 1: fill in the bubble sort template | 10 |
| Activity 2: trace it in the PyCharm debugger and compare with `sorted()` | 5 |
| **Total** | **30** |

### Why this matters

Learning outcome 1 of this course asks you to *analyse and solve a problem and then implement the solution in a programming language*. The order matters: think first, type second. Sorting is a classic problem for control structures, so this bridge uses bubble sort as the worked example.

### Watch: T#70 Bubble Sort (7:21)

Watch the video once, then read the pseudocode below.

- **T#70** [Bubble Sort](https://www.youtube.com/watch?v=Vca808JTbI8&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) (7:21): how neighbouring values are compared and swapped.

### The problem-solving process

Good programmers rarely start by typing code. They follow four steps.

1. **Understand.** Say the problem in your own words. What goes in? What should come out? What are some example answers?
2. **Pseudocode.** Write the steps in plain English, in short lines. *Pseudocode* means "fake code": it is a plan, not a program, so the computer never runs it.
3. **Code.** Turn each line of pseudocode into Python.
4. **Test.** Run it on examples where you already know the answer. Try odd cases too, such as an empty list.

Here is a tiny example. The problem: "find the average of some marks".

```output
Understand: input is a list of marks, output is one number.
            [72, 85, 64] should give about 73.7.
Pseudocode: 1. start the total at 0
            2. for each mark, add it to the total
            3. divide the total by how many marks there are
Test:       try [72, 85, 64], then [100], then []
```

The code is now easy to write:

```python
marks = [72, 85, 64]
total = 0
for mark in marks:
    total = total + mark
print(total / len(marks))
```

Testing the empty list `[]` would show a problem: dividing by zero. Finding that during testing, not after you hand it in, is the point of step 4. You will use this process for the grade calculator in the Build block.

### Sorting: bubble sort pseudocode

*Sorting* means putting items in order, such as smallest to largest. **Bubble sort** is a simple method. It looks at neighbouring pairs and swaps them when they are in the wrong order. Big values slowly "bubble" to the end.

Here is the plan as pseudocode. It is not Python yet.

```output
bubble_sort(numbers):
    1. make a copy of numbers and call it items
    2. repeat for each pass:
           the last position still to check is "end"
           (the first pass checks up to the last position, and each pass stops one place earlier)
           for each neighbouring pair (i and i + 1) up to end:
               if items[i] is bigger than items[i + 1]:
                   swap them
    3. return items
```

After the first pass the biggest value has reached the end. Each pass fixes one more value in place.

::::::::::::::::::::::::::::::::::::: challenge

### Activity 1: fill in the template (10 minutes)

Copy this template into a new PyCharm file called `bubble_sort_template.py`. Replace each `___` with the right code. The comments tell you what each line does.

```python
def bubble_sort(numbers):
    items = list(numbers)                                    # 1. make a copy
    for end in range(___, 0, -1):                            # 2. each pass stops one place earlier
        for i in range(end):                                 # 3. each neighbouring pair up to end
            if items[i] ___ items[i + 1]:                    # 4. is the pair in the wrong order?
                items[i], items[i + 1] = items[i + 1], items[i]   # 5. swap them
    return items
```

There are three blanks:

- The first `___` is the starting position for the first pass. It is the last index of the list: `len(items) - 1`.
- The second `___` is the number of pairs to check in a pass. Use `end`.
- The third `___` is the comparison that means "wrong order": `>`.

Then add `print(bubble_sort([6, 2, 5, 3]))` at the bottom and run it. You should see `[2, 3, 5, 6]`.

Writing bubble sort from a blank page is an optional stretch, after the template works.

### Activity 2: trace and compare (5 minutes)

A *trace* means following a program one step at a time and watching the variables. In T#16 you saw how PyCharm's debugger does this.

1. Click in the grey gutter beside the `if` line. A red dot (a *breakpoint*) appears.
2. Right-click the file and choose **Debug**. The program pauses at the breakpoint.
3. Look at the **Threads & Variables** panel. Watch `items`, `i` and `end`.
4. Press **Resume Program** (green arrow) to move to the next time the line runs.
5. On paper, write the list after each swap. Note the values of `end` when the second pass starts.

Then add these lines and run the file:

```output
data = [6, 2, 5, 3]
print(bubble_sort(data))
print(sorted(data))
print(bubble_sort(data) == sorted(data))
print(data)
```

Both sorted results should match, and `data` should not change. Python's `sorted()` is fast and well tested, so real programs use it. Bubble sort is for learning how sorting works, and it is slow on long lists.

:::::::::::::::: solution

### Model answer

Check your work after you have tried the template yourself.

```python
def bubble_sort(numbers):
    items = list(numbers)                                    # 1. make a copy
    for end in range(len(items) - 1, 0, -1):                 # 2. each pass stops one place earlier
        for i in range(end):                                 # 3. each neighbouring pair up to end
            if items[i] > items[i + 1]:                      # 4. is the pair in the wrong order?
                items[i], items[i + 1] = items[i + 1], items[i]   # 5. swap them
    return items


print(bubble_sort([6, 2, 5, 3]))           # [2, 3, 5, 6]
print(bubble_sort([]), bubble_sort([1]))   # [] [1]
```

For the list `[6, 2, 5, 3]`, the swaps happen like this:

1. Pass 1 (end = 3): `[6, 2, 5, 3]` → `[2, 6, 5, 3]` → `[2, 5, 6, 3]` → `[2, 5, 3, 6]`
2. Pass 2 (end = 2): `[2, 5, 3, 6]` → `[2, 3, 5, 6]`
3. Pass 3 (end = 1): no swaps are needed.

Four swaps in total. The second pass starts with `end` equal to 2 and `i` equal to 0.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

### Further reading

- Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Accessed: 2 November 2026).
- Romano, F. (2018) *Learn Python Programming*. 2nd edn. Birmingham: Packt Publishing.

## Practice task: Grade Calculator {#week-3-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [starter.py](files/week-3/starter.py)
- [solution.py](files/week-3/solution.py)
- [test_solution.py](files/week-3/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time: about 2 hours.** This is your portfolio item for Week 3. Your tutor marks it at the end of the week.

### Goal

Write a program that asks for marks, stores them, then reports the average mark and a grade. You will use a list, a dictionary, loops, `if`/`elif`/`else` and functions.

Week 4 gives you a similar grade calculator and asks you to rewrite it in a functional style. That task is self-contained, so you do not need this one.

### Before you code: write pseudocode (10 minutes)

Pseudocode is a plan in plain English. Follow the steps from the Concepts Bridge: understand, pseudocode, code, test. Write 5 to 8 short lines at the top of `starter.py`. For example: "ask for a subject; ask for a mark; check the mark; store it; repeat until done; print the report."

### Grade scale

| Mark | Grade |
|---|---|
| 85 to 100 | HD |
| 75 to 84 | D |
| 65 to 74 | C |
| 50 to 64 | P |
| 0 to 49 | F |

### Steps

Open `starter.py` in PyCharm. It has the function names ready, with TODO comments.

Leave the last two lines (`if __name__ == "__main__":` and `main()`) as they are. They run `main()` when you click Run. Week 6 explains why.

1. **`average(marks)`**: takes a list of marks and returns the average. If the list is empty, return `0.0`. Use a `for` loop to add up the marks.
2. **`grade(mark)`**: takes one mark and returns `"HD"`, `"D"`, `"C"`, `"P"` or `"F"`. Use `if`/`elif`/`else`.
3. **`is_valid_mark(mark)`**: returns `True` if the mark is from 0 to 100, otherwise `False`.
4. **`highest(marks)`** (optional stretch: skip it if you are short of time): returns the biggest mark in the list using a loop (do not use `max()`). For an empty list, return `None`.
5. **`grades_for(marks_by_subject)`**: takes a dictionary such as `{"Maths": 90}` and returns a new dictionary of grades, such as `{"Maths": "HD"}`.
6. **`main()`**: this is the only place that uses `input()`. Use a `while True` loop. Ask for a subject name (type `done` to stop), then a mark. Reject bad marks and ask again. Store good marks in a dictionary. At the end, print each subject, mark and grade, then the average (with its grade) and, if you did the stretch, the highest mark.

Keep `input()` and `print()` out of the other functions. Functions that only take values and return values are easy to test.

### Example run

```output
Grade calculator. Type done as the subject name to finish.
Subject: Maths
Mark (0 to 100): 90
Subject: Art
Mark (0 to 100): abc
Please enter a whole number.
Subject: Art
Mark (0 to 100): 120
A mark must be from 0 to 100.
Subject: Art
Mark (0 to 100): 48
Subject: English
Mark (0 to 100): 66
Subject: done

Maths: 90 (HD)
Art: 48 (F)
English: 66 (C)
Average: 68.0 (C)
Highest: 90
```

The `Highest` line is part of the optional stretch.

### Portfolio checklist

Your portfolio for this week has two files:

- `starter.py`, your grade calculator, with your pseudocode at the top as comments.
- `bubble_sort_template.py`, the Concepts Bridge template with the three blanks filled in.

### Hints

- `text.isdigit()` is `True` when a string such as `"72"` is only digits. `input()` always gives you a string, so use `int(text)` to turn it into a number after that check.
- `continue` jumps back to the top of a loop. `break` leaves the loop.
- `marks_by_subject[subject] = mark` adds an item to a dictionary.
- `list(marks_by_subject.values())` gives the marks as a list.
- `f"{value:.1f}"` shows a number with one decimal place.
- Python can chain comparisons: `0 <= mark <= 100`.

### Check your work

- [ ] I wrote pseudocode before coding.
- [ ] `average([80, 70, 90])` gives `80`, and `average([])` gives `0.0`.
- [ ] `grade(85)` is `"HD"` and `grade(84)` is `"D"`. Check the edge of every grade.
- [ ] Only `main()` calls `input()`.
- [ ] My program rejects `abc` and `120` without crashing.
- [ ] The tests pass. In `test_solution.py`, change `from solution import` to `from starter import`, then in the PyCharm Terminal run `python -m pytest weeks/week-3/practice` (or right-click `test_solution.py` and choose **Run**). If you skipped `highest`, its test is expected to fail.
- [ ] I ran the program by hand with at least three subjects.

If you are stuck, compare with `solution.py` after you have tried the step yourself.

### If you finish early

Do `highest(marks)` if you skipped it. Then add a `lowest(marks)` function. Print how many subjects are a pass (50 or more).

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- Python runs the first branch whose condition is True.
- Indentation shows which lines belong to each branch.
- A while loop repeats while its condition is True.
- A for loop goes through each item of a sequence.
- break stops a loop; continue skips to the next step.
- def defines a function; calling it runs the code.
- return sends a value back; without it a function returns None.
- Functions that take values and return values are easy to test.
- Think first, type second.
- Pseudocode is a plan in plain English.
- The debugger lets you watch a program run line by line.
- Keep input() and print() in main(); other functions take values and return values.

::::::::::::::::::::::::::::::::::::::::::::::::
