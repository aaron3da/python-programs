import csv
import os

filename = "attendance.csv"

while True:

    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        status = input("Enter attendance (P/A): ").upper()

        if status not in ["P", "A"]:
            print("Invalid attendance status")

        else:
            file_exists = os.path.exists(filename)

            with open(filename, "a", newline="") as file:

                writer = csv.writer(file)

                if not file_exists:
                    writer.writerow(["Roll No", "Name", "Status"])

                writer.writerow([roll, name, status])

            print("Attendance saved!")

    elif choice == "2":

        try:
            with open(filename, "r") as file:

                reader = csv.reader(file)

                for row in reader:
                    print(row)

        except FileNotFoundError:
            print("No attendance records found")

    elif choice == "3":
        break

    else:
        print("Invalid choice")
