# Для использования .punctuation
import string

# Добавил всё в цикл, чтобы имитировать какое-никакое общение.
while True:
    initial_input = input("Для запуска введите «Старт», "
                          "для выхода введите «Выход»."
                          "\n> ").lower().strip()

    if initial_input == "старт":
        while True:

            user_input = input("Для проверки палиндрома введите текст:"
                               "\n> ").lower()
            # Убираем переносы и табуляцию.
            user_input = user_input.replace("\n", "").replace("\t", "")
            # Убираем пробелы внутри предложения.
            # Иначе не заметит ввод по типу "Аби ріці риба".
            user_input = user_input.replace(" ", "")

            # Убираем все знаки препинания с помощью цикла.
            for character in string.punctuation:
                user_input = user_input.replace(character, "")
            # Создаем переменную, чтобы затем использовать её в if/else.
            palindrome = user_input[::-1]

            # Собственно, сама проверка на палиндром.
            if palindrome == "":
                print("Вы ничего не ввели. Попробуйте заново "
                      "или введите «Выход» для выхода.")
                continue
            elif user_input == palindrome:
                print(f"Введённый текст является палиндромом — {palindrome}.")
            elif user_input == "выход":
                print("Выход из программы..."
                      "\n...завершён.")
                exit()
            # Небольшой прикол.
            elif palindrome == "выход":
                print("Кажется, вы нашли пасхалочку.")
                exit()
            else:
                print(f"{user_input} не является палиндромом.")
    elif initial_input == "выход":
        print("Выход из программы..."
              "\n...завершён.")
        exit()
    else:
        print("Некорректный ввод. Попробуйте заново.")
        continue
