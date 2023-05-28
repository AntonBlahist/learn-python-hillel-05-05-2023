# Для использования .punctuation
import string

user_input = input("Для проверки палиндрома введите текст: ")
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
else:
    print(f"{user_input} не является палиндромом.")
