print("Программа удаляет из текста все круглые скобки "
      "и всё, что было внутри этих скобок.")


# Создал функцию parentheses_text_remove.
# Она делает всю работу, а в конце мы просто вызываем её.
def parentheses_text_remove(text):
    # Цикл, чтобы находило все скобки в тексте.
    while "(" in text:
        # Переменная start, находит открывающую скобку.
        start = text.index("(")
        """
        Следующая строка кода нужна для удаления пробела перед "(".
        Слайсим весь текст до start, т.е. до "(" и ищем последний
        пробел до start.
        """
        start = text[:start].rfind(" ", 0, start)
        # Переменная end находит закрывающую скобку.
        end = text.index(")", start)
        """
        Объединяем всё, что ДО скобок с тем, что ПОСЛЕ.
        Всё, что внутри скобок, включая сами скобки,
        в новом тексте не участвует.
        """
        text = text[:start] + text[end + 1:]
    return text


# Добавил всё в цикл, чтобы имитировать какое-никакое общение.
while True:
    initial_input = input("Для запуска введите «Старт», "
                          "для выхода введите «Выход»."
                          "\n> ")
    initial_input = initial_input.lower()
    initial_input = initial_input.strip()

    if initial_input == "старт":
        while True:
            # Собственно, ввод и вывод текста.
            user_input = input("Введите текст: ")
            final_output = parentheses_text_remove(user_input)
            if user_input == "":
                print("Вы ничего не ввели. Попробуйте заново "
                      "или введите «Выход» для выхода.")
                continue
            elif user_input in ["выход", "Выход", "ВЫХОД"]:
                print("Выход из программы..."
                      "\n...завершён.")
                exit()
            print("Результат:", final_output)
    elif initial_input == "выход":
        print("Выход из программы..."
              "\n...завершён.")
        quit()
    else:
        print("Некорректный ввод. Попробуйте заново.")
        continue
