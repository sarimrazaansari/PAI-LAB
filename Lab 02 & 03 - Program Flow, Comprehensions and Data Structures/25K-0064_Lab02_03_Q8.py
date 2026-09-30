# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 8

students = [("Ali", 78), ("Sara", 92), ("Bilal", 65), ("Hina", 85), ("Usman", 74)]

studentDict = dict(students)
average = sum(studentDict.values()) / len(studentDict)

aboveAvg = sorted(
    [(name, mark) for name, mark in studentDict.items() if mark > average],key=lambda item: item[1],reverse=True
)

print("Students:", studentDict)
print("Class average:", average)
print("Above average:")

for name, mark in aboveAvg:
    print(name, mark)
