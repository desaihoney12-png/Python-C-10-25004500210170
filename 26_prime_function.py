def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

roll_no = int(input("Enter your roll number: "))
for n in range(roll_no, roll_no + 11):
    if is_prime(n):
        print(n, "is prime")
