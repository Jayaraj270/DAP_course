numbers = [4, 7, 2, 7, 9, 4, 1, 3, 2, 6, 2]
duplicates = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

print("Duplicate values in the list are:", duplicates)
