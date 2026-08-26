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