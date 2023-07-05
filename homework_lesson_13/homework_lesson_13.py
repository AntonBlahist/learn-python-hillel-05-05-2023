from random import choices, randint


class Cat:
    def __init__(self, name: str, age: int, breed: str, preferred_food: set):
        self.name = name
        self.age = age
        self.breed = breed
        self.preferred_food = preferred_food
        self.hungry = True
        self.hours_outdoors = 0

    def __str__(self):
        output_string = f"{self.breed} {self.name}, {self.age} "
        if self.age == 1:
            output_string += "year"
        else:
            output_string += "years"
        output_string += f", hours outdoors: {self.hours_outdoors}, " \
                         f"hungry: {self.hungry}"
        return output_string

    def eat(self, food: str):
        if self.hungry:
            if food in self.preferred_food:
                print(f"{self.name} eats {food}")
                self.hungry = False
            else:
                print(f"{self.name} doesn't eat {food}")
                self.meow()
        else:
            print(f"{self.name} is not hungry")

    def walk(self):
        hours = randint(1, 4)
        if hours == 1:
            print(f"{self.name} walked for {hours} hour")
        else:
            print(f"{self.name} walked for {hours} hours")
        self.hours_outdoors += hours
        if self.hours_outdoors > 3:
            self.hungry = True

    def meow(self):
        print(f"{self.name} says: Meow")


if __name__ == "__main__":
    tom = Cat("Tom", 1, "Persian cat", {"dry cat food", "milk", "chicken"})
    felix = Cat("Felix", 2, "Maine Coon", {"dry cat food", "fish"})
    oscar = Cat("Oscar", 3, "British Shorthair", {"dry cat food", "milk"})
    leo = Cat("Leo", 4, "Sphynx", {"dry cat food", "chicken", "fish"})
    simba = Cat("Simba", 5, "Savannah cat", {"bugs"})
    luna = Cat("Luna", 6, "Bengal cat", {"dry cat food"})

    cats = [tom, felix, oscar, leo, simba, luna]

    potential_food = ["dry cat food", "milk", "chicken",
                      "fish", "bugs", "bread", "apple",
                      "banana", "candy"]
    for cat in cats:
        print(f"Feeding {cat.name}")
        for random_food in choices(potential_food, k=3):
            cat.eat(random_food)
        cat.walk()
        print(cat)
        print('=' * 20)

    week = ("Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday")
