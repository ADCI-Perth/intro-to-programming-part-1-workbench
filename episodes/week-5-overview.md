---
title: 'Week 5: Object-oriented programming and files'
teaching: 84
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 5?
- How should I spend my time this week?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your Week 5 study time using the time plan.
- Find the videos, sections, Concepts Bridge and practice task for the week.

::::::::::::::::::::::::::::::::::::::::::::::::

**Theme:** build your own types with classes, then save data to files.

By the end of this week you will be able to:

- Write a **class** and create several **objects** (instances) from it.
- Use **inheritance** so one class can build on another.
- Read and write text files and JSON files, and handle a missing file with `try/except`.
- Explain in plain words that "everything is an object" in Python, and why `0.1 + 0.2` is not exactly `0.3`.

## Time plan (about 5 h 35 m, within the 6 h cap)

| Block | What | Time |
|---|---|---|
| Watch | 10 videos (below) | 1 h 24 m |
| Read & practise | Section 5.1 Classes and objects; Section 5.2 File handling | 1 h 40 m |
| Concepts Bridge | [Everything is an object, and floating-point risk](week-5-bridge.md) | 30 m |
| Build | [Animal class and mini project Part 1](week-5-practice.md) | 2 h |
| **Total** | | **5 h 34 m** |

The remaining time is a buffer. Use it for the optional Dog step in the Animal task or for the optional material below.

## Watch (1 h 24 m)

Watch these in order. They start with objects, then cover inheritance and operators, then files. Pause and run the code yourself in PyCharm.

| # | Video | Length | What to look for |
|---|---|---|---|
| 1 | [T#48 Object Oriented Programming Intro](https://www.youtube.com/watch?v=gZwPdqC2Os0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 7:02 | Why programmers group data and actions together. |
| 2 | [T#49 Class and Object](https://www.youtube.com/watch?v=8O5kX73OkIY&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:01 | The difference between a class (blueprint) and an object (the thing built from it). |
| 3 | [T#50 `__init__` Method](https://www.youtube.com/watch?v=WIP3-woodlU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:46 | How `__init__` sets up a new object's data. |
| 4 | [T#51 Constructor, Self, Comparing Objects](https://www.youtube.com/watch?v=ic6wdPxcHc0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:04 | What `self` means, and why two objects with the same data are still different objects. |
| 5 | [T#55 Inheritance](https://www.youtube.com/watch?v=Cn7AkDb4pIU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:51 | How a child class reuses its parent's methods. You need this for the Animal task. |
| 6 | [T#57 Introduction to Polymorphism](https://www.youtube.com/watch?v=P1vH3Pfw6BI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 1:46 | One name, many forms. A short idea you will meet again in T#58 and T#59. |
| 7 | [T#58 Duck Typing](https://www.youtube.com/watch?v=CuK0g8OFzwo&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:17 | Python cares what an object can do, not what class it is. |
| 8 | [T#59 Operator Overloading](https://www.youtube.com/watch?v=9wd50TKv_OQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 14:29 | How methods such as `__add__` make `+` work on your own objects. The Bridge builds on this. |
| 9 | [T#65 File Handling](https://www.youtube.com/watch?v=aequTxAvQq4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 12:14 | Opening, reading and writing a file, and closing it safely. |
| 10 | [[Tech With Tim] How To Use JSON In Python](https://www.youtube.com/watch?v=-51jxlQaxyA) | 6:11 | Turning a dictionary into JSON text and back again. You need this for the mini project. |

## Read & practise (1 h 40 m)

Read each lesson with PyCharm open. Type the examples yourself and run them.

### Section 5.1: Classes and objects (about 55 m)

Lesson: [Section 5.1: Classes and Objects](5-1-classes-and-objects.md)

- **Read:** Creating a Class, Creating an Object, Class Constructor, Object Methods, Object Default Methods, Method to Modify Class Default Values, Inheritance, Overriding parent method.
- **Do:** Exercises Level 1. This is the `Statistics` class. Start with `count`, `sum`, `min`, `max`, `range` and `mean`, and stop there if time is short. Add the rest only if you have time.
- The lesson uses `super().__init__(...)` in the Inheritance section. Compare it with the `Dog` class you will write in the Build block.

### Section 5.2: File handling (about 45 m)

Lesson: [Section 5.2: File Handling](5-2-file-handling.md)

- **Read:** Opening Files for Reading, Opening Files for Writing and Updating, Deleting Files, File with txt Extension, and the JSON sections (File with json Extension, Changing JSON to Dictionary, Changing Dictionary to JSON, Saving as JSON File).
- **Skip:** the csv, xlsx and xml sections. You do not need them this week.
- **Do:** Exercises Level 1 (count lines and words in the speeches; find the most spoken languages). Do the first speeches exercise fully and attempt the rest if time allows.

**Where are the files?** The lesson opens files such as `./data/obama_speech.txt` and `./files/reading_file_example.txt`. In this repository they live in [`assets/data/`](data/course-data.zip) and [`assets/files/`](data/course-data.zip) at the top level. If your script sits in `weeks/week-5/`, use paths like `../../assets/data/obama_speech.txt`. Alternatively, copy the file you need next to your script. PyCharm runs a script with its own folder as the working directory, so a copy beside the script is found by just its name.

**PyCharm note:** the lessons were written with VS Code in mind. In PyCharm, right-click your file and choose **Run**, or press the green arrow. Nothing else changes.

## Concepts Bridge (30 m)

[Everything is an object, and floating-point risk](week-5-bridge.md): Part 1 7 m, Part 2 15 m (including the video), activity 8 m. It connects duck typing and operator overloading (T#58, T#59) to `type()`, `id()` and dunder methods. It also explains why `0.1 + 0.2 != 0.3`, and introduces `Decimal`. It includes the [Computerphile] Floating Point Numbers video (9:16).

## Build (2 h)

[Practice tasks](week-5-practice.md):

1. **Animal class** (about 30 minutes): a class and several objects. The `Dog` subclass is an optional stretch (about 15 more minutes).
2. **Mini project, Part 1** (about 90 minutes): a [library loan manager](week-5-practice.md) using classes, a dictionary, try/except and JSON. You finish it in Week 6.

These are practice tasks. They are not graded.

## Optional

Only do these if you have time left. Nothing here is required.

**Videos**

- T#52 Types of Variables
- T#53 Types of Methods
- T#54 Inner Class
- T#56 Constructor in Inheritance
- T#60 Method Overloading and Overriding
- Abstract classes
- [Bro Code] [Learn Python Dates & Times in 6 Minutes](https://www.youtube.com/watch?v=DwBDHsdX6XQ) (6:18), to go with Section 5.3
- [Socratica] [Regular Expressions in Python](https://www.youtube.com/watch?v=nxjwB8up2gI) (13:23), to go with Section 5.4

**Optional lessons**

- [Section 5.3: Python datetime](../learners/5-3-date-time.md)
- [Section 5.4: Regular expressions](../learners/5-4-regular-expressions.md)

**Extra practice**

- A **Currency class using `Decimal`** (working with money safely). Follow on from the Bridge.
- A string-shuffle program (text processing).

**Reading**

- Driscoll, M. (2017) *Python 101*, Chapters 11, 13, 15, 16 and 22. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Accessed: 2 November 2026).

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- The whole week fits in 6 hours or less.

::::::::::::::::::::::::::::::::::::::::::::::::
