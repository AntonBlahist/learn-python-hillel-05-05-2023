import math

# Предложение выбрать нужную операцию.
option = input("Выберите программу: "
               "\n1) Сложение "
               "\n2) Вычитание "
               "\n3) Умножение "
               "\n4) Деление"
               "\nВведите quit для выхода."
               "\n> ")
option = option.lower()

# Переменные для вмещения вводимых чисел.
sum_list = []  # список для операции сложения
subtract_list = []  # список для операции вычитания
multiply_list = []  # список для операции умножения
divide_list = []  # список для операции деления

if option in ["1", "1)", "сложение"]:
    print("Введите числа по одному, затем — «sum» для сложения.")
    while True:
        num = input("> ")
        if num == "sum":
            break
        sum_list.append(float(num))
    # Ввод операции сложения.
    sum_result = sum(sum_list)
    print(f"Результат операции сложения: {sum_result}")

elif option in ["2", "2)", "вычитание"]:
    print("Введите числа по одному, затем — «subtract» для вычитания.")
    while True:
        num = input("> ")
        if num == "subtract":
            break
        subtract_list.append(float(num))
    # Ввод операции вычитания.
    subtract_result = subtract_list[0] - sum(subtract_list[1:])
    print(f"Результат операции вычитания: {subtract_result}")

elif option in ["3", "3)", "умножение"]:
    print("Введите числа по одному, затем — «multiply» для умножения.")
    while True:
        num = input("> ")
        if num == "multiply":
            break
        multiply_list.append(float(num))
    # Ввод операции умножения.
    multiply_result = math.prod(multiply_list)
    print(f"Результат операции умножения: {multiply_result}")

elif option in ["4", "4)", "деление"]:
    print("Введите числа по одному, затем — «divide» для деления.")
    while True:
        num = input("> ")
        if num == "divide":
            break
        divide_list.append(float(num))
    # Ввод операции деления.
    divide_result = divide_list[0] / math.prod(divide_list[1:])
    print(f"Результат операции деления: {divide_result}")
# Для выхода.
elif option == "quit":
    print("Выход из программы...\n...завершён.")
    exit()
# Неправильный ввод на этапе выбора программы.
else:
    print("Вы не выбрали программу. Попробуйте заново.")
    option = input("> ").lower()
