def large(i):
    largest = i[0]  
    for num in i:
        if num > largest:
            largest = num
    return largest
numbers = [27,9,7,3,4,23]
largest_number = large(numbers)
print(f"Largest number is: {largest_number}")
