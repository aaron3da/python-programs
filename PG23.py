contacts = {}

while True:

    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            contacts[name] = input("Enter new phone number: ")
            print("Contact updated")
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == "5":
        print(contacts)

    elif choice == "6":
        break

    else:
        print("Invalid choice")
