"""
Чтобы не нагромождать проект повторяющимися комментариями,
я решил не писать их в тех частях кода,
которые ранее (выше) уже были прокомментированы,
поскольку они отличаются только расчётом (+-*/).
Надеюсь, это не ошибка.
"""
import math


while True:
    # Предложение выбрать нужную операцию.
    option = input("Выберите программу: "
                   "\n1) Сложение "
                   "\n2) Вычитание "
                   "\n3) Умножение "
                   "\n4) Деление"
                   "\nВведите «quit» для выхода."
                   "\n> ")
    option = option.lower()

    # Переменные для вмещения вводимых чисел.
    sum_list = []  # Список для операции сложения.
    subtract_list = []  # Список для операции вычитания.
    multiply_list = []  # Список для операции умножения.
    divide_list = []  # Список для операции деления.

    # Если выбрали сложение.
    if option in ["1", "1)", "сложение"]:
        print("Введите числа по одному, затем — «sum» для сложения."
              "\nВведите «quit» для выхода.")
        # Запуск цикла для ввода чисел.
        while True:
            num = input("> ")
            # Здесь и в дальнейшем - ключевое слово для расчёта.
            if num == "sum":
                # Здесь и в дальнейшем - остановка цикла.
                break
            # Выход на данном этапе.
            elif num == "quit":
                quit()
            # Здесь и в дальнейшем - добавление всех введённых чисел в список.
            try:
                sum_list.append(float(num))
            # Если ввели не число и не sum, будет ошибка. Обходим её.
            except ValueError:
                print("Введите числа, затем «sum»."
                      "\nВведите «quit» для выхода.")
        # Расчёт операции сложения.
        sum_result = sum(sum_list)
        print(f"Результат операции сложения: {sum_result}")
    # Если выбрали вычитание.
    elif option in ["2", "2)", "вычитание"]:
        print("Введите числа по одному, затем — «subtract» для вычитания."
              "\nВведите «quit» для выхода.")
        while True:
            num = input("> ")
            if num == "subtract":
                break
            elif num == "quit":
                quit()
            try:
                subtract_list.append(float(num))
            except ValueError:
                print("Введите числа, затем «subtract»."
                      "\nВведите «quit» для выхода.")
        # Расчёт операции вычитания.
        subtract_result = subtract_list[0] - sum(subtract_list[1:])
        print(f"Результат операции вычитания: {subtract_result}")
    # Если выбрали умножение.
    elif option in ["3", "3)", "умножение"]:
        print("Введите числа по одному, затем — «multiply» для умножения."
              "\nВведите «quit» для выхода.")
        while True:
            num = input("> ")
            if num == "multiply":
                break
            elif num == "quit":
                quit()
            try:
                multiply_list.append(float(num))
            except ValueError:
                print("Введите числа, затем «multiply»."
                      "\nВведите «quit» для выхода.")
        # Расчёт операции умножения.
        multiply_result = math.prod(multiply_list)
        print(f"Результат операции умножения: {multiply_result}")
    # Если выбрали деление.
    elif option in ["4", "4)", "деление"]:
        print("Введите числа по одному, затем — «divide» для деления."
              "\nВведите «quit» для выхода.")
        while True:
            num = input("> ")
            if num == "divide":
                break
            elif num == "quit":
                quit()
            try:
                divide_list.append(float(num))
            except ValueError:
                print("Введите числа, затем «divide»."
                      "\nВведите «quit» для выхода.")
        # Расчёт операции деления.
        divide_result = divide_list[0] / math.prod(divide_list[1:])
        print(f"Результат операции деления: {divide_result}")
    # Выход на этапе выбора программы.
    elif option == "quit":
        print("Выход из программы...\n...завершён.")
        exit()
    # Неправильный ввод на этапе выбора программы.
    else:
        print("Вы не выбрали программу. Попробуйте заново.")
        option = input("> ").lower()
        continue
