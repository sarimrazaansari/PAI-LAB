def bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(value):
    if value < 18.5:
        return "Underweight"
    elif value < 25:
        return "Normal"
    elif value < 30:
        return "Overweight"
    return "Obese"

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
value = bmi(weight, height)
print(value)
print(bmi_category(value))