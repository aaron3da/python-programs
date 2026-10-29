# Corrected program: print numbers from 1 to n

n = int(input("Enter the limit: "))

if n < 1:
    print("Enter a positive limit")
else:
    for i in range(1, n + 1):
        print(i)
