r1 = int(input("Enter rows of A: "))
c1 = int(input("Enter columns of A: "))

r2 = int(input("Enter rows of B: "))
c2 = int(input("Enter columns of B: "))

if c1 != r2:
    print("Matrix multiplication not possible")

else:
    A = []
    B = []

    print("Enter Matrix A:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input("Enter element: ")))
        A.append(row)

    print("Enter Matrix B:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input("Enter element: ")))
        B.append(row)

    C = [[0 for j in range(c2)] for i in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    print("Result:")
    for row in C:
        print(row)
