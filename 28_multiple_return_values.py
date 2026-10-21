def stats(a, b, c):
    total = a + b + c
    average = total / 3
    return total, average, min(a, b, c), max(a, b, c)

total, average, smallest, largest = stats(10, 20, 30)
print("Sum:", total)
print("Average:", average)
print("Minimum:", smallest)
print("Maximum:", largest)
