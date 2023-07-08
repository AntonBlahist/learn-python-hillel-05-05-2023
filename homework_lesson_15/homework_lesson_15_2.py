def word_generator(string: str):
    """
    The function yield words from the text.
    :param string: str
    """
    if string == "":
        print("You didn't enter anything.")
    for x in string.split():
        yield x


if __name__ == "__main__":
    print("The program prints words from the text you enter"
          " one by one.")
    text = input("Please enter the text: ")
    for word in word_generator(text):
        print(word)
