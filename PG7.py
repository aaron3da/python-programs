n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Invalid number")
else:
    temp = n
    count = 0
    total = 0
    reverse = 0

    if n == 0:
        count = 1

    while temp > 0:
        digit = temp % 10

        count += 1
        total += digit
        reverse = reverse * 10 + digit

        temp = temp // 10

    print("Digit count:", count)
    print("Digit sum:", total)
    print("Reversed number:", reverse)
