n = int(input("Enter a number: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n, "is prime")
else:
    print(n, "is not prime")

limit = int(input("Print prime numbers up to: "))
for number in range(2, limit + 1):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        print(number, end=" ")
