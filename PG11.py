balance = float(input("Enter starting balance: "))
deposit = float(input("Enter monthly deposit: "))
months = int(input("Enter number of months: "))

if balance < 0 or deposit < 0 or months < 0:
    print("Invalid input")
else:
    for month in range(1, months + 1):
        balance = balance + deposit
        print("Month", month, "Balance:", balance)

    print("Final balance:", balance)
