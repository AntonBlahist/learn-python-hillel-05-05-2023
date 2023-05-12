# input_message = input("Введите строку: ")
# print(input_message[::-1])

user_input = input("Для проверки палиндрома введите слово: ")
user_input = user_input.lower()
palindrome = user_input[::-1]

if user_input == palindrome:
    print(f"Слово {user_input} является палиндромом — {palindrome}.")
else:
    print(f"Слово {user_input} не является палиндромом.")
