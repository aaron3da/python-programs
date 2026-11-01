r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

A = []
B = []

print("Enter Matrix A:")

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter element: ")))
    A.append(row)

print("Enter Matrix B:")

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter element: ")))
    B.append(row)

C = []
D = []

for i in range(r):
    row1 = []
    row2 = []

    for j in range(c):
        row1.append(A[i][j] + B[i][j])
        row2.append(A[i][j] - B[i][j])

    C.append(row1)
    D.append(row2)

print("Addition:")
for row in C:
    print(row)

print("Subtraction:")
for row in D:
    print(row)
