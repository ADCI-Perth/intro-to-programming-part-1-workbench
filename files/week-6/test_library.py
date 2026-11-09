"""Tests for the Week 6 mini project: library.py, and main.py run as a menu.

To test your own work, set MINI_PROJECT_DIR to the folder holding your
library.py and main.py (see the README). Without it, the tests use the
model solution in solution/.
"""

import os
import subprocess
import sys
from pathlib import Path

import pytest

SOLUTION_DIR = Path(os.environ.get("MINI_PROJECT_DIR") or Path(__file__).parent / "solution")
sys.path.insert(0, str(SOLUTION_DIR))

from library import Book, Library  # noqa: E402


@pytest.fixture
def library():
    lib = Library()
    lib.add_book(Book("Dune", "Frank Herbert", "111"))
    lib.add_book(Book("Emma", "Jane Austen", "222"))
    lib.add_book(Book("Persuasion", "Jane Austen", "333"))
    return lib


# ---- Library ------------------------------------------------------------

def test_search_by_title_ignores_case(library):
    assert [b.isbn for b in library.search("dUnE")] == ["111"]


def test_search_by_author(library):
    assert {b.isbn for b in library.search("austen")} == {"222", "333"}


def test_search_no_match(library):
    assert library.search("zzz") == []


def test_lend_and_available(library):
    library.lend("111")
    assert library.books["111"].on_loan is True
    assert {b.isbn for b in library.available_books()} == {"222", "333"}


def test_lend_errors(library):
    with pytest.raises(KeyError):
        library.lend("999")
    library.lend("111")
    with pytest.raises(ValueError):
        library.lend("111")


def test_return_errors(library):
    with pytest.raises(KeyError):
        library.return_book("999")
    with pytest.raises(ValueError):
        library.return_book("111")
    library.lend("111")
    library.return_book("111")
    assert library.books["111"].on_loan is False


def test_book_str_matches_week_5():
    book = Book("Dune", "Frank Herbert", "111")
    assert str(book) == "Dune by Frank Herbert (111) - available"
    book.on_loan = True
    assert str(book) == "Dune by Frank Herbert (111) - on loan"


# ---- main.py as a menu ---------------------------------------------------

def run_menu(*answers):
    """Run main.py, typing each answer on its own line. Return the output."""
    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=SOLUTION_DIR,
        input="\n".join(answers) + "\n",
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


def test_menu_add_then_list():
    out = run_menu("1", "Dune", "Frank Herbert", "111", "2", "6")
    assert "Book added." in out
    assert "Dune by Frank Herbert (111) - available" in out


def test_menu_bad_choice_shows_hint():
    out = run_menu("9", "6")
    assert "Please enter a number from 1 to 6." in out


def test_menu_unknown_isbn_does_not_crash():
    out = run_menu("3", "999", "6")
    assert "No book with that ISBN." in out


def test_menu_refuses_empty_fields():
    out = run_menu("1", "", "Frank Herbert", "111", "6")
    assert "cannot be empty" in out
    assert "Book added." not in out


def test_menu_search():
    out = run_menu("1", "Dune", "Frank Herbert", "111", "5", "herbert", "6")
    assert out.count("Dune by Frank Herbert (111) - available") == 1
    assert "No matches." not in out


def test_menu_quit_says_books_are_not_saved():
    out = run_menu("6")
    assert "Books are not saved yet." in out
