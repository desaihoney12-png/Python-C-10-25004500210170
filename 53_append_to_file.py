with open("diary.txt", "a") as file:
    note = input("Write a short note: ")
    file.write(note + "\n")

print("Your note was saved.")
