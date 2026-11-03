---
title: 'Week 1: Getting started: how programs run, values and operators'
teaching: 82
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 1?
- How should I spend my time this week?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your Week 1 study time using the time plan.
- Find the videos, sections, Concepts Bridge and practice task for the week.

::::::::::::::::::::::::::::::::::::::::::::::::

**Theme:** how a Python program runs, and the building blocks you use in every program: values, variables and operators.


## What you will be able to do this week

- Install Python and PyCharm, then write, run and debug a short script.
- Store values in variables and name the basic data types (numbers, text, true/false).
- Use arithmetic, comparison and logical operators.
- Explain, in plain words, how Python code becomes something a computer can run.

## Time plan (under 6 hours)

| Block | What you do | Time |
|---|---|---|
| Watch | 8 short videos | 1 h 22 m |
| Read & practise | Sections 1.1, 1.2 and 1.3, with the assigned exercises | 2 h 4 m |
| Concepts Bridge | [How code runs](week-1-bridge.md) | 0.5 h |
| Build | [Practice task](week-1-practice.md) | 2 h |
| **Total** | | **5 h 56 m** |

Suggested order: watch a video, then read the matching lesson, then try the code yourself in PyCharm. Do the Bridge and Build blocks last.

## Watch (1 h 22 m)

Watch in this order. Each link opens inside the Telusko playlist. **T#n** means "Telusko video number n".

| # | Video | Length | Look for |
|---|---|---|---|
| 1 | [T#1 Introduction to Python](https://www.youtube.com/watch?v=hEgO047GxaQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 4:13 | What Python is and what people use it for. |
| 2 | [T#2 Python Installation, PyCharm](https://www.youtube.com/watch?v=CScxy0294SE&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 9:33 | The steps to install Python and PyCharm. See the PyCharm note below. |
| 3 | [T#3 Getting Started with Python](https://www.youtube.com/watch?v=DWgzHbglNIo&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 14:49 | How to write and run your first line with `print()`. |
| 4 | [T#16 Working with PyCharm: Run, Debug, Trace](https://www.youtube.com/watch?v=akcEaEH91gI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 10:26 | How to run a file, and how to pause it line by line to see what happens. |
| 5 | [T#4 Variables in Python](https://www.youtube.com/watch?v=TqPzwenhMj0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 10:22 | A variable is a name that points to a value. |
| 6 | [T#10 Data Types in Python](https://www.youtube.com/watch?v=gCCVsvgR2KU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 14:35 | The main types: `int`, `float`, `str`, `bool`. |
| 7 | [T#11 Operators in Python](https://www.youtube.com/watch?v=v5MR5JnKcZI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:07 | What `+`, `-`, `*`, `/`, `//`, `%` and `**` each do. |
| 8 | [T#67 Is Python Compiled or Interpreted?](https://www.youtube.com/watch?v=0BhSWyDEDC4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:48 | The difference between compiling and interpreting. The Bridge builds on this. |

**Video total: 1 h 22 m.**

### PyCharm note

T#2 was recorded before 2025. The PyCharm download page now looks different: there is **one** PyCharm download, with no "Community" or "Professional" choice. Install it and carry on with the free core features. This course uses PyCharm for everything.

## Read & practise (2 h 4 m)

Read each lesson, type the examples into PyCharm and run them. Then do the exercises in the table below (about 3 minutes each). Skip Level 2 and Level 3 unless you have time left over.

Each time includes reading the lesson plus about 3 minutes for each assigned exercise. Total: 35 + 40 + 49 = 124 minutes (2 h 4 m).

**Where is the data?** Some lessons open files such as `data/...` or `files/...`. These live in `assets/data/` and `assets/files/` at the root of this repository. You will not need them this week.

| Lesson | Time | Read | Exercises |
|---|---|---|---|
| [Section 1.1: Introduction](1-1-introduction.md) | about 35 min | Everything except the VS Code section (see below). | Level 1 |
| [Section 1.2: Variables and built-in functions](1-2-variables.md) | about 40 min | All of it. | Level 1, exercises 1 to 7. |
| [Section 1.3: Operators](1-3-operators.md) | about 49 min | All of it. | The Section 1.3 exercises (the page has one list, not levels). Do exercises 1 to 11, then 17 to 22 if time allows. |

### Section 1.1 uses VS Code. Use PyCharm instead.

The Section 1.1 lesson shows how to set up **Visual Studio Code**. You do not need it. Skip the section called **"Installing Visual Studio Code"** and its sub-section **"How to use visual studio code"**. Use PyCharm instead:

1. Open PyCharm and choose **New Project**.
2. Name the project `IntroToProgramming` (or any name you like).
3. Right-click the project name, choose **New > Python File** and call it `helloworld`.
4. Type `print("Hello, World!")` and click the green **Run** arrow.

Everything else in Section 1.1 (the Python shell, syntax, comments, data types) works the same in PyCharm.

If a lesson asks you to make a folder such as `section_1_2`, make it inside your PyCharm project. Right-click the project name, then choose **New > Directory**.

## Concepts Bridge (0.5 h)

Open [bridge.md](week-1-bridge.md). It explains how code runs: machine code, assembly, compilers and interpreters. You compare "Hello World" in C, Java and assembly with Python. It builds on video T#67.

## Build (2 h)

Open the [practice task](week-1-practice.md). You write a small unit converter, then write five sentences comparing Python's "Hello World" with another language. This is practice only. It is not marked.

## Optional

Nothing here is required. Try these if you want more.

**Videos**

- T#9 More on variables
- T#12 Number system conversion
- T#14 Bitwise operators
- T#15 Math functions
- T#17 Swap two variables
- [Max Rohowsky] [PyCharm Tutorial: Basics in 10 Minutes](https://www.youtube.com/watch?v=HHcZbXsZtm0) (10:00)

Find the Telusko videos by number in the [playlist](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3).

**Reading**

- Section 1.1, 1.2 and 1.3: the Level 2 and Level 3 exercises.
- Section 1.2, Level 1, exercises 8 to 13. These are six one-line variable declarations (age, year, true/false values and several variables on one line). Do them if you want extra practice.
- Driscoll, M. (2017) *Python 101*, chapters 1 and 3. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/
- Romano, F. (2018) *Learn Python Programming*, 2nd edn, chapter 1. Birmingham: Packt.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- The whole week fits in 6 hours or less.

::::::::::::::::::::::::::::::::::::::::::::::::
