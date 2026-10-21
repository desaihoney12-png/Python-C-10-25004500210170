class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Average:", round(self.average(), 2))

students = [
    Student("Asha", [80, 85, 90]),
    Student("Ravi", [70, 75, 78]),
    Student("Mina", [90, 92, 95])
]

for student in students:
    student.display()
    print()
