"""
while <условное выражение> == True:
    тело цикла
break - команда выхода из цикла
exit - команда выхода из программы
quit - команда выхода из программы
"""

"""
WHILE

while True:
    x = input("Where are you from? (type 'exit' to leave)\n> ")
    if x.lower() == "exit":
        print("Closing...")
        print("Done!")
        break
"""

"""
Цикл WHILE

floors = int(input("На какой этаж вам нужно попасть?\n> "))
i = 1  # i итератор - переменная, которая хранит прогресс цикла между итерациями
while i < floors:
    print(f"Вы на {i} этаже.")
    i += 1  # i = i + 1
    print(f"Вы поднялись на {i} этаж.")
print(f"Вы поднялись на нужный этаж.")
"""

"""
Цикл FOR

for i in range(floors):
    print(f"Вы на {i+1} этаже.")
print(f"Вы поднялись на {i+1} этаж.")
"""

"""
Список list
"""

x = [3, 3.5, "string", True, [5, False, "another_string"]]
print(type(x))
print(len(x))  # Длина списка
# append - добавить элемент в конец списка
# insert(0, "smth") - добавить элемент, где 0 - нужный индекс, "smth" - новый элемент
