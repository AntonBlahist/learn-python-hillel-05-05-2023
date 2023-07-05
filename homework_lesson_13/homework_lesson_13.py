from random import choices, randint


class Cat:
    def __init__(self, name: str, age: int, breed: str, preferred_food: set):
        """
        Class Cat
        :param name: name
        :param age: age
        :param breed: breed
        :param preferred_food: preferred_food
        """
        self.name = name
        self.age = age
        self.breed = breed
        self.preferred_food = preferred_food
        self.hungry = True  # default status for each object
        self.hours_outdoors = 0  # default status object
        self.week = ("Sunday", "Monday", "Tuesday", "Wednesday",
                     "Thursday", "Friday", "Saturday")

    def __str__(self):
        """
        The function returns a string description for each object.
        """
        output_string = f"{self.breed} {self.name}, {self.age} "
        if self.age == 1:
            output_string += "year"
        else:
            output_string += "years"
        output_string += f", hours outdoors: {self.hours_outdoors}, " \
                         f"hungry: {self.hungry}"
        return output_string

    def eat(self):
        """
        A method for feeding cats every day.
        It compares random food with preferred
        and shows the status by the end of each day.
        """
        potential_food = ["dry cat food", "milk", "chicken",
                          "fish", "bugs", "bread", "apple",
                          "banana", "candy"]
        for day in self.week:
            print("=" * 20 + f" It's {day} " + "=" * 20)
            self.hungry = True
            for food in choices(potential_food, k=3):
                if self.hungry:
                    if food in self.preferred_food:
                        print(f"{self.name} eats {food}")
                        self.hungry = False
                        break
                    else:
                        print(f"{self.name} doesn't eat {food}")
                        self.meow()
                else:
                    print(f"{self.name} is not hungry now")
            if self.hungry:
                print(f"{self.name} is hungry today!!!")
            else:
                print(f"{self.name} is not hungry today")

    def walk(self):
        """
        A method for walking for a random number of hours.
        """
        for day in self.week:
            hours = randint(1, 4)
            if hours == 1:
                print(f"{self.name} walked for {hours} hour on {day}")
            elif hours == 0:
                print(f"{self.name} didn't walk today")
            else:
                print(f"{self.name} walked for {hours} hours on {day}")
            self.hours_outdoors += hours

    def meow(self):
        """
        A method for meow.  ╱|、
                          (˚ˎ 。7
                           |、˜〵
                          じしˍ,)ノ
        """
        print(f"{self.name} says: Meow")


if __name__ == "__main__":
    tom = Cat("Tom", 1, "Persian cat", {"dry cat food", "milk", "chicken"})
    felix = Cat("Felix", 2, "Maine Coon", {"dry cat food", "fish"})
    oscar = Cat("Oscar", 3, "British Shorthair", {"dry cat food", "milk"})
    leo = Cat("Leo", 4, "Sphynx", {"dry cat food", "chicken", "fish"})
    simba = Cat("Simba", 5, "Savannah cat", {"bugs"})
    luna = Cat("Luna", 6, "Bengal cat", {"dry cat food"})

    cats = [tom, felix, oscar, leo, simba, luna]

    for cat in cats:
        cat.eat()
        print("=" * 50)
        cat.walk()
        print("=" * 50)
        print(cat)
        print("=" * 50)
