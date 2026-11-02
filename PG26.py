import csv

filename = "marks.csv"

try:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        students = []

        for row in reader:
            name = row["name"]
            marks = float(row["marks"])

            students.append((name, marks))

    if len(students) == 0:
        print("No student records found")

    else:
        total = 0

        with open("report.txt", "w") as report:

            report.write("STUDENT MARKS REPORT\n")

            for name, marks in students:
                report.write(name + " : " + str(marks) + "\n")
                total += marks

            average = total / len(students)
            highest = max(students, key=lambda x: x[1])
            lowest = min(students, key=lambda x: x[1])

            report.write("\nAverage Marks: " + str(average))
            report.write("\nHighest Marks: " + str(highest))
            report.write("\nLowest Marks: " + str(lowest))

        print("Report generated successfully!")

except FileNotFoundError:
    print("marks.csv file not found")
