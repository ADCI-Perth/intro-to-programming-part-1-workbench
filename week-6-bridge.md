---
title: 'Week 6 Concepts Bridge: Type Safety, Library Risk and Choosing a Paradigm'
teaching: 20
exercises: 10
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I use packages safely?
- How do I choose a paradigm for a problem?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Add type hints to a function.
- Describe the risks of third-party libraries.
- Compare paradigms using a set of criteria.

::::::::::::::::::::::::::::::::::::::::::::::::

**Time: 30 minutes.** Video 11 min (Indently, 11:25), reading 10 min, activity 9 min.

## Why this matters

Choosing approaches and tools means knowing the risks of third-party libraries, and understanding type safety and memory safety. The lessons this week show how to *use* packages. This note shows how to use them *safely*, then gives you a table of criteria for LO 4: judging which paradigm best suits a problem.

## 1. Type safety

A **type** says what kind of value you have: a whole number (`int`), text (`str`) and so on. **Type safety** means the language or its tools stop you using a value the wrong way.

Python checks types only while the program runs. This is called **dynamic typing**. A mistake can hide until the exact line runs:

```python
def double(x):
    return x * 2

print(double(4))
print(double("ha"))
```

Both lines work, but the second gives `haha`, which you may not have wanted. A **type hint** (or type annotation) tells readers, and checking tools, what you expect:

```python
def double(x: int) -> int:
    return x * 2

print(double(4))
```

`x: int` means "x should be an int". `-> int` means "this function returns an int". Python itself ignores hints when it runs. They are notes for people and tools.

A tool called **mypy** reads the hints and warns you *before* you run the code. This is **static type checking**. It is a third-party package, so install it with pip first (inside your virtual environment):

```
python -m pip install mypy
```

Now save this as `bad_types.py`:

```python
def double(x: int) -> int:
    return x * 2

double("ha")
```

Then run mypy:

```
python -m mypy bad_types.py
```

Mypy reports an error like `Argument 1 to "double" has incompatible type "str"; expected "int"`. The code still runs in plain Python, but mypy caught the likely mistake early. You do not need mypy to finish this course. The commands are here so you know what it does.

### Watch

**[Indently]** A Quick Guide to Type Annotations (ft. Mypy) (11:25): https://www.youtube.com/watch?v=Y9fT4HVdCuQ

Look for: how to hint a function, a list (`list[int]`) and a value that might be `None`.

## 2. Third-party library risk

Every package you install is code written by a stranger. It runs with your permissions. Two simple habits lower the risk.

**Pin versions.** A **version** is a number such as `2.34.2`. If you ask for "the latest" `requests`, you may get a different version next month, and it might break your program or contain a new bug. **Pinning** means asking for one exact version. Record pins in a file called `requirements.txt`:

```
requests==2.34.2
```

`==` means "exactly this version". Anyone can then rebuild your setup with:

```
python -m pip install -r requirements.txt
```

You can create the file from your current environment with `python -m pip freeze > requirements.txt`. Pinning also gives you a calm moment to read what changed before you update. Pinning an old version is not automatically safe: `requests` 2.32.5, for example, has a known security advisory (CVE-2026-25645) fixed in 2.33.0. Check for security advisories before you pin (run `python -m pip install pip-audit` then `python -m pip_audit`, or read the package's GitHub "Security" page), and update your pins regularly.

**Watch out for look-alike packages.** Attackers upload packages with names close to popular ones. This is **typosquatting**: they rely on a typing slip. For example, `reqeusts` or `python-requests` instead of `requests`. Such a package may steal passwords or files when you install or import it. Before you install:

- Copy the exact name from the official documentation. Do not type it from memory.
- Check the package page on pypi.org: its age, download numbers, and project links.
- Be wary of tiny, brand-new packages with names that nearly match a famous one.
- Install only what you need.

## 3. Memory safety

A **memory-safe** language stops code from reading or writing memory it does not own. Python checks every list position and frees unused memory for you, while C leaves that work to the programmer, which is faster but allows bugs such as buffer overflows. (Optional: **[Low Level]** How Can Memory-Safe Code Stop Hackers? 7:43, https://www.youtube.com/watch?v=lxUYZVX_FjQ.)

## 4. Choosing a paradigm (LO 4)

A **paradigm** is a style of programming. Python supports the four you have met in this course. No style is best everywhere. Judge a problem against the same criteria each time:

| Criterion | Imperative | Object-oriented | Functional | Logic |
|---|---|---|---|---|
| **State and data flow** | Step-by-step commands change variables. | Data and the methods that change it live together in objects. | Functions take values in and return new values. Data is not changed. | You state facts and rules. The system works out the answers. |
| **Fits when** | The job is a short, clear sequence of steps. | You model many things that each have their own changing state. | You transform data through stages (filter, map, calculate). | The problem is about relationships and rules, such as "who is related to whom". |
| **Testability** | Fair: tests must set up and check shared variables. | Good if each object is small. Tests must build objects in the right state first. | Best: same input always gives the same output, with nothing to set up. | Good for the rules themselves. Tracing why an answer appeared can be hard. |
| **Example in this course** | Week 3 grade calculator (loops and if statements). | Week 5 library (`Book` and `Library` classes). | Week 4 rewrite of the grade calculator (`map`, `filter`, small functions). | Week 4 family tree (facts and rules about parents). |

Real programs mix styles. The Week 6 library is object-oriented overall, but its `search` is a functional list comprehension. When you judge a problem, ask: where does the state live, how easy is each part to test, and does the problem look like steps, things, transformations or rules?

::::::::::::::::::::::::::::::::::::: challenge

## Activity (about 8 minutes)

1. Take this function and add type hints to the parameters and the return value:

   ```python
   def full_name(first, last):
       return first + " " + last
   ```

2. Add a `requirements.txt` line that pins `requests` to version `2.34.2`.
3. Write one sentence: which of the names `requests`, `reqeusts`, `request` would you check carefully on pypi.org before installing, and why?
4. Using the table in section 4, name the paradigm you would pick for a program that works out "who is a grandparent of whom" from a list of parent facts, and give one reason.

:::::::::::::::: solution

## Model answer

1. ```python
   def full_name(first: str, last: str) -> str:
       return first + " " + last

   print(full_name("Ada", "Lovelace"))
   ```
2. `requests==2.34.2`
3. All three need checking, but `reqeusts` (a typo) and `request` (a different, similar package) are the risky ones. Copying the name from the official docs avoids typosquatting.
4. Logic programming, as in the Week 4 family tree: you state parent facts and one grandparent rule, and the system finds every answer. An imperative version would need nested loops that are harder to read and extend.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Further reading

- Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (accessed 2 November 2026).
- Romano, F. (2018) *Learn Python Programming*, 2nd edn. Birmingham: Packt Publishing.
- Indently (no date) *A quick guide to type annotations (ft. Mypy)* [Video]. Available at: https://www.youtube.com/watch?v=Y9fT4HVdCuQ (accessed 2 November 2026).

:::::::::::::::::::::::::::::::::::::: keypoints

- Type hints document intent and let tools find mistakes.
- Pin versions and check package names before installing.
- No paradigm is best everywhere: judge each problem against the same criteria.

::::::::::::::::::::::::::::::::::::::::::::::::
