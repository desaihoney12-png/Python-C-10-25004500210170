class Dog:
    def speak(self):
        print("Dog says woof")

class Cat:
    def speak(self):
        print("Cat says meow")

class Cow:
    def speak(self):
        print("Cow says moo")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.speak()
