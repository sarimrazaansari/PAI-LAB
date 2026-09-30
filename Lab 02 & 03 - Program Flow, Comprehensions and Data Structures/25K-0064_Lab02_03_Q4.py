# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 4

marks = {"Physics": 78, "Chemistry": 45, "Maths": 78, "English": 92}

inverted = {mark: subject for subject, mark in marks.items()}

print(inverted)

# If two subjects have the same mark, the later subject overwrites the earlier subject for that key.
