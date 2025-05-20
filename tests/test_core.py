from typing import Tuple
import pytest
from src.core import Category, Product
import random


@pytest.fixture
def init_n_products_inside_test_category() -> Tuple:
    n = random.randint(10, 20)
    test_category = Category("test1", "test2", [])
    for x in range(n):
        test_category.add_product(Product.new_product({"name": "test1", "description": "test2", "price": n, "quantity": n}))
    return test_category, n

def test_init_n_products_inside_test_category(init_n_products_inside_test_category) -> None:
    test_category = init_n_products_inside_test_category[0]
    n = init_n_products_inside_test_category[1]

    assert test_category.name == "test1"
    assert test_category.description == "test2"
    assert len(test_category.products) == len(f"test1, {n} руб. Остаток: {n} шт.") * n + (4 * n)
    assert test_category.category_count == 1
    assert test_category.product_count == n

def test_product_init():
    test_product = Product.new_product({"name": "test1", "description": "test2", "price": 3.64, "quantity": 23123})
    assert test_product.name == "test1"
    assert test_product.description == "test2"
    assert test_product.price == 3.64
    assert test_product.quantity == 23123
    test_product.price = 12.5
    assert test_product.price == 12.5

def test_product_setter_error(capsys):
    test_product = Product.new_product({"name": "test1", "description": "test2", "price": 0.0, "quantity": 23123})
    test_product.price = -3.64
    captured = capsys.readouterr()
    assert test_product.price == 0.0
    assert captured.out == "“Цена не должна быть нулевая или отрицательная”\n"