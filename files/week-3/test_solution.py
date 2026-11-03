"""Tests for the grade calculator.

To test your own work, change `solution` to `starter` on the next line.
"""
from solution import average, grade, grades_for, highest, is_valid_mark


def test_average_of_several_marks():
    assert average([80, 70, 90]) == 80


def test_average_with_decimal_result():
    assert average([50, 51]) == 50.5


def test_average_of_empty_list_is_zero():
    assert average([]) == 0.0


def test_grade_boundaries():
    assert grade(100) == "HD"
    assert grade(85) == "HD"
    assert grade(84) == "D"
    assert grade(75) == "D"
    assert grade(74) == "C"
    assert grade(65) == "C"
    assert grade(64) == "P"
    assert grade(50) == "P"
    assert grade(49) == "F"
    assert grade(0) == "F"


def test_is_valid_mark():
    assert is_valid_mark(0)
    assert is_valid_mark(100)
    assert is_valid_mark(72)
    assert not is_valid_mark(-1)
    assert not is_valid_mark(101)


def test_highest():
    assert highest([55, 91, 70]) == 91
    assert highest([40]) == 40
    assert highest([]) is None


def test_grades_for():
    marks = {"Maths": 90, "English": 66, "Art": 30}
    assert grades_for(marks) == {"Maths": "HD", "English": "C", "Art": "F"}
