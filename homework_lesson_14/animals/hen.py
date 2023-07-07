from random import randint
from .animal import Animal


class Hen(Animal):
    """
    The class is responsible for simulating an animal - dog.
    """
    def __init__(self, name: str, age: int, say_word="Cluck!"):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={"grain"}
        )

    def treat(self, hours: int) -> str:
        """
        If we take care of the hen the proper amount of time, we get 10 eggs.
        If less - 1 to 5 eggs.
        :param hours: time we spent
        :return: from 1 to 10 eggs
        """
        if hours > 5:
            print(f"You take care of {self.name} for {hours} hours"
                  f" and get a dozen chicken eggs")
            return "chicken eggs (10)"
        print(f"You take care of {self.name} for {hours} hours"
              f" and get a few chicken eggs")
        return f"chicken eggs ({randint(1, 5)})"
