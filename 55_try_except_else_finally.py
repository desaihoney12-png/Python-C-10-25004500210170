try:
    number = int(input("Enter a number: "))
    answer = 100 / number
except ValueError:
    print("Please enter a valid whole number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("Answer:", answer)
    print("No error occurred.")
finally:
    print("Program finished.")
