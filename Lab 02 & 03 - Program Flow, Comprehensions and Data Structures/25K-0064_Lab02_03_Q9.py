# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 9

list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 6, 8, 10]
list3 = [0, 2, 4, 6, 12]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

common = set1 & set2 & set3
exactlyOne = (set1 ^ set2 ^ set3) - common
distinct = set1 | set2 | set3

print("Common to all three:", common)
print("Appearing in exactly one:", exactlyOne)
print("Complete set of distinct values:", distinct)
