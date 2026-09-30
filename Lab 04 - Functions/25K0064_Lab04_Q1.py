def is_even(n):
    return n % 2 == 0

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(list(filter(is_even, numbers)))