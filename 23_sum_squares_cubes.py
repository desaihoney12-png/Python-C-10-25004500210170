n = int(input("Enter N: "))
sum_n = 0
sum_squares = 0
sum_cubes = 0

for i in range(1, n + 1):
    sum_n = sum_n + i
    sum_squares = sum_squares + i ** 2
    sum_cubes = sum_cubes + i ** 3

print("Sum of natural numbers =", sum_n)
print("Sum of squares =", sum_squares)
print("Sum of cubes =", sum_cubes)
