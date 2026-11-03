---
title: 'Week 3: Control flow and functions'
teaching: 82
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 3?
- How should I spend my time this week?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your Week 3 study time using the time plan.
- Find the videos, sections, Concepts Bridge and practice task for the week.

::::::::::::::::::::::::::::::::::::::::::::::::

This week your programs start to make decisions, repeat steps and reuse code. These ideas are the heart of programming.

## Learning goals

By the end of this week you can:

- make a program choose between actions with `if`, `elif` and `else`;
- repeat steps with `while` and `for` loops, and stop or skip with `break` and `continue`;
- write your own functions that take values and return a result;
- plan a solution in pseudocode, write a simple sorting method yourself, and trace it in the PyCharm debugger.

## Time plan (6 hours)

| Block | Time | What you do |
|---|---|---|
| Watch | 1 h 22 m | 8 short videos |
| Read & practise | 2 h 8 m | Sections 3.1, 3.2 and 3.3, with Level 1 exercises |
| Concepts Bridge | 0.5 h | [Problem solving and sorting](week-3-bridge.md) |
| Build | 2 h | [Grade calculator](week-3-practice.md) |
| **Total** | **6 h** | |

Read & practise includes an optional 1 h online drop-in or Q&A session. Do the Watch block first, then read, then bridge, then build. You can mix videos and reading by day: for example, watch T#19 and then read Section 3.1.

## Watch (1 h 22 m)

All links open in the Telusko *Python for Beginners (Full Course)* playlist.

| # | Video | Length | Look for |
|---|---|---|---|
| T#19 | [If Elif Else Statement](https://www.youtube.com/watch?v=PqFKRqpHrjw&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 15:38 | How Python picks one branch, and why the indentation matters |
| T#20 | [While Loop](https://www.youtube.com/watch?v=HZARImviDxg&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 12:43 | The condition is checked before every repeat |
| T#21 | [For Loop](https://www.youtube.com/watch?v=0ZvaDa8eT5s&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 7:27 | Looping over a list and over `range()` |
| T#22 | [Break Continue Pass](https://www.youtube.com/watch?v=yCZBnjF4_tU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 10:20 | What each keyword does to a loop |
| T#32 | [Functions in Python](https://www.youtube.com/watch?v=BVfCWuca9nw&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:13 | How to define a function with `def` and call it |
| T#33 | [Function Arguments](https://www.youtube.com/watch?v=ijXMGpoMkhQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 7:52 | Passing values in, and getting a value back with `return` |
| T#34 | [Types of Arguments](https://www.youtube.com/watch?v=eci9iU_s6Ag&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 9:55 | Positional, keyword and default arguments |
| T#70 | [Bubble Sort](https://www.youtube.com/watch?v=Vca808JTbI8&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 7:21 | How neighbouring values are compared and swapped. You will trace this in the Bridge. |

## Read & practise (2 h 8 m)

Read each lesson, type and run every example in PyCharm, then do the Level 1 exercises. Create one `.py` file per section, such as `section_3_1.py`. Where a lesson says to use VS Code, use PyCharm instead: **File > New > Python File**, then click the green arrow to run.

| Lesson | Read | Level 1 exercises |
|---|---|---|
| [Conditionals](3-1-conditionals.md) | All sections. Short Hand and Nested Conditions can be a quick skim. | 1 to 3 |
| [Loops](3-2-loops.md) | While Loop, Break and Continue, For Loop, The Range Function, Nested For Loop. Skim For Else and Pass. | 1 to 8 |
| [Functions](3-3-functions.md) | Everything down to "Function with Default Parameters". Skim the arbitrary-arguments and dictionary-unpacking sections. | 1, 2, 4, 5, 8, 9, 11, 13 |

Notes:

- Section 3.3 exercise 3 asks you to check types. Skip that part; just add up the numbers.
- Section 3.2 Level 2 and 3 use files from the `data` folder (`countries.py`, `countries-data.py`). In this course they are in [assets/data](data/course-data.zip). They are optional extras.
- Section 6.1 (modules) is taught in Week 6.

## Concepts Bridge (0.5 h)

[Bridge: solving problems and sorting](week-3-bridge.md). Learn the understand, pseudocode, code, test process. Then write bubble sort yourself from pseudocode, trace it in the PyCharm debugger, and compare it with Python's `sorted()`.

## Build (2 h)

[Practice task: grade calculator](week-3-practice.md). Enter marks, store them, and report the average and a grade, using functions and `if`/`elif`. Write short pseudocode first. This task is for practice and is not marked.

## Optional

Only if you have time. Nothing here is needed to finish the week.

**Videos (Telusko)**

- T#22.1 Break vs continue vs pass
- T#23 Printing patterns
- T#24 For-else
- T#25 Prime numbers
- T#35 `**kwargs`
- T#36 Global vs local
- T#37 Pass list to function
- T#38 Fibonacci
- T#39 Factorial
- T#68 Linear search
- T#69 Binary search
- T#71 Selection sort

Find these in the [playlist](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3).

**Lessons**

- [Section 6.1: Modules](6-1-modules.md) (taught in Week 6)

**Reading**

- Driscoll, M. (2017) *Python 101*, Chapters 4 to 6 and 10. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/

## Next week

[Week 4](week-4-overview.md) covers recursion, functional programming and error handling. You will rewrite a similar grade calculator in a functional style. Week 4's task is self-contained, so you do not need your Week 3 files.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- The whole week fits in 6 hours or less.

::::::::::::::::::::::::::::::::::::::::::::::::
