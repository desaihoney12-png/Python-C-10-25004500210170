basic = float(input("Enter basic salary: "))

hra = basic * 20 / 100
da = basic * 10 / 100
pf = basic * 12 / 100
gross = basic + hra + da
net = gross - pf

print("HRA =", hra)
print("DA =", da)
print("PF =", pf)
print("Gross salary =", gross)
print("Net salary =", net)
