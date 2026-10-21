a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Before swap:", a, b)
a, b = b, a
print("After tuple swap:", a, b)

# Arithmetic swap
a = a + b
b = a - b
a = a - b
print("After arithmetic swap:", a, b)
