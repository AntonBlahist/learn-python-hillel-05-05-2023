def find_replace(user_text: str):
    """
    string_to_replace для ввода слова, которое будем менять,
    index_to_replace для метода .find, поиска и вывода индекса,
    а также для блока if/else.
    """
    user_text = user_text.lower()
    punctuation = [".", ",", "-", ":", ";", "?", "!"]
    for symbol in punctuation:
        user_text = user_text.replace(symbol, "")
    user_text = user_text.rstrip()

    string_to_replace = input("Введите слово или словосочетание, "
                              "которое вы хотите заменить в предложении: ")
    index_to_replace = user_text.find(string_to_replace)

    if index_to_replace == -1:
        print(f"{string_to_replace} не найдено в предложении.")
        find_replace(user_text)
    else:
        print(f"{string_to_replace} найдено. Индекс = {index_to_replace}.")
        new_string = input("Введите слово или словосочетание, "
                           "на которое вы хотите заменить: ")
        updated_string = user_text.replace(string_to_replace, new_string)
        print("Результат: ")
        print(updated_string)


if __name__ == "__main__":
    user_input_string = input("Введите предложение: ")
    find_replace(user_input_string)
