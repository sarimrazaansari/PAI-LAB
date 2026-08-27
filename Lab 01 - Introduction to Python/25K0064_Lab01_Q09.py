# 9. Print the multiplication table (1 to 10) of a number entered by the user.

# Name: Sarim Raza Ansari
#Roll No: 25K0064
#Q9

while True:
    no=int(input("Enter a number: (bw 1-10) :"))
    if no <1 or no>10:
        print("Enter bw 1-10 ")
        continue

    for i in range(1,11):
        print(f"{no} x {i} = {no*i}")
    break