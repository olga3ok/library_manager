import unittest
from library_manager.library import Library, BookNotFoundError


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создает новый объект библиотеки перед каждым тестом"""
        self.library = Library()

    def test_add_book(self):
        """Тестирует добавление книги."""
        book = self.library.add_book("Название", "Автор", 2000)
        self.assertEqual(book.title, "Название")
        self.assertEqual(book.author, "Автор")
        self.assertEqual(book.year, 2000)

    def test_remove_book(self):
        """Тестирует удаление книги."""
        book = self.library.add_book("Название", "Автор", 2000)
        self.library.remove_book(book.id)
        self.assertEqual(len(self.library.books), 0)

        with self.assertRaises(BookNotFoundError):
            self.library.remove_book(999)

    def test_search_books(self):
        """Тестирует поиск книг по ключевому слову"""
        self.library.add_book("Название", "Автор", 2000)
        self.library.add_book("Другое название", "Другой автор", 2001)

        results = self.library.search_books("название")
        self.assertEqual(len(results), 2)

        results = self.library.search_books("Автор")
        self.assertEqual(len(results), 2)

        results = self.library.search_books("Другой")
        self.assertEqual(len(results), 1)

        results = self.library.search_books("Неизвестно")
        self.assertEqual(len(results), 0)

    def test_change_status(self):
        """Тестирует изменение статуса книги."""
        book = self.library.add_book("Название", "Автор", 2000)
        self.library.change_status(book.id, "выдана")
        self.assertEqual(book.status, "выдана")

        with self.assertRaises(BookNotFoundError):
            self.library.change_status(999, "выдана")

        with self.assertRaises(ValueError):
            self.library.change_status(book.id, "неизвестный статус")

    def test_display_all_books(self):
        """Тестирует отображение всех книг"""
        self.library.add_book("Название", "Автор", 2000)
        self.library.add_book("Другое название", "Другой автор", 2001)
        displayed_books = self.library.display_all_books()
        self.assertEqual(len(displayed_books), 2)


if __name__ == "__main__":
    unittest.main()


