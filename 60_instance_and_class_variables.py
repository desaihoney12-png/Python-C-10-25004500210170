class Employee:
    company = "ABC Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary, Employee.company)

e1 = Employee("Asha", 25000)
e2 = Employee("Ravi", 30000)
e1.display()
e2.display()
