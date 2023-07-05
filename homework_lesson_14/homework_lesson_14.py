from animals import Dog, Hen, Cow, Cat
from random import choices, randint


if __name__ == "__main__":
    animals = [
        Dog("Baron", 3),
        Hen("McNugget", 2),
        Cow("Otis", 5),
        Cat("Leo", 4)
    ]

available_food = ["grass", "dry dog food", "dry cat food",
                  "grain", "apple", "pie", "meat", "fish"]

what_we_got = list()

for animal in animals:
    animal.say()
    for food in choices(available_food, k=2):
        animal.eat(food)
    if animal.hungry:
        print(f"{animal.name} is hungry! Please, feed him.")
    what_we_got.append(animal.treat(randint(1, 10)))
    print("=" * 80)

print(f"Today we got {', '.join(what_we_got)}.")
