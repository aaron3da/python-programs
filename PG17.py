numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

search = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search:
        print("Number found at index:", i)
        found = True
        break

if not found:
    print("Number not found")

# Selection sort
for i in range(len(numbers)):
    min_index = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Sorted list:", numbers)
print("Using built-in sort:", sorted(numbers))
