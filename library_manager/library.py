from .book import Book


class LibraryError(Exception):
    """Базовое исключение для Library"""


class BookNotFoundError(LibraryError):
    """Исключение, возникающее при отсутствии книги."""


class Library:
    """
    Класс для управления библиотекой&
    """

    def __init__(self) -> None:
        """ Инициализация библиотеки. """

        self.books = []
        self.current_id = 1

    def add_book(self, title: str, author: str, year: int) -> object:
        """
        Добавляет новую книгу в библиотеку.
        :param title: название книги
        :param author: автор книги
        :param year: год издания книги
        :return: объект новой книги
        """
        book = Book(self.current_id, title, author, year)
        self.books.append(book)
        self.current_id += 1
        return book

    def remove_book(self, book_id: int) -> None:
        """ Удаляет книгу из библиотеки по ID. """
        initial_length = len(self.books)
        self.books = [book for book in self.books if book.id != book_id]
        if len(self.books) == initial_length:
            raise BookNotFoundError(f"Книга с ID {book_id} не найдена.")

    def search_books(self, keyword: str) -> list:
        """ Ищет книги по ключевому слову. """
        if not keyword:
            raise ValueError("Ключевое слово для поиска не может быть пустым.")
        return [
            book for book in self.books
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword == str(book.id) or keyword == str(book.year)
        ]

    def change_status(self, book_id: int, status: str) -> object:
        """ Изменяет статус книги. """
        if status not in ("в наличии", "выдана"):
            raise ValueError("Статус может быть только 'в наличии' или 'выдана'.")
        for book in self.books:
            if book.id == book_id:
                book.status = status
                return book
        raise BookNotFoundError(f"Книга с ID {book_id} не найдена.")

    def display_all_books(self) -> list:
        """Возвращает список всех книг с сортировкой."""
        return self.books
