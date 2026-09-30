# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 5

primes_loop = []

for number in range(2, 101):
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes_loop.append(number)

primes_comprehension = [number for number in range(2, 101) if all(number % divisor != 0 for divisor in range(2, number))]

print("Nested loops:", primes_loop)
print("Comprehension:", primes_comprehension)

# The nested-loop version makes the divisibility check and break explicit, while the comprehension is shorter.
