---
title: '4.4 Exception Handling'
teaching: 18
exercises: 12
---

:::::::::::::::::::::::::::::::::::::: questions

- How can my program keep going when something goes wrong?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Use try, except, else and finally.
- Catch specific error types.
- Pack and unpack arguments with * and **.

::::::::::::::::::::::::::::::::::::::::::::::::

## Exception Handling

Python uses _try_ and _except_ to handle errors gracefully. A graceful exit (or graceful handling) of errors is a simple programming idiom - a program detects a serious error condition and "exits gracefully", in a controlled manner as a result. Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this makes our application more robust. The cause of an exception is often external to the program itself. An example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device. Graceful handling of errors prevents our applications from crashing.

We have covered the different Python _error_ types in the previous section. If we use _try_ and _except_ in our program, then it will not raise errors in those blocks.

```python
try:
    ...  # Run this code
except ValueError:  # the exception name is optional
    ...  # Run this code when there is an exception
else:
    ...  # No exception? Run this code
finally:
    ...  # Always run this code
```

```python
# syntax
try:
    code in this block runs if things go well
except:
    code in this block runs if things go wrong
```

**Example:**

```python
try:
    print(10 + '5')
except:
    print('Something went wrong')
# Something went wrong
```

In the example above the second operand is a string. We could change it to float or int to add it with the number to make it work. But without any changes, the second block, _except_, will be executed.

**Example:**

```python
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2026 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
```

```output
Enter your name:Jack
Year you were born:2001
Something went wrong
```

In the above example, the exception block will run and we do not know exactly the problem. To analyze the problem, we can use the different error types with except.

In the following example, it will handle the error and will also tell us the kind of error raised.

```python
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2026 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occurred')
except ValueError:
    print('Value error occurred')
except ZeroDivisionError:
    print('Zero division error occurred')
```

```output
Enter your name:Jack
Year you were born:2001
Type error occurred
```

In the code above the output is going to be _TypeError_.
Now, let's add an additional block:

```python
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occurred')
except ValueError:
    print('Value error occurred')
except ZeroDivisionError:
    print('Zero division error occurred')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')
```

```output
Enter your name:Jack
Year you were born:2001
You are Jack. And your age is 25.
I usually run with the try block
I always run.
```

We can also shorten the above code as follows:

```python
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

```

## Packing and Unpacking Arguments in Python

We use two operators:

- \* for tuples
- \*\* for dictionaries

Let us take as an example below. It takes only arguments but we have list. We can unpack the list and changes to argument.

### Unpacking

#### Unpacking Lists

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst))  # this would give: TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

If we ran this code, it would raise an error, because this function takes numbers (not a list) as arguments. Let us unpack/destructure the list.

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

We can also use unpacking in the range built-in function that expects a start and an end.

```python
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(list(numbers))  # [2, 3, 4, 5, 6]

```

A list or a tuple can also be unpacked like this:

```python
countries = ['Australia', 'New Zealand', 'Fiji', 'Samoa', 'Tonga']
aus, nz, fiji, *rest = countries
print(aus, nz, fiji, rest)   # Australia New Zealand Fiji ['Samoa', 'Tonga']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      # 1 [2, 3, 4, 5, 6] 7
```

#### Unpacking Dictionaries

```python
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {city}, {country}. He is {age} years old.'
dct = {'name':'Jack', 'country':'Australia', 'city':'Perth', 'age':25}
print(unpacking_person_info(**dct)) # Jack lives in Perth, Australia. He is 25 years old.
```

### Packing

Sometimes we never know how many arguments need to be passed to a python function. We can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.

### Packing Lists

```python
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### Packing Dictionaries

```python
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Jack",
      country="Australia", city="Perth", age=25))
```

```output
name = Jack
country = Australia
city = Perth
age = 25
{'name': 'Jack', 'country': 'Australia', 'city': 'Perth', 'age': 25}
```

## Spreading in Python

Like in JavaScript, spreading is possible in Python. Let us check it in an example below:

```python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Australia', 'New Zealand']
country_lst_two = ['Fiji', 'Samoa', 'Tonga']
oceania_countries = [*country_lst_one, *country_lst_two]
print(oceania_countries)  # ['Australia', 'New Zealand', 'Fiji', 'Samoa', 'Tonga']
```

## Enumerate

If we are interested in an index of a list, we use _enumerate_ built-in function to get the index of each item in the list.

```python
for index, item in enumerate([20, 30, 40]):
    print(index, item)
# 0 20
# 1 30
# 2 40
```

```python
countries = ['Australia', 'New Zealand', 'Fiji', 'Samoa', 'Tonga']
for index, i in enumerate(countries):
    if i == 'Fiji':
        print(f'The country {i} has been found at index {index}')
```

```output
The country Fiji has been found at index 2
```

## Zip

Sometimes we would like to combine lists when looping through them. See the example below:

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```output
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

::::::::::::::::::::::::::::::::::::: challenge

## Exercises

1. names = ['Australia', 'New Zealand', 'Fiji', 'Samoa', 'Tonga', 'Japan', 'China']. Unpack the first five countries and store them in a variable oceania_countries, store Japan and China in jp and cn respectively.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- try runs risky code; except handles the error.
- Catch the specific error you expect, not every error.
- * unpacks lists and ** unpacks dictionaries.

::::::::::::::::::::::::::::::::::::::::::::::::
