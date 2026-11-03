---
title: 'Week 2 Concepts Bridge: Choosing the Right Structure'
teaching: 20
exercises: 10
---

:::::::::::::::::::::::::::::::::::::: questions

- Which data structure should I use for a job?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Choose between a list, tuple, set and dictionary for a given task.

::::::::::::::::::::::::::::::::::::::::::::::::

**Time:** 30 minutes. [Back to Week 2](week-2-overview.md)

## Why this matters

Programmers often have to choose a data structure and explain why one fits a job better than another. This links to LO 1 (analyse and solve a problem) and LO 2 (apply programming techniques). Python gives you four main structures. This note helps you pick the right one.

## Four structures, four questions

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

### List: a changeable sequence

```python
queue = ["Amy", "Ben"]
queue.append("Cara")   # change it
queue[0] = "Alice"     # change one item
print(queue)           # ['Alice', 'Ben', 'Cara']
```

### Tuple: a fixed group

```python
point = (31.95, 115.86)   # latitude, longitude
print(point[0])
# point[0] = 0   # remove the # and run it: Python raises a TypeError
```

Use a tuple when the values belong together and should not change.

### Set: unique items, fast "is it in there?"

```python
visitors = {"Amy", "Ben", "Amy"}
print(len(visitors))        # 2, the repeat is dropped
print("Ben" in visitors)    # True
print(list({3, 1, 2, 3}))   # order is not something to rely on
```

Sets are also good for comparing groups, such as "who is in both?" with `&`.

### Dict: look up by name

```python
phone_book = {"Amy": "0400 111 222", "Ben": "0400 333 444"}
print(phone_book["Ben"])
phone_book["Cara"] = "0400 555 666"
print(len(phone_book))
```

Python finds a key quickly, even in a very large dict. A list has to be searched item by item.

### Structures can be nested

You can put one structure inside another. In this week's practice task you use a dict of lists: a name maps to a list of numbers.

```python
contacts = {"Ben": ["0400 333 444", "08 9000 1111"]}
contacts["Ben"].append("0400 777 888")
print(contacts["Ben"])
```

::::::::::::::::::::::::::::::::::::: challenge

## Activity: the 6-scenario quiz (10 minutes)

For each scenario, write down which structure you would use and **one reason**. Use the four questions above. Then check the model answers.

1. A shopping list where you add and remove items, and the order you added them matters.
2. The latitude and longitude of Perth. They should never be changed by accident.
3. A list of 500 survey answers with many repeats. You want to know the different answers given.
4. Student numbers mapped to student names, with fast lookup by student number.
5. The days of the week, in order, used all through a program.
6. A club has two email lists. You want people who are on both lists.

**Stretch:** for scenario 4, could you use a list instead? What would be slower or harder?

:::::::::::::::: solution

## Model answers

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

## Quick rule of thumb

- Need to change it and keep order? **List.**
- Should it never change? **Tuple.**
- Only need unique items or "is it in there?" **Set.**
- Need to find a value by name? **Dict.**

## Further reading

Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Chapters 2 and 3) (Accessed: 2 November 2026).

:::::::::::::::::::::::::::::::::::::: keypoints

- Ask: does order matter, can it change, must items be unique, do I look up by name?

::::::::::::::::::::::::::::::::::::::::::::::::
