def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        z = i - 1

        while z >= 0 and numbers[z] > key:
            numbers[z + 1] = numbers[z]
            z -= 1

        numbers[z + 1] = key
    return numbers
my_list = [5, 3, 4]
print(insertion_sort(my_list))