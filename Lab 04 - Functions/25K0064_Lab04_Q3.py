def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

celsius = list(map(float, input("Enter Celsius values separated by spaces: ").split()))
fahrenheit = list(map(celsius_to_fahrenheit, celsius))
converted = list(map(fahrenheit_to_celsius, fahrenheit))

for c, f in zip(celsius, fahrenheit):
    print(c, f)

print(converted)