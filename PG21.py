r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

A = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input("Enter element: ")))
    A.append(row)

print("Original Matrix:")
for row in A:
    print(row)

print("Transpose:")

for j in range(c):
    for i in range(r):
        print(A[i][j], end=" ")
    print()
