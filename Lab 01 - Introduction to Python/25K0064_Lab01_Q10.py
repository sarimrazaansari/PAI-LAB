# 10. Get the largest number from a list input by the user.

# Name: Sarim Raza Ansari
#Roll No: 25K0064
#Q10

lst=[]
while True:
    no= int( input( "Enter a number (-1 to break) :"))
    if no==-1:
        break
    lst.append(no)

print("Largest value: ",max(lst))