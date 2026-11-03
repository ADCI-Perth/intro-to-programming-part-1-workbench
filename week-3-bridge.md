---
title: 'Week 3 Concepts Bridge: Solving Problems and Sorting'
teaching: 20
exercises: 10
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I plan a solution before I code it?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Use the understand, pseudocode, code, test process.
- Write bubble sort from pseudocode and trace it in the debugger.

::::::::::::::::::::::::::::::::::::::::::::::::

**Time: 30 minutes.** There is no extra video. You already watched T#70 Bubble Sort in the Watch block.

| Part | Minutes |
|---|---|
| Read: the problem-solving process | 5 |
| Read: bubble sort pseudocode | 3 |
| Activity 1: write `bubble_sort` yourself | 12 |
| Activity 2: trace it in the PyCharm debugger | 7 |
| Activity 3: compare with `sorted()` and check the model answer | 3 |
| **Total** | **30** |

## Why this matters

Learning outcome 1 of this course asks you to *analyse and solve a problem and then implement the solution in a programming language*. The order matters: think first, type second. Writing a sorting algorithm from scratch is also a classic exercise for logical and control structures. This bridge covers both: you will write bubble sort yourself.

## The problem-solving process

Good programmers rarely start by typing code. They follow four steps.

1. **Understand.** Say the problem in your own words. What goes in? What should come out? What are some example answers?
2. **Pseudocode.** Write the steps in plain English, in short lines. *Pseudocode* means "fake code": it is a plan, not a program, so the computer never runs it.
3. **Code.** Turn each line of pseudocode into Python.
4. **Test.** Run it on examples where you already know the answer. Try odd cases too, such as an empty list.

Here is a tiny example. The problem: "find the average of some marks".

```output
Understand: input is a list of marks, output is one number.
            [72, 85, 64] should give about 73.7.
Pseudocode: 1. start the total at 0
            2. for each mark, add it to the total
            3. divide the total by how many marks there are
Test:       try [72, 85, 64], then [100], then []
```

The code is now easy to write:

```python
marks = [72, 85, 64]
total = 0
for mark in marks:
    total = total + mark
print(total / len(marks))
```

Testing the empty list `[]` would show a problem: dividing by zero. Finding that during testing, not after you hand it in, is the point of step 4. You will use this process for the grade calculator in the Build block.

## Sorting: bubble sort pseudocode

*Sorting* means putting items in order, such as smallest to largest. **Bubble sort** is a simple method. It looks at neighbouring pairs and swaps them when they are in the wrong order. Big values slowly "bubble" to the end.

Here is the plan as pseudocode. It is not Python yet.

```output
bubble_sort(numbers):
    1. make a copy of numbers and call it items
    2. repeat for each pass:
           the last position still to check is "end"
           (the first pass checks up to the last position, and each pass stops one place earlier)
           for each neighbouring pair (i and i + 1) up to end:
               if items[i] is bigger than items[i + 1]:
                   swap them
    3. return items
```

After the first pass the biggest value has reached the end. Each pass fixes one more value in place.

::::::::::::::::::::::::::::::::::::: challenge

## Activity (about 22 minutes)

Use the list `[6, 2, 5, 3]`.

### 1. Write it yourself (12 minutes)

1. Understand: what should the sorted list look like?
2. In a new PyCharm file, write `def bubble_sort(numbers):` from the pseudocode. Do not look at the model answer yet. Hints:
   - `list(numbers)` makes a copy, so the original list is not changed.
   - `range(len(items) - 1, 0, -1)` counts down for the passes.
   - `range(end)` gives each neighbouring pair `i` and `i + 1` in a pass.
   - `items[i], items[i + 1] = items[i + 1], items[i]` swaps two values in one line.
3. Add `print(bubble_sort([6, 2, 5, 3]))` at the bottom and run it.
4. Test it: also try `[]`, `[1]` and `[3, 3, 1]`.

If you are stuck after 8 minutes, peek at the model answer at the end, then close it and type your own version.

### 2. Trace it in the PyCharm debugger (7 minutes)

A *trace* means following a program one step at a time and watching the variables. In T#16 you saw how PyCharm's debugger does this.

1. Click in the grey gutter beside your `if` line that compares two items. A red dot (a *breakpoint*) appears.
2. Right-click the file and choose **Debug**. The program pauses at the breakpoint.
3. Look at the **Threads & Variables** panel. Watch `items`, `i` and `end`.
4. Press **Resume Program** (green arrow) to move to the next time the line runs, or **Step Over** (F8) to go one line at a time.
5. On paper, write the list after every swap and count the swaps. Find the values of `i` and `end` when the second pass starts.

### 3. Compare with `sorted()` (3 minutes)

Python already has a sorting function. It is fast and well tested, so in real programs you use it. Writing your own bubble sort is for learning how sorting works.

Add these lines to your file and run it:

```output
data = [6, 2, 5, 3]
print(bubble_sort(data))
print(sorted(data))
print(bubble_sort(data) == sorted(data))
print(data)
```

Both should give the same answer, and neither should change `data`. Bubble sort is slow on long lists because it compares so many pairs. Python's `sorted()` is much faster.

:::::::::::::::: solution

## Model answer

Check your work after you have tried it yourself.

1. Sorted list: `[2, 3, 5, 6]`.
2. A complete `bubble_sort`. The `print` line shows every swap; you can leave it out.

```python
def bubble_sort(numbers):
    items = list(numbers)          # work on a copy
    for end in range(len(items) - 1, 0, -1):
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                print("swap:", items)
    return items


data = [6, 2, 5, 3]
print(bubble_sort(data))
print(sorted(data))
print(bubble_sort(data) == sorted(data))
print(data)
print(bubble_sort([]), bubble_sort([1]), bubble_sort([3, 3, 1]))
```

Output:

```output
swap: [2, 6, 5, 3]
swap: [2, 5, 6, 3]
swap: [2, 5, 3, 6]
swap: [2, 3, 5, 6]
[2, 3, 5, 6]
[2, 3, 5, 6]
swap: [2, 6, 5, 3]
swap: [2, 5, 6, 3]
swap: [2, 5, 3, 6]
swap: [2, 3, 5, 6]
True
[6, 2, 5, 3]
swap: [3, 1, 3]
swap: [1, 3, 3]
[] [1] [1, 3, 3]
```

3. The list after each swap is the four `swap:` lines above: 4 swaps in total. Pass 1 ends at `[2, 5, 3, 6]`. Pass 2 makes the last swap. Pass 3 finds nothing to swap.
4. Pass 2 starts with `end` equal to 2 and `i` equal to 0. `items` is `[2, 5, 3, 6]`.
5. `sorted()` gives `[2, 3, 5, 6]`, the same as your trace, and `data` is unchanged.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Further reading

- Driscoll, M. (2017) *Python 101*. Available at: https://web.archive.org/web/20260309033724/https://python101.pythonlibrary.org/ (Accessed: 2 November 2026).
- Romano, F. (2018) *Learn Python Programming*. 2nd edn. Birmingham: Packt Publishing.

:::::::::::::::::::::::::::::::::::::: keypoints

- Think first, type second.
- Pseudocode is a plan in plain English.
- The debugger lets you watch a program run line by line.

::::::::::::::::::::::::::::::::::::::::::::::::
