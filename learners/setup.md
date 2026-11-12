---
title: Setup
---

You need two free programs: **Python** (the language) and **PyCharm** (the editor you write code in). Section 1.1 walks through both installs; this page is a short checklist.

## Software Setup

::::::::::::::::::::::::::::::::::::::: discussion

### What you will install

- **Python 3.12 or newer** from [python.org](https://www.python.org/downloads/).
- **PyCharm** from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/). Since version 2025.1 there is one PyCharm download; its core features are free. Ignore the Pro trial if you are offered one: everything in this course works in the free core.

Video help: Telusko T#2 [Python Installation, PyCharm](https://www.youtube.com/watch?v=CScxy0294SE&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) (9:33). The PyCharm download page in the video is older, so it looks a little different.

:::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::: solution

### Windows

1. Download Python from python.org and run the installer.
2. On the first screen, tick **Add python.exe to PATH**, then choose **Install Now**.
3. Open **Command Prompt** and type `python --version`. You should see `Python 3.12` or newer.
4. Download and install PyCharm with the default options.

:::::::::::::::::::::::::

:::::::::::::::: solution

### Mac

1. Download the macOS installer from python.org and run it.
2. Open **Terminal** and type `python3 --version`. You should see `Python 3.12` or newer.
3. Download PyCharm (choose Apple Silicon or Intel to match your Mac) and drag it into Applications.

:::::::::::::::::::::::::

:::::::::::::::: solution

### Linux

1. Most Linux systems already have Python 3. Check with `python3 --version`; if it is older than 3.12, install a newer version with your package manager.
2. Install PyCharm from the JetBrains website or with JetBrains Toolbox.

:::::::::::::::::::::::::

## Get the course files

Download the [course zip file](data/course-data.zip) and unzip it into your Documents folder. It gives you an `IntroToProgramming` folder with:

- a `weeks` folder with the lesson code for each section, and each week's practice task (starter file, model solution and tests);
- an `assets` folder with a `data` folder. It holds the two country lists that some optional exercises use (`countries.py` and `countries-data.py`).

Open the `IntroToProgramming` folder in PyCharm (**File > Open**). **Keep the folder layout.** The test commands in the practice tasks are run from the top of this folder, so they will not work if you move the files.

## Your own files

1. Keep your own work inside the `IntroToProgramming` folder.
2. Create one `.py` file per section, for example `section_1_2.py`, and click the green arrow to run it.
3. Each week's practice task tells you which starter file to work in.

When a lesson mentions a file such as `data/countries.py`, you will find it in `assets/data/`.
