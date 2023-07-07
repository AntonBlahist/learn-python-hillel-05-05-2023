from random import randint


class Animal:
    def __init__(self, name: str, age: int, say_word: str, preferred_food: set):
        """
        The class is responsible for
        simulating the life of an animal on the farm.
        :param name: animal name
        :param age: animal age
        :param say_word: animal "phrase"
        :param preferred_food: diet
        """
        self.name = name
        self.age = age
        self.say_word = say_word
        self.preferred_food = preferred_food
        self.hungry = True
        self.vet_check = False

    def say(self):
        """
        The animal pronounces prepared "phrases".
        """
        print(f"{self.name} says: {self.say_word}")

    def eat(self, food: str):
        """
        The method is responsible for
        simulating feeding the animal on the farm.
        If the offered food is in the preferred_food,
        the animal will eat and <self.hungry> = False.
        Otherwise, the animal will not eat.
        :param food: what to eat
        """
        if not self.hungry:
            return
        if food in self.preferred_food:
            print(f"{self.name} eats {food}")
            self.hungry = False
        else:
            print(f"{self.name} doesn't eat: {food}")
            self.say()

    def treat(self, hours: int):
        """
        The method is responsible for caring for an animal.
        :param hours: how many hours we spend with the animal
        :return: what we get in return
        """
        raise NotImplementedError

    def go_to_vet(self):
        """
        Depending on the odds,
        the animal either needs to be seen by a vet or not.
        """
        chances = randint(0, 1)
        if chances == 1:
            self.vet_check = True
            return f"{self.name} needs to be examined by a vet"
        else:
            return ""
