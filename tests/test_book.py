import unittest
from library_manager.book import Book


class TestBook(unittest.TestCase):
    def test_book_creation(self):
        """Тестирует создание книги."""
        book = Book(1, "Название", "Автор", 2000)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Название")
        self.assertEqual(book.author, "Автор")
        self.assertEqual(book.year, 2000)
        self.assertEqual(book.status, "в наличии")

    def test_book_to_dict(self):
        """Тестирует преобразование книги в словарь."""
        book = Book(1, "Название", "Автор", 2000)
        book_dict = book.to_dict()
        expected_dict = {
            "id": 1,
            "title": "Название",
            "author": "Автор",
            "year": 2000,
            "status": "в наличии",
        }
        self.assertEqual(book_dict, expected_dict)

    def test_book_from_dict(self):
        """Тестирует создание книги из словаря."""
        book_dict = {
            "id": 1,
            "title": "Название",
            "author": "Автор",
            "year": 2000,
            "status": "выдана",
        }
        book = Book.from_dict(book_dict)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Название")
        self.assertEqual(book.author, "Автор")
        self.assertEqual(book.year, 2000)
        self.assertEqual(book.status, "выдана")
