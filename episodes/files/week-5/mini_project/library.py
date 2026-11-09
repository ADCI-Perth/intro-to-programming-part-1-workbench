"""Library loan manager, Part 1: model solution (in memory)."""


class Book:
    """One book. isbn is its unique identifier."""

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.on_loan = False

    def __str__(self):
        status = "on loan" if self.on_loan else "available"
        return f"{self.title} by {self.author} ({self.isbn}) - {status}"


class Library:
    """A collection of books, stored in a dictionary keyed by isbn."""

    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def lend(self, isbn):
        book = self.books[isbn]  # raises KeyError if the isbn is unknown
        if book.on_loan:
            raise ValueError(f"{book.title} is already on loan")
        book.on_loan = True

    def return_book(self, isbn):
        book = self.books[isbn]  # raises KeyError if the isbn is unknown
        if not book.on_loan:
            raise ValueError(f"{book.title} is not on loan")
        book.on_loan = False

    def available_books(self):
        return [book for book in self.books.values() if not book.on_loan]


if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Dune", "Frank Herbert", "111"))
    library.add_book(Book("Emma", "Jane Austen", "222"))
    library.lend("111")
    for book in library.available_books():
        print(book)
