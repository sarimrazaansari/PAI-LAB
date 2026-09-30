# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 1

numbers = [12, 7, 40, 3, 25, 18, 9, 21]

for number in numbers:
    if number % 3 == 0:
        print(number)

print([number for number in numbers if number % 3 == 0])
