"""Tests for the Week 4 practice task.

To test your own work, change the import below from `solution` to `starter`.
"""

import solution as calc


def test_parse_mark_valid():
    assert calc.parse_mark("72") == 72.0
    assert calc.parse_mark(" 85.5 ") == 85.5
    assert calc.parse_mark("0") == 0.0
    assert calc.parse_mark("100") == 100.0


def test_parse_mark_invalid_returns_none():
    assert calc.parse_mark("abc") is None
    assert calc.parse_mark("") is None
    assert calc.parse_mark("101") is None
    assert calc.parse_mark("-5") is None


def test_valid_marks_skips_bad_input():
    assert calc.valid_marks(["70", "oops", "", "105", "55.5"]) == [70.0, 55.5]


def test_average():
    assert calc.average([60, 70, 80]) == 70
    assert calc.average([]) == 0.0


def test_grade_boundaries():
    assert calc.grade(100) == "HD"
    assert calc.grade(85) == "HD"
    assert calc.grade(84.9) == "D"
    assert calc.grade(75) == "D"
    assert calc.grade(65) == "C"
    assert calc.grade(50) == "P"
    assert calc.grade(49.9) == "F"
    assert calc.grade(0) == "F"


def test_letter_grades():
    assert calc.letter_grades([90, 76, 66, 55, 10]) == ["HD", "D", "C", "P", "F"]


def test_passing_marks():
    assert calc.passing_marks([90, 49, 50, 10]) == [90, 50]


def test_grade_counts():
    counts = calc.grade_counts([90, 95, 55, 10])
    assert counts == {"HD": 2, "D": 0, "C": 0, "P": 1, "F": 1}


def test_functions_do_not_change_their_input():
    marks = [90, 49, 50]
    copy = list(marks)
    calc.letter_grades(marks)
    calc.passing_marks(marks)
    calc.grade_counts(marks)
    assert marks == copy
