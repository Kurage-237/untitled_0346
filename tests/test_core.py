import random
from typing import Tuple

import pytest

from src import core


@pytest.fixture
def init_n_categories() -> Tuple[list, int]:
    n = random.randint(10, 20)
    objects = []
    for x in range(n):
        objects.append(core.Category("test", "test", []))
    return objects, n


def test_init_category(init_n_categories: Tuple) -> None:
    assert core.Category.category_count == init_n_categories[1]
    for x in init_n_categories[0]:
        assert x.name == "test"
        assert x.description == "test"
        assert x.products == []


@pytest.fixture
def init_n_products() -> Tuple[list, int]:
    n = random.randint(10, 20)
    objects = []
    for x in range(n):
        objects.append(core.Product("test", "test", float(n), n))
    return objects, n


def test_init_product(init_n_products: Tuple) -> None:
    assert core.Category.products_count == init_n_products[1]
    for x in init_n_products[0]:
        assert x.name == "test"
        assert x.description == "test"
        assert x.price == init_n_products[1]
        assert x.quantity == init_n_products[1]
