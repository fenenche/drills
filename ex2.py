def index_of_smallest(numbers):
    if not numbers:
        return -1
    smallest_index = 0
    for i, num in enumerate(numbers):
        if num < numbers[smallest_index]:
            smallest_index = i

    return smallest_index

my_list = [8, 3, 12, 1, 7]
my_list = [-3, -10, -1, -6]

print(index_of_smallest(my_list))
