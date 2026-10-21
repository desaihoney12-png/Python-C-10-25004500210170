students = [("Asha", 72), ("Ravi", 55), ("Mina", 91),
            ("Jay", 63), ("Kiran", 48)]

students.sort(key=lambda student: student[1], reverse=True)
print("Sorted by marks:")
for student in students:
    print(student)

print("Students with marks 60 or more:")
for student in students:
    if student[1] >= 60:
        print(student)
