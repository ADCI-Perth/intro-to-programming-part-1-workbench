---
title: 'Week 1 Practice: Unit Converter'
teaching: 0
exercises: 120
---

:::::::::::::::::::::::::::::::::::::: questions

- Can I combine input, variables and operators in a small program?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Write a unit converter or calculator that runs in PyCharm.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: callout

## Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [starter.py](files/week-1/starter.py)
- [solution.py](files/week-1/solution.py)
- [test_solution.py](files/week-1/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time:** about 2 hours. This is practice only. It is not marked.

## Goal

Write a small script that asks for a distance and a temperature, converts them and prints the answers. Then write five sentences comparing Python's "Hello World" with another language.

You only need what you learned this week: variables, `input()`, `float()`, arithmetic operators and `print()`.

## Part 1: the converter (about 1 h 15 min)

Work in `starter.py`. Follow the TODO comments.

1. Ask the user for a distance in **kilometres**. `input()` gives you text, so wrap it in `float()` to get a number.
2. Convert it to **miles**: `miles = kilometres * 0.621371`.
3. Ask for a temperature in **degrees Celsius** and convert it to **Fahrenheit**: `fahrenheit = celsius * 9 / 5 + 32`.
4. Round each answer to 2 decimal places with `round(value, 2)`.
5. Print both answers in exactly this form, so the checks can read them:

```
Enter a distance in kilometres: 10
Enter a temperature in Celsius: 25
10.0 km is 6.21 miles
25.0 C is 77.0 F
```

The `10` and `25` are typed by the user. Everything else is printed by your script.

### Hints

- `float("10")` gives `10.0`. That is why the output says `10.0 km`.
- `input("Enter ...: ")` shows a message (a **prompt**) and waits for the user to type.
- Print with commas: `print(kilometres, "km is", miles, "miles")`. `print` puts a space between the items.
- `*` is multiply, `/` is divide. Python does multiplication and division before `+`.

### Stretch (only if you have time)

Add a third conversion, such as kilograms to pounds (1 kg = 2.20462 lb). Keep the same style.

## Part 2: compare Hello World (about 45 min)

Create a plain text file called `comparison.txt` (in PyCharm: **New > File**). Write **exactly five sentences** comparing Python's Hello World with one other language: C, Java or assembly from the [Bridge](week-1-bridge.md). You can use your notes from the Bridge activity.

Think about:

- How many lines does each version need?
- Which one is easier for a beginner to read, and why?
- What does the other language make you write that Python does not?
- Is each one compiled, interpreted or both?
- What is one good reason to choose the other language anyway?

## Check your work

- [ ] `starter.py` runs with no errors.
- [ ] It asks for kilometres, then Celsius.
- [ ] 10 km prints `10.0 km is 6.21 miles`.
- [ ] 25 C prints `25.0 C is 77.0 F`.
- [ ] You used only variables, `input()`, `float()`, `round()`, arithmetic and `print()`.
- [ ] `comparison.txt` has five sentences, and they name the other language.

## Run the automatic checks (optional)

The file `test_solution.py` checks the model answer in `solution.py`. It runs the script the way a user would: it types the answers in for you, then checks what the script printed. You can point it at your own work. In a terminal, from the project folder:

**Windows (PowerShell):**

```
$env:CONVERTER_SCRIPT = "starter.py"; python -m pytest weeks/week-1/practice
```

**macOS or Linux:**

```
CONVERTER_SCRIPT=starter.py python -m pytest weeks/week-1/practice
```

If pytest is not installed, run `python -m pip install pytest` first. Try the task yourself before you look at `solution.py`.

:::::::::::::::::::::::::::::::::::::: keypoints

- Small programs are built from variables, input, operators and print.

::::::::::::::::::::::::::::::::::::::::::::::::
