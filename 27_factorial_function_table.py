def factorial(n):
    answer = 1
    for i in range(1, n + 1):
        answer = answer * i
    return answer

print("Number   Factorial")
for n in range(1, 11):
    print(n, "      ", factorial(n))
