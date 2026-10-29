age = int(input("Enter age: "))
quantity = int(input("Enter number of tickets: "))

if age < 0 or quantity <= 0:
    print("Invalid input")
else:
    if age < 5:
        rate = 0
    elif age < 18:
        rate = 100
    elif age < 60:
        rate = 200
    else:
        rate = 120

    total = rate * quantity

    print("Rate per ticket: Rs.", rate)
    print("Total ticket cost: Rs.", total)
