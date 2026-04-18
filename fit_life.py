print("Привет, пользователь!")

# Начало работы, получение данных от пользователья, расчеты
user_name = input("Как тебя зовут? ")
user_age = int(input("Сколько тебе лет? "))
weight = float(input("Какой у тебя вес (кг)? "))
height = float(input("Какой у тебя рост (в метрах, используя точку: 1.75)? "))
bmi = round((weight / (height ** 2)), 1)
water_l = round(((weight * 30) / 1000), 1)

# Рыба для отчета:
title = "Отчет о пользователе:"
footer = "Отчет завершен. Будьте здоровы!"
border = 60


def title_shift(text):
    """Функция для центрирования заголовка и футера."""
    title_len = len(text)
    title_shift = (border - title_len) // 2
    return title_shift


# Вывод отчета
print("=" * border)
print(" " * title_shift(title) + title)
print("=" * border)
print(f"{user_name.title()}, возраст: {user_age}.")
print(f"Индекс массы тела (ИМТ): {bmi}.")
print(f"Рекомендуемое суточное потребление воды (л): {water_l}.")
print("=" * border)
print(" " * title_shift(footer) + footer)
print("=" * border)
