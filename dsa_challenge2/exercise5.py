def most_frequent(numbers):
    if not numbers:
        return None
    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) +1
    most_common = numbers[0]

    for number in numbers:
        if frequency[number] > frequency[most_common]:
            most_common = number
    return most_common

my_list = [2, 5, 2, 8, 2, 5]
my_list2 = [4, 7, 7, 4] 
print(most_frequent(my_list))
print(most_frequent(my_list2))
