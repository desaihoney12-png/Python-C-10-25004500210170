class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(self.title, "by", self.author)

book1 = Book("Python Basics", "R. Shah")
book1.display()
