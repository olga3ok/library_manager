import unittest
import os
from library_manager.library import Library
from library_manager.storage import Storage


class TestStorage(unittest.TestCase):
    def setUp(self) -> None:
        """Создает временные данные для тестирования."""
        self.library = Library()
        self.storage = Storage("test_library.json")
        self.library.add_book("Название", "Автор", 2000)
        self.library.add_book("Другое название", "Другой автор", 2001)

    def tearDown(self):
        """Удаляет временные файлы после теста."""
        if os.path.exists("test_library.json"):
            os.remove("test_library.json")

    def test_save_and_load(self):
        """Тестирует сохранение и загрузку данных."""
        # Сохраняем данные
        self.storage.save(self.library)

        # Загружаем данные в новую библиотеку
        new_library = Library()
        self.storage.load(new_library)

        self.assertEqual(len(new_library.books), 2)
        self.assertEqual(new_library.books[0].title, "Название")
        self.assertEqual(new_library.books[1].year, 2001)

    def test_load_nonexistent_file(self):
        """Тестирует загрузку при отсутствии файла."""
        if os.path.exists("test_library.json"):
            os.remove("test_library.json")

        new_library = Library()
        self.storage.load(new_library)

        self.assertEqual(len(new_library.books), 0)

    def test_save_error_handling(self):
        """Тестирует обработку ошибок при сохранении."""
        self.storage.filename = "/invalid_path/test_library.json"
        with self.assertRaises(Exception):
            self.storage.save(self.library)


if __name__ == "__main__":
    unittest.main()

