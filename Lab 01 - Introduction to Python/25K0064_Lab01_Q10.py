# 10. Get the largest number from a list input by the user.
lst=[]
while True:
    no= int( input( "Enter a number (-1 to break) :"))
    if no==-1:
        break
    lst.append(no)

print("Largest value: ",max(lst))