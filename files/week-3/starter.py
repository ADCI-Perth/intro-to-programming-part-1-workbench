"""Grade calculator - starter (Week 3 practice task).

Write your pseudocode here first, as comments:
# 1. ...
# 2. ...
"""

PASS_MARK = 50


def average(marks):
    """Return the average of a list of marks. An empty list gives 0.0."""
    # TODO: if the list is empty, return 0.0
    # TODO: add up the marks with a for loop, then divide by how many there are
    pass


def grade(mark):
    """Return "HD", "D", "C", "P" or "F" for one mark from 0 to 100."""
    # TODO: use if / elif / else
    # HD 85+, D 75-84, C 65-74, P 50-64, F below 50
    pass


def is_valid_mark(mark):
    """Return True if mark is from 0 to 100 (inclusive), otherwise False."""
    # TODO
    pass


def highest(marks):
    """Optional stretch: return the largest mark. An empty list gives None."""
    # TODO: use a loop. Do not use max().
    pass


def grades_for(marks_by_subject):
    """Turn {"Maths": 90} into {"Maths": "HD"}."""
    # TODO: make an empty dictionary, loop over the subjects, call grade()
    pass


def main():
    marks_by_subject = {}
    # TODO: while True loop. Ask for a subject ("done" stops) and a mark.
    # TODO: reject marks that are not whole numbers (text.isdigit()) or not 0-100
    # TODO: store each mark in marks_by_subject
    # TODO: print each subject, mark and grade, then the average and highest mark
    pass


# Leave the next two lines as they are. They run main() when you click Run.
# Week 6 explains why.
if __name__ == "__main__":
    main()
