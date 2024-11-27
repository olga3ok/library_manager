from .library import Library, BookNotFoundError
from .storage import Storage


class Menu:
    """Класс меню приложения для взаимодействия с пользователем."""

    def __init__(self):
        self.library = Library()
        self.storage = Storage()
        self.load_data()
        self.flag = 1

        # Словарь для вызова методов по выбору пользователя
        self.choices = {
            "1": self.add_book,
            "2": self.remove_book,
            "3": self.search_books,
            "4": self.display_all_books,
            "5": self.change_status,
            "0": self.exit_program,
        }

    def load_data(self) -> None:
        """Загружает данные из хранилища"""
        try:
            self.storage.load(self.library)
            print("Данные успешно загружены.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")


    def save_data(self) -> None:
        """Сохраняет данные в хранилище."""
        try:
            self.storage.save(self.library)
            print("Данные успешно сохранены")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def display_menu(self) -> None:
        """Отображает основное меню для взаимодействия с приложением."""
        print("\033[1;37m\n▐░░░░░░░ МЕНЮ ░░░░░░░░▌\033[0m")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выйти")

    def add_book(self) -> None:
        """Добавляет новую книгу"""
        print("Добавление книги.")
        try:
            title = input("Введите название книги: ").strip()
            if not title:
                raise ValueError

            author = input("Введите автора книги: ").strip()
            if not author:
                raise ValueError

            year = int(input("Введите год издания книги: ").strip())
            if len(str(year)) > 4 or not year:
                raise ValueError

            book = self.library.add_book(title, author, year)
            print(f"Книга '{book.title}' добавлена с ID {book.id}.")
            self.save_data()
        except ValueError:
            print("Ошибка: поля названия книги, автора, года издания не могут быть пустыми, год издания должен быть числом в формате YYYY.")
        except Exception as e:
            print('Ошибка: ', e)

    def remove_book(self) -> None:
        """Удаляет книгу по ID."""
        print("Удаление книги.")
        try:
            book_id = int(input("Введите ID книги для удаления: ").strip())
            if not isinstance(book_id, int) or not book_id:
                raise ValueError('ID книги должен быть числом.')
            self.library.remove_book(book_id)
            print(f"Книга с ID {book_id} удалена.")
            self.save_data()
        except BookNotFoundError as e:
            print(f"Ошибка: {e}")

    def search_books(self) -> None:
        """Поиск книги по ключевому слову"""
        print("Поиск книги.")
        keyword = input("Введите ключевое слово для поиска (название книги/имя автора/год издания): ").strip()
        results = self.library.search_books(keyword)
        if results:
            print(f"Найдено книг: {len(results)}")
            print(f"{'ID':<9} | {'TITLE':<20} | {'AUTHOR':<20} | {'YEAR':<20} | {'STATUS':<20}")
            print(f"{'-' * 91}")
            for book in results:
                print(book)
        else:
            print("Книги не найдены.")

    def display_all_books(self) -> None:
        """Показыает список всех книг."""
        try:
            books = self.library.display_all_books()
            if books:
                print("Список книг: ")
                print(f"{'ID':<9} | {'TITLE':<20} | {'AUTHOR':<20} | {'YEAR':<20} | {'STATUS':<20}")
                print(f"{'-' * 91}")
                for book in books:
                    print(book)
            else:
                print("Библиотека пуста. Чтобы добавить новую книгу, выберите пункт 1.")
        except Exception as e:
            print(e)

    def change_status(self) -> None:
        """Изменяет статус книги."""
        print("Изменение статуса книги.")
        try:
            book_id = int(input("Введите ID книги: ").strip())
            status = input("Укажите новый статус книги (в наличии/выдана): ").strip()

            book = self.library.change_status(book_id, status)
            print(f"Статус книги '{book.title}' изменён на '{book.status}'.")
            self.save_data()
        except BookNotFoundError as e:
            print(f"Ошибка: {e}")
        except ValueError as e:
            print(f"Ошибка: ID книги должен быть числом, статус может быть только \"в наличии\"/\"выдана\"")

    def exit_program(self) -> None:
        """Сохраняет данные и завершает программу."""
        self.save_data()
        print("Выход из программы.")
        exit(0)

    def run(self) -> None:
        """Запускает главное меню."""
        while True:
            self.display_menu()
            choice = input("\nВыберите действие: ").strip()
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("Неверный пункт меню. Попробуйте снова.")
