from .animal import Animal


class Cow(Animal):
    """
    The class is responsible for simulating an animal - cow.
    """
    def __init__(self, name: str, age: int, say_word="Moo!"):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={"grass"}
        )

    def treat(self, hours: int) -> str:
        """
        By taking care of the cow for the right amount of time, we get milk.
        :param hours: time we spent
        :return: a bucket of milk or nothing
        """
        if hours > 1:
            print(f"You are taking care of {self.name} for {hours} hours"
                  f" and you get a bucket of milk")
            return "a bucket of milk"
        print(f"You are taking care of {self.name} for {hours} hours")
        return ""
