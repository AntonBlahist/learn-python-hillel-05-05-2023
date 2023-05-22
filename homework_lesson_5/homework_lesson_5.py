import math

# Предложение выбрать нужную операцию.
option = input("Выберите программу: "
               "\n1) Сложение "
               "\n2) Вычитание "
               "\n3) Умножение "
               "\n4) Деление"
               "\n> ")
option = option.lower()

# Списки для вмещения вводимых чисел.
sum_list = []
subtract_list = []
multiply_list = []
divide_list = []

if option == "1" or "1)" or "сложение":
    print("Вводите числа по одному, затем — «sum» для сложения.")
    for_sum = input("> ").lower()
    # Сделать добавление вводимых чисел в список.
    # Сделать ввод sum.
    sum_result = sum(sum_list)
    print(sum_result)
elif option == "2" or "2)" or "вычитание":
    print("Вводите числа по одному, затем — «subtract» для вычитания.")
    for_subtract = input("> ").lower()
    # Сделать добавление вводимых чисел в список.
    # Сделать ввод subtract.
    subtract_result =  # вычитание(subtract_list).
    print(subtract_result)
elif option == "3" or "3)" or "умножение":
    print("Вводите числа по одному, затем — «multiply» для умножения.")
    for_multiply = input("> ").lower()
    # Сделать добавление вводимых чисел в список.
    # Сделать ввод multiply.
    multiply_result = math.prod(multiply_list)
    print(multiply_result)
elif option == "4" or "4)" or "деление":
    print("Вводите числа по одному, затем — «divide» для деления.")
    for_divide = input("> ").lower()
    # Сделать добавление вводимых чисел в список.
    # Сделать ввод divide.
    divide_result =  # деление(divide_list)
    print(divide_result)
elif option == "quit":
    print("Выход из программы...\n...завершён.")
    exit()
else:
    print("Вы не выбрали программу. Попробуйте заново.")
    option = input("> ").lower()
