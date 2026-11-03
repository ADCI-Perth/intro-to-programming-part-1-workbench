---
title: 'Week 4 Concepts Bridge: Functional and Logic Programming'
teaching: 20
exercises: 10
---

:::::::::::::::::::::::::::::::::::::: questions

- What are programming paradigms?
- How do functional and logic programming differ from what I have done so far?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Explain pure functions, side effects and recursion.
- Run a small logic program and write the same rules in Python.

::::::::::::::::::::::::::::::::::::::::::::::::

**Time: 30 minutes** (2 min functional ideas, 8 min video, 4 min SWISH, 1 min Python version, 15 min activity)

## Why this matters

Python can be used in a functional way, even though it is also object-oriented. This supports LO 2 (apply object-oriented, imperative, functional and logic programming techniques). Today you meet two **paradigms** (styles of programming): functional and logic.

## Functional ideas (2 min)

A **side effect** is anything a function does besides returning a value, such as printing or changing a list outside the function. A **pure function** has no side effects: the same input always gives the same answer.

```python
def add_gst_pure(price):
    return round(price * 1.1, 2)      # pure: only uses its input


def add_gst_impure(price, log):
    total = round(price * 1.1, 2)
    log.append(total)                 # side effect: changes a list outside
    return total


history = []
print(add_gst_pure(100))              # 110.0
print(add_gst_impure(100, history))   # 110.0
print(add_gst_impure(50, history))    # 55.0
print(history)                        # [110.0, 55.0] (the outside list changed)
```

Pure functions are easy to test, because you only check input and output.

**Recursion** means a function calls itself on a smaller problem. It needs a **base case**, the simple answer that stops the calls.

```python
def add_up(items):
    if not items:                          # base case: empty list
        return 0
    return items[0] + add_up(items[1:])    # smaller problem


print(add_up([4, 5, 6]))  # 15
```

There is no changing variable. This is why functional languages like recursion.

## Logic programming (LO 2)

In **logic programming** you do not write steps. You state **facts** (things that are true) and **rules** (how new facts follow from old ones). Then you ask **queries** (questions) and the system searches for answers. Prolog is the best-known logic language.

### Video (8 min)

**[Programming Epitome] Prolog Programming Basics: Facts, Rules and Queries** (7:57)
https://www.youtube.com/watch?v=4F2FLNQ6yms

Watch for: how a fact, a rule and a query look, and how Prolog finds the answers by itself.

### Run it: a family tree in Prolog (4 min)

1. Open SWISH: https://swish.swi-prolog.org/ (free, runs in your browser, no account needed to run queries). If it shows a welcome page, choose to create a new Prolog program.
2. Paste this program into the editor (the main text area).

```prolog
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

ancestor(X, Z) :- parent(X, Z).
ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).
```

`:-` means "is true if". Names starting with a capital letter (X, Y, Z) are variables. Every line ends with a full stop.

3. In the query box at the bottom right, type `grandparent(tom, Who).` and click **Run!**. You should see `Who = ann`, then use **Next** to see `Who = pat`.
4. Now run `ancestor(tom, Who).` and click **Next** to see every answer. Notice you did not write any search steps. Prolog found the answers itself.

### The same idea in Python (1 min)

Facts are a set of tuples. Rules are functions. Queries are function calls. Run this with `python -I` or in PyCharm.

```python
# Facts: (parent, child)
parent_facts = {
    ("tom", "bob"),
    ("tom", "liz"),
    ("bob", "ann"),
    ("bob", "pat"),
}


# Rules
def is_parent(x, y):
    return (x, y) in parent_facts


def children(x):
    return sorted([c for (p, c) in parent_facts if p == x])


def is_sibling(a, b):
    if a == b:
        return False
    for (p, child) in parent_facts:
        if child == a and is_parent(p, b):
            return True
    return False


# Queries
print(is_parent("tom", "bob"))    # True
print(children("tom"))            # ['bob', 'liz']
print(is_sibling("ann", "pat"))   # True
print(is_sibling("ann", "liz"))   # False
```

In Prolog you write the rule once and the system does the searching. In Python you write the search yourself with a `for` loop. Python is not a logic language, but you can copy the idea.

::::::::::::::::::::::::::::::::::::: challenge

## Activity (15 min)

Use the Python code above as your starting point.

1. Add the fact that `liz` is the parent of `joe`.
2. Write a rule `is_grandparent(x, z)` that returns `True` or `False`. Loop over `parent_facts`, use `is_parent`, and keep it **pure** (no printing, no changing `parent_facts`).
3. Write a **recursive** rule `is_ancestor(x, z)`. An ancestor is a parent, or a parent of an ancestor. Hint: return `True` straight away if `x` is a parent of `z`. Otherwise use a `for` loop over the facts, and for each child `y` of `x`, ask `is_ancestor(y, z)`. If nothing works, return `False`.
4. Test: is `tom` an ancestor of `ann`? Of `joe`? Is `ann` an ancestor of `tom`?
5. In one or two sentences: which parts of your answer are functional, and which are logic-style?

:::::::::::::::: solution

## Model answer

```python
parent_facts = {
    ("tom", "bob"),
    ("tom", "liz"),
    ("bob", "ann"),
    ("bob", "pat"),
    ("liz", "joe"),   # new fact
}


def is_parent(x, y):
    return (x, y) in parent_facts


def is_grandparent(x, z):
    for (p, y) in parent_facts:
        if p == x and is_parent(y, z):
            return True
    return False


def is_ancestor(x, z):
    if is_parent(x, z):                      # base case
        return True
    for (p, y) in parent_facts:              # recursive case
        if p == x and is_ancestor(y, z):
            return True
    return False


print(is_grandparent("tom", "joe"))  # True
print(is_ancestor("tom", "ann"))     # True
print(is_ancestor("tom", "joe"))     # True
print(is_ancestor("ann", "tom"))     # False
```

Note: the rules are pure functions that only read the facts, and `is_ancestor` uses recursion, so they are functional. The facts-rules-queries layout is logic-style, but Python needs us to write the search ourselves, whereas Prolog does it for us.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Further reading

- Programming Epitome (n.d.) *Prolog Programming Basics: Facts, Rules and Queries* [Video]. YouTube. Available at: https://www.youtube.com/watch?v=4F2FLNQ6yms (Accessed: 2 November 2026).
- Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Accessed: 2 November 2026).

:::::::::::::::::::::::::::::::::::::: keypoints

- A pure function has no side effects.
- Recursion solves a problem by calling the function on a smaller problem.
- Logic programming states facts and rules, then asks questions.

::::::::::::::::::::::::::::::::::::::::::::::::
