num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
