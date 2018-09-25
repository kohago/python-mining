from abc import ABCMeta,abstractmethod

#metaclass = ABCMeta will make it be an abstract class
class Animal(metaclass = ABCMeta):
    @abstractmethod
    def sound(self):
        return "---super--"

#set superclass to be child class parameter
class Cat(Animal):
    def sound(self):
        return "---Meow---"

# # not define necessary method
# # TypeError: Can't instantiate abstract class Dog with abstract methods sound
# class Dog(Animal):
#     pass
# Dog()

# other pattern: regisiter
class Cow():
    def sound(self):
        return "--momomo--"

Animal.register(Cow)

# call parent's methord
class Bird(Animal):
    def sound(self):
        print(super(Bird, self).sound())
        return "---jijiji---"

#If it walks like a duck and quacks like a duck, it must be a duck
def is_animal(animal):
    print(animal.__class__.__name__,end = ":")
    print(animal.sound())


if __name__ == "__main__":
    print("cat issubclass of Animal: " + str(issubclass(Cat().__class__,Animal)))
    print("cat isinstance of Animal: " + str(isinstance(Cat(),Animal)))
    print("cow issubclass of Animal: " + str(issubclass(Cow().__class__,Animal)))

    bird = Bird()
    print(bird.sound())

    cat = Cat()
    is_animal(cat)

    cow = Cow()
    is_animal(cow)
