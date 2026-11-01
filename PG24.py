inventory = {}

while True:

    print("\n1. Add Product")
    print("2. Display Inventory")
    print("3. Calculate Stock Value")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        if quantity < 0 or price < 0:
            print("Invalid values")
        else:
            inventory[name] = {
                "quantity": quantity,
                "price": price
            }

            print("Product added")

    elif choice == "2":

        for name, details in inventory.items():
            print(name, details)

    elif choice == "3":

        total = 0

        for details in inventory.values():
            total += details["quantity"] * details["price"]

        print("Total stock value: Rs.", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
