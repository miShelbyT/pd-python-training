class Animal: 
    ANIMALS = []

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def add_dog(self, dog):
        self.__class__.append(dog)
        print(self.ANIMALS)


newAnimal = Animal("fido", "mutt")
print(newAnimal.name)