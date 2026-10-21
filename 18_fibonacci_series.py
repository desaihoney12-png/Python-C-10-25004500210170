terms = int(input("How many terms? "))
a = 0
b = 1
count = 0

while count < terms:
    print(a, end=" ")
    a, b = b, a + b
    count = count + 1
