from Animal import Animal;

# still figuring out how parent Class works with child Class
class Dog(Animal):
    ALL = []

    def __init__(self, name, breed):
        self.name = name
        # self._name = name  => would indicate a private variable
        self.breed = breed
        self.tricks = []
        self.__class__.ALL.append(self)

# instance method that can also be called on the class
# instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state. ??
    def growl(self):
        print('{} says grrr').format(self.name)

# ??? works but not as expected
    def growl2(self):
        print('{} says grrrrrrrrrrr').format(self.name, self.__class__)

# class method uses a decorator.....
    @classmethod
    def bark(cls):
        print(cls)

tiger_rose = Dog("Tiger Rose", "jindo")
heidi = Dog("Heidi", "big")
cocoBean = Dog("Coconut", "westie")

tiger_rose.growl2() # or
# Dog.growl(tiger_rose) # not best practice
# Dog.bark()
print(Dog.ALL)