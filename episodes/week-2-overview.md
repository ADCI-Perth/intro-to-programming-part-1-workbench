---
title: 'Week 2: Input, strings and data structures'
teaching: 59
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 2?
- How should I spend my time this week?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your Week 2 study time using the time plan.
- Find the videos, sections, Concepts Bridge and practice task for the week.

::::::::::::::::::::::::::::::::::::::::::::::::

**Theme:** getting text and numbers into a program, and storing groups of values.


## What you will be able to do

By the end of this week you can:

- Ask the user for input with `input()` and tidy the text with string methods.
- Create, change and slice lists, tuples, sets and dictionaries.
- Explain how lists, tuples, sets and dictionaries differ, and pick the right one.
- Build a small phone-book program using a dictionary of lists.

## Time plan (6 hours)

| Block | Time | What you do |
|---|---|---|
| Watch | 59 min | Five core videos |
| Read & practise | 2 h 31 min | Sections 2.1 to 2.5, with exercises |
| Concepts Bridge | 30 min | Choosing the right structure |
| Build | 2 h | Phone-book practice task |
| **Total** | **6 h** | |

Aim to finish the week in order: Watch, Read & practise, Bridge, Build. You can mix Watch and Read & practise by topic if you prefer. Watch the strings video, then read Section 2.1, and so on.

## Watch (59 minutes)

Pause often and type along in PyCharm.

| # | Video | Length | Look for |
|---|---|---|---|
| 1 | **T#18** [User Input in Python](https://www.youtube.com/watch?v=4OX49nLNPEE&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 11:59 | `input()` always gives you text (a string), even when you type a number. |
| 2 | **[Programming with Mosh]** [How to Use Strings in Python](https://www.youtube.com/watch?v=Ctqi5Y4X-jA) | 16:46 | Indexing, slicing, and methods such as `upper()` and `replace()`. |
| 3 | **T#5** [List in Python](https://www.youtube.com/watch?v=Eaz5e6M8tL4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 10:42 | How to add, remove and change list items. |
| 4 | **T#6** [Tuple, Set in Python](https://www.youtube.com/watch?v=Mf7eFtbVxFM&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 6:41 | A tuple cannot change. A set has no repeats. |
| 5 | **Telusko** [Dictionary in Python](https://www.youtube.com/watch?v=2IsF7DEtVjg&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) | 12:24 | Keys and values, and how to look a value up by its key. |

The five videos add up to 58 min 32 s, shown as 59 min.

## Read & practise (2 h 31 min)

Read each lesson and run the examples in PyCharm. Then do the exercises. The lessons were written for VS Code. In PyCharm, create a new Python file, paste the example and click **Run**.

| Lesson | Time | Read | Exercises |
|---|---|---|---|
| [Section 2.1: Strings](2-1-strings.md) | 33 min | About 21 min. Read down to "Skipping Characters While Slicing", then skim "String Methods" as a reference. The Mosh video already covers it. | Exercises 1 to 4 (12 min). |
| [Section 2.2: Lists](2-2-lists.md) | 47 min | About 32 min. Whole lesson. | Level 1, exercises 1 to 5 (15 min). |
| [Section 2.3: Tuples](2-3-tuples.md) | 18 min | About 12 min. Whole lesson. | Level 1, exercises 1 and 2 (6 min). |
| [Section 2.4: Sets](2-4-sets.md) | 25 min | About 19 min. Whole lesson. | Level 1, exercises 1 and 2 (6 min). |
| [Section 2.5: Dictionaries](2-5-dictionaries.md) | 28 min | About 19 min. Whole lesson. | Exercises 1 to 3 (9 min). |
| **Total** | **2 h 31 min** | | |

Notes:

- The exercise times assume about 3 minutes per exercise. The Section 2.1 to 2.5 exercises not listed above are Optional (see the end of this page).
- Section 2.1 has no input examples. `input()` is taught in the T#18 video. Try it yourself: `name = input("Your name: ")`, then `print("Hello, " + name)`.
- Section 2.2 mentions a long list of countries in `data/countries.py`. You only need it for Level 2, which is Optional. The file is in `assets/data/` at the top of this repository ([countries.py](data/countries.py)).
- The lessons link to `data/` and `files/` folders. In this course these are `assets/data/` and `assets/files/`.
- Stuck? Join the optional one-hour online drop-in session. If you go, count it inside your Read & practise time.

## Concepts Bridge (30 min)

[Choosing the right structure](week-2-bridge.md): list, tuple, set or dictionary? You work through a six-scenario quiz. It shows how to pick a structure for a job.

## Build (2 h)

[Practice task: phone book](week-2-practice.md). You write a contacts program with a dictionary of lists and user input. It is practice only and has no marks. The folder has a starter file, a model solution and a test file.

## Optional

Not required. Do these only if you have time left over.

**Videos**

- **[Bro Code]** [String Methods in Python](https://www.youtube.com/watch?v=tb6EYiHtcXU) (12:06)
- **[Corey Schafer]** [Slicing Lists and Strings](https://www.youtube.com/watch?v=ajrtAuDg3yw) (10:44)
- **T#26** Arrays and **T#27** Array values from user, in the [Telusko playlist](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3)

**Reading**

- Driscoll, M. (2017) *Python 101*, Chapters 2 and 3. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Accessed: 2 November 2026).

**More practice** (nothing is lost; these are the exercises moved out of the core list):

- Section 2.1 Strings: exercises 5 to 35.
- Section 2.2 Lists: Level 1 exercises 6 to 27, and all of Level 2.
- Section 2.3 Tuples: Level 1 exercises 3 to 5, and all of Level 2.
- Section 2.4 Sets: Level 1 exercises 3 to 5, and all of Levels 2 and 3.
- Section 2.5 Dictionaries: exercises 4 to 11.
- Section 2.1 "String Methods": read it in full, or watch the Bro Code video above.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- The whole week fits in 6 hours or less.

::::::::::::::::::::::::::::::::::::::::::::::::
