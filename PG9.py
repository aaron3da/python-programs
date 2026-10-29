n = int(input("Enter a number: "))
limit = int(input("Enter the table limit: "))

if limit < 1:
    print("Limit must be positive")
else:
    for i in range(1, limit + 1):
        print(n, "x", i, "=", n * i)
