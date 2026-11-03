"""Library loan manager, Part 1: model solution."""

import json


class Book:
    """One book. isbn is its unique identifier."""

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.on_loan = False

    def to_dict(self):
        """Return the book as a plain dictionary (ready to save as JSON)."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "on_loan": self.on_loan,
        }

    @classmethod
    def from_dict(cls, data):
        """Build a Book from a dictionary made by to_dict()."""
        book = cls(data["title"], data["author"], data["isbn"])
        book.on_loan = data["on_loan"]
        return book

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

    def save(self, path):
        data = [book.to_dict() for book in self.books.values()]
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    def load(self, path):
        self.books = {}
        try:
            with open(path, encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return  # no saved file yet: stay empty
        for item in data:
            book = Book.from_dict(item)
            self.books[book.isbn] = book


if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Dune", "Frank Herbert", "111"))
    library.add_book(Book("Emma", "Jane Austen", "222"))
    library.lend("111")
    for book in library.books.values():
        print(book)
    library.save("library.json")
    print("Saved to library.json")
