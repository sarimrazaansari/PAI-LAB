# 8. Iterate over 1 to 50 printing `Fizz` for multiples of three, `Buzz` for multiples of five and `FizzBuzz` for multiples of both.

# Name: Sarim Raza Ansari
#Roll No: 25K0064
#Q8

for i in range(1,50):
    if i%15==0:
        i='FizzBuzz'
    elif i %3 ==0:
        i='Fuzz'
    elif i%5==0:
        i='Buzz'
    print(i)
    