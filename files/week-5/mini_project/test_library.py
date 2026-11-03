"""Tests for the library loan manager, Part 1.

While you work, change MODULE_NAME to "library_starter" to test your own
code. Change it back to "library" to test the model solution.
"""

import importlib
import json

import pytest

MODULE_NAME = "library"

module = importlib.import_module(MODULE_NAME)
Book = module.Book
Library = module.Library


def make_library():
    library = Library()
    library.add_book(Book("Dune", "Frank Herbert", "111"))
    library.add_book(Book("Emma", "Jane Austen", "222"))
    return library


# ---- Book ---------------------------------------------------------------

def test_book_attributes():
    book = Book("Dune", "Frank Herbert", "111")
    assert book.title == "Dune"
    assert book.author == "Frank Herbert"
    assert book.isbn == "111"
    assert book.on_loan is False


def test_book_to_dict():
    assert Book("Dune", "Frank Herbert", "111").to_dict() == {
        "title": "Dune",
        "author": "Frank Herbert",
        "isbn": "111",
        "on_loan": False,
    }


def test_book_from_dict_round_trip():
    book = Book("Dune", "Frank Herbert", "111")
    book.on_loan = True
    copy = Book.from_dict(book.to_dict())
    assert isinstance(copy, Book)
    assert copy.to_dict() == book.to_dict()


def test_book_str():
    book = Book("Dune", "Frank Herbert", "111")
    assert str(book) == "Dune by Frank Herbert (111) - available"
    book.on_loan = True
    assert str(book) == "Dune by Frank Herbert (111) - on loan"


# ---- Library ------------------------------------------------------------

def test_new_library_is_empty():
    assert Library().books == {}


def test_add_book_keyed_by_isbn():
    library = make_library()
    assert set(library.books) == {"111", "222"}
    assert library.books["111"].title == "Dune"


def test_lend_marks_book_on_loan():
    library = make_library()
    library.lend("111")
    assert library.books["111"].on_loan is True
    assert library.books["222"].on_loan is False


def test_lend_unknown_isbn_raises_key_error():
    with pytest.raises(KeyError):
        make_library().lend("999")


def test_lend_twice_raises_value_error():
    library = make_library()
    library.lend("111")
    with pytest.raises(ValueError):
        library.lend("111")


def test_return_book():
    library = make_library()
    library.lend("111")
    library.return_book("111")
    assert library.books["111"].on_loan is False


def test_return_unknown_isbn_raises_key_error():
    with pytest.raises(KeyError):
        make_library().return_book("999")


def test_return_book_not_on_loan_raises_value_error():
    with pytest.raises(ValueError):
        make_library().return_book("111")


def test_available_books():
    library = make_library()
    library.lend("111")
    available = library.available_books()
    assert isinstance(available, list)
    assert [book.isbn for book in available] == ["222"]


# ---- Saving and loading -------------------------------------------------

def test_save_writes_json(tmp_path):
    library = make_library()
    library.lend("111")
    path = tmp_path / "library.json"
    library.save(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert len(data) == 2


def test_save_then_load_round_trip(tmp_path):
    library = make_library()
    library.lend("111")
    path = tmp_path / "library.json"
    library.save(path)

    other = Library()
    other.load(path)
    assert set(other.books) == {"111", "222"}
    assert other.books["111"].on_loan is True
    assert other.books["222"].on_loan is False
    assert isinstance(other.books["111"], Book)


def test_load_replaces_existing_books(tmp_path):
    path = tmp_path / "library.json"
    make_library().save(path)
    other = Library()
    other.add_book(Book("Old", "Someone", "000"))
    other.load(path)
    assert "000" not in other.books
    assert set(other.books) == {"111", "222"}


def test_load_missing_file_leaves_library_empty(tmp_path):
    library = Library()
    library.add_book(Book("Old", "Someone", "000"))
    library.load(tmp_path / "does_not_exist.json")
    assert library.books == {}
