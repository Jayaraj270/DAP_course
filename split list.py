my_list = [1, 1, 2, 3, 4, 4, 5, 1]
split_length = 3
if 0 <= split_length <= len(my_list):
    first_part = []
    second_part = []

    for i in range(len(my_list)):
        if i < split_length:
            first_part.append(my_list[i])
        else:
            second_part.append(my_list[i])

    print("First part of the list:", first_part)
    print("Second part of the list:", second_part)
else:
    print("Invalid split length.")
