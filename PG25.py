import csv
from collections import defaultdict

filename = "expenses.csv"

category = input("Enter expense category: ")
amount = float(input("Enter expense amount: "))
description = input("Enter description: ")

with open(filename, "a", newline="") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["Category", "Amount", "Description"])

    writer.writerow([category, amount, description])

print("Expense saved successfully!")

totals = defaultdict(float)

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        totals[row["Category"]] += float(row["Amount"])

print("\nExpense Summary:")

for category, total in totals.items():
    print(category, ":", total)
