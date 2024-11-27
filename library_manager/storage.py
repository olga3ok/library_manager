import json
from .book import Book


class StorageError(Exception):
    """Исключения для работы с хранилищем"""


class Storage:
    """ Класс для работы с хранилищем данных."""

    def __init__(self, filename: str = "library.json") -> None:
        self.filename = filename

    def save(self, library: object) -> None:
        """Сохраняет библиотеку в файл."""
        try:
            data = {
                "books": [book.to_dict() for book in library.books],
                "current_id": library.current_id,
            }
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise StorageError(f"Ошибка при сохранении данных: {e}")

    def load(self, library: object) -> None:
        """ Загружает данные из файла в библиотеку."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                library.books = [Book.from_dict(book) for book in data["books"]]
                library.current_id = data["current_id"]
        except FileNotFoundError:
            print("Файл не найден. Начинаем с пустой библиотеки.")
        except json.JSONDecodeError:
            raise StorageError("Ошибка декодирования файла данных.")
        except Exception as e:
            raise StorageError(f"Ошибка при загрузке данных: {e}")
