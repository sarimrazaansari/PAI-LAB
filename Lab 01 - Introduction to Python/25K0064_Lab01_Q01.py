# 1. Calculate the BMI from two values input by the user, where BMI = weight / (height)².

weight=int(input("Enter weight: "))
height=int(input("Enter height: "))

bmi=weight/(height)**2

print(f"BMI = {bmi}")
