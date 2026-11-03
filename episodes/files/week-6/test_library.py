"""Tests for the Week 6 mini project. Run: python -m pytest weeks/week-6/practice

To test your own work, set MINI_PROJECT_DIR to the folder holding your library.py
(see the README). Without it, the tests use the model solution.
"""

import os
import sys
from pathlib import Path

SOLUTION_DIR = Path(os.environ.get("MINI_PROJECT_DIR") or Path(__file__).parent / "solution")
sys.path.insert(0, str(SOLUTION_DIR))

import pytest  # noqa: E402

from library import Book, Library  # noqa: E402


@pytest.fixture
def library() -> Library:
    lib = Library()
    lib.add_book(Book("Dune", "Frank Herbert", "111"))
    lib.add_book(Book("Emma", "Jane Austen", "222"))
    lib.add_book(Book("Persuasion", "Jane Austen", "333"))
    return lib


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


def test_book_dict_round_trip():
    book = Book("Dune", "Frank Herbert", "111")
    book.on_loan = True
    copy = Book.from_dict(book.to_dict())
    assert copy.to_dict() == book.to_dict()
    assert "Dune" in str(book)


def test_book_str_matches_week_5():
    book = Book("Dune", "Frank Herbert", "111")
    assert str(book) == "Dune by Frank Herbert (111) - available"
    book.on_loan = True
    assert str(book) == "Dune by Frank Herbert (111) - on loan"


def test_save_load_round_trip(library, tmp_path):
    library.lend("222")
    path = tmp_path / "lib.json"
    library.save(path)
    loaded = Library()
    loaded.load(path)
    assert set(loaded.books) == {"111", "222", "333"}
    assert loaded.books["222"].on_loan is True
    assert loaded.books["111"].on_loan is False


def test_load_missing_file_gives_empty_library(tmp_path):
    lib = Library()
    lib.load(tmp_path / "nope.json")
    assert lib.books == {}
