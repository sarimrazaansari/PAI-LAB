# 5. Take a list and a number, then delete every element of the list that is less than that number.

# Name: Sarim Raza Ansari
#Roll No: 25K0064
#Q5

lst=[]

while True:
    no=int(input("Enter a number to add in list (-1 to exit) :"))

    if no==-1:
        break

    lst.append(no)

delete=int(input("Enter a number less than will delete: "))

for i in lst:
    lst.remove(i) if i<delete else None

print("List: ",lst)