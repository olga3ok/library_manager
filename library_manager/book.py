

class Book:
    """
    Класс, описывающий книгу в библиотеке
    """
    def __init__(self, book_id: int, title: str, author: str, year: int, status = "в наличии") -> None:
        """
        Инициализация книги.

        :param book_id: Уникальный идентификатор книги
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        :param status: Статус книги ("в наличии", "выдана")
        """
        self.id: int = book_id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status

    def __str__(self) -> str:
        """ Возвращает строковое представление книги. """
        return f"[ID: {self.id:<3}] | {self.title:<20} | {self.author:<20} | {self.year:<20} | {self.status:<20}"
        # return f"[ID: {self.id}] {self.title} - {self.author} ({self.year}), статус: {self.status}"

    def to_dict(self) -> dict:
        """ Возвращает словарь с данными книги. """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> object:
        """
        Возвращает объект Book из словаря.
        :param data: словарь с данными для создания объекта
        :return: объект Book
        """
        return Book(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"]
        )

    def get_book_id(self) -> int:
        """ Возвращает id книги. """
        return self.id

