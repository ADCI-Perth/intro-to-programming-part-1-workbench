---
title: 'Week 6: Modules, libraries and choosing a paradigm'
teaching: 49
exercises: 0
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 6?
- How should I spend my time this week?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your Week 6 study time using the time plan.
- Find the videos, sections, Concepts Bridge and practice task for the week.

::::::::::::::::::::::::::::::::::::::::::::::::

**Theme:** split your code into modules, use other people's code safely, and decide which programming style suits a problem.

This is the last week. You also finish the mini project you started in Week 5.

## Learning goals

By the end of this week you can:

1. Write your own module and import it, and explain what `if __name__ == "__main__":` does.
2. Use built-in modules such as `random` and `math`.
3. Install a third-party package with `pip` inside a virtual environment, and say why pinning versions matters.
4. Explain, in a few sentences, which programming paradigm (style) suits a problem and why.

## Time plan (5 h 19 min)

| Block | Time | What you do |
|---|---|---|
| Watch | 49 min | Six videos (below) |
| Read & practise | 1 h | Section 6.1 and Section 6.2 notes, install practice, plus Level 1 exercises |
| Concepts Bridge | 30 min | [bridge.md](week-6-bridge.md): type safety, library risk, choosing a paradigm |
| Build | 3 h | [Mini project, Part 2](week-6-practice.md) |
| **Total** | **5 h 19 min** | Under the 6 h cap, so there is spare time for catching up |

Optional material is not counted in the total.

## Watch (49 min)

Watch in this order. Pause and try things in PyCharm as you go.

| # | Video | Length | Look out for |
|---|---|---|---|
| 1 | **T#45** Modules | 7:20 | How `import` finds a file and runs it. https://www.youtube.com/watch?v=1RuMJ53CKds&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 |
| 2 | **T#46** Special Variable `__name__` | 5:43 | Why code under `if __name__ == "__main__":` runs only when you run the file directly. https://www.youtube.com/watch?v=pzNISmtmzcY&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 |
| 3 | **[Corey Schafer]** pip: An In-Depth Look at the Package Management System | 9:06 | The main pip commands: install, uninstall, list, freeze. https://www.youtube.com/watch?v=U2ZN104hIcc |
| 4 | **[Tech With Tim]** Python Virtual Environments: Full Tutorial for Beginners | 9:05 | Why each project gets its own "box" of packages. https://www.youtube.com/watch?v=Y21OR1OPC9A |
| 5 | **T#28** Why NumPy? Installing NumPy | 6:58 | How PyCharm installs a package for you. https://www.youtube.com/watch?v=8LlXhtfNZEQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3 |
| 6 | **[Computerphile]** Programming Paradigms | 10:44 | The names of the styles and what each is good at. You will use this for your paradigm note. https://www.youtube.com/watch?v=sqV3pL5x8PI |

## Read & practise (1 h)

Open each lesson, read it, type out the examples and run them. Do not just copy and paste.

### Section 6.1: Modules (about 22 min)

Lesson: [Section 6.1: Modules](6-1-modules.md). Code: [lessons/6.1_code/](files/code/6.1/).

- Read: What is a Module, Creating a Module, Importing a Module, the two "Import Functions" sections, and the built-in modules **Math** and **Random**.
- Skim: OS, Sys, Statistics and String modules. Just know they exist.
- Do the **Level 1** exercises (1 to 3). They use `random`.

### Section 6.2: pip and packages (about 28 min)

Lesson: [Section 6.2: pip and Packages](6-2-packages.md). Code: [lessons/6.2_code/mypackage/](files/code/6.2/mypackage).

- Read: What is PIP, Installing packages using pip, Uninstalling, List of Packages, Show Package, PIP Freeze, Creating a Package.
- Skim: Reading from URL. You need an internet connection and the `requests` package.
- Section 6.2's exercises read web data and use statistics, so they are too big for this block. Instead, create a small package of your own (a folder with `__init__.py` and one module), then import it from a separate file.

### Installing packages: command line and PyCharm (about 10 min hands-on)

The lessons show the command line (Mac or Linux style). On Windows, use PowerShell or the **Terminal** tab inside PyCharm. If `pip` is not found, type `python -m pip` instead.

**Command line way**

```
python -m venv .venv
.venv\Scripts\activate
python -m pip install requests
python -m pip freeze
```

- On Mac or Linux, activate with `source .venv/bin/activate`.
- A **virtual environment** is a private folder of packages for one project. It stops projects from clashing.

**PyCharm way**

- Make a virtual environment: *File > Settings > Project > Python Interpreter > Add Interpreter > Add Local Interpreter > Virtualenv Environment > New*. (On Mac: *PyCharm > Settings*.) New projects usually do this for you.
- Install a package: in the same *Python Interpreter* page, click the **+** button, search for the package (for example `requests`), then click **Install Package**. This is what T#28 shows with NumPy.
- You can also open the **Terminal** tab at the bottom of PyCharm. It starts with your virtual environment already active.

### Data files

Some optional lessons open files such as `data/weight-height.csv`. Those files live in [`assets/data/`](data/course-data.zip) at the top of this repository. Point your code at that folder.

## Concepts Bridge (30 min)

Go to [bridge.md](week-6-bridge.md). It covers type hints, risks of third-party libraries, and a criteria table for choosing a paradigm (LO 4).

## Build (3 h)

Go to [practice/README.md](week-6-practice.md). You finish the Week 5 mini project (a library-loan manager): add search, type hints, a menu program, and a short note on paradigms.

This is practice only. Nothing here is marked.

## Optional

Only if you have time and are curious.

**Videos**

- **T#47** `__name__` part 2 (Telusko playlist)
- **T#29 to T#31** NumPy arrays and matrices (Telusko playlist)
- **T#77** Jupyter Notebook (Telusko playlist)
- **T#74** Git and GitHub with Python (Telusko playlist)
- **[Low Level]** How Can Memory-Safe Code Stop Hackers? (7:43): https://www.youtube.com/watch?v=lxUYZVX_FjQ

**Lessons**

- [Section 6.4: Virtual environments](../learners/6-4-virtual-environments.md)
- [Section 6.3: Web scraping](../learners/6-3-web-scraping.md)
- [Section 6.5: Statistics (NumPy)](../learners/6-5-statistics-numpy.md)
- [Section 6.6: Pandas](../learners/6-6-pandas.md)

**Other**

- Unix time and time-related bugs: https://www.youtube.com/watch?v=-5wpm-gesOY
- Driscoll, M. (2017) *Python 101*, chapters 27, 29 and 33. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/
- Romano, F. (2018) *Learn Python Programming*, 2nd edn, chapter 5. Packt.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- The whole week fits in 6 hours or less.

::::::::::::::::::::::::::::::::::::::::::::::::
