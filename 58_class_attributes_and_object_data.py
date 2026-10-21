class Student:
    college = "LJMCA"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll number:", self.roll_no)
        print("College:", Student.college)

student1 = Student("Asha", 1)
student2 = Student("Ravi", 2)
student1.display()
student2.display()
