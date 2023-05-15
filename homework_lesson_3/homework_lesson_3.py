"""Задал переменную для предложения пользователя."""

user_input_string = input('Введите предложение: ')

"""strip с символами не работал внутри строки. 
Применил replace к каждому символу.
lower для нижнего регистра.
rstrip для удаления пробелов справа.
"""

user_input_string = user_input_string.lower()
user_input_string = user_input_string.replace('.', '')
user_input_string = user_input_string.replace(',', '')
user_input_string = user_input_string.replace('-', '')
user_input_string = user_input_string.replace(':', '')
user_input_string = user_input_string.replace(';', '')
user_input_string = user_input_string.replace('?', '')
user_input_string = user_input_string.replace('!', '')
user_input_string = user_input_string.rstrip()

"""Задал функцию find_replace, чтобы запускать её
в "условном" блоке if/else. 
"""


def find_replace():

    """string_to_replace для ввода слова, которое будем менять,
    index_to_replace для метода .find, поиска и вывода индекса,
    а также для блока if/else.
    """

    string_to_replace = input('Введите слово или словосочетание, '
                              'которое вы хотите заменить в предложении: ')

    index_to_replace = user_input_string.find(string_to_replace)

    """В случае неправильного ввода на предыдущем этапе
    вывод сообщения и запуск ввода заново.
    """

    if index_to_replace == -1:
        print(f'"{string_to_replace}" не найдено в предложении.')
        find_replace()
    else:

        """При правильном вводе на предыдущем этапе — вывод индекса,
        предложение ввести новое слово, замена через метод replace,
        вывод конечного результата.
        """

        print(f'"{string_to_replace}" найдено. Индекс = {index_to_replace}.')
        new_string = input('Введите слово или словосочетание, '
                           'на которое вы хотите заменить: ')

        updated_string = user_input_string.replace(string_to_replace, new_string)
        print('Результат: ')
        print(updated_string)


find_replace()
