# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 3

numbers = [4, 2, 4, 7, 2, 9, 7, 7, 1]

seen = set()
unique = []

for number in numbers:
    if number not in seen:
        seen.add(number)
        unique.append(number)

removed = len(numbers) - len(unique)

print("Original:", numbers)
print("Without duplicates:", unique)
print("Duplicates removed:", removed)
