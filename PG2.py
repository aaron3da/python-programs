marks = float(input("Enter percentage marks: "))
income = float(input("Enter annual family income: "))
attendance = float(input("Enter attendance percentage: "))

if marks >= 80 and income <= 250000 and attendance >= 75:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
