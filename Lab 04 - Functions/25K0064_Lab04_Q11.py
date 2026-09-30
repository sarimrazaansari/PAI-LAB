def describe(**details):
    for field, value in details.items():
        print(field, "=", value)

def total(*numbers):
    return sum(numbers)

describe(name="Ali")
describe(name="Sara", age=20)
describe(name="Bilal", age=21, section="A")

print(total(5))
print(total(5, 10))
print(total(5, 10, 15, 20))