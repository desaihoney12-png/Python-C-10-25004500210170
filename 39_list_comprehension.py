squares = [n * n for n in range(1, 21)]
evens = [n for n in range(1, 51) if n % 2 == 0]
sentence = "Python makes learning programming fun"
long_words = [word for word in sentence.split() if len(word) > 4]
cubes = [n ** 3 for n in range(1, 16) if n % 2 != 0]

print("Squares:", squares)
print("Even numbers:", evens)
print("Words longer than 4 letters:", long_words)
print("Cubes of odd numbers:", cubes)
