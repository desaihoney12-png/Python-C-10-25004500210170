num = int(input("Enter a 3-digit number: "))

hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

print("Hundreds digit:", hundreds)
print("Tens digit:", tens)
print("Units digit:", units)
print("Sum of digits:", hundreds + tens + units)
print("Product of digits:", hundreds * tens * units)
