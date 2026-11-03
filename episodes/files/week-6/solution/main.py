"""Text menu for the library-loan manager."""

from library import Book, Library

DATA_FILE = "library.json"

MENU = """
1. Add a book
2. List available books
3. Lend a book
4. Return a book
5. Search
6. Save and quit
"""


def add_book(library: Library) -> None:
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()
    if not title or not author or not isbn:
        print("Title, author and ISBN cannot be empty.")
        return
    library.add_book(Book(title, author, isbn))
    print("Book added.")


def list_available(library: Library) -> None:
    books = library.available_books()
    if not books:
        print("No books available.")
    for book in books:
        print(book)


def lend_book(library: Library) -> None:
    isbn = input("ISBN to lend: ").strip()
    try:
        library.lend(isbn)
        print("Lent.")
    except KeyError:
        print("No book with that ISBN.")
    except ValueError as error:
        print(error)


def return_book(library: Library) -> None:
    isbn = input("ISBN to return: ").strip()
    try:
        library.return_book(isbn)
        print("Returned.")
    except KeyError:
        print("No book with that ISBN.")
    except ValueError as error:
        print(error)


def search_books(library: Library) -> None:
    text = input("Search for: ").strip()
    results = library.search(text)
    if not results:
        print("No matches.")
    for book in results:
        print(book)


def main() -> None:
    library = Library()
    library.load(DATA_FILE)
    while True:
        print(MENU)
        try:
            choice = input("Choose 1-6: ").strip()
        except EOFError:
            choice = "6"
        if choice == "1":
            add_book(library)
        elif choice == "2":
            list_available(library)
        elif choice == "3":
            lend_book(library)
        elif choice == "4":
            return_book(library)
        elif choice == "5":
            search_books(library)
        elif choice == "6":
            library.save(DATA_FILE)
            print("Saved. Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
