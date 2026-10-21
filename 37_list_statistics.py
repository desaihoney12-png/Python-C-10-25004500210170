numbers = []
n = int(input("How many numbers? "))

for i in range(n):
    numbers.append(int(input("Enter a number: ")))

print("List:", numbers)
print("Sorted:", sorted(numbers))
print("Reversed:", numbers[::-1])
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
