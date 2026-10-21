previous = int(input("Previous meter reading: "))
current = int(input("Current meter reading: "))

units = current - previous
bill = units * 5.50 + 100

print("Units consumed =", units)
print("Total bill =", bill)
