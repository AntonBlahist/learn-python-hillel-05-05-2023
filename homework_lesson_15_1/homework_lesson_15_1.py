def fibonacci_generator(n: int):
    """
    The function yield numbers in the Fibonacci sequence
    up to the n value user entered.
    :param n: int
    """
    if n <= 0:
        print("Please enter a positive number.")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("The program prints numbers in the Fibonacci sequence"
          "up to the index value you enter.")
    end_index = int(input("Please enter an index: "))
    for number in fibonacci_generator(end_index):
        print(number)
