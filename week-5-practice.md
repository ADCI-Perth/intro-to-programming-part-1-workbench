---
title: 'Week 5 Practice: Animal Class and Mini Project (Part 1)'
teaching: 0
exercises: 120
---

:::::::::::::::::::::::::::::::::::::: questions

- Can I model real things with classes and save them to a file?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Write an Animal class, then start a library-loan manager that saves to JSON.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: callout

## Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [animal_starter.py](files/week-5/animal_starter.py)
- [animal_solution.py](files/week-5/animal_solution.py)
- [test_animal.py](files/week-5/test_animal.py)
- [library_starter.py](files/week-5/mini_project/library_starter.py)
- [library.py](files/week-5/mini_project/library.py)
- [test_library.py](files/week-5/mini_project/test_library.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Build block: 2 hours.** This is practice, not an assessment. There are no marks. Use the tests to check yourself.

| Part | Task | Time |
|---|---|---|
| 1 | Animal class (steps 1 to 4 and 6; step 5 is an optional stretch) | about 30 minutes |
| 2 | Mini project, Part 1: library loan manager | about 90 minutes |
| | **Total** | **2 hours** |

The mini project is the bigger task, so it gets most of the time. If the Animal class runs over, skip step 5 and move on.

You will need Section 5.1 (classes), Section 5.2 (files and JSON) and Section 4.4 (try/except, from Week 4).

---

## Part 1: Animal class (about 30 minutes, plus about 15 for the optional step 5)

### Goal

Write a class, make several objects from it, then write a **subclass** (a class that inherits from another). This is a classic first OOP exercise: one class, many objects.

Key terms:

- **Class:** a blueprint for objects.
- **Object (or instance):** one thing built from the blueprint. `Animal("Mittens", ...)` and `Animal("Daisy", ...)` are two instances.
- **Attribute:** a variable that belongs to an object, such as `self.name`.
- **Subclass:** a class that inherits the attributes and methods of a parent class and can add or replace some.

### Steps

Open `animal_starter.py` and work through TODO 1 to 6. Step 5 is an optional stretch.

1. **`Animal`** takes `name`, `species`, `sound` and `age` (age defaults to `0`). Store all four on `self`.
2. **`speak()`** returns (does not print) text such as `"Mittens says Meow"`.
3. **`have_birthday()`** adds 1 to the animal's age.
4. **`__str__()`** returns text such as `"Mittens the cat (age 3)"`. Python uses it when you `print()` the object.
5. **Optional stretch: `Dog`** inherits from `Animal`. Its `__init__` takes only `name` and `age=0` and calls `super().__init__(...)` with species `"dog"` and sound `"Woof"`. It **overrides** `speak()` (replaces the parent's version) to return `"Rex says Woof! Woof!"`, and adds a new method `fetch(item)` returning `"Rex fetches the ball"`.
6. In the `if __name__ == "__main__":` block, create at least two `Animal` objects. Print each, call `speak()`, give one a birthday, and print it again. If you did step 5, add a `Dog` too and call `fetch()`.

   Leave the line `if __name__ == "__main__":` exactly as it is in the starter and put your test code inside that block. Week 6 explains why it is there; for now, just treat it as "run this part when I press Run".

### Example output

```
Mittens the cat (age 3)
Mittens says Meow
Daisy the cow (age 0)
Daisy says Moo
Rex the dog (age 2)
Rex says Woof! Woof!
Rex the dog (age 3)
Rex fetches the ball
```

### Hints

- Inside a method, `self` means "this object". Every method's first parameter is `self`.
- Use `return` in `speak()`, not `print()`. Returned text is easier to test.
- Changing one object's age must not change another's. If it does, check that you used `self.age`.
- Stuck on `super()`? Compare with the `Student(Person)` example in Section 5.1 (Inheritance).

### Check your work

- [ ] Two `Animal` objects keep separate names and ages.
- [ ] `print(...)` of an animal shows the `__str__` text, not something like `<__main__.Dog object at 0x...>`.
- [ ] (Step 5 only) `Dog("Rex")` works without giving a species or sound.
- [ ] (Step 5 only) `isinstance(rex, Animal)` is `True`.
- [ ] `test_animal.py` passes (see "Running the tests" below).

Tests for `Dog` are skipped until you write it. Further stretch (optional): add a `Cat` subclass whose `speak()` is different, then loop over a list holding an `Animal`, a `Dog` and a `Cat` and call `speak()` on each. That is polymorphism and duck typing (T#57 and T#58) in action.

---

## Part 2: Mini project, Part 1 (about 90 minutes)

Go to [mini_project/README.md](week-5-practice.md). You will build a library loan manager with a `Book` class, a `Library` class and JSON saving. Week 6 finishes it.

---

## Running the tests

Tests are small programs that check your code. We use **pytest**.

1. Open `test_animal.py`. Near the top, change `MODULE_NAME = "animal_solution"` to `MODULE_NAME = "animal_starter"`. Now the tests check your code.
2. In PyCharm, right-click `test_animal.py` and choose **Run 'pytest in test_animal.py'**. Or, in the Terminal tab, from the repository root:
   ```
   python -m pytest weeks/week-5/practice/test_animal.py
   ```
3. Read any failure message from the top. It names the test and shows what it expected.

Peek at `animal_solution.py` only after you have tried each step yourself. The same method works for the mini project with `test_library.py`.

If `pytest` is missing, run `python -m pip install pytest` in the Terminal tab.

## Mini Project, Part 1: Library Loan Manager


**Time: about 90 minutes.** This is practice, not an assessment. There are no marks.

### What you are building

A small library system. It keeps track of books, lets you lend and return them, and saves everything to a JSON file so nothing is lost when the program stops.

You will use ideas from this week: classes (Section 5.1), a dictionary of objects, try/except (Week 4), and saving to JSON (Section 5.2).

### Files

| File | What it is |
|---|---|
| `library_starter.py` | Your work. It has TODOs to fill in. |
| `test_library.py` | Tests that check your work. |
| `library.py` | The model solution. Look only after you have tried. |

### Steps

Open `library_starter.py` and work through the TODOs in order.

#### 1. The `Book` class (about 30 minutes)

- `__init__(self, title, author, isbn)` stores the three values. It also sets `self.on_loan = False`.
- `to_dict(self)` returns a dictionary: `{"title": ..., "author": ..., "isbn": ..., "on_loan": ...}`.
- `__str__(self)` returns text like:
  ```
  Dune by Frank Herbert (111) - available
  Dune by Frank Herbert (111) - on loan
  ```
- `from_dict` is already written for you. It uses `@classmethod`. A **class method** belongs to the class instead of one object, and its first parameter is `cls` (the class itself). That lets `Book.from_dict(data)` build a new `Book` from a dictionary, which is how a book comes back from the saved file. Read it, but you do not need to change it.

#### 2. The `Library` class (about 35 minutes)

- `__init__` creates `self.books = {}`. The **key** is each book's `isbn` and the **value** is the `Book` object. (An ISBN is a book's unique number. We use short text codes like `"111"`.)
- `add_book(book)` stores the book under its isbn.
- `lend(isbn)` sets `on_loan` to `True`.
  - Unknown isbn: Python raises `KeyError` for you if you write `self.books[isbn]`.
  - Book already on loan: `raise ValueError("...")` with a helpful message (see the `raise` hint below).
- `return_book(isbn)` sets `on_loan` to `False`.
  - Unknown isbn: `KeyError`.
  - Book not on loan: `ValueError`.
- `available_books()` returns a **list** of the `Book` objects that are not on loan.

#### 3. Saving and loading (about 15 minutes, then 10 to run it and check)

- `save(path)` is already written for you. Read it: it turns each book into a dictionary with `to_dict()`, puts them in a list, and uses `json.dump(data, file, indent=2)`.
- `load(path)` is yours to write. It reads the file, turns each dictionary back into a `Book` with `Book.from_dict(...)`, and **replaces** `self.books`. Wrap the file reading in `try/except FileNotFoundError`. If the file does not exist yet, leave the library empty and do not crash.

### Try it yourself

After the tests pass, add a short block at the bottom of `library_starter.py`:

```python
if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Dune", "Frank Herbert", "111"))
    library.add_book(Book("Emma", "Jane Austen", "222"))
    library.lend("111")
    for book in library.books.values():
        print(book)
    library.save("library.json")
```

Leave the line `if __name__ == "__main__":` as it is and put your test code inside that block. Week 6 explains why it is there.

Open `library.json` and look at the saved text.

### Hints

- **`raise`** means "stop here and signal an error on purpose". You choose the error type and the message:
  ```python
  if book.on_loan:
      raise ValueError("Dune is already on loan")
  ```
  Python stops the method at that line, and the error message appears unless some other code catches it with `try/except`. The tests check that the right error is raised.

- Use the keys `"title"`, `"author"`, `"isbn"` and `"on_loan"` exactly. Other code (and Week 6) depends on these names.
- Write the `to_dict` and `__str__` code first and test it, then move on.
- `"on loan" if book.on_loan else "available"` is a handy one-line way to choose between two words.
- `with open(path, "w", encoding="utf-8") as file:` closes the file for you.
- In PyCharm, the `tmp_path` in the tests is a temporary folder that pytest creates and cleans up. Your real files are never touched.

### Running the tests

1. Open `test_library.py`. Change `MODULE_NAME = "library"` to `MODULE_NAME = "library_starter"` so the tests check your code.
2. Right-click the file in PyCharm and choose **Run 'pytest in test_library.py'**, or run this in the Terminal from the repository root:
   ```
   python -m pytest weeks/week-5/practice/mini_project
   ```

### Check your work

- [ ] A new `Book` is not on loan.
- [ ] `print(book)` gives text in the exact format above.
- [ ] Lending the same book twice raises `ValueError`.
- [ ] Lending or returning an unknown isbn raises `KeyError`.
- [ ] `available_books()` leaves out books that are on loan.
- [ ] Save, then load into a new `Library`, gives the same books and loan status.
- [ ] Loading a file that does not exist leaves the library empty without an error.
- [ ] All tests in `test_library.py` pass.

### Coming in Week 6 (Part 2)

In Week 6 you will finish this project. You will move the classes into a proper **module** (a reusable `.py` file) and write a separate program file with a text **menu** so a person can add, lend and return books without writing code. You will add a **search** feature (for example, finding books by title or author) and add **type hints** (notes that say what type each value should be) so your code is easier to read and check. Keep the names in this Part 1 exactly as they are: Week 6 builds on them.

:::::::::::::::::::::::::::::::::::::: keypoints

- Classes keep data and behaviour together.
- JSON files let a program remember data between runs.

::::::::::::::::::::::::::::::::::::::::::::::::
