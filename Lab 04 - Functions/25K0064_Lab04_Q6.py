def statistics(numbers):
    if not numbers:
        return 0, 0, 0, 0, 0

    total = sum(numbers)
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return len(numbers), total, total / len(numbers), largest, smallest

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
count, total, average, largest, smallest = statistics(numbers)
print(count, total, average, largest, smallest)