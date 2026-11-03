---
title: '3.3 Functions'
teaching: 25
exercises: 17
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I write code once and reuse it?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Define functions with parameters and return values.
- Use default, keyword and arbitrary arguments.

::::::::::::::::::::::::::::::::::::::::::::::::

## Functions

So far we have seen many built-in Python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, let us learn what a function is and why we need them?

### Defining a Function

A function is a reusable block of code or programming statements designed to perform a certain task. To define or declare a function, Python provides the _def_ keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.

### Declaring and Calling a Function

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

### Function without Parameters

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

### Function Returning a Value - Part 1

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

### Function with Parameters

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

### Passing Arguments with Key and Value

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

### Function Returning a Value - Part 2

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

### Function with Default Parameters

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

### Arbitrary Number of Arguments

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

### Default and Arbitrary Number of Parameters in Functions

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
### Dictionary unpacking

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

### Arbitrary Number of Named Arguments

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

### Function as a Parameter of Another Function

```python
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 9
```

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 1

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

## Exercises: Level 2

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

## Exercises: Level 3

1. Write a function called is_prime, which checks if a number is prime.
1. Write a functions which checks if all items are unique in the list.
1. Write a function which checks if all the items of the list are of the same data type.
1. Write a function which check if provided variable is a valid python variable
1. Go to the data folder and access the countries-data.py file.

- Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
- Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- def defines a function; calling it runs the code.
- return sends a value back; without it a function returns None.
- Functions that take values and return values are easy to test.

::::::::::::::::::::::::::::::::::::::::::::::::
