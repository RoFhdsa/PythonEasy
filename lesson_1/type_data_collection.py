# =============================================
# Лекция 1: Работа с коллекциями
# =============================================

# ----- Списки (list) -----
# Изменяемая последовательность элементов
fruits = ["apple", "banana", "cherry"]
print("[list] Исходный список:", fruits)

# Основные операции
fruits.append("orange")          # Добавление элемента
fruits.insert(1, "kiwi")         # Вставка по индексу
fruits.remove("banana")          # Удаление элемента
popped = fruits.pop(2)           # Удаление и возврат элемента по индексу

print("После изменений:", fruits)
print(f"Удаленный элемент: {popped}")
print("Срез [0:2]:", fruits[0:2])  # Срезы

# ----- Кортежи (tuple) -----
# Неизменяемая последовательность
colors = ("red", "green", "blue")
print("\n[tuple] Исходный кортеж:", colors)

# Попытка изменения вызовет ошибку
try:
    colors[0] = "pink"
except TypeError as e:
    print(f"Ошибка: {e} (кортежи неизменяемы!)")

# Преобразование list ↔ tuple
converted_list = list(colors)
converted_tuple = tuple(fruits)
print(f"Преобразование в list: {type(converted_list)}, \t {converted_list}")
print(f"Преобразование в tuple: {type(converted_tuple)}, \t {converted_tuple}")

# ----- Множества (set) -----
# Уникальные неупорядоченные элементы
unique_numbers = {1, 2, 3, 2, 1, 4, 5}
print("\n[set] Множество после создания:", unique_numbers)  # {1, 2, 3, 4, 5}

# Операции с множествами
a = {1, 2, 3}
b = {3, 4, 5}

print("Объединение:", a | b)        # {1, 2, 3, 4, 5}
print("Пересечение:", a & b)        # {3}
print("Разность:", a - b)           # {1, 2}

# Удаление дубликатов из списка
duplicates = [2, 3, 2, 5, 3, 7]
unique = list(set(duplicates))
print(f"\nУникальные элементы: {unique} (было {duplicates})")

# =============================================
# 6. Примеры использования коллекций
# =============================================

# ----- Фильтрация данных -----
users = ["Анна", "Иван", "Петр", "Мария", "Иван"]
unique_users = list(set(users))
print("\nУникальные пользователи:", unique_users)

# ----- Сортировка -----
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)  # Возвращает новый список
print("Сортированный список:", sorted_numbers)
print("Исходный список не изменился:", numbers)

# ----- Поиск пересечений -----
admins = {"Иван", "Мария", "Андрей"}
active_users = {"Петр", "Мария", "Андрей"}
both_groups = admins & active_users
print("\nПользователи в обеих группах:", both_groups)

# ----- Именованные кортежи (пример продвинутого использования) -----
from collections import namedtuple

# Создаем тип данных "Координата"
Coordinate = namedtuple("Coordinate", ["x", "y"])
point = Coordinate(10, -5)
print(f"\nИменованный кортеж: X={point.x}, Y={point.y}")