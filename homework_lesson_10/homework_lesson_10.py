def notes_add(input_note):
    """
    The function saves users' notes and their lengths into a tuple
    and returns the corresponding tuple.
    """
    length = len(input_note)
    input_note = (input_note, length)
    return input_note


def show_all(notes_list):
    """
    The function returns all the saved notes.
    """
    i = 0
    k = 0
    pop_notes = []
    for x in notes_list:
        pop_notes = notes_list.pop[i][k]
        i = i + 2
    return pop_notes


def notes_earliest():
    """
    The function returns saved notes in chronological order -
    from the earliest to the latest.
    *возвращает список без длины в оригинальном порядке*
    """


def notes_latest():
    """
    The function returns the saved notes in chronological order -
    from the latest to the earliest.
    *возвращает список без длины в обратном порядке*
    """


def notes_longest():
    """
    The function returns the saved notes in order of their length -
    from the longest to the shortest.
    """


def notes_shortest():
    """
    The function returns the saved notes in order of their length -
    from the shortest to the longest.
    """


def notes_help():
    """
    The function returns a list (str actually) of keywords and what they do.
    """
    help_print = "add - to add a note." \
                 "\nall - to show all the notes." \
                 "\nearliest - to show all the notes" \
                 "from the earliest to the latest." \
                 "\nlatest - to show all the notes" \
                 "from the latest to the earliest." \
                 "\nlongest - to show all the notes" \
                 "from the longest to the shortest." \
                 "\nshortest - to show all the notes" \
                 "from the shortest to the longest." \
                 "\nquit - to quit."
    return help_print


if __name__ == "__main__":
    print("Use keywords to start. To see all keywords, use \"help\".")
    while True:
        all_notes = []
        user_input = input("> ").lower().strip()
        if user_input == "add":
            note = input("Enter your note:\n> ")
            note = notes_add(note)
            all_notes += note
        if user_input == "all":
            notes = show_all(all_notes)
            for note in notes:
                print(note)
            continue
        if user_input == "earliest":
            pass
        if user_input == "latest":
            pass
        if user_input == "longest":
            pass
        if user_input == "shortest":
            pass
        if user_input == "help":
            print(notes_help())
            continue
        if user_input == "quit":
            print("Bye-bye!")
            exit()
        else:
            print("Incorrect input. Try again.\n> ")
            continue
