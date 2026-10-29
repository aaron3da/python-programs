n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Enter a positive integer")
elif n == 1:
    print("1 is neither prime nor composite")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, "is a prime number")
    else:
        print(n, "is a composite number")
