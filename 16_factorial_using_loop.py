n = int(input("Enter a non-negative number: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial =", factorial)
