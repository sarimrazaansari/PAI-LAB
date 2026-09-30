def grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    return "F"

marks = [92, 85, 76, 68, 59, 43, 81]
result = [(mark, grade(mark)) for mark in marks]

counts = {}
for mark, letter in result:
    counts[letter] = counts.get(letter, 0) + 1

print(result)
print(counts)