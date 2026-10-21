with open("students.txt", "w") as file:
    file.write("Asha Patel\nRavi Shah\nMina Dave\n")

with open("students.txt", "r") as file:
    names = file.readlines()

for number, name in enumerate(names, 1):
    print(number, "-", name.strip())
