num = int(input("Enter a number: "))
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

print("Armstrong numbers from 1 to 999:")
for n in range(1, 1000):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp = temp // 10
    if total == n:
        print(n, end=" ")
