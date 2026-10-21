student_name = input("Student name: ")
roll_no = input("Roll number: ")
marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 500 * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 35:
    grade = "D"
else:
    grade = "Fail"

print("\n----- REPORT CARD -----")
print(f"Name: {student_name}")
print(f"Roll No: {roll_no}")
print(f"Total: {total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
