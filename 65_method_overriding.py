class Animal:
    def sound(self):
        print("Animal makes a sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

animal = Animal()
cat = Cat()
animal.sound()
cat.sound()
