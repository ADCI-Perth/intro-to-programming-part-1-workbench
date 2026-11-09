"""Library loan manager, Part 1: starter (in memory).

Fill in each TODO. Run test_library.py (see README.md) to check your work.
"""


class Book:
    """One book. isbn is its unique identifier."""

    def __init__(self, title, author, isbn):
        # TODO 1: store title, author and isbn on self.
        # Also set self.on_loan to False (a new book is not on loan).
        pass

    def __str__(self):
        # TODO 2: return text like
        #   "Dune by Frank Herbert (111) - available"
        # or "... - on loan" when the book is on loan.
        pass


class Library:
    """A collection of books, stored in a dictionary keyed by isbn."""

    def __init__(self):
        # TODO 3: create an empty dictionary called self.books.
        pass

    def add_book(self, book):
        # TODO 4: store the book in self.books using book.isbn as the key.
        pass

    def lend(self, isbn):
        # TODO 5: mark the book as on loan.
        #   - Unknown isbn: let a KeyError happen (self.books[isbn] does it).
        #   - Already on loan: raise ValueError("...").
        pass

    def return_book(self, isbn):
        # TODO 6: mark the book as not on loan.
        #   - Unknown isbn: KeyError.
        #   - Not on loan: raise ValueError("...").
        pass

    def available_books(self):
        # TODO 7: return a list of the Book objects that are not on loan.
        pass
