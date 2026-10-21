paragraph = input("Enter a paragraph: ").lower()
words = paragraph.split()
frequency = {}

for word in words:
    word = word.strip(".,!?")
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

for word, count in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
    print(word, ":", count)
