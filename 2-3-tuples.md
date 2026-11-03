---
title: '2.3 Tuples'
teaching: 18
exercises: 12
---

:::::::::::::::::::::::::::::::::::::: questions

- When should I use a tuple instead of a list?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Create tuples and access their items.
- Explain why tuples cannot be changed, and convert between tuples and lists.

::::::::::::::::::::::::::::::::::::::::::::::::

# Section 2.3:

## Tuples

A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

- tuple(): to create an empty tuple
- count(): to count the number of a specified item in a tuple
- index(): to find the index of a specified item in a tuple
- `+` operator: to join two or more tuples and to create a new tuple

### Creating a Tuple

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

### Tuple length

We use the _len()_ method to get the length of a tuple.

```python
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

### Accessing Tuple Items

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

### Slicing tuples

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

### Changing Tuples to Lists

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

### Checking an Item in a Tuple

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

### Joining Tuples

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

### Deleting Tuples

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

## Exercises: Level 1

1. Create an empty tuple
2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
3. Join brothers and sisters tuples and assign it to siblings
4. How many siblings do you have?
5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 2

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

:::::::::::::::::::::::::::::::::::::: keypoints

- A tuple is an ordered collection that cannot be changed.
- Use a tuple for values that belong together and should stay fixed.

::::::::::::::::::::::::::::::::::::::::::::::::
