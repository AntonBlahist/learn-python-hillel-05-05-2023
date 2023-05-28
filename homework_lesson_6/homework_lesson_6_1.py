# Для использования .punctuation
import string

# Добавил всё в цикл, чтобы имитировать какое-никакое общение.
while True:
    initial_input = input("Для запуска введите «Старт», "
                          "для выхода введите «Выход»."
                          "\n> ")
    initial_input = initial_input.lower()
    initial_input = initial_input.strip()

    if initial_input == "старт":
        while True:

            user_input = input("Для проверки палиндрома введите текст:"
                               "\n> ")
            user_input = user_input.lower()
            # Убираем переносы и табуляцию по краям.
            user_input = user_input.strip()
            # Убираем переносы и табуляцию внутри строки.
            user_input = user_input.replace("\n", "")
            user_input = user_input.replace("\t", "")
            # Убираем пробелы внутри предложения.
            # Иначе не заметит ввод по типу "Аби ріці риба".
            user_input = user_input.replace(" ", "")

            # Убираем все знаки препинания с помощью цикла.
            for character in string.punctuation:
                user_input = user_input.replace(character, "")

            # Создаем переменную, чтобы затем использовать её в if/else.
            palindrome = user_input[::-1]

            # Собственно, сама проверка на палиндром.
            if user_input == palindrome:
                print(f"Введённый текст является палиндромом — {palindrome}.")
            elif user_input == "выход":
                break
            # Небольшой прикол.
            elif palindrome == "выход":
                print("Кажется, вы нашли пасхалочку.")
                break
            else:
                print(f"{user_input} не является палиндромом.")
    elif initial_input == "выход":
        print("Выход из программы..."
              "\n...завершён.")
        quit()
    else:
        print("Некорректный ввод. Попробуйте заново.")
        continue
