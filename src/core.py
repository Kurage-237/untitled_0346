from abc import ABC, abstractmethod


class Category:
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_products = 0
        for x in self.__products:
            total_products += x.quantity
        return f"{self.name}, количество продуктов: {total_products} шт."

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Объект должен быть дочерним от класса Product")

    def middle_price(self):
        price_sum = 0.0
        try:
            for x in self.__products:
                price_sum += x.price
            return price_sum / len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        result = []
        for x in self.__products:
            result.append(str(x))
        return str(result)


class BaseProduct(ABC):

    # noinspection PyUnusedLocal
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass # pragma: no cover

    @abstractmethod
    def __str__(self):
        pass # pragma: no cover

    @abstractmethod
    def __add__(self, other):
        pass # pragma: no cover

    @classmethod
    @abstractmethod
    def new_product(cls, params):
        pass # pragma: no cover

    @property
    @abstractmethod
    def price(self):
        pass # pragma: no cover

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass # pragma: no cover


class InitPrintMixin:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({str(self.__dict__)[1:-1]})"


class Product(InitPrintMixin, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0 :
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) == type(other):
            a = self.__price * self.quantity
            b = other.__price * other.quantity
            return a + b
        else:
            raise TypeError("Типы продуктов должны быть одинаковыми")

    @classmethod
    def new_product(cls, params):
        return cls(**params)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("“Цена не должна быть нулевая или отрицательная”")
        else:
            self.__price = new_price


class Smartphone(Product):
    efficiency: int
    model: str
    memory: float
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: int,
        model: str,
        memory: float,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: float
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: float,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
