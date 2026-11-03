"""Library loan manager, Part 1: starter.

Fill in each TODO. Run test_library.py (see README.md) to check your work.
"""

import json


class Book:
    """One book. isbn is its unique identifier."""

    def __init__(self, title, author, isbn):
        # TODO 1: store title, author and isbn on self.
        # Also set self.on_loan to False (a new book is not on loan).
        pass

    def to_dict(self):
        """Return the book as a plain dictionary (ready to save as JSON)."""
        # TODO 2: return a dictionary with the keys
        # "title", "author", "isbn" and "on_loan".
        pass

    # ---- Pre-written for you ------------------------------------------
    # @classmethod marks a method that belongs to the class itself, not to
    # one object. "cls" means "this class", so cls(...) makes a new Book.
    # Book.from_dict(data) rebuilds a Book from the dictionary that
    # to_dict() produced. You do not need to change it.
    @classmethod
    def from_dict(cls, data):
        book = cls(data["title"], data["author"], data["isbn"])
        book.on_loan = data["on_loan"]
        return book
    # --------------------------------------------------------------------

    def __str__(self):
        # TODO 3: return text like
        #   "Dune by Frank Herbert (111) - available"
        # or "... - on loan" when the book is on loan.
        pass


class Library:
    """A collection of books, stored in a dictionary keyed by isbn."""

    def __init__(self):
        # TODO 4: create an empty dictionary called self.books.
        pass

    def add_book(self, book):
        # TODO 5: store the book in self.books using book.isbn as the key.
        pass

    def lend(self, isbn):
        # TODO 6: mark the book as on loan.
        #   - Unknown isbn: let a KeyError happen (self.books[isbn] does it).
        #   - Already on loan: raise ValueError("...").
        pass

    def return_book(self, isbn):
        # TODO 7: mark the book as not on loan.
        #   - Unknown isbn: KeyError.
        #   - Not on loan: raise ValueError("...").
        pass

    def available_books(self):
        # TODO 8: return a list of the Book objects that are not on loan.
        pass

    def save(self, path):
        # Pre-written for you. Read it: it turns each book into a dictionary,
        # then writes the list to the file as JSON (Section 5.2).
        data = [book.to_dict() for book in self.books.values()]
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    def load(self, path):
        # TODO 9: replace self.books with the books stored in the file.
        # Use try/except FileNotFoundError: if the file is missing, leave
        # the library empty. Otherwise use json.load, then Book.from_dict
        # for each item.
        pass
