marks = (70, 80, 65, 90, 75)

print("First mark:", marks[0])
print("First three:", marks[:3])
print("Length:", len(marks))
print("Minimum:", min(marks))
print("Maximum:", max(marks))
print("Average:", sum(marks) / len(marks))

try:
    marks[0] = 100
except TypeError:
    print("A tuple cannot be changed")

mark_list = list(marks)
mark_list[0] = 100
marks = tuple(mark_list)
print("Updated tuple:", marks)
