---
title: 'Week 5 Concepts Bridge: Everything Is an Object, and Floating-Point Risk'
teaching: 20
exercises: 10
---

:::::::::::::::::::::::::::::::::::::: questions

- What does "everything is an object" mean?
- Why is 0.1 + 0.2 not exactly 0.3?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Use type(), id() and dunder methods to inspect objects.
- Explain floating-point error and use Decimal for money.

::::::::::::::::::::::::::::::::::::::::::::::::

**Time: 30 minutes.** Part 1: 7 minutes. Part 2: 15 minutes (the 9:16 video plus about 5 minutes of reading and running the code). Activity: 8 minutes.

## Why this matters

Object-oriented programming in Python starts from one idea: "everything is an object". Working with numbers safely means knowing about floating-point problems such as the Ariane 5 failure. Both support LO 2 (apply object-oriented techniques) and LO 3 (build to a specification, which includes knowing where your numbers can go wrong).

## Part 1: Everything is an object (about 7 minutes)

An **object** is a piece of data bundled with the actions (methods) that work on it. This week you built your own objects with `class`. Here is the surprise: Python's built-in values are objects too. Whole numbers, strings, lists and even functions are all objects.

Two built-in functions let you look inside:

- `type(x)` tells you which class an object was made from.
- `id(x)` gives a number that identifies that one object while the program runs. Two different objects never share an id at the same time.

```python
print(type(42))
print(type("hello"))
print(type([1, 2, 3]))
print(type(len))

class Dog:
    pass

rex = Dog()
print(type(rex))
print(type(Dog))          # even a class is an object

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)             # same contents?
print(a is b)             # same object?
print(a is c)             # c is just another name for a
print(id(a) == id(c))
print((42).bit_length())  # a whole number has methods
```

Run it and read the output. A list has methods like `.append()` because it is an object of the `list` class. A whole number has methods such as `.bit_length()` for the same reason.

### Duck typing and dunder methods

In T#58 you met **duck typing**: if an object has the method you need, Python does not care what class it is. The saying is "if it walks like a duck and quacks like a duck, it is a duck".

In T#59 you met **operator overloading**. The link between the two is the **dunder method**. "Dunder" is short for "double underscore", such as `__init__` or `__add__`. Python calls these special methods behind the scenes:

| You write | Python actually calls |
|---|---|
| `len(x)` | `x.__len__()` |
| `a + b` | `a.__add__(b)` |
| `str(x)` and `print(x)` | `x.__str__()` |
| `a == b` | `a.__eq__(b)` |

That is why `+` works on numbers, strings and lists: each class defines its own `__add__`. It is also why your own class can use `len()` or `+` once you define the right dunder method.

```python
print(3 + 4)
print("3" + "4")
print([3] + [4])
print((3).__add__(4))       # exactly what 3 + 4 does

class Basket:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return Basket(self.items + other.items)

    def __str__(self):
        return "Basket with " + ", ".join(self.items)

mine = Basket(["apple", "pear"])
yours = Basket(["plum"])
print(len(mine))            # works because of __len__
print(mine + yours)         # works because of __add__ and __str__
```

`Basket` and `list` are different classes, yet `len()` works on both. That is duck typing again: `len()` only asks "do you have `__len__`?".

**Optional, if you have time later:** Driscoll (2017) Chapter 11, "Classes" (<https://web.archive.org/web/20260308142225/https://python101.pythonlibrary.org/chapter11_classes.html>). It is not part of the 30 minutes.

## Part 2: Floating-point risk (about 15 minutes)

### Watch first (9:16, about 10 minutes with pauses)

**[Computerphile] Floating Point Numbers (9:16)** — <https://www.youtube.com/watch?v=PZRI1IfStY0>

Look for how a computer stores a number using a fixed number of binary digits, and why some decimal numbers cannot be stored exactly.

### Why `0.1 + 0.2 != 0.3`

Computers store numbers in binary (base 2). In the decimal system you cannot write one third exactly (0.3333...). In binary, you cannot write one tenth exactly. Python's `float` type stores the closest value it can fit, so tiny errors creep in.

```python
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")       # see the real stored value of 0.1
print(round(0.1 + 0.2, 2) == 0.3)
```

The first line prints `0.30000000000000004`. The comparison is `False`. This is not a Python bug. Almost every language that uses standard floating-point numbers behaves this way.

Two safe habits:

1. Never compare floats with `==`. Compare with a tolerance, such as `math.isclose(a, b)`.
2. For money, use whole cents (integers) or the `Decimal` type.

```python
import math
print(math.isclose(0.1 + 0.2, 0.3))
```

### The `Decimal` type

`decimal.Decimal` stores numbers as decimal digits, so 0.1 really is 0.1. It is slower than `float`, but exact for the sums people do by hand. Always create a `Decimal` from a **string**. If you pass a float, the float's error comes along too.

```python
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal(0.1))        # the float's error is copied in
print(Decimal("19.95") * 3)
```

### Case study: Ariane 5 (1996)

On 4 June 1996 the first Ariane 5 rocket broke up about 37 seconds after launch. Software reused from Ariane 4 tried to convert a 64-bit floating-point value into a 16-bit signed whole number. The faster Ariane 5 produced a value too big to fit, the overflow stopped the inertial reference system computers (both the primary and the backup), and the rocket lost its guidance data. Number types have limits, so check that a value fits before you convert it (Lions, 1996).

## Activity (about 8 minutes)

1. Without running it, predict the output of each line:
   ```python
   print(0.1 * 3)
   print(0.1 * 3 == 0.3)
   print(type(0.1 * 3))
   print(type(Decimal("0.1") * 3))
   ```
   Then run it (add `from decimal import Decimal` at the top) and check your predictions.
2. A shop sells an item for 0.10 dollars. Add up the price 10 times in a loop using a `float`, then using a `Decimal`. Compare each total with `1`. What do you notice?
3. In two sentences, explain to a classmate why `len("abc")` and `len([1, 2])` both work. Use the words "object" and "dunder method".

### Model answer

1. Predictions: `0.30000000000000004`, `False`, `<class 'float'>`, `<class 'decimal.Decimal'>`.
2. The `float` total is `0.9999999999999999`, so `total == 1` is `False`. The `Decimal` total is exactly `1.0`, so the comparison is `True`.
3. Strings and lists are both objects, and each of their classes defines a `__len__` dunder method. `len()` simply calls `__len__` on whatever object it is given, which is duck typing.

Working code for questions 1 and 2:

```python
from decimal import Decimal

print(0.1 * 3)
print(0.1 * 3 == 0.3)
print(type(0.1 * 3))
print(type(Decimal("0.1") * 3))

float_total = 0.0
decimal_total = Decimal("0")
for _ in range(10):
    float_total += 0.1
    decimal_total += Decimal("0.1")

print(float_total, float_total == 1)
print(decimal_total, decimal_total == 1)
```

## Reference

- Lions, J.L. (1996) *Ariane 5 Flight 501 Failure: Report by the Inquiry Board*. Paris: European Space Agency.

:::::::::::::::::::::::::::::::::::::: keypoints

- Every value in Python is an object with a type and methods.
- Floats are approximations; use Decimal when exact values matter.

::::::::::::::::::::::::::::::::::::::::::::::::
