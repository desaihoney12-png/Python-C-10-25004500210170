p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time in years: "))

si = p * r * t / 100
amount = p + si

print("Simple interest =", si)
print("Total amount =", amount)
