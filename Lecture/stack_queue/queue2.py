from abc import *
from enum import Enum

class Animal_type(Enum):
    DOG = "DOG",
    CAT = "CAT"

class Animal(metaclass=ABCMeta):
    def __init__(self, animal_type, name):
        self.animal_type = animal_type
        self.name = name
        self.order = 0

    def set_order(self, order):
        self.order = order

    def get_order(self):
        return self.order

    def info(self):
        return str(self.order) + ") type: " + str(self.animal_type) + ", name: " + self.name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(Animal_type.DOG, name)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(Animal_type.CAT, name)

class Animal_shelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 1

    def enqueue(self, animal):
        animal.set_order(self.order)
        self.order += 1
        if animal.animal_type == Animal_type.DOG:
            self.dogs.append(animal)
        elif animal.animal_type == Animal_type.CAT:
            self.cats.append(animal)

    def dequeue_dog(self):
        return self.dogs.pop(0)

    def dequeue_cat(self):
        return self.cats.pop(0)

    def dequeue(self):
        if len(self.dogs) == 0 and len(self.cats) == 0:
            return None
        elif len(self.dogs) == 0:
            return self.cats.pop(0)
        elif len(self.cats) == 0:
            return self.dogs.pop(0)

        dog = self.dogs[0]
        cat = self.cats[0]

        if cat.order < dog.order:
            return self.cats.pop(0)
        else:
            return self.dogs.pop(0)

d1 = Dog("puppy")
d2 = Dog("chichi")
d3 = Dog("choco")
c1 = Cat("shasha")
c2 = Cat("miumiu")
c3 = Cat("gaga")

animal_shelter = Animal_shelter()
animal_shelter.enqueue(d1)
animal_shelter.enqueue(c1)
animal_shelter.enqueue(d2)
animal_shelter.enqueue(c2)
animal_shelter.enqueue(d3)
animal_shelter.enqueue(c3)

print(animal_shelter.dequeue_cat().info())
print(animal_shelter.dequeue_dog().info())
print(animal_shelter.dequeue().info())
print(animal_shelter.dequeue().info())
print(animal_shelter.dequeue().info())
print(animal_shelter.dequeue().info())
