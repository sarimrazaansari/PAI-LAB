def apply_to_all(func, items):
    result = []
    for item in items:
        result.append(func(item))
    return result

def double(n):
    return n * 2

numbers = [1, 2, 3, 4, 5]
print(apply_to_all(double, numbers))
print(apply_to_all(lambda n: n ** 2, numbers))