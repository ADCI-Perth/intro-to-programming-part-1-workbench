"""Week 4 practice: functional grade calculator (model solution)."""

GRADE_ORDER = ["HD", "D", "C", "P", "F"]
PASS_MARK = 50


def parse_mark(text):
    """Turn text into a mark from 0 to 100.

    Returns None (instead of crashing) if the text is not a valid mark.
    """
    try:
        mark = float(text)
    except ValueError:
        return None
    if mark < 0 or mark > 100:
        return None
    return mark


def valid_marks(texts):
    """Parse many pieces of text and keep only the valid marks."""
    return [m for m in map(parse_mark, texts) if m is not None]


def average(marks):
    """Average of a list of marks. An empty list gives 0.0."""
    try:
        return sum(marks) / len(marks)
    except ZeroDivisionError:
        return 0.0


def grade(mark):
    """Letter grade for one mark."""
    if mark >= 85:
        return "HD"
    elif mark >= 75:
        return "D"
    elif mark >= 65:
        return "C"
    elif mark >= PASS_MARK:
        return "P"
    return "F"


def letter_grades(marks):
    """A new list with the letter grade for every mark."""
    return list(map(grade, marks))


def passing_marks(marks):
    """A new list with only the marks that pass."""
    return list(filter(lambda m: m >= PASS_MARK, marks))


def grade_counts(marks):
    """How many of each letter grade, as a dictionary."""
    grades = letter_grades(marks)
    return {g: grades.count(g) for g in GRADE_ORDER}


def main():
    print("Enter marks from 0 to 100. Press Enter on an empty line to finish.")
    texts = []
    while True:
        text = input("Mark: ")
        if text == "":
            break
        if parse_mark(text) is None:
            print("  Not a valid mark, ignoring it.")
        else:
            texts.append(text)

    marks = valid_marks(texts)
    if not marks:
        print("No valid marks entered.")
        return

    print(f"Average: {average(marks):.1f}")
    print(f"Grades: {letter_grades(marks)}")
    print(f"Passing marks: {passing_marks(marks)}")
    print(f"Grade counts: {grade_counts(marks)}")


if __name__ == "__main__":
    main()
