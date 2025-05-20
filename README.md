### Класс `Category`
Представляет категорию товаров.

**Атрибуты:**
- `name` (str): Название категории.
- `description` (str): Описание категории.
- `products` (list): Список товаров в категории.
- `category_count` (int, классовый атрибут): Счетчик созданных категорий.
- `products_count` (int, классовый атрибут): Счетчик всех созданных товаров (во всех категориях).

**Методы:**
- `__init__(self, name, description, products)`: Инициализирует категорию. Увеличивает `category_count` на 1.

### Класс `Product`
Представляет товар.

**Атрибуты:**
- `name` (str): Название товара.
- `description` (str): Описание товара.
- `price` (float): Цена товара.
- `quantity` (int): Доступное количество.

**Методы:**
- `__init__(self, name, description, price, quantity)`: Инициализирует товар. Увеличивает `Category.products_count` на 1.

## Пример использования

```python
# Создание товаров
product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 5)
product2 = Product("Смартфон", "Совейший смартфон", 699.99, 10)

# Создание категории с товарами
electronics = Category("Электроника", "Техника и гаджеты", [product1, product2])

# Проверка счетчиков
print(f"Всего категорий: {Category.category_count}")  # 1
print(f"Всего товаров: {Category.products_count}")     # 2