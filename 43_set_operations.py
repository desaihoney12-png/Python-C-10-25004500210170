set1 = set(range(1, 16, 2))
set2 = {n for n in range(1, 16) if n % 3 == 0}

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Set1 - Set2:", set1 - set2)
print("Set2 - Set1:", set2 - set1)
print("Symmetric difference:", set1 ^ set2)
