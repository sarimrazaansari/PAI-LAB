# 2. A simple calculator for `+ − * /` on two numbers, where (a) a `+` sign must not be used for addition, (b) a maximum of 3 variables is allowed, and (c) the program asks the user which operation to perform.

# Name: Sarim Raza Ansari
#Roll No: 25K0064
#Q2

var1=int(input("Enter a number: "))
var2=int(input("Enter a number: "))
operator=input("Enter operator (+ - / * ): ")

if operator=='+':
    print(var1-(-var2))
elif operator == '-':
    print(var1-var2)
elif operator == '*':
    print(var1*var2)
elif operator == '/':
    print(var1/var2)
else:
    print("Invalid operator ")