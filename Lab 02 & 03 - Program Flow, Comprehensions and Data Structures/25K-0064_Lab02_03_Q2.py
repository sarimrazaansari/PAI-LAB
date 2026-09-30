# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 2

fizzbuzz = ["FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n) for n in range(1, 51)]

for item in fizzbuzz:
    print(item)
