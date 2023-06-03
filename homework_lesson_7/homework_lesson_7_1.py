import math


def choice():
    """
    Функция отвечает за выбор конвертера и
    возвращает выбор в главную часть.
    Если user_choice == q, программа закрывается.
    """
    while True:
        option = input("Введите 1 для конвертации градусов в радианы,"
                       " введите 2 для конвертации радиан в градусы,"
                       " введите q для выхода."
                       "\n> ").lower().strip()
        if option in ["1", "2"]:
            return option
        elif option == "q":
            print("Выход из программы.")
            quit()
        else:
            continue


def converter_input(option):
    """
    Функция вызывает ввод данных в зависимости от выбора конвертера.
    """
    while True:
        try:
            if option == "1":
                degrees_input = float((input("Введите градусы: ").strip()))
                return degrees_input
            if option == "2":
                radians_input = float((input("Введите значение радианы: ").strip()))
                return radians_input
        except ValueError:
            print("Некорректный ввод. Попробуйте заново.")
            continue


def degrees_to_radians(converter_calculation):
    """
    Функция отвечает за конвертацию градусы->радианы
    и возвращает ответ в главную часть.
    """
    radians_output = round(((converter_calculation * math.pi) / 180), 5)
    return radians_output


def radians_to_degrees(converter_calculation):
    """
    Функция отвечает за конвертацию радианы->градусы
    и возвращает ответ в главную часть.
    """
    degrees_output = round(((converter_calculation * 180) / math.pi), 5)
    return degrees_output


if __name__ == "__main__":
    print("Программа конвертирует градусы в радианы, радианы в градусы.")
    #  Вызываем функции, сохраняем их "возврат" в переменные.
    converter_choice = choice()
    calculation_input = converter_input(converter_choice)
    if converter_choice == "1":
        result = degrees_to_radians(calculation_input)
        print(f"{calculation_input}°, равняется, {result} rad.")
    elif converter_choice == "2":
        result = radians_to_degrees(calculation_input)
        print(f"{calculation_input}rad, равняется, {result}°.")
