---
title: 'Week 3 Practice: Grade Calculator'
teaching: 0
exercises: 120
---

:::::::::::::::::::::::::::::::::::::: questions

- Can I plan and build a program with functions and decisions?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Write pseudocode, then a grade calculator using functions and if/elif.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: callout

## Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [starter.py](files/week-3/starter.py)
- [solution.py](files/week-3/solution.py)
- [test_solution.py](files/week-3/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time: about 2 hours.** This is a practice task. It is not marked.

## Goal

Write a program that asks for marks, stores them, then reports the average mark and a grade. You will use a list, a dictionary, loops, `if`/`elif`/`else` and functions.

Week 4 gives you a similar grade calculator and asks you to rewrite it in a functional style. That task is self-contained, so you do not need this one.

## Before you code: write pseudocode (10 minutes)

Pseudocode is a plan in plain English. Follow the steps from the Concepts Bridge: understand, pseudocode, code, test. Write 5 to 8 short lines at the top of `starter.py`. For example: "ask for a subject; ask for a mark; check the mark; store it; repeat until done; print the report."

## Grade scale

| Mark | Grade |
|---|---|
| 85 to 100 | HD |
| 75 to 84 | D |
| 65 to 74 | C |
| 50 to 64 | P |
| 0 to 49 | F |

## Steps

Open `starter.py` in PyCharm. It has the function names ready, with TODO comments.

Leave the last two lines (`if __name__ == "__main__":` and `main()`) as they are. They run `main()` when you click Run. Week 6 explains why.

1. **`average(marks)`**: takes a list of marks and returns the average. If the list is empty, return `0.0`. Use a `for` loop to add up the marks.
2. **`grade(mark)`**: takes one mark and returns `"HD"`, `"D"`, `"C"`, `"P"` or `"F"`. Use `if`/`elif`/`else`.
3. **`is_valid_mark(mark)`**: returns `True` if the mark is from 0 to 100, otherwise `False`.
4. **`highest(marks)`** (optional stretch: skip it if you are short of time): returns the biggest mark in the list using a loop (do not use `max()`). For an empty list, return `None`.
5. **`grades_for(marks_by_subject)`**: takes a dictionary such as `{"Maths": 90}` and returns a new dictionary of grades, such as `{"Maths": "HD"}`.
6. **`main()`**: this is the only place that uses `input()`. Use a `while True` loop. Ask for a subject name (type `done` to stop), then a mark. Reject bad marks and ask again. Store good marks in a dictionary. At the end, print each subject, mark and grade, then the average (with its grade) and, if you did the stretch, the highest mark.

Keep `input()` and `print()` out of the other functions. Functions that only take values and return values are easy to test.

## Example run

```output
Grade calculator. Type done as the subject name to finish.
Subject: Maths
Mark (0 to 100): 90
Subject: Art
Mark (0 to 100): abc
Please enter a whole number.
Subject: Art
Mark (0 to 100): 120
A mark must be from 0 to 100.
Subject: Art
Mark (0 to 100): 48
Subject: English
Mark (0 to 100): 66
Subject: done

Maths: 90 (HD)
Art: 48 (F)
English: 66 (C)
Average: 68.0 (C)
Highest: 90
```

The `Highest` line is part of the optional stretch.

## Hints

- `text.isdigit()` is `True` when a string such as `"72"` is only digits. `input()` always gives you a string, so use `int(text)` to turn it into a number after that check.
- `continue` jumps back to the top of a loop. `break` leaves the loop.
- `marks_by_subject[subject] = mark` adds an item to a dictionary.
- `list(marks_by_subject.values())` gives the marks as a list.
- `f"{value:.1f}"` shows a number with one decimal place.
- Python can chain comparisons: `0 <= mark <= 100`.

## Check your work

- [ ] I wrote pseudocode before coding.
- [ ] `average([80, 70, 90])` gives `80`, and `average([])` gives `0.0`.
- [ ] `grade(85)` is `"HD"` and `grade(84)` is `"D"`. Check the edge of every grade.
- [ ] Only `main()` calls `input()`.
- [ ] My program rejects `abc` and `120` without crashing.
- [ ] The tests pass. In `test_solution.py`, change `from solution import` to `from starter import`, then in the PyCharm Terminal run `python -m pytest weeks/week-3/practice` (or right-click `test_solution.py` and choose **Run**). If you skipped `highest`, its test is expected to fail.
- [ ] I ran the program by hand with at least three subjects.

If you are stuck, compare with `solution.py` after you have tried the step yourself.

## If you finish early

Do `highest(marks)` if you skipped it. Then add a `lowest(marks)` function. Print how many subjects are a pass (50 or more).

:::::::::::::::::::::::::::::::::::::: keypoints

- Keep input() and print() in main(); other functions take values and return values.

::::::::::::::::::::::::::::::::::::::::::::::::
