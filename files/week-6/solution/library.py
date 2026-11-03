"""Library-loan manager: Part 1 (Week 5) plus Part 2 (Week 6)."""

import json
from pathlib import Path


class Book:
    """One book in the library."""

    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.on_loan = False

    def to_dict(self) -> dict:
        """Turn the book into a dictionary so json can save it."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "on_loan": self.on_loan,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        """Build a Book from a dictionary made by to_dict()."""
        book = cls(data["title"], data["author"], data["isbn"])
        book.on_loan = data["on_loan"]
        return book

    def __str__(self) -> str:
        status = "on loan" if self.on_loan else "available"
        return f"{self.title} by {self.author} ({self.isbn}) - {status}"


class Library:
    """A collection of books, keyed by ISBN."""

    def __init__(self) -> None:
        self.books: dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        self.books[book.isbn] = book

    def lend(self, isbn: str) -> None:
        """Mark a book as on loan. KeyError if unknown, ValueError if already out."""
        book = self.books[isbn]
        if book.on_loan:
            raise ValueError(f"{book.title} is already on loan")
        book.on_loan = True

    def return_book(self, isbn: str) -> None:
        """Mark a book as returned. KeyError if unknown, ValueError if not on loan."""
        book = self.books[isbn]
        if not book.on_loan:
            raise ValueError(f"{book.title} is not on loan")
        book.on_loan = False

    def available_books(self) -> list[Book]:
        return [book for book in self.books.values() if not book.on_loan]

    def search(self, text: str) -> list[Book]:
        """Books whose title or author contains text (ignoring case)."""
        needle = text.lower()
        return [
            book
            for book in self.books.values()
            if needle in book.title.lower() or needle in book.author.lower()
        ]

    def save(self, path: str | Path) -> None:
        data = [book.to_dict() for book in self.books.values()]
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    def load(self, path: str | Path) -> None:
        """Replace the books with those in the file. A missing file gives an empty library."""
        self.books = {}
        try:
            with open(path, encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return
        for item in data:
            self.add_book(Book.from_dict(item))
