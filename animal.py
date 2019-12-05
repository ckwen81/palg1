class Mammal:
    population = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I am an instance of {self.__class__}. My name is {self.name}. "

    def __repr__(self):
        return self.__str__()

    def make_sound(self):
        return f"{self.name} is trying to speak but its method doesn’t do much"


class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def __str__(self):
        return f"{super().__str__()}\nMy breed is {self.breed}"

    def make_sound(self):
        return f"{self.name} says woof!"


class Donkey(Mammal):
    pass


animals = {"Ned": ("Donkey", None), "Rex": ("Dog", "mongrel"), "Sam": ("Dog", "labrador")}
animals_list = []

for k in animals:
    if animals[k][1]:
        animals_list.append(globals()[animals[k][0]](k, animals[k][1]))
    else:
        animals_list.append(globals()[animals[k][0]](k))

    Mammal.population += 1

for animal in animals_list:
    print(f"\n{animal}")
    print(f"{animal.make_sound()}")

print(f"\nAnimal population is {Mammal.population}")