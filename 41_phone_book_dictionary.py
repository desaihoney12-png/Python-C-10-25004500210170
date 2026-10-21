phone_book = {
    "Asha": "9876543210",
    "Ravi": "9876501234",
    "Mina": "9988776655",
    "Jay": "9123456780",
    "Kiran": "9000011111"
}

name = input("Search contact name: ")
if name in phone_book:
    print("Number:", phone_book[name])
else:
    print("Contact not found")

phone_book["Ravi"] = "9000099999"
phone_book["Neha"] = "9111122222"
phone_book.pop("Jay", None)

print("All contacts:")
for name in sorted(phone_book):
    print(name, ":", phone_book[name])
