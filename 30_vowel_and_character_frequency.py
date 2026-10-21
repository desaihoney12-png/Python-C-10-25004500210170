def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count = count + 1
    return count

def char_frequency(text):
    frequency = {}
    for ch in text:
        if ch in frequency:
            frequency[ch] = frequency[ch] + 1
        else:
            frequency[ch] = 1
    return frequency

sentence = input("Enter a sentence: ")
print("Vowels:", count_vowels(sentence))
print("Character frequency:", char_frequency(sentence))
