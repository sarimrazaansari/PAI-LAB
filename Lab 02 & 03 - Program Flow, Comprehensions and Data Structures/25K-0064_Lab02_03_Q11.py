# Name: Sarim Raza Ansari
# Roll number: 25K-0064
# Question number: 11

cart = {}

while True:
    print("\n1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Total")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        cart[item] = cart.get(item, 0) + quantity
        print("Item added.")

    elif choice == "2":
        item = input("Enter item: ")
        if item in cart:
            quantity = int(input("Enter quantity to remove: "))
            if quantity >= cart[item]:
                del cart[item]
            else:
                cart[item] -= quantity
            print("Item removed.")
        else:
            print("Item not found.")

    elif choice == "3":
        if cart:
            for item, quantity in cart.items():
                print(item, ":", quantity)
        else:
            print("Cart is empty.")

    elif choice == "4":
        total = sum(cart.values())
        print("Total quantity:", total)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
