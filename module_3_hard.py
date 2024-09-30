def calculate_structure_sum(data):
    total = 0

    if isinstance(data, (int, float)):  # Если элемент - число
        return data
    elif isinstance(data, str):  # Если элемент - строка
        return len(data)
    elif isinstance(data, (list, tuple, set)):  # Если элемент - список, кортеж или множество
        for item in data:
            total += calculate_structure_sum(item)  # Вызываем функцию
    elif isinstance(data, dict):  # Если элемент - словарь
        for key, value in data.items():
            total += calculate_structure_sum(key)  # Считаем длины ключей
            total += calculate_structure_sum(value)  # Считаем значения

    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)