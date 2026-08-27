# 3. Take an integer list from the user, count all the even numbers in it, and print the count.

# Name: Sarim Raza Ansari
#Roll No: 25K0064
#Q3

lst=[]
count=0
while True:
    number=int(input("Enter a number (Enter -1 to exit) :"))
    if number==-1:
        break
    
    count+=1 if number%2==0 else 0

    lst.append(number)


print("List: ",lst)
print("Even: ", count)