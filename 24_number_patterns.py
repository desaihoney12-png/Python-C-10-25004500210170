print("Ascending pattern")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("Descending pattern")
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
