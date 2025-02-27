class Book:
    """Класс, представляющий книгу."""

    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация экземпляра книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Возвращает строку, по которой можно создать такой же экземпляр."""
        return f"Book(id_={self.id}, name={self.name!r}, pages={self.pages})"


class Library:
    """Класс, представляющий библиотеку книг."""

    def __init__(self, books: list[Book] = None):
        """
        Инициализация библиотеки.

        :param books: Необязательный список книг (по умолчанию пустой список).
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий доступный идентификатор книги.

        :return: Следующий ID (1, если книг нет, иначе ID последней книги + 1).
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по ее ID.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с указанным ID нет в библиотеке.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


BOOKS_DATABASE = [
    {"id": 1, "name": "test_name_1", "pages": 200},
    {"id": 2, "name": "test_name_2", "pages": 400},
]

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверяем следующий ID для пустой библиотеки (должен быть 1)

    # Создаем список книг
    list_books = [Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in
                  BOOKS_DATABASE]

    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий ID (должен быть 3)

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с ID = 1 (должен быть 0)
