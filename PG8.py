n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Invalid number")
else:
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    if total == n:
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")
