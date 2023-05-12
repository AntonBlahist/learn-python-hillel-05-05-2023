# Создал папку для домашнего задания после второго урока - homework_lesson_2.
# В этой папке будут 4 файла для 4 задач соответственно.
# Это файл для первой задачи — конвертер градусов и радиан.
# Я хочу сделать конвертер, который сможет преобразовывать градусы в радианы и наоборот.
# В зависимости от выбора пользователя.

import math

# Задал переменную выбора конвертера choice.

choice = input('Введите "1" для конвертации градусов в радианы, введите "2" для конвертации радиан в градусы: ')

# Использовал условные операторы для запуска нужного конвертера.

if choice == '1':

    # Задал переменную degrees_input для пользовательского ввода.
    # Задал переменную radians_output для вывода результата.
    # Написал формулу преобразования градусов в радианы.
    # Округлил результат до 5 цифр после точки с помощью round.
    # Добавил команду для вывода результата.

    degrees_input = float((input('Введите значение "Градусы": ')))
    radians_output = round(((degrees_input * math.pi) / 180), 5)
    print(degrees_input, '° равняется', radians_output, 'рад.')

elif choice == '2':

    # Задал переменную radians_input для пользовательского ввода.
    # Задал переменную degrees_output для вывода результата.
    # Написал формулу преобразования радиан в градусы.
    # Округлил результат до 5 цифр после точки с помощью round.
    # Добавил команду для вывода результата.

    radians_input = float((input('Введите значение "Радианы": ')))
    degrees_output = round(((radians_input * 180) / math.pi), 5)
    print(radians_input, 'рад равняется ', degrees_output, '°.')

else:

    # В случае неправильного ввода при выборе конвертера.

    print('Используйте только "1" или "2" для выбора конвертера.')
    choice = input('Введите "1" для конвертации градусов в радианы, введите "2" для конвертации радиан в градусы: ')

# Теперь нужно сделать так, чтобы после else программа работала дальше.
