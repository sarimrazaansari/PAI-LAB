pairs = [
    ("Ali", [78, 45, 90]),
    ("Sara", [88, 92, 95]),
    ("Bilal", [40, 38, 52]),
    ("Hina", [61, 72, 58])
]

names, marks = zip(*pairs)
averages = list(map(lambda values: sum(values) / len(values), marks))
ranked = sorted(zip(names, marks, averages), key=lambda item: item[2], reverse=True)

class_average = sum(averages) / len(averages)
above_average = list(filter(lambda item: item[2] > class_average, ranked))

print(ranked)
print(above_average)