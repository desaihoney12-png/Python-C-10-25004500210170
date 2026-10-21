correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Wrong PIN")
        attempts = attempts + 1

if attempts == 3:
    print("Card Blocked")
