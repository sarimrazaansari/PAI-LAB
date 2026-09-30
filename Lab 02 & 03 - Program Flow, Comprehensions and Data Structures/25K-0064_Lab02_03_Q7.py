# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 7

marks1 = {"Physics": 78, "Maths": 90, "Chemistry": 45}
marks2 = {"Maths": 80, "Chemistry": 55, "English": 70}

merged = marks1.copy()

for subject, mark in marks2.items():
    merged[subject] = merged.get(subject, 0) + mark

print(merged)
