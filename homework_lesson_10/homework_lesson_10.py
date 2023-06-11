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
            for x in all_notes:
                print(x)
            continue
        elif user_input == "latest":
            for x in all_notes[::-1]:
                print(x)
            continue
        elif user_input == "longest":
            longest_list = sorted(all_notes, key=len, reverse=True)
            for x in longest_list:
                print(x)
            continue
        elif user_input == "shortest":
            shortest_list = sorted(all_notes, key=len)
            for x in shortest_list:
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
