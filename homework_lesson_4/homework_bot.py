print("Бот готов к работе.\nДля запуска введите предложение.")
in_phrase = input("> ")
in_phrase = in_phrase.lower()
in_phrase = in_phrase.replace('.', '')
in_phrase = in_phrase.replace(',', '')
in_phrase = in_phrase.replace('-', '')
in_phrase = in_phrase.replace(':', '')
in_phrase = in_phrase.replace(';', '')
in_phrase = in_phrase.replace('?', '')
in_phrase = in_phrase.replace('!', '')
in_phrase = in_phrase.rstrip()

greetings = ["привет", "здравствуйте", "здравствуй", "добрый день",
             "добрый вечер", "доброе утро"]
whassup = ["как дела", "что делаешь", "чем занимаешься",
           "чем занят", "как у тебя дела", "что ты делаешь",
           "чем ты занимаешься", "чем ты занят", "что нового",
           "что у тебя нового"]
movies = ["фильм", "кино", "сериал", "кинотеатр"]

farewell = ["гудбай", "до встречи", "до свидания", "прощай", "пока"]

while True:
    if in_phrase == "":
        print("Кажется, Вы ничего не ввели. Попробуйте заново.\n> ")
    elif any([x in in_phrase for x in greetings]):
        print("Привет. Я самый простенький бот. Вроде бы, пока работаю.\n> ")
    elif any([x in in_phrase for x in whassup]):
        print("Пытаюсь душить Python, но пока что Python душит меня.\n> ")
    elif any([x in in_phrase for x in movies]):
        print("Ни слова больше. Лучше посмотрите фильм Игра 1997 года.\n> ")
    elif any([x in in_phrase for x in farewell]):
        print("Надеюсь, ещё увидимся.")
        exit()
    else:
        print("Ничего не понятно, но очень интересно.\n> ")
