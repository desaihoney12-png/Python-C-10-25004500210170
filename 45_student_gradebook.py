students = {
    "Asha": [80, 75, 90],
    "Ravi": [65, 70, 68],
    "Mina": [92, 95, 89],
    "Jay": [72, 74, 70]
}

averages = {}
for name, marks in students.items():
    averages[name] = sum(marks) / len(marks)

for name, average in sorted(averages.items(), key=lambda item: item[1], reverse=True):
    print(name, "average:", round(average, 2))

top_student = max(averages, key=averages.get)
print("Top student:", top_student)
