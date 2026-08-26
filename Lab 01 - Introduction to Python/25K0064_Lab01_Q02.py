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