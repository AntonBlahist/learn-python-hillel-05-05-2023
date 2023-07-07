from random import randint
from .animal import Animal


class Dog(Animal):
    """
    The class is responsible for simulating an animal - dog.
    """
    def __init__(self, name: str, age: int, say_word="Woof!"):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={"dry dog food"}
        )

    def treat(self, hours: int) -> str:
        """
        Taking care of a dog for the right amount of time makes us feel good.
        :param hours: time we spent
        :return: a good mood or nothing
        """
        if hours > 2:
            print(f"You are walking {self.name} for {hours} hours"
                  f" and your mood improves")
            return "a good mood"
        print(f"You are walking {self.name} for {hours} hours")
        return ""
