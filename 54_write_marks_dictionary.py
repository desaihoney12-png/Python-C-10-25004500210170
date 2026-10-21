marks = {"Asha": 88, "Ravi": 76, "Mina": 91}

with open("marks.txt", "w") as file:
    for name, score in marks.items():
        file.write(f"{name}: {score}\n")

print("Marks saved to marks.txt")
