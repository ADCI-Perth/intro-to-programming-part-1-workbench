---
title: 'Week 2: Input and data structures'
teaching: 133
exercises: 177
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 2, and how should I spend my 6 hours?
- How do I store many values in order and change them?
- When should I use a tuple instead of a list?
- How do I keep only unique values and compare groups?
- How do I store values that I look up by name?
- Which data structure should I use for a job?
- Can I use a dictionary of lists to manage real data?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Create lists and access items by index and slice.
- Add, remove, sort and copy list items.
- Create tuples and access their items.
- Explain why tuples cannot be changed, and convert between tuples and lists.
- Create sets and add or remove items.
- Use union, intersection and difference.
- Create dictionaries and read values by key.
- Add, change and remove key-value pairs safely.
- Choose between a list, tuple, set and dictionary for a given task.
- Build a phone-book program that stores and looks up contacts.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 2 overview {#week-2-overview}

**Theme:** getting information from the user, and storing groups of values in lists, tuples, sets and dictionaries.


### What you will be able to do

By the end of this week you can:

- Ask the user for input with `input()`, and explain why it always gives you text.
- Create, change and look up items in lists, tuples, sets and dictionaries.
- Explain how these four structures differ, and pick the right one for a job.
- Build a small phone-book program that stores a dictionary of lists.

### Time plan (under 6 hours)

| Block | What you do | Time |
|---|---|---|
| Watch | 4 short videos | 0 h 42 m |
| Read & practise | Sections 2.2 to 2.5, with the assigned exercises | 1 h 58 m |
| Concepts Bridge | [Choosing the right structure](#week-2-bridge) | 0.5 h |
| Build | [Phone-book practice task](#week-2-practice), your portfolio item for this week | 2 h |
| Quiz | Canvas quiz, 6 questions | 0.25 h |
| **Total** | | **5 h 25 m** |

Aim to finish the week in order: Watch, Read & practise, Bridge, Build, then the Quiz. You can mix Watch and Read & practise by topic if you prefer.

### Watch (42 minutes)

Pause often and type along in PyCharm.

| # | Video | Length | Look for |
|---|---|---|---|
| 1 | **T#18** [User Input in Python](https://www.youtube.com/watch?v=4OX49nLNPEE&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:59 | `input()` always gives you text (a string), even when you type a number. |
| 2 | **T#5** [List in Python](https://www.youtube.com/watch?v=Eaz5e6M8tL4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 10:42 | How to add, remove and change list items. |
| 3 | **T#6** [Tuple, Set in Python](https://www.youtube.com/watch?v=Mf7eFtbVxFM&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:41 | A tuple cannot change. A set has no repeats. |
| 4 | **Telusko** [Dictionary in Python](https://www.youtube.com/watch?v=2IsF7DEtVjg&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 12:24 | Keys and values, and how to look a value up by its key. |

The four videos add up to 41 min 46 s, shown as 42 min.

### Read & practise (1 h 58 min)

Read each lesson and run the examples in PyCharm. Then do the exercises. In PyCharm, create a new Python file, paste the example and click **Run**.

| Lesson | Time | Read | Exercises |
|---|---|---|---|
| [Section 2.2: Lists](#section-2-2) | 47 min | Whole lesson. | Level 1, exercises 1 to 5 (15 min). |
| [Section 2.3: Tuples](#section-2-3) | 18 min | Whole lesson. | Level 1, exercises 1 and 2 (6 min). |
| [Section 2.4: Sets](#section-2-4) | 25 min | Whole lesson. | Level 1, exercises 1 and 2 (6 min). |
| [Section 2.5: Dictionaries](#section-2-5) | 28 min | Whole lesson. | Exercises 1 to 3 (9 min). |
| **Total** | **1 h 58 min** | | |

Notes:

- The exercise times assume about 3 minutes per exercise. The other exercises are Optional (see the end of this page).
- The practice task uses two string methods, `.strip()` and `.title()`, to tidy what the user types. They are explained in the practice task, along with `", ".join(...)` and f-strings (text in `f"..."`, with values inside `{}`). Strings are covered properly in Week 7.
- Section 2.2 mentions a long list of countries in `data/countries.py`. You only need it for Level 2, which is Optional. The file is in `assets/data/` at the top of this repository ([countries.py](data/countries.py)).
- The lessons link to `data/` and `files/` folders. In this course these are `assets/data/` and `assets/files/`.
- Stuck? Join the optional one-hour online drop-in session. If you go, count it inside your Read & practise time.

### Concepts Bridge (30 min)

[Choosing the right structure](#week-2-bridge): list, tuple, set or dictionary? You work through a six-scenario quiz. It shows how to pick a structure for a job.

### Build (2 h)

[Practice task: phone book](#week-2-practice). You write a contacts program with a dictionary of lists and user input. It is your portfolio item for this week. The folder has a starter file, a model solution and a test file.

### Quiz (0.25 h)

Take the Canvas quiz for Week 2 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `starter.py` (your phone book)
- `structure_note.txt` (three sentences, see the practice task)

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Not required. Do these only if you have time left over.

**Videos**

- **T#26** Arrays and **T#27** Array values from user, in the [Telusko playlist](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3)

**Reading**

- Driscoll, M. (2017) *Python 101*, Chapters 2 and 3. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Accessed: 2 November 2026).

**More practice** (these are the exercises moved out of the core list):

- Section 2.2 Lists: Level 1 exercises 6 to 27, and all of Level 2.
- Section 2.3 Tuples: Level 1 exercises 3 to 5, and all of Level 2.
- Section 2.4 Sets: Level 1 exercises 3 to 5, and all of Levels 2 and 3.
- Section 2.5 Dictionaries: exercises 4 to 11.

## 2.2 Lists {#section-2-2}

### Lists

There are four collection data types in Python :

- List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
- Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
- Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
- Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

#### How to Create a List

In Python we can create lists in two ways:

- Using list built-in function

```python
# syntax
lst = list()
```

```python
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

- Using square brackets, []

```python
# syntax
lst = []
```

```python
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

Lists with initial values. We use _len()_ to find the length of a list.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongoDB'] # list of web technologies
countries = ['Australia', 'New Zealand', 'Fiji', 'Papua New Guinea', 'Samoa']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```

Output:

```output
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
Number of web technologies: 7
Countries: ['Australia', 'New Zealand', 'Fiji', 'Papua New Guinea', 'Samoa']
Number of countries: 5
```

- Lists can have items of different data types

```python
lst = ['Jack', 25, True, {'country': 'Australia', 'city': 'Perth'}] # list containing different data types
```

#### Accessing List Items Using Positive Indexing

We access each item in a list using their index. A list index starts from 0. The picture below shows clearly where the index starts
| Item | `'banana'` | `'orange'` | `'mango'` | `'lemon'` |
|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 |

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit) # lemon
```

#### Accessing List Items Using Negative Indexing

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.

| Item | `'banana'` | `'orange'` | `'mango'` | `'lemon'` |
|---|---|---|---|---|
| Index | -4 | -3 | -2 | -1 |

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```

#### Unpacking List Items

```python
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

```

```python
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon', 'lime', 'apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4, 5, 6, 7, 8, 9]
print(tenth)          # 10
# Third Example about unpacking list
cities = ['Perth', 'Adelaide', 'Darwin', 'Brisbane', 'Sydney', 'Melbourne', 'Hobart']
perth, adelaide, darwin, *east_coast, hobart = cities
print(perth)          # Perth
print(adelaide)       # Adelaide
print(darwin)         # Darwin
print(east_coast)     # ['Brisbane', 'Sydney', 'Melbourne']
print(hobart)         # Hobart
```

#### Slicing Items from a List

- Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2nd item - ['banana', 'mango']
```

- Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
```

#### Modifying Lists

List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

#### Checking Items in a List

Checking an item if it is a member of a list using *in* operator. See the example below.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

#### Adding Items to a List

To add item to the end of an existing list we use the method *append()*.

```python
# syntax
lst = list()
lst.append(item)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

#### Inserting Items into a List

We can use *insert()* method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The *insert()* methods takes two arguments:index and an item to insert.

```python
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

#### Removing Items from a List

The remove method removes a specified item from a list

```python
# syntax
lst = ['item1', 'item2']
lst.remove(item)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

#### Removing Items Using Pop

The *pop()* method removes the specified index, (or the last item if index is not specified):

```python
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

#### Removing Items Using Del

The *del* keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely

```python
# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
# print(fruits)     # this would give: NameError: name 'fruits' is not defined
```

#### Clearing List Items

The *clear()* method empties the list:

```python
# syntax
lst = ['item1', 'item2']
lst.clear()
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

#### Copying a List

It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way of avoiding the problem above is using _copy()_.

```python
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

#### Joining Lists

There are several ways to join, or concatenate, two or more lists in Python.

- Plus Operator (+)

```python
# syntax
list3 = list1 + list2
```

```python
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

- Joining using extend() method
  The *extend()* method allows to append list in a list. See the example below.

```python
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2) # ['item1', 'item2', 'item3', 'item4', 'item5']
```

```python
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

#### Counting Items in a List

The *count()* method returns the number of times an item appears in a list:

```python
# syntax
lst = ['item1', 'item2']
lst.count(item)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

#### Finding Index of an Item

The *index()* method returns the index of an item in the list:

```python
# syntax
lst = ['item1', 'item2']
lst.index(item)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence
```

#### Reversing a List

The *reverse()* method reverses the order of a list.

```python
# syntax
lst = ['item1', 'item2']
lst.reverse()

```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
```

#### Sorting List Items

To sort lists we can use _sort()_ method or _sorted()_ built-in functions. The _sort()_ method reorders the list items in ascending order and modifies the original list. If an argument of _sort()_ method reverse is equal to true, it will arrange the list in descending order.

- sort(): this method modifies the original list

  ```python
  # syntax
  lst = ['item1', 'item2']
  lst.sort()                # ascending
  lst.sort(reverse=True)    # descending
  ```

  **Example:**

  ```python
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits.sort()
  print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
  fruits.sort(reverse=True)
  print(fruits) # ['orange', 'mango', 'lemon', 'banana']
  ages = [22, 19, 24, 25, 26, 24, 25, 24]
  ages.sort()
  print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]
 
  ages.sort(reverse=True)
  print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
  ```

  sorted(): returns the ordered list without modifying the original list
  **Example:**

  ```python
  fruits = ['banana', 'orange', 'mango', 'lemon']
  print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
  # Reverse order
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits = sorted(fruits,reverse=True)
  print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
  ```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Declare an empty list
2. Declare a list with more than 5 items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types, put your (name, age, height, whether you are a student, suburb)
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7. Print the list using _print()_
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists:

    ```python
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```

27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. The following is a list of 10 students ages:

```bash
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

- Sort the list and find the min and max age
- Add the min age and the max age again to the list
- Find the median age (one middle item or two middle items divided by two)
- Find the average age (sum of all items divided by their number )
- Find the range of the ages (max minus min)
- Compare the value of (min - average) and (max - average), use _abs()_ method

1. Find the middle country(ies) in the [countries list](data/countries.py)
1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
1. ['China', 'Japan', 'USA', 'Australia', 'New Zealand', 'Fiji', 'Samoa']. Unpack the first three countries and the rest as oceania_countries.

::::::::::::::::::::::::::::::::::::::::::::::::

## 2.3 Tuples {#section-2-3}

## Section 2.3:

### Tuples

A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

- tuple(): to create an empty tuple
- count(): to count the number of a specified item in a tuple
- index(): to find the index of a specified item in a tuple
- `+` operator: to join two or more tuples and to create a new tuple

#### Creating a Tuple

- Empty tuple: Creating an empty tuple
  
  ```python
  # syntax
  empty_tuple = ()
  # or using the tuple constructor
  empty_tuple = tuple()
  ```

- Tuple with initial values
  
  ```python
  # syntax
  tpl = ('item1', 'item2','item3')
  ```

  ```python
  fruits = ('banana', 'orange', 'mango', 'lemon')
  print(fruits)       # ('banana', 'orange', 'mango', 'lemon')
  print(len(fruits))  # 4
  ```

#### Tuple length

We use the _len()_ method to get the length of a tuple.

```python
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

#### Accessing Tuple Items

- Positive Indexing
  Similar to the list data type we use positive or negative indexing to access tuple items.
  | Item | `'banana'` | `'orange'` | `'mango'` | `'lemon'` |
|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 |

  ```python
  # Syntax
  tpl = ('item1', 'item2', 'item3')
  first_item = tpl[0]
  second_item = tpl[1]
  ```

  ```python
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[0]
  second_fruit = fruits[1]
  last_index = len(fruits) - 1
  last_fruit = fruits[last_index]
  print(first_fruit)   # banana
  print(second_fruit)  # orange
  print(last_fruit)    # lemon
  ```

- Negative indexing
  Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last and the negative of the list/tuple length refers to the first item.
  | Item | `'banana'` | `'orange'` | `'mango'` | `'lemon'` |
|---|---|---|---|---|
| Index | -4 | -3 | -2 | -1 |

  ```python
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  first_item = tpl[-4]
  second_item = tpl[-3]
  ```

  ```python
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[-4]
  second_fruit = fruits[-3]
  last_fruit = fruits[-1]
  print(first_fruit)   # banana
  print(second_fruit)  # orange
  print(last_fruit)    # lemon
  ```

#### Slicing tuples

We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.

- Range of Positive Indexes

  ```python
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[0:4]         # all items
  all_items = tpl[0:]         # all items
  middle_two_items = tpl[1:3]  # does not include item at index 3
  ```

  ```python
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[0:4]    # all items
  all_fruits = fruits[0:]     # all items
  orange_mango = fruits[1:3]  # doesn't include item at index 3
  orange_to_the_rest = fruits[1:]
  print(all_fruits)          # ('banana', 'orange', 'mango', 'lemon')
  print(orange_mango)        # ('orange', 'mango')
  print(orange_to_the_rest)  # ('orange', 'mango', 'lemon')
  ```

- Range of Negative Indexes

  ```python
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[-4:]         # all items
  middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
  ```

  ```python
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[-4:]    # all items
  orange_mango = fruits[-3:-1]  # doesn't include item at index 3
  orange_to_the_rest = fruits[-3:]
  print(all_fruits)          # ('banana', 'orange', 'mango', 'lemon')
  print(orange_mango)        # ('orange', 'mango')
  print(orange_to_the_rest)  # ('orange', 'mango', 'lemon')
  ```

#### Changing Tuples to Lists

We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.

```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

#### Checking an Item in a Tuple

We can check if an item exists or not in a tuple using _in_, it returns a boolean.

```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
# fruits[0] = 'apple'  # this would give: TypeError: 'tuple' object does not support item assignment
```

#### Joining Tuples

We can join two or more tuples using + operator

```python
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)  # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
```

#### Deleting Tuples

It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using _del_.

```python
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
# print(fruits)  # this would give: NameError: name 'fruits' is not defined
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Create an empty tuple
2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
3. Join brothers and sisters tuples and assign it to siblings
4. How many siblings do you have?
5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Unpack siblings and parents from family_members
1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
1. Change the above food_stuff_tp tuple to a food_stuff_lt list
1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
1. Slice out the first three items and the last three items from food_stuff_lt list
1. Delete the food_stuff_tp tuple completely
1. Check if an item exists in  tuple:

- Check if 'Japan' is an Oceania country
- Check if 'Fiji' is an Oceania country

  ```python
  oceania_countries = ('Australia', 'Fiji', 'New Zealand', 'Papua New Guinea', 'Samoa')
  ```

::::::::::::::::::::::::::::::::::::::::::::::::

## 2.4 Sets {#section-2-4}

### Sets

Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the _union_, _intersection_, _difference_, _symmetric difference_, _subset_, _super set_ and _disjoint set_ among sets.

#### Creating a Set

To create an empty set, we use the set() function. Empty curly brackets {} will create a dictionary. 

- Creating an empty set

```python
# syntax
st = set()
```

- Creating a set with initial items

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```

**Example:**

```python
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

#### Getting Set's Length

We use **len()** method to find the length of a set.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

**Example:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))  # 4
```

#### Accessing Items in a Set

We use loops to access items. We will see this in loop section

#### Checking an Item

To check if an item exist in a list we use _in_ membership operator.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

**Example:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```

#### Adding Items to a Set

Once a set is created we cannot change any items and we can also add additional items.

- Add one item using _add()_

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

**Example:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)  # {'banana', 'orange', 'mango', 'lemon', 'lime'} - order may differ: sets have no order
```

- Add multiple items using _update()_
  The _update()_ allows to add multiple items to a set. The _update()_ takes a list argument.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

**Example:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(len(fruits))  # 9
```

#### Removing Items from a Set

We can remove an item from a set using _remove()_ method. If the item is not found _remove()_ method will raise errors, so it is good to check if the item exist in the given set. However, _discard()_ method doesn't raise any errors.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

The pop() methods remove a random item from a list and it returns the removed item.

**Example:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print(len(fruits))  # 3

```

If we are interested in the removed item.

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)  # one of the four fruits - which one is random
```

#### Clearing Items in a Set

If we want to clear or empty the set we use _clear_ method.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**Example:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

#### Deleting a Set

If we want to delete the set itself we use _del_ operator.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**Example:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
# print(fruits)  # this would give: NameError: name 'fruits' is not defined
```

#### Converting List to Set

We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.

```python
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
```

**Example:**

```python
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits)
print(fruits)  # {'mango', 'lemon', 'banana', 'orange'} - order may differ: sets have no order
```

#### Joining Sets

We can join two sets using the _union()_ or _update()_ method or _|_ symbol .

- Union
  This method returns a new set

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2
```

**Example:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'} - order may differ
# or using this : print(fruits | vegetables)
```

- Update
  This method inserts a set into a given set

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```

**Example:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'} - order may differ
```

#### Finding Intersection Items

Intersection returns a set of items which are in both the sets or using _&_ symbol. See the example

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# or using this: st1 & st2
```

**Example:**

```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers)) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))     # {'o', 'n'} - order may differ
# python & dragon
```

#### Checking Subset and Super Set

A set can be a subset or super set of other sets:

- Subset: _issubset()_
- Super set: _issuperset_

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

**Example:**

```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers)) # False, because it is a super set
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon))     # False
```

#### Checking the Difference Between Two Sets

It returns the difference between two sets or using _-_ symbol .

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1
```

**Example:**

```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers)) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))     # {'p', 'y', 't', 'h'} - order may differ: sets have no order
# python - dragon
print(dragon.difference(python))     # {'d', 'r', 'a', 'g'} - order may differ
# dragon - python
```

#### Finding Symmetric Difference Between Two Sets

It returns the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1
```

**Example:**

```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers)) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'} - order may differ
# python ^ dragon
```

#### Checking for Disjoint Sets

If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using _isdisjoint()_ method.

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```

**Example:**

```python
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

```python
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Find the length of the set it_companies
2. Add 'Atlassian' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4. Remove one of the companies from the set it_companies
5. What is the difference between remove and discard

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Join A and B
2. Find A intersection B
3. Is A subset of B
4. Are A and B disjoint sets
5. Join A with B and B with A
6. What is the symmetric difference between A and B
7. Delete the sets completely

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 3

1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
2. Explain the difference between the following data types: string, list, tuple and set
3. _I am a student and I love to learn and to practise coding._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

::::::::::::::::::::::::::::::::::::::::::::::::

## 2.5 Dictionaries {#section-2-5}

### Dictionaries

A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

#### Creating a Dictionary

To create a dictionary we use curly brackets, {} or the *dict()* built-in function.

```python
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
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
```

The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.

#### Dictionary Length

It checks the number of 'key: value' pairs in the dictionary.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
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
print(len(person)) # 7

```

#### Accessing Dictionary Items

We can access Dictionary items by referring to its key name.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
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
print(person['first_name']) # Jack
print(person['country'])    # Australia
print(person['skills'])     # ['Python', 'Excel', 'SQL']
print(person['skills'][0])  # Python
print(person['address']['street']) # 12 Hay Street
# print(person['city'])     # this would give: KeyError: 'city'
```

Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the _get_ method. The get method returns None, which is a NoneType object data type, if the key does not exist.
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
print(person.get('first_name')) # Jack
print(person.get('country'))    # Australia
print(person.get('skills'))     # ['Python', 'Excel', 'SQL']
print(person.get('city'))   # None
```

#### Adding Items to a Dictionary

We can add new key and value pairs to a dictionary

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
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
person['job_title'] = 'Data analyst'
person['skills'].append('Power BI')
print(person['job_title'])  # Data analyst
print(person['skills'])     # ['Python', 'Excel', 'SQL', 'Power BI']
```

#### Modifying Items in a Dictionary

We can modify items in a dictionary

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
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
person['first_name'] = 'Olivia'
person['age'] = 26
print(person['first_name'])  # Olivia
print(person['age'])         # 26
```

#### Checking Keys in a Dictionary

We use the _in_ operator to check if a key exist in a dictionary

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

#### Removing Key and Value Pairs from a Dictionary

- _pop(key)_: removes the item with the specified key name:
- _popitem()_: removes the last item
- _del_: removes an item with specified key name

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
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
person.pop('first_name')        # Removes the first_name item
person.popitem()                # Removes the last item, address
del person['is_student']        # Removes the is_student item
print(person)  # {'last_name': 'Wilson', 'age': 25, 'country': 'Australia', 'skills': ['Python', 'Excel', 'SQL']}
```

#### Changing Dictionary to a List of Items

The _items()_ method changes dictionary to a list of tuples.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

#### Clearing a Dictionary

If we don't want the items in a dictionary we can clear them using _clear()_ method

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.clear()
print(dct) # {}
```

#### Deleting a Dictionary

If we do not use the dictionary we can delete it completely

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

#### Copy a Dictionary

We can copy a dictionary using a _copy()_ method. Using copy we can avoid mutation of the original dictionary.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct_copy) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
```

#### Getting Dictionary Keys as a List

The _keys()_ method gives us all the keys of a dictionary as a list.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

#### Getting Dictionary Values as a List

The _values_ method gives us all the values of a dictionary as a list.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

1. Create  an empty dictionary called dog
2. Add name, color, breed, legs, age to the dog dictionary
3. Create a student dictionary and add first_name, last_name, age, is_student, skills, country, city and address as keys for the dictionary
4. Get the length of the student dictionary
5. Get the value of skills and check the data type, it should be a list
6. Modify the skills values by adding one or two skills
7. Get the dictionary keys as a list
8. Get the dictionary values as a list
9. Change the dictionary to a list of tuples using _items()_ method
10. Delete one of the items in the dictionary
11. Delete one of the dictionaries

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Choosing the Right Structure {#week-2-bridge}

**Time:** 30 minutes. [Back to Week 2](#week-2-overview)

### Why this matters

Programmers often have to choose a data structure and explain why one fits a job better than another. This links to LO 1 (analyse and solve a problem) and LO 2 (apply programming techniques). Python gives you four main structures. This note helps you pick the right one.

### Four structures, four questions

A **data structure** is a way to hold a group of values. Ask these questions to choose one.

- **Mutable?** Can you change it after you make it? *Mutable* means changeable. *Immutable* means fixed.
- **Ordered?** Do items keep their position, so you can ask for "the first one"?
- **Unique?** Does it refuse repeated items?
- **Lookup?** How do you find something: by position, by value, or by a name (a key)?

| Structure | Written | Mutable? | Ordered? | Repeats allowed? | You find items by |
|---|---|---|---|---|---|
| list | `[1, 2, 3]` | Yes | Yes | Yes | position (index) |
| tuple | `(1, 2, 3)` | No | Yes | Yes | position (index) |
| set | `{1, 2, 3}` | Yes | No | No | membership (`in`) |
| dict | `{"a": 1}` | Yes | Yes (by insertion) | Keys: no. Values: yes | key |

A dict keeps items in the order you added them. You still look values up by key, not by position.

#### List: a changeable sequence

```python
queue = ["Amy", "Ben"]
queue.append("Cara")   # change it
queue[0] = "Alice"     # change one item
print(queue)           # ['Alice', 'Ben', 'Cara']
```

#### Tuple: a fixed group

```python
point = (31.95, 115.86)   # latitude, longitude
print(point[0])
# point[0] = 0   # remove the # and run it: Python raises a TypeError
```

Use a tuple when the values belong together and should not change.

#### Set: unique items, fast "is it in there?"

```python
visitors = {"Amy", "Ben", "Amy"}
print(len(visitors))        # 2, the repeat is dropped
print("Ben" in visitors)    # True
print(list({3, 1, 2, 3}))   # order is not something to rely on
```

Sets are also good for comparing groups, such as "who is in both?" with `&`.

#### Dict: look up by name

```python
phone_book = {"Amy": "0400 111 222", "Ben": "0400 333 444"}
print(phone_book["Ben"])
phone_book["Cara"] = "0400 555 666"
print(len(phone_book))
```

Python finds a key quickly, even in a very large dict. A list has to be searched item by item.

#### Structures can be nested

You can put one structure inside another. In this week's practice task you use a dict of lists: a name maps to a list of numbers.

```python
contacts = {"Ben": ["0400 333 444", "08 9000 1111"]}
contacts["Ben"].append("0400 777 888")
print(contacts["Ben"])
```

::::::::::::::::::::::::::::::::::::: challenge

### Activity: the 6-scenario quiz (10 minutes)

For each scenario, write down which structure you would use and **one reason**. Use the four questions above. Then check the model answers.

1. A shopping list where you add and remove items, and the order you added them matters.
2. The latitude and longitude of Perth. They should never be changed by accident.
3. A list of 500 survey answers with many repeats. You want to know the different answers given.
4. Student numbers mapped to student names, with fast lookup by student number.
5. The days of the week, in order, used all through a program.
6. A club has two email lists. You want people who are on both lists.

**Stretch:** for scenario 4, could you use a list instead? What would be slower or harder?

:::::::::::::::: solution

### Model answers

Your wording will differ. The reasons matter most.

1. **List.** It is mutable and ordered, and it allows repeats if you buy two of something.
2. **Tuple.** The pair belongs together and is immutable, so it cannot be changed by mistake.
3. **Set.** Converting with `set(answers)` drops the repeats. Uniqueness is built in.
4. **Dict.** Student number is the key and name is the value. You look up by key, so you do not search a list.
5. **Tuple.** The days are ordered and never change. (A list also works, but a tuple tells readers they are fixed.)
6. **Set.** Make a set from each list and use `&` to find the people on both.

For scenario 4, a list would force you to check each item one by one to find a student number. That is slower and the code is longer.

Check scenarios 3 and 6 in Python:

```python
answers = ["yes", "no", "yes", "maybe", "no", "yes"]
print(set(answers))            # the different answers (order may vary)

list_a = {"amy@example.com", "ben@example.com"}
list_b = {"ben@example.com", "cara@example.com"}
print(list_a & list_b)         # {'ben@example.com'}
```

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

### Quick rule of thumb

- Need to change it and keep order? **List.**
- Should it never change? **Tuple.**
- Only need unique items or "is it in there?" **Set.**
- Need to find a value by name? **Dict.**

### Further reading

Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Chapters 2 and 3) (Accessed: 2 November 2026).

## Practice task: Phone Book {#week-2-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [starter.py](files/week-2/starter.py)
- [solution.py](files/week-2/solution.py)
- [test_solution.py](files/week-2/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time:** about 2 hours. This is your portfolio item for Week 2. Your tutor marks it at the end of the week.


### Goal

Write a small phone-book program. It stores contacts in a **dictionary of lists**. Each name (the key) holds a list of phone numbers (the value). The program asks you questions with `input()` and prints the results.

You will practise:

- `input()` and string methods such as `.strip()` and `.title()`
- dictionaries: adding, `.get()`, `.pop()`, `.keys()`
- lists: `.append()`, `.sort()`, `", ".join(...)`
- a set, in the stretch step

You have not learnt `if`, loops or functions yet. That is fine. **Do not use them.** Week 3 covers them.

### New terms

- **Dictionary of lists:** a dictionary where every value is a list. Example: `{"Ben": ["0400 333 444", "08 9000 1111"]}`.
- **Default value:** what a method gives back when it cannot find what you asked for.

### Steps

Open `starter.py` in PyCharm. Work from the top, one step at a time. Run the file after each step.

1. **Start data.** `contacts` already holds two people. Read it. Notice that each value is a list, even when it holds only one number.
2. **Add a contact.**
   - Ask for a name. Tidy it with `.strip()` and `.title()`, so `"  cara jones "` becomes `"Cara Jones"`.
   - Ask for a mobile number.
   - Add the name to `contacts`. The value is a list holding the mobile number.
3. **Add a second number.** Ask for a home or work number. Use `.append()` to add it to the list for the same name.
4. **Look up a contact.** Ask which contact to look up. Tidy the answer. Use `contacts.get(name, ["not found"])` to get the numbers. Print one line, for example `Ben: 0400 333 444, 08 9000 1111`.
5. **Remove a contact.** Ask which contact to remove. Tidy the answer. Use `contacts.pop(name, None)`. The second value is a default, so nothing breaks if the name is not there.
6. **Show the phone book.** Make a list of the names with `list(contacts.keys())`. Sort it with `.sort()`. Print one line, for example `Contacts (2): Ben, Cara Jones`. Use `len(contacts)` for the count.
7. **Stretch (optional).** Use a set to count the different numbers the new contact and Ben have together. A set keeps each value once. Do this before Step 5, so the name still exists.

### Example run

Your typing is shown after each prompt.

```
New contact name: cara jones
Mobile number: 0411 000 111
Second number (home or work): 08 9111 2222
Different numbers for Cara Jones and Ben: 4
Look up which contact? ben
Ben: 0400 333 444, 08 9000 1111
Remove which contact? amy
Contacts (2): Ben, Cara Jones
```

The "Different numbers" line is the stretch step. Your prompts can be worded differently. The **printed lines** should look like the ones above.

### Hints

- `.strip()` removes spaces from both ends. `.title()` makes each word start with a capital letter.
- `contacts[name] = [mobile]` creates a new key with a one-item list.
- `contacts[name].append(extra)` adds to the list stored under that key.
- `", ".join(numbers)` turns `["a", "b"]` into `"a, b"`.
- An f-string such as `f"{name}: {text}"` is a tidy way to build a line.
- If you see a `KeyError`, you asked for a key that is not in the dictionary. Check your spelling, or use `.get()`.

### Check your work

- [ ] The program runs from top to bottom without errors.
- [ ] `structure_note.txt` has exactly three sentences.
- [ ] A name typed as `  cara jones ` is stored as `Cara Jones`.
- [ ] Looking up a name that does not exist prints `not found`, not an error.
- [ ] Removing a name that does not exist changes nothing.
- [ ] The names in the last line are in alphabetical order.
- [ ] You did not use `if`, `for`, `while` or `def`.

### Part 2: structure note (about 20 min)

Create a plain text file called `structure_note.txt` (in PyCharm: **New > File**). Write **exactly three sentences**:

1. Which structure you used to store the contacts, and why.
2. Why a list would be slower for finding a contact by name.
3. One thing the set in the stretch step does that a list does not.

Use the [Concepts Bridge](#week-2-bridge) to help you choose your words.

### Test your program (optional)

The test file runs your program, types answers into it and checks what it prints. It tests `solution.py` by default. To test your own file, set `PHONEBOOK_FILE`.

From the repository root, in the PyCharm terminal (PowerShell):

```powershell
$env:PHONEBOOK_FILE = "starter.py"
python -m pytest weeks/week-2/practice
```

If a test fails, read the message. It shows the line the test expected. Try not to open `solution.py` until you have had a good go.

### Extra challenges (if you have time)

- Add a tuple for each contact, such as `("Cara Jones", "Perth")`, and print it.
- Use `.upper()` or `.lower()` to make the lookup ignore capital letters.
- Store a third number and print how many numbers each person has with `len()`.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- A list is an ordered, changeable collection.
- Methods like append(), insert(), remove() and pop() change the list itself.
- Use copy() when you need an independent copy.
- A tuple is an ordered collection that cannot be changed.
- Use a tuple for values that belong together and should stay fixed.
- A set holds unique items with no order.
- Converting a list to a set removes duplicates.
- Set operations compare whole groups at once.
- A dictionary maps keys to values.
- Use get() to avoid a KeyError when a key may be missing.
- items(), keys() and values() let you work through a dictionary.
- Ask: does order matter, can it change, must items be unique, do I look up by name?
- A dictionary of lists stores several values for each key.

::::::::::::::::::::::::::::::::::::::::::::::::
