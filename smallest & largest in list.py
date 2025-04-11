numbers = [25, 47, 3, 19, 8, 18]
smallest = numbers[0]
largest = numbers[0]
for num in numbers[1:]:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print("Smallest number in the list is:", smallest)
print("Largest number in the list is:", largest)
