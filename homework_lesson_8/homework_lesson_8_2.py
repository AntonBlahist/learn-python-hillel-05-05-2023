PRIME_SET = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
             43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}


def number_check(user_input):
    """
    The function checks if the number is entered
    and if it is — checks if the number is not greater than 100.
    Returns int <user_input>.
    """
    if user_input == "":
        print("You didn't enter anything.")
        exit()
    try:
        user_input = int(user_input)
    except TypeError and ValueError:
        print("Please enter only natural numbers up to 100.")
        exit()
    if user_input <= 100:
        return user_input
    else:
        print("Please enter natural numbers up to 100 only.")
        exit()


def prime_numbers(user_input):
    """
    The function checks if the number entered is in the set of prime numbers
    and returns True or False.
    """
    if user_input in PRIME_SET:
        return True
    else:
        return False


if __name__ == "__main__":
    print("The program checks if the natural number entered"
          " (up to 100) is in the set of prime numbers.")
    input_num = input("Please enter a natural number up to 100: ")
    num_to_check = number_check(input_num)
    prime_num = prime_numbers(num_to_check)
    if prime_num:
        print(f"{num_to_check} is a prime number.")
    if not prime_num:
        print(f"{num_to_check} is not a prime number.")
