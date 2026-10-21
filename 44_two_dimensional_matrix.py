matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

for row in matrix:
    print("Row sum:", sum(row))

diagonal_sum = matrix[0][0] + matrix[1][1] + matrix[2][2]
print("Main diagonal sum:", diagonal_sum)
