def is_anagram(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()
    return sorted(first) == sorted(second)

pairs = [("listen", "silent"), ("hello", "world"),
         ("earth", "heart"), ("cat", "act")]

for first, second in pairs:
    print(first, second, ":", is_anagram(first, second))
