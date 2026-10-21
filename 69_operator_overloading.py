class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

first = Number(10)
second = Number(20)
print("Sum:", first + second)
