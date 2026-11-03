---
title: '2.4 Sets'
teaching: 18
exercises: 12
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I keep only unique values and compare groups?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Create sets and add or remove items.
- Use union, intersection and difference.

::::::::::::::::::::::::::::::::::::::::::::::::

## Sets

Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the _union_, _intersection_, _difference_, _symmetric difference_, _subset_, _super set_ and _disjoint set_ among sets.

### Creating a Set

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

### Getting Set's Length

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

### Accessing Items in a Set

We use loops to access items. We will see this in loop section

### Checking an Item

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

### Adding Items to a Set

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

### Removing Items from a Set

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

### Clearing Items in a Set

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

### Deleting a Set

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

### Converting List to Set

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

### Joining Sets

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

### Finding Intersection Items

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

### Checking Subset and Super Set

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

### Checking the Difference Between Two Sets

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

### Finding Symmetric Difference Between Two Sets

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

### Checking for Disjoint Sets

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

## Exercises

```python
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 1

1. Find the length of the set it_companies
2. Add 'Atlassian' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4. Remove one of the companies from the set it_companies
5. What is the difference between remove and discard

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 2

1. Join A and B
2. Find A intersection B
3. Is A subset of B
4. Are A and B disjoint sets
5. Join A with B and B with A
6. What is the symmetric difference between A and B
7. Delete the sets completely

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Exercises: Level 3

1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
2. Explain the difference between the following data types: string, list, tuple and set
3. _I am a student and I love to learn and to practise coding._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- A set holds unique items with no order.
- Converting a list to a set removes duplicates.
- Set operations compare whole groups at once.

::::::::::::::::::::::::::::::::::::::::::::::::
