try:
    with open("marks.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found.")

def check_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")
    return marks

try:
    score = int(input("Enter marks: "))
    print("Valid marks:", check_marks(score))
except ValueError as error:
    print("Problem:", error)
