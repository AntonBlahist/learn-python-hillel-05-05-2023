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


# Собственно, ввод и вывод текста.
user_input = input("Введите текст: ")
final_output = parentheses_text_remove(user_input)
print("Результат:", final_output)
