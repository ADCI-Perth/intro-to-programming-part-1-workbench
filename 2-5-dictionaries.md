---
title: '2.5 Dictionaries'
teaching: 18
exercises: 12
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I store values that I look up by name?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Create dictionaries and read values by key.
- Add, change and remove key-value pairs safely.

::::::::::::::::::::::::::::::::::::::::::::::::

## Dictionaries

A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

### Creating a Dictionary

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

### Dictionary Length

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

### Accessing Dictionary Items

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

### Adding Items to a Dictionary

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

### Modifying Items in a Dictionary

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

### Checking Keys in a Dictionary

We use the _in_ operator to check if a key exist in a dictionary

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Removing Key and Value Pairs from a Dictionary

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

### Changing Dictionary to a List of Items

The _items()_ method changes dictionary to a list of tuples.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### Clearing a Dictionary

If we don't want the items in a dictionary we can clear them using _clear()_ method

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.clear()
print(dct) # {}
```

### Deleting a Dictionary

If we do not use the dictionary we can delete it completely

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### Copy a Dictionary

We can copy a dictionary using a _copy()_ method. Using copy we can avoid mutation of the original dictionary.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct_copy) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
```

### Getting Dictionary Keys as a List

The _keys()_ method gives us all the keys of a dictionary as a list.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### Getting Dictionary Values as a List

The _values_ method gives us all the values of a dictionary as a list.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

::::::::::::::::::::::::::::::::::::: challenge

## Exercises

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

:::::::::::::::::::::::::::::::::::::: keypoints

- A dictionary maps keys to values.
- Use get() to avoid a KeyError when a key may be missing.
- items(), keys() and values() let you work through a dictionary.

::::::::::::::::::::::::::::::::::::::::::::::::
