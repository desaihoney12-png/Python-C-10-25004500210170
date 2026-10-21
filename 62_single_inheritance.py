class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

class Student(Person):
    def study(self):
        print(self.name, "is studying Python")

student = Student("Mina")
student.introduce()
student.study()
