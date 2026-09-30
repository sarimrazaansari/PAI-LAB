def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def power(base, exponent=2):
    return base ** exponent

for i in range(1, 11):
    print(i, factorial(i))

for i in range(1, 6):
    print(i, power(i), power(i, 3))