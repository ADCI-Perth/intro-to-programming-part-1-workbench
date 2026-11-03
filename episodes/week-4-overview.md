---
title: 'Week 4: Recursion, functional programming and errors'
teaching: 53
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 4?
- How should I spend my time this week?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your Week 4 study time using the time plan.
- Find the videos, sections, Concepts Bridge and practice task for the week.

::::::::::::::::::::::::::::::::::::::::::::::::

**Theme:** write smaller, cleaner code with functions and comprehensions, and stop your programs from crashing when something goes wrong.

## What you will be able to do by the end of this week

- Explain recursion (a function that calls itself) and write a simple recursive function.
- Use list comprehensions, `lambda`, `map()` and `filter()` to transform and select data.
- Read a Python error message and name the type of error.
- Use `try` / `except` to handle bad input without crashing.

## Time plan (about 5 h 25 min)

| Block | What you do | Time |
|---|---|---|
| Watch | 6 core videos | 53 min |
| Read & practise | Sections 4.1, 4.2, 4.3 and 4.4, plus exercises | 2 h |
| Concepts Bridge | Pure functions, side effects, recursion and logic programming | 30 min |
| Build | Practice task: functional rewrite of a grade calculator | 2 h |
| **Total** | | **5 h 23 min** |

Suggested split for Read & practise: Section 4.1 (35 min), Section 4.2 (40 min), Section 4.3 (30 min), Section 4.4 (15 min).

The week totals less than 6 h on purpose. Use any spare time to repeat exercises you found hard, or try the optional material.

If your teacher runs an optional one-hour online drop-in or Q&A, it counts inside the Read & practise time.

---

## 1. Watch (53 min)

Watch these in order. Pause and try the code yourself in PyCharm. "T#" videos come from the Telusko *Python for Beginners (Full Course)* playlist.

| # | Video | Length | Link | Look for |
|---|---|---|---|---|
| 1 | T#40 Recursion | 5:43 | https://www.youtube.com/watch?v=XkL3SUioNvo&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 | What a function does when it calls itself. |
| 2 | T#41 Factorial using Recursion | 4:57 | https://www.youtube.com/watch?v=TqqQld6m6A0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 | The "stop" case (base case) that ends the calls. |
| 3 | T#42 Anonymous Functions, Lambda | 4:38 | https://www.youtube.com/watch?v=hYzwCsKGRrg&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 | How a one-line `lambda` replaces a short `def`. |
| 4 | T#43 Filter Map Reduce | 11:34 | https://www.youtube.com/watch?v=kj850Y8y8FI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 | What `map` (change every item) and `filter` (keep some items) each give back. |
| 5 | [Bro Code] Learn Python List Comprehensions in 10 Minutes | 10:20 | https://www.youtube.com/watch?v=YlY2g2xrl6Q | The pattern `[expression for item in list if condition]`. |
| 6 | T#63 Exception Handling | 15:59 | https://www.youtube.com/watch?v=6SPDvPK38tw&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 | Which code goes in `try` and which in `except`. |

**Total: about 53 min.**

---

## 2. Read & practise (2 h)

Open each lesson, read it, type the examples into PyCharm and run them. Then do the exercises.

### Section 4.1: List comprehension and lambda (about 35 min)

- Lesson: [Section 4.1](4-1-list-comprehension.md)
- Read all of it: list comprehension first, then lambda functions.
- This lesson has no levels. Do exercises 1 to 6 at the end. Exercises 1, 2 and 5 are the easiest, so start there.

### Section 4.2: Higher-order functions (about 40 min)

- Lesson: [Section 4.2](4-2-higher-order-functions.md)
- Read "Higher Order Functions" (functions as parameters and return values), "Python Closures" (a function that remembers values from the function around it), and "Built-in Higher Order Functions" (map, filter, reduce).
- **Skip** "Python Decorators". They are optional (see below).
- Type the closure example into PyCharm and run it. Then change `ten` to another number and predict the output before you run it again.
- Do the Level 1 exercises.
- Some Level 2 and 3 exercises use country data. The data files are in [assets/data](data/course-data.zip) (see `countries.py` and `countries-data.py`). The lesson's `data/...` paths mean this folder.

### Section 4.3: Error types (about 30 min)

- Lesson: [Section 4.3](4-3-error-types.md)
- Read all of it. Each section shows one kind of error, such as `NameError` or `ValueError`.
- The one exercise is to try every example yourself. In PyCharm, use the **Python Console** tab at the bottom. Note the name of each error you see.

### Section 4.4: Exception handling (about 15 min)

- Lesson: [Section 4.4](4-4-exception-handling.md)
- Core: read **only the "Exception Handling" section** (the `try` / `except` part).
- **Skip** packing and unpacking, spreading, enumerate and zip for now. They are optional.
- The lesson's exercise is about unpacking, so skip it. Write your own instead. Ask for a number with `input()`, convert it with `int()`, and print a friendly message in an `except ValueError` block if the text is not a number.

> **PyCharm note:** the lessons were written with VS Code in mind. In PyCharm, right-click a file and choose **Run**, or use the Python Console for short tests.

---

## 3. Concepts Bridge (30 min)

Pure functions, side effects, recursion, and a first look at logic programming with a short Prolog video.

- [Open the Week 4 Bridge](week-4-bridge.md)

---

## 4. Build (2 h)

Rewrite part of a grade calculator in a functional style, and add `try` / `except` checks for bad input.

- [Open the Week 4 practice task](week-4-practice.md)

---

## Optional (not required)

Only do these if you have time left after the core work.

**Videos**
- T#44 Decorators (Telusko)
- Zip function (Telusko)
- T#61 Iterators (Telusko)
- T#62 Generators (Telusko)

**Lesson sections**
- Section 4.2: decorators.
- Section 4.4: packing and unpacking, spreading, enumerate and zip.

**Reading**
- Driscoll, M. (2017) *Python 101*, chapters 7, 25 and 26. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/

---

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- The whole week fits in 6 hours or less.

::::::::::::::::::::::::::::::::::::::::::::::::
