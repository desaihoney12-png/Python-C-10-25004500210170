class Student:
    school = "LJMCA"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def welcome():
        print("Welcome to the student program")

student = Student("Ravi")
Student.welcome()
Student.change_school("New College")
print(student.name, student.school)
