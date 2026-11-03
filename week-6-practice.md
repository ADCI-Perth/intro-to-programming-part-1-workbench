---
title: 'Week 6 Practice: Mini Project (Part 2)'
teaching: 0
exercises: 180
---

:::::::::::::::::::::::::::::::::::::: questions

- Can I finish a complete program and justify its design?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Finish the library-loan manager across modules, and compare two paradigms in it.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: callout

## Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [library.py](files/week-6/solution/library.py)
- [main.py](files/week-6/solution/main.py)
- [test_library.py](files/week-6/test_library.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time guide: 3 hours.** This is practice, not a graded task. You finish the project you started in Week 5.

## Goal

Turn your Week 5 `library.py` into a small program with a text menu. You will add a search, type hints, error handling and a short written note.

New words this week:

- **Type hint:** a note in the code saying what type a value should be, such as `title: str`.
- **Module:** a `.py` file whose code another file can `import`.
- **Paradigm:** a style of programming (for example object-oriented, functional or imperative).

## What you start with

Your Week 5 `Library` and `Book` classes:

- `Book(title, author, isbn)` with `on_loan` (starts as `False`), `to_dict()`, `from_dict(data)` and `__str__`.
- `Library` with `books` (a dictionary keyed by ISBN), `add_book`, `lend`, `return_book`, `available_books`, `save(path)` and `load(path)`.

If your Part 1 is not finished, finish the [Week 5 mini project](week-5-practice.md) first, or look at `solution/library.py` after a real attempt.

## Steps

### Step 1: Set up the Week 6 folder (10 min)

1. Make a new folder for Week 6, for example `mini_project_part2`.
2. Copy your Week 5 `library.py` into it. It is in your own Week 5 project folder; the course version is [`weeks/week-5/practice/mini_project/library.py`](files/week-5/mini_project/library.py).
3. Open the folder as a project in PyCharm.

### Step 2: Add `search` (30 min)

Add this method to `Library`:

```python
def search(self, text):
    ...
```

- It returns a list of `Book` objects whose title **or** author contains `text`.
- Ignore upper and lower case: searching `"austen"` finds `"Jane Austen"`.
- Use a **list comprehension** (`[... for ... in ... if ...]`) or `filter`.

Hint: `text.lower() in book.title.lower()`.

### Step 3: Add type hints (20 min)

Add hints to every method in `Book` and `Library`, including the return type. For example:

```python
def add_book(self, book: Book) -> None:
def available_books(self) -> list[Book]:
```

Hints:

- Methods that return nothing use `-> None`.
- Inside `Book`, a method that returns a `Book` writes the type in quotes: `-> "Book"`.
- A file path can be `str | Path` (add `from pathlib import Path`).
- Optional: if you have installed mypy (`python -m pip install mypy`), run `python -m mypy library.py`. See the Bridge note.

### Step 4: Write `main.py` (60 min)

Create `main.py` next to `library.py`. Start with `from library import Book, Library`.

Show this menu in a loop:

```
1. Add a book
2. List available books
3. Lend a book
4. Return a book
5. Search
6. Save and quit
```

- Load the library from `library.json` when the program starts (a missing file is fine: it gives an empty library).
- Option 6 saves to `library.json` and stops the loop.
- Put the menu loop in a function called `main()`, and finish the file with:

```python
if __name__ == "__main__":
    main()
```

This means the menu runs only when you run `main.py` directly, not when another file imports it (see T#46).

### Step 5: Handle bad input (30 min)

Use `try` and `except` so the program never crashes:

- Lending or returning an unknown ISBN raises `KeyError`. Print a friendly message.
- Lending a book already on loan (or returning one that is not) raises `ValueError`. Print the message.
- A menu choice that is not 1 to 6 should print a hint and show the menu again.
- Empty title, author or ISBN when adding a book should be refused.

### Step 6: Write the paradigm note (20 min)

Write 5 to 6 sentences in a file called `note.txt` (or a comment at the top of `main.py`). Compare **at least two named paradigms** (object-oriented, imperative, functional or logic) using the criteria table in ["Choosing a paradigm" in the Bridge](week-6-bridge.md): how each handles state, when it fits, and how easy it is to test.

1. Name the paradigms you are comparing (at least two).
2. Which parts of your library project are object-oriented? Point to one example, such as `Library.lend`.
3. Which parts are functional? Point to one example, such as the `search` list comprehension.
4. Would a purely imperative version (no classes, just functions and a dictionary) be better or worse? Why?
5. Say which style is easier to test, and why.
6. Say what you would change if the library had a million books.

Use the Bridge table, the [Computerphile] paradigms video and your Week 4 notes. There is no single right answer. Explain your reasoning.

### Step 7: Test and tidy (10 min)

Run the checks below, then fix anything that fails.

## Example session

```
1. Add a book
2. List available books
...
Choose 1-6: 1
Title: Dune
Author: Frank Herbert
ISBN: 111
Book added.
Choose 1-6: 3
ISBN to lend: 999
No book with that ISBN.
Choose 1-6: 5
Search for: herbert
Dune by Frank Herbert (111) - available
```

## Check your work

- [ ] `search("AUSTEN")` and `search("austen")` give the same result.
- [ ] Every method has type hints.
- [ ] `main.py` imports `library` and uses `if __name__ == "__main__":`.
- [ ] Bad ISBNs and bad menu choices print a message and do not crash.
- [ ] Quitting with option 6 saves, and starting again shows your books.
- [ ] Your 5 to 6 sentence paradigm note compares at least two paradigms.

## Run the tests

From the top folder of the course repository, test your own folder by setting `MINI_PROJECT_DIR` to it.

PowerShell:

```
$env:MINI_PROJECT_DIR = "C:\path\to\mini_project_part2"
python -m pytest weeks/week-6/practice
```

Mac or Linux:

```
MINI_PROJECT_DIR=/path/to/mini_project_part2 python -m pytest weeks/week-6/practice
```

If pytest is missing, run `python -m pip install pytest`. Without `MINI_PROJECT_DIR`, the tests run against the model solution in `solution/`.

Run `main.py` from PyCharm (right-click, **Run**) or with `python main.py` from inside your folder.

## Model solution

Try it yourself first. Then compare with [solution/library.py](files/week-6/solution/library.py) and [solution/main.py](files/week-6/solution/main.py).

:::::::::::::::::::::::::::::::::::::: keypoints

- Splitting code into modules keeps programs manageable.
- Explain design choices using clear criteria.

::::::::::::::::::::::::::::::::::::::::::::::::
