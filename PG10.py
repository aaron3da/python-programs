n = int(input("Enter number of rows: "))

print("Number triangle:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nInverted star triangle:")
for i in range(n, 0, -1):
    print("* " * i)

print("\nPyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
