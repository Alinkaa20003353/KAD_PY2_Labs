import doctest

class Car:
    """
    Класс описывает автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Создаёт объект автомобиля.

        :param brand: Марка автомобиля (например, "Toyota")
        :param model: Модель автомобиля (например, "Camry")
        :param year: Год выпуска автомобиля. Должен быть не меньше 1886 (год выпуска первого авто).
        """
        if year < 1886:
            raise ValueError("Год выпуска не может быть меньше 1886.")
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False  # Флаг: запущен ли двигатель

    def start_engine(self) -> None:
        """
        Запускает двигатель автомобиля.

        :return: None

        Пример использования (doctest):
        >>> my_car = Car("Toyota", "Camry", 2020)
        >>> my_car.start_engine()
        ...
        """
        self.is_running = True
        ...

    def stop_engine(self) -> None:
        """
        Глушит двигатель автомобиля.

        :return: None

        Пример использования (doctest):
        >>> my_car = Car("Toyota", "Camry", 2020)
        >>> my_car.start_engine()
        >>> my_car.stop_engine()
        ...
        """
        self.is_running = False
        ...

    def drive(self, distance: float) -> None:
        """
        Едет на заданное расстояние (условно).

        :param distance: Расстояние в километрах, должно быть >= 0
        :return: None

        Пример использования (doctest):
        >>> my_car = Car("Tesla", "Model S", 2021)
        >>> my_car.start_engine()
        >>> my_car.drive(10.0)
        ...
        """
        if distance < 0:
            raise ValueError("Нельзя ехать на отрицательное расстояние.")
        if not self.is_running:
            raise RuntimeError("Нельзя ехать: двигатель не запущен.")
        ...

class Book:
    """
    Класс описывает книгу.
    """

    def initit__(self, title: str, author: str, pages: int):
        """
        Создаёт объект книги.

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц (должно быть больше 0)
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1  # Текущая страница чтения

    def read_pages(self, number_of_pages: int) -> None:
        """
        «Читает» заданное количество страниц и двигает счётчик прочитанных.

        :param number_of_pages: Число страниц для чтения, >= 1
        :return: None

        Пример использования (doctest):
        >>> b = Book("Война и мир", "Лев Толстой", 1225)
        >>> b.read_pages(5)
        ...
        """
        if number_of_pages < 1:
            raise ValueError("Нужно читать хотя бы одну страницу.")
        if self.current_page + number_of_pages > self.pages:
            # Предположим, нельзя «выйти за пределы» книги
            raise ValueError("Столько страниц в книге нет.")
        self.current_page += number_of_pages
        ...

    def bookmark_page(self, page: int) -> None:
        """
        Ставит закладку на указанной странице (условно).

        :param page: Страница, на которую ставится закладка
        :return: None

        Пример использования (doctest):
        >>> b = Book("1984", "Джордж Оруэлл", 328)
        >>> b.bookmark_page(10)
        ...
        """
        if page < 1 or page > self.pages:
            raise ValueError("Некорректная страница для закладки.")
        ...

    def close(self) -> None:
        """
        «Закрывает» книгу, делая текущей страницей первую.

        :return: None

        Пример использования (doctest):
        >>> b = Book("Преступление и наказание", "Федор Достоевский", 500)
        >>> b.close()
        ...
        """
        self.current_page = 1
        ...

class Phone:
    """
    Класс описывает мобильный телефон.
    """

    def init(self, brand: str, model: str, battery_level: float):
        """
        Создаёт объект телефона.

        :param brand: Бренд (Samsung, Apple и т.д.)
        :param model: Модель (например, iPhone X)
        :param battery_level: Уровень заряда батареи (0..100)
        """
        if not (0 <= battery_level <= 100):
            raise ValueError("Уровень заряда должен быть в пределах 0..100%.")
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def call(self, phone_number: str, minutes: int) -> None:
        """
        Имитирует звонок на заданный номер на заданное время.

        :param phone_number: Номер, на который звонит пользователь
        :param minutes: Продолжительность звонка в минутах
        :return: None

        Пример использования (doctest):
        >>> p = Phone("Nokia", "3310", 50)
        >>> p.call("+1234567890", 2)
        ...
        """
        if minutes < 0:
            raise ValueError("Время звонка не может быть отрицательным.")
        if self.battery_level <= 0:
            raise RuntimeError("Батарея разряжена, звонок невозможен.")
        # Предположим, что на каждую минуту разговора уходит 1% заряда
        if self.battery_level - minutes < 0:
            raise RuntimeError("Недостаточно заряда для звонка.")
        self.battery_level -= minutes
        ...

    def charge(self, amount: float) -> None:
        """
        Заряжает телефон на заданный процент.

        :param amount: На сколько процентов зарядить (>= 0)
        :return: None
        Пример использования (doctest):
                >>> p = Phone("Xiaomi", "Mi10", 10)
                >>> p.charge(20)
                ...
                """
        if amount < 0:
            raise ValueError("Нельзя заряжать телефон отрицательным значением.")
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100
        ...

    def send_message(self, message: str) -> None:
        """
        Имитирует отправку текстового сообщения.

        :param message: Текст сообщения
        :return: None

        Пример использования (doctest):
        >>> p = Phone("Apple", "iPhone 12", 15)
        >>> p.send_message("Hello!")
        ...
        """
        if self.battery_level <= 0:
            raise RuntimeError("Батарея разряжена, отправка сообщения невозможна.")
        # Пусть отправка сообщения съедает 1% заряда
        self.battery_level -= 1
        if self.battery_level < 0:
            self.battery_level = 0
        ...

if __name__ == "__main__":
    doctest.testmod()