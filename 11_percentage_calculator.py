m1 = float(input("Marks in subject 1: "))
m2 = float(input("Marks in subject 2: "))
m3 = float(input("Marks in subject 3: "))
m4 = float(input("Marks in subject 4: "))
m5 = float(input("Marks in subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 500 * 100
average = total / 5

print("Total =", total)
print("Percentage =", percentage)
print("Average =", average)
