"""Week 4 practice: rewrite the grade calculator in a functional style.

PART A (given): the imperative version, using loops and if/elif.
PART B (your job): rewrite it using comprehensions, map, filter and lambda,
and add try/except checking. Fill in each TODO.
"""

# ---------------------------------------------------------------------------
# PART A: the imperative version (given, already works). Read it first.
# ---------------------------------------------------------------------------

def average_loop(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


def grade_if(mark):
    if mark >= 85:
        return "HD"
    elif mark >= 75:
        return "D"
    elif mark >= 65:
        return "C"
    elif mark >= 50:
        return "P"
    else:
        return "F"


def grades_loop(marks):
    result = []
    for mark in marks:
        result.append(grade_if(mark))
    return result


def passing_loop(marks):
    result = []
    for mark in marks:
        if mark >= 50:
            result.append(mark)
    return result


def main_loop():
    marks = []
    text = input("Mark (empty line to finish): ")
    while text != "":
        marks.append(float(text))          # crashes on bad input!
        text = input("Mark (empty line to finish): ")
    print("Average:", average_loop(marks))
    print("Grades:", grades_loop(marks))
    print("Passing:", passing_loop(marks))


# ---------------------------------------------------------------------------
# PART B: your functional version.
# Keep the names below, because the tests look for them.
# ---------------------------------------------------------------------------

GRADE_ORDER = ["HD", "D", "C", "P", "F"]
PASS_MARK = 50


def parse_mark(text):
    """Return text as a float from 0 to 100, or None if it is not valid."""
    # TODO: use try/except ValueError around float(text).
    # TODO: return None if the mark is below 0 or above 100.
    pass


def valid_marks(texts):
    """Parse every text and keep only the valid marks (no None values)."""
    # TODO: one list comprehension, using map(parse_mark, texts).
    pass


def average(marks):
    """Average of the marks. An empty list gives 0.0 (no crash)."""
    # TODO: sum(marks) / len(marks), with try/except ZeroDivisionError.
    pass


def grade(mark):
    """Letter grade for one mark (same rules as grade_if)."""
    # TODO: copy your if/elif logic from grade_if.
    pass


def letter_grades(marks):
    """A new list of letter grades."""
    # TODO: use map() with grade.
    pass


def passing_marks(marks):
    """A new list holding only the marks that pass."""
    # TODO: use filter() with a lambda.
    pass


def grade_counts(marks):
    """A dictionary such as {"HD": 2, "D": 0, "C": 0, "P": 1, "F": 1}."""
    # TODO: a dictionary comprehension over GRADE_ORDER.
    pass


def main():
    # TODO: ask for marks with input() until an empty line.
    # TODO: tell the user when a mark is not valid, then carry on.
    # TODO: print the average, grades, passing marks and grade counts.
    pass


# Leave the next two lines as they are. They mean "run main() when this file is
# run directly". You will learn how they work in Week 6.
if __name__ == "__main__":
    main()
