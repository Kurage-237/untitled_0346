import random
from typing import Tuple

import pytest

from src.core import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def init_n_products_inside_test_category() -> Tuple:
    n = random.randint(10, 20)
    test_category = Category("test1", "test2", [])
    for x in range(n):
        test_category.add_product(
            Product.new_product({"name": "test1", "description": "test2", "price": n, "quantity": n})
        )
    return test_category, n


def test_init_n_products_inside_test_category(init_n_products_inside_test_category) -> None:
    test_category = init_n_products_inside_test_category[0]
    n = init_n_products_inside_test_category[1]

    assert test_category.name == "test1"
    assert test_category.description == "test2"
    assert len(test_category.products) == len(f"test1, {n} руб. Остаток: {n} шт.") * n + (4 * n)
    assert test_category.category_count == 1
    assert test_category.product_count == n
    assert str(test_category) == f"{test_category.name}, количество продуктов: {n*n} шт."


def test_product_init():
    test_product = Product.new_product({"name": "test1", "description": "test2", "price": 3.64, "quantity": 23123})
    assert test_product.name == "test1"
    assert test_product.description == "test2"
    assert str(test_product) == "test1, 3.64 руб. Остаток: 23123 шт."
    assert test_product.price == 3.64
    assert test_product.quantity == 23123
    assert test_product + test_product == 23123 * 3.64 * 2
    test_product.price = 12.5
    assert test_product.price == 12.5


def test_product_setter_error(capsys):
    test_product = Product.new_product({"name": "test1", "description": "test2", "price": 0.0, "quantity": 23123})
    test_product.price = -3.64
    captured = capsys.readouterr()
    assert test_product.price == 0.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert "Product('name': 'test1', 'description': 'test2', '_Product__price': 0.0, 'quantity': 23123)" in captured.out


def test_product_subclasses():
    test_product = Smartphone("test1", "test2", 2000.1, 123, 90, "test3", 234.1, "test4")
    assert test_product.efficiency == 90
    assert test_product.model == "test3"
    assert test_product.memory == 234.1
    assert test_product.color == "test4"
    test_product = LawnGrass("test1", "test2", 2000.1, 123, "test3", 932.3, "test4")
    assert test_product.country == "test3"
    assert test_product.germination_period == 932.3
    assert test_product.color == "test4"


def test_type_errors():
    with pytest.raises(TypeError):
        Smartphone("test1", "test2", 2000.1, 123, 90, "test3", 234.1, "test4") + LawnGrass(
            "test1", "test2", 2000.1, 123, "test3", 932.3, "test4"
        )
    with pytest.raises(TypeError):
        Category("test1", "test2", []).add_product(Category("test1", "test2", []))
