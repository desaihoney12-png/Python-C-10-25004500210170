numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
other_numbers = [2, 4, 6, 8]

print("Original list:", numbers)
print("Without duplicates:", list(set(numbers)))
print("In first list but not second:", list(set(numbers) - set(other_numbers)))

frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print("Counts:", frequency)
