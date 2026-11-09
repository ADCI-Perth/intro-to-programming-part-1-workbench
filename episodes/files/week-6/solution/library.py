"""Library loan manager: Week 6 model solution (in memory).

The same Book and Library classes as Week 5, with search added.
"""


class Book:
    """One book. isbn is its unique identifier."""

    def __init__(self, title, author, isbn):
        """Store the details and mark the book as not on loan."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.on_loan = False

    def __str__(self):
        """Return a one-line description, such as 'Dune by ... - available'."""
        status = "on loan" if self.on_loan else "available"
        return f"{self.title} by {self.author} ({self.isbn}) - {status}"


class Library:
    """A collection of books, stored in a dictionary keyed by isbn."""

    def __init__(self):
        """Start with no books."""
        self.books = {}

    def add_book(self, book):
        """Store a book under its isbn."""
        self.books[book.isbn] = book

    def lend(self, isbn):
        """Mark a book as on loan. KeyError if unknown, ValueError if already out."""
        book = self.books[isbn]
        if book.on_loan:
            raise ValueError(f"{book.title} is already on loan")
        book.on_loan = True

    def return_book(self, isbn):
        """Mark a book as returned. KeyError if unknown, ValueError if not on loan."""
        book = self.books[isbn]
        if not book.on_loan:
            raise ValueError(f"{book.title} is not on loan")
        book.on_loan = False

    def available_books(self):
        """Return a list of the books that are not on loan."""
        return [book for book in self.books.values() if not book.on_loan]

    def search(self, text):
        """Return the books whose title or author contains text, ignoring case."""
        needle = text.lower()
        return [
            book
            for book in self.books.values()
            if needle in book.title.lower() or needle in book.author.lower()
        ]
