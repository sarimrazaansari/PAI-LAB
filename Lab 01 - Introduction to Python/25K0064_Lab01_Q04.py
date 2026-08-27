# 4. Take a list of numbers and return the sum of all its elements.

# Name: Sarim Raza Ansari
#Roll No: 25K0064
#Q4

lst=list()
while True:
    number= int(input("Enter a number (Enter -1 to exit) :"))
    if number ==-1:
        break
    lst.append(number)

print("Sum of the number in list is: ",sum(lst))
