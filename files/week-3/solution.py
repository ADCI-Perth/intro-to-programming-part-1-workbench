"""Grade calculator - model solution (Week 3 practice task).

Pseudocode
----------
1. Ask for a subject name and a mark. Type "done" as the subject to stop.
2. Check the mark is a whole number from 0 to 100. If not, ask again.
3. Store each mark in a dictionary: subject -> mark.
4. When finished, work out the average, the highest mark and each grade.
5. Print a short report.
"""

PASS_MARK = 50


def average(marks):
    """Return the average of a list of marks. An empty list gives 0.0."""
    if len(marks) == 0:
        return 0.0
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


def grade(mark):
    """Return the grade letters for one mark from 0 to 100."""
    if mark >= 85:
        return "HD"
    elif mark >= 75:
        return "D"
    elif mark >= 65:
        return "C"
    elif mark >= PASS_MARK:
        return "P"
    else:
        return "F"


def is_valid_mark(mark):
    """Return True if mark is a number from 0 to 100 (inclusive)."""
    return 0 <= mark <= 100


def highest(marks):
    """Return the largest mark in a list. An empty list gives None."""
    if len(marks) == 0:
        return None
    best = marks[0]
    for mark in marks:
        if mark > best:
            best = mark
    return best


def grades_for(marks_by_subject):
    """Return a dictionary of subject -> grade from a dictionary of subject -> mark."""
    result = {}
    for subject in marks_by_subject:
        result[subject] = grade(marks_by_subject[subject])
    return result


def main():
    marks_by_subject = {}
    print("Grade calculator. Type done as the subject name to finish.")

    while True:
        subject = input("Subject: ")
        if subject == "done":
            break

        text = input("Mark (0 to 100): ")
        # isdigit() is True only for whole numbers such as "72".
        if not text.isdigit():
            print("Please enter a whole number.")
            continue

        mark = int(text)
        if not is_valid_mark(mark):
            print("A mark must be from 0 to 100.")
            continue

        marks_by_subject[subject] = mark

    if len(marks_by_subject) == 0:
        print("No marks entered.")
        return

    marks = list(marks_by_subject.values())
    grades = grades_for(marks_by_subject)

    print()
    for subject in marks_by_subject:
        print(f"{subject}: {marks_by_subject[subject]} ({grades[subject]})")
    print(f"Average: {average(marks):.1f} ({grade(average(marks))})")
    print(f"Highest: {highest(marks)}")


if __name__ == "__main__":
    main()
