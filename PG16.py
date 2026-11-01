n = int(input("Enter number of marks: "))

marks = []

for i in range(n):
    value = float(input("Enter mark: "))
    marks.append(value)

print("Marks:", marks)
print("Minimum:", min(marks))
print("Maximum:", max(marks))
print("Sum:", sum(marks))
print("Average:", sum(marks) / n)
