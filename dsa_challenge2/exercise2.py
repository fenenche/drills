def move_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros_count = len(numbers) - len(non_zeros)
    return non_zeros + [0] * zeros_count
my_list = [0, 1, 0, 3, 12]
my_list2 = [4, 0, 5, 0, 2]
my_list3 = [1, 2, 3]
print(move_zeros(my_list))
print(move_zeros(my_list2))
print(move_zeros(my_list3))