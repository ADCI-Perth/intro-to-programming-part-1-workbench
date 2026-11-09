"""Tests for the library loan manager, Part 1 (in memory).

While you work, change MODULE_NAME to "library_starter" to test your own
code. Change it back to "library" to test the model solution.
"""

import importlib

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
