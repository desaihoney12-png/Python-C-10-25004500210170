class LivingThing:
    def breathe(self):
        print("Breathing")

class Animal(LivingThing):
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.breathe()
dog.eat()
dog.bark()
