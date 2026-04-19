"""
Калькулятор индекса массы тела и суточной потребности воды.

Принимает от пользователя:
        имя (user_name), возраст (user_age), вес (weight) и рост (height).
Расcчитывает ИМТ (bmi) и суточную потребность в воде (water_l)
На основание полученных и расчитанных данных формирует отчет.
"""


WATER_PER_KG = 30
MILLILITERS_IN_A_LITER = 1000
TITLE = "Отчет о пользователе:"
FOOTER = "Отчет завершен. Будьте здоровы!"
BORDER = 60

print("Привет, пользователь!")

user_name = input("Как тебя зовут? ").title()

while True:
    try:
        user_age = int(input("Сколько тебе лет? "))
        if user_age <= 0:
            print("Возраст должен быть больше 0!")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите возраст целым числом.")

while True:
    try:
        weight = float(input("Какой у тебя вес (кг)? "))
        if weight <= 0:
            print("Вес должен быть больше 0!")
            continue
        break
    except ValueError:
        print("Используйте цифры и точку. Например: 75.5")

while True:
    try:
        height = float(input("Какой у тебя рост (в метрах)? "))
        if height <= 0:
            print("Рост должен быть больше 0!")
            continue
        break
    except ValueError:
        print("Используйте цифры и точку. Например: 1.75")

bmi = round((weight / (height ** 2)), 1)
water_l = round(((weight * WATER_PER_KG) / MILLILITERS_IN_A_LITER), 1)


def title_shift(text):
    """
    Вычисляет длину отступа слева для центрирования TITLE и FOOTER.

    Параметр:
            text(str): текст для центрирования.

    Возвращаемое значение:
            int: необходимое количество пробелов для отступа слева.
    """
    return (BORDER - len(text)) // 2


print("=" * BORDER)
print(" " * title_shift(TITLE) + TITLE)
print("=" * BORDER)
print(f"{user_name}, возраст: {user_age}.")
print(f"Индекс массы тела (ИМТ): {bmi}.")
print(f"Рекомендуемое суточное потребление воды (л): {water_l}.")
print("=" * BORDER)
print(" " * title_shift(FOOTER) + FOOTER)
print("=" * BORDER)
