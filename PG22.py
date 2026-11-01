n = int(input("Enter order of square matrix: "))

A = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input("Enter element: ")))
    A.append(row)

identity = True
diagonal = True

for i in range(n):
    for j in range(n):

        if i == j and A[i][j] != 1:
            identity = False

        if i != j and A[i][j] != 0:
            identity = False
            diagonal = False

print("Identity matrix:", identity)
print("Diagonal matrix:", diagonal)

print("Generated identity matrix:")

for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
