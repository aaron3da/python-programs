import csv
from datetime import date, datetime

filename = "tasks.csv"

today = date.today()

try:
    with open(filename, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            task = row["task"]
            due_date = datetime.strptime(
                row["due_date"], "%Y-%m-%d"
            ).date()

            done = row["done"].lower() == "yes"

            if done:
                status = "Completed"

            elif due_date < today:
                status = "Overdue"

            else:
                status = "Pending"

            print("Task:", task)
            print("Due Date:", due_date)
            print("Status:", status)
            print("-------------------")

except FileNotFoundError:
    print("Task file not found")
