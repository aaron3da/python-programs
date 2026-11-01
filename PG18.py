rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []

    for j in range(cols):
        value = int(input("Enter element: "))
        row.append(value)

    matrix.append(row)

print("Matrix:")

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
