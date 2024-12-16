class Pets:
    animals = []
    
    def __init__(self, animals):
        self.animals = animals
        
    def walk(self):
        return [animal.walk() for animal in self.animals]


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def walk(self):
        return f"{self.name} is just walking around"


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add another Cat
class Chilli(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all the pets (create 3 cat instances from the above).
my_cats = [Simon("Simon", 5), Sally("Sally", 7), Chilli("Chilli", 3)]

# 3 Instantiate the Pets class with all your cats.
my_pets = Pets(my_cats)

# 4 Output all walking
print(my_pets.walk())
