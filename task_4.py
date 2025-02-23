class Vehicle:
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        - brand (str): Бренд транспортного средства.
        - model (str): Модель транспортного средства.
        - year (int): Год выпуска.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска (не может быть меньше 1886).
        """
        if year < 1886:
            raise ValueError("Год выпуска не может быть раньше 1886 года.")

        self._brand = brand
        self._model = model
        self.year = year

    @property
    def brand(self) -> str:
        """Геттер для марки автомобиля."""
        return self._brand

    @property
    def model(self) -> str:
        """Геттер для модели автомобиля."""
        return self._model

    def move(self) -> str:
        """
        Перемещение транспортного средства.
        Метод будет переопределяться в дочерних классах.

        :return: Строка с сообщением о движении.
        """
        return f"{self.brand} {self.model} движется."

    def __str__(self) -> str:
        """
        Строковое представление объекта.

        :return: Описание транспортного средства.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Формальное представление объекта для отладки.

        :return: Строка с информацией об объекте.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year})"


class Car(Vehicle):
    """
    Класс легкового автомобиля.

    Атрибуты:
        - fuel_type (str): Тип топлива (бензин, дизель, электричество).
    """

    def __init__(self, brand: str, model: str, year: int, fuel_type: str):
        """
        Инициализация легкового автомобиля.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param fuel_type: Тип топлива (бензин, дизель, электричество).
        """
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def move(self) -> str:
        """
        Переопределённый метод движения.
        В отличие от базового метода, добавляет информацию о типе топлива.

        :return: Строка с сообщением о движении автомобиля.
        """
        return f"{self.brand} {self.model} едет на {self.fuel_type}."

    def __repr__(self) -> str:
        """
        Формальное представление объекта для отладки.

        :return: Строка с информацией об объекте.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year}, fuel_type={self.fuel_type!r})"


class Truck(Vehicle):
    """
    Класс грузового автомобиля.

    Атрибуты:
        - max_load_capacity (float): Максимальная грузоподъёмность в тоннах.
    """

    def __init__(self, brand: str, model: str, year: int, max_load_capacity: float):
        """
        Инициализация грузового автомобиля.

        :param brand: Марка грузовика.
        :param model: Модель грузовика.
        :param year: Год выпуска.
        :param max_load_capacity: Грузоподъёмность в тоннах.
        """
        super().__init__(brand, model, year)
        if max_load_capacity <= 0:
            raise ValueError("Грузоподъёмность должна быть положительной.")
        self.max_load_capacity = max_load_capacity

    def move(self) -> str:
        """
        Переопределённый метод движения.
        У грузовика важно учитывать нагрузку, поэтому добавляется информация о грузоподъёмности.

        :return: Строка с сообщением о движении грузовика.
        """
        return f"{self.brand} {self.model} перевозит груз до {self.max_load_capacity} тонн."

    def __repr__(self) -> str:
        """
        Формальное представление объекта для отладки.

        :return: Строка с информацией об объекте.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year}, max_load_capacity={self.max_load_capacity})"


# Тестирование
if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2022, "бензин")
    truck = Truck("Volvo", "FH16", 2021, 30.5)

    print(car)
    print(truck)

    print(car.move())
    print(truck.move())

    print(repr(car))
    print(repr(truck))

    # Проверка валидации
    try:
        invalid_truck = Truck("MAN", "TGS", 2023, -5)
    except ValueError as e:
        print(e)


