def notes_earliest(notes):
    """
    The function returns a list of the saved notes
    from the earliest to the latest.
    """
    earliest_list = notes
    return earliest_list


def notes_latest(notes):
    """
    The function returns a list of the saved notes
    from the latest to the earliest.
    """
    latest_list = notes[::-1]
    return latest_list


def notes_longest(notes):
    """
    The function returns a list of the saved notes
    from the longest to the shortest.
    """
    longest_list = sorted(notes, key=len, reverse=True)
    return longest_list


def notes_shortest(notes):
    """
    The function returns a list of the saved notes
    from the shortest to the longest.
    """
    shortest_list = sorted(notes, key=len)
    return shortest_list


def notes_help():
    """
    The function returns a list (str actually) of keywords and what they do.
    """
    help_print = "add - to add a note." \
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
    all_notes = []
    while True:
        user_input = input("> ").lower().strip()
        if user_input == "add":
            note = input("Enter your note:\n> ").lower().strip()
            all_notes.append(note)
            continue
        elif user_input == "earliest":
            result = notes_earliest(all_notes)
            for x in result:
                print(x)
            continue
        elif user_input == "latest":
            result = notes_latest(all_notes)
            for x in result:
                print(x)
            continue
        elif user_input == "longest":
            result = notes_longest(all_notes)
            for x in result:
                print(x)
            continue
        elif user_input == "shortest":
            result = notes_shortest(all_notes)
            for x in result:
                print(x)
            continue
        elif user_input == "help":
            print(notes_help())
            continue
        elif user_input == "quit":
            print("Bye-bye!")
            exit()
        else:
            print("Incorrect input. Try again.")
            continue
