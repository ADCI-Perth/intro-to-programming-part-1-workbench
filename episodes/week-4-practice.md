---
title: 'Week 4 Practice: Functional Grade Calculator'
teaching: 0
exercises: 120
---

:::::::::::::::::::::::::::::::::::::: questions

- How does a functional version of a program compare with an imperative one?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Rewrite a grade calculator with comprehensions, map/filter and try/except.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: callout

## Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [starter.py](files/week-4/starter.py)
- [solution.py](files/week-4/solution.py)
- [test_solution.py](files/week-4/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time: about 2 hours.** This is a practice task. It is not marked.

## Goal

Take a short grade calculator written with loops and rewrite it in a **functional style**. Then make it safe against bad input with `try` / `except`.

You do not need your Week 3 files. The Week 3 version is already inside `starter.py` (Part A).

## Files

| File | What it is |
|---|---|
| `starter.py` | Part A: the loop version (given). Part B: your functions to fill in. |
| `test_solution.py` | Tests for the functions. |
| `solution.py` | A model answer. Try the task yourself before you look. |

## Steps

1. Read Part A in `starter.py`. To try it, scroll to the last line of the file and **temporarily** change `main()` to `main_loop()`. Run the file, then type `abc` when it asks for a mark. It crashes. That is the problem we will fix. Change the last line back to `main()` before you carry on.
   - Near the bottom you will see `if __name__ == "__main__":`. Leave those two lines as they are. They mean "run this when the file is run directly", and Week 6 explains how they work.
2. In Part B, write `parse_mark(text)`. Use `try` / `except ValueError`. Return `None` for text that is not a number, or a number outside 0 to 100. Otherwise return the mark as a float.
3. Write `valid_marks(texts)` with a **list comprehension**. Use `map(parse_mark, texts)` and drop the `None` values.
4. Write `average(marks)`. Use `try` / `except ZeroDivisionError` so an empty list gives `0.0`.
5. Write `grade(mark)`. Copy the if/elif logic from Part A.
6. Write `letter_grades(marks)` with `map()`.
7. Write `passing_marks(marks)` with `filter()` and a `lambda`.
8. Write `grade_counts(marks)` with a **dictionary comprehension** over `GRADE_ORDER`.
9. Write `main()`. Ask for marks until an empty line. Tell the user when a mark is not valid and carry on. Print the results.
10. Write your 5-sentence note (see below).

## Example run

```output
Enter marks from 0 to 100. Press Enter on an empty line to finish.
Mark: 90
Mark: abc
  Not a valid mark, ignoring it.
Mark: 55
Mark: 120
  Not a valid mark, ignoring it.
Mark: 
Average: 72.5
Grades: ['HD', 'P']
Passing marks: [90.0, 55.0]
Grade counts: {'HD': 1, 'D': 0, 'C': 0, 'P': 1, 'F': 0}
```

Your wording can differ.

## Hints

- `float("abc")` raises a `ValueError`. That is the error you catch.
- `[m for m in map(f, items) if m is not None]` keeps only the answers that are not `None`.
- `list(map(grade, marks))` and `list(filter(lambda m: m >= 50, marks))` need `list(...)` to give you a list.
- `grades.count("HD")` counts how many times `"HD"` appears in a list.
- A **dictionary comprehension** builds a dictionary in one line, like a list comprehension but with `key: value`. For example, `{g: grades.count(g) for g in GRADE_ORDER}` makes a dictionary with one entry per grade in `GRADE_ORDER`, where each value is how often that grade appears in `grades`. (Here `grades` is the list of letter grades you get from `letter_grades(marks)`.)
- Keep `input()` and `print()` inside `main()` only. Functions that only take input and return output are **pure** and easy to test.

## Your 5-sentence note

Write five sentences, in a file or a comment at the bottom of your code, comparing the loop version (Part A) with your functional version (Part B). You could cover:

1. Which version is shorter?
2. Which is easier to read, and for whom?
3. Which is easier to test, and why?
4. What did `try` / `except` change for the user?
5. Which style would you choose for this problem, and why?

## Check your work

- [ ] Run the tests. In PyCharm, right-click `test_solution.py` and choose **Run pytest**, or in the terminal: `python -m pytest weeks/week-4/practice`.
- [ ] To test your own file, open `test_solution.py` and change `import solution as calc` to `import starter as calc`.
- [ ] Typing `abc`, `-5` or `150` does not crash the program.
- [ ] An empty list of marks does not crash `average`.
- [ ] `letter_grades`, `passing_marks` and `grade_counts` do not change the list you give them.
- [ ] Your note has five sentences.

:::::::::::::::::::::::::::::::::::::: keypoints

- The same problem can be solved in more than one style.

::::::::::::::::::::::::::::::::::::::::::::::::
