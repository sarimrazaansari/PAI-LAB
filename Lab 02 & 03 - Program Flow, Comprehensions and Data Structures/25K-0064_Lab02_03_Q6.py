# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 6

height = int(input("Enter height: "))

for i in range(1, height + 1):
    for j in range(i):
        print("*", end="")
    print()

print()

for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
