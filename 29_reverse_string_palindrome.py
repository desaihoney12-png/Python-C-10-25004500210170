def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == reverse_string(s)

words = ["madam", "racecar", "Ahmedabad", "Python"]
for word in words:
    print(word, "reversed:", reverse_string(word))
    print("Palindrome:", is_palindrome(word))
