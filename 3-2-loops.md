---
title: '3.2 Loops'
teaching: 25
exercises: 17
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I repeat steps without copying code?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Write while and for loops.
- Use range(), break and continue.
- Loop over lists, strings and dictionaries.

::::::::::::::::::::::::::::::::::::::::::::::::

## Loops

Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

1. while loop
2. for loop

### While Loop

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

### Break and Continue - Part 1

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

### For Loop

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

### Break and Continue - Part 2

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

### The Range Function

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

### Nested For Loop

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

### For Else

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

### Pass

In Python, when a statement is required (after a colon), but we don't like to execute any code there, we can write the word _pass_ to avoid errors. Also we can use it as a placeholder, for future statements.

**Example:**

```python
for number in range(6):
    pass
```

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 1

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

## Exercises: Level 2

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

## Exercises: Level 3

1. Go to the data folder and use the [countries.py](data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
1. Go to the data folder and use the [countries_data.py](data/countries-data.py) file.
   1. What are the total number of languages in the data
   2. Find the ten most spoken languages from the data
   3. Find the 10 most populated countries in the world

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- A while loop repeats while its condition is True.
- A for loop goes through each item of a sequence.
- break stops a loop; continue skips to the next step.

::::::::::::::::::::::::::::::::::::::::::::::::
