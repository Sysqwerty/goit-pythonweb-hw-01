import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    format="%(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: str) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, title: str, author: str, year: str) -> None:
        self.books.append(Book(title, author, year))

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                break

    def show_books(self) -> None:
        for book in self.books:
            logging.info(book)


class LibraryManager(LibraryInterface):
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        self.library.add_book(title, author, year)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
