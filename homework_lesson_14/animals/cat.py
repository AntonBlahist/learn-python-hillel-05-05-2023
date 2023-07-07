from random import randint
from .animal import Animal


class Cat(Animal):
    """
    The class is responsible for simulating an animal - cat.
    """

    def __init__(self, name: str, age: int, say_word="Meow!"):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={"dry cat food"}
        )

    def treat(self, hours: int) -> str:
        """
        Taking care of a cat makes us feel good.
        :param hours: time we spent
        :return: a good mood
        """
        print(f"You are playing with {self.name} for {hours} hours"
              f" and your mood improves")
        return "a good mood"
