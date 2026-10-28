def second_largest(numbers):
    largest = None
    second = None
    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number
    return second

my_list = [10, 5, 8, 10, 3]
my_list2 = [4, 4, 4]
my_list3 = [-5, -2, -8, -3]
print(second_largest(my_list))
print(second_largest(my_list2))
print(second_largest(my_list3))