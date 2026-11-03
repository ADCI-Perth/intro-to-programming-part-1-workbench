---
title: 'Week 2 Practice: Phone Book'
teaching: 0
exercises: 120
---

:::::::::::::::::::::::::::::::::::::: questions

- Can I use a dictionary of lists to manage real data?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Build a phone-book program that stores and looks up contacts.

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: callout

## Files for this task

Download these files into a folder for this task and open the folder in PyCharm.

- [starter.py](files/week-2/starter.py)
- [solution.py](files/week-2/solution.py)
- [test_solution.py](files/week-2/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time:** about 2 hours. This is practice, not an assessment. There are no marks.


## Goal

Write a small phone-book program. It stores contacts in a **dictionary of lists**. Each name (the key) holds a list of phone numbers (the value). The program asks you questions with `input()` and prints the results.

You will practise:

- `input()` and string methods such as `.strip()` and `.title()`
- dictionaries: adding, `.get()`, `.pop()`, `.keys()`
- lists: `.append()`, `.sort()`, `", ".join(...)`
- a set, in the stretch step

You have not learnt `if`, loops or functions yet. That is fine. **Do not use them.** Week 3 covers them.

## New terms

- **Dictionary of lists:** a dictionary where every value is a list. Example: `{"Ben": ["0400 333 444", "08 9000 1111"]}`.
- **Default value:** what a method gives back when it cannot find what you asked for.

## Steps

Open `starter.py` in PyCharm. Work from the top, one step at a time. Run the file after each step.

1. **Start data.** `contacts` already holds two people. Read it. Notice that each value is a list, even when it holds only one number.
2. **Add a contact.**
   - Ask for a name. Tidy it with `.strip()` and `.title()`, so `"  cara jones "` becomes `"Cara Jones"`.
   - Ask for a mobile number.
   - Add the name to `contacts`. The value is a list holding the mobile number.
3. **Add a second number.** Ask for a home or work number. Use `.append()` to add it to the list for the same name.
4. **Look up a contact.** Ask which contact to look up. Tidy the answer. Use `contacts.get(name, ["not found"])` to get the numbers. Print one line, for example `Ben: 0400 333 444, 08 9000 1111`.
5. **Remove a contact.** Ask which contact to remove. Tidy the answer. Use `contacts.pop(name, None)`. The second value is a default, so nothing breaks if the name is not there.
6. **Show the phone book.** Make a list of the names with `list(contacts.keys())`. Sort it with `.sort()`. Print one line, for example `Contacts (2): Ben, Cara Jones`. Use `len(contacts)` for the count.
7. **Stretch (optional).** Use a set to count the different numbers the new contact and Ben have together. A set keeps each value once. Do this before Step 5, so the name still exists.

## Example run

Your typing is shown after each prompt.

```
New contact name: cara jones
Mobile number: 0411 000 111
Second number (home or work): 08 9111 2222
Different numbers for Cara Jones and Ben: 4
Look up which contact? ben
Ben: 0400 333 444, 08 9000 1111
Remove which contact? amy
Contacts (2): Ben, Cara Jones
```

The "Different numbers" line is the stretch step. Your prompts can be worded differently. The **printed lines** should look like the ones above.

## Hints

- `.strip()` removes spaces from both ends. `.title()` makes each word start with a capital letter.
- `contacts[name] = [mobile]` creates a new key with a one-item list.
- `contacts[name].append(extra)` adds to the list stored under that key.
- `", ".join(numbers)` turns `["a", "b"]` into `"a, b"`.
- An f-string such as `f"{name}: {text}"` is a tidy way to build a line.
- If you see a `KeyError`, you asked for a key that is not in the dictionary. Check your spelling, or use `.get()`.

## Check your work

- [ ] The program runs from top to bottom without errors.
- [ ] A name typed as `  cara jones ` is stored as `Cara Jones`.
- [ ] Looking up a name that does not exist prints `not found`, not an error.
- [ ] Removing a name that does not exist changes nothing.
- [ ] The names in the last line are in alphabetical order.
- [ ] You did not use `if`, `for`, `while` or `def`.

## Test your program (optional)

The test file runs your program, types answers into it and checks what it prints. It tests `solution.py` by default. To test your own file, set `PHONEBOOK_FILE`.

From the repository root, in the PyCharm terminal (PowerShell):

```powershell
$env:PHONEBOOK_FILE = "starter.py"
python -m pytest weeks/week-2/practice
```

If a test fails, read the message. It shows the line the test expected. Try not to open `solution.py` until you have had a good go.

## Extra challenges (if you have time)

- Add a tuple for each contact, such as `("Cara Jones", "Perth")`, and print it.
- Use `.upper()` or `.lower()` to make the lookup ignore capital letters.
- Store a third number and print how many numbers each person has with `len()`.

:::::::::::::::::::::::::::::::::::::: keypoints

- A dictionary of lists stores several values for each key.

::::::::::::::::::::::::::::::::::::::::::::::::
