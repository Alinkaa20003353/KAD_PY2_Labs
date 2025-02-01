class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """ Название книги """
        return self._name

    @property
    def author(self) -> str:
        """ Автор книги """
        return self._author

    def __str__(self) -> str:
        """ Представление книги """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        """ Строковое представление объекта для отладки """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """Проверка на корректность количества страниц."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __repr__(self) -> str:
        """Представление для отладки с учётом количества страниц."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Класс для аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Продолжительность аудиокниги в часах."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """Проверка на корректность продолжительности."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __repr__(self) -> str:
        """Представление для отладки с учётом продолжительности."""
        return f"{self.__class__.__name__}(name={self.name!r}, author = {self.author!r}, duration = {self.duration})"

# Проверка работы классов
if __name__ == "__main__":
    paper_book = PaperBook("Голодные игры", "Сьюзен Коллинз", 384)
    audio_book = AudioBook("Краткая история человечества", "Юваль Ной Харари", 16.5)

    print(paper_book)
    print(audio_book)

    print(repr(paper_book))
    print(repr(audio_book))

    # Проверка ошибок:
    try:
        paper_book.pages = -10  # Ошибка: отрицательное число
    except ValueError as e:
        print(e)

    try:
        audio_book.duration = "два часа"  # Ошибка: некорректный тип данных
    except ValueError as e:
        print(e)