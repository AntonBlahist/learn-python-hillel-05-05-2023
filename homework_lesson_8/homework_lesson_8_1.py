#  Decided to use constants.
HOUR_IN_DAY = 24
MIN_IN_HOUR = 60
SEC_IN_MIN = 60


def converting(seconds):
    """
    The function checks if the input is a negative number or a string.
    If it is, the program is closed.
    If the input is correct, the function converts seconds
    into days, hours, minutes and seconds.
    It returns the tuple of the corresponding variables.
    """
    try:
        seconds = int(seconds)
        if not seconds <= 0:
            minutes, seconds = divmod(seconds, SEC_IN_MIN)
            hours, minutes = divmod(minutes, MIN_IN_HOUR)
            days, hours = divmod(hours, HOUR_IN_DAY)
            result_tuple = (days, hours, minutes, seconds)
            return result_tuple
        else:
            print("Oops! Time cannot be negative.")
            exit()
    except ValueError:
        print("Please, enter a number only.")
        exit()


def converting_dict(result_tuple):
    """
    The function creates a dictionary with the values from <result_tuple>.
    It returns the dictionary with the corresponding values.
    """
    #  The dictionary contains results as values.
    dictionary = {"days": result_tuple[0],
                  "hours": result_tuple[1],
                  "minutes": result_tuple[2],
                  "seconds": result_tuple[3]}
    return dictionary


if __name__ == "__main__":
    sec = input("Enter a value in seconds: ")
    result = converting(sec)
    result_dict = converting_dict(result)
    print(result_dict)
