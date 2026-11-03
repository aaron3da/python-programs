import csv
import os

filename = "inventory.csv"


def add_product():

    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    if not name or quantity < 0 or price < 0:
        print("Invalid product details")
        return

    exists = os.path.exists(filename)

    with open(filename, "a", newline="") as file:

        writer = csv.writer(file)

        if not exists:
            writer.writerow(["Name", "Quantity", "Price"])

        writer.writerow([name, quantity, price])

    print("Product added successfully!")


def view_products():

    try:
        with open(filename, "r") as file:

            reader = csv.reader(file)

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No products found")


def calculate_value():

    total = 0

    try:
        with open(filename, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                total += int(row["Quantity"]) * float(row["Price"])

        print("Total inventory value:", total)

    except FileNotFoundError:
        print("No inventory available")


while True:

    print("\n--- INVENTORY MANAGEMENT ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Calculate Stock Value")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        calculate_value()

    elif choice == "4":
        print("Application closed")
        break

    else:
        print("Invalid choice")
