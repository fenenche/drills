def closest_number(numbers, target):
    if not numbers:
        return None
    closest = numbers[0]

    for number in numbers:
        if abs(number - target) < abs(closest - target):
            closest = number
        elif abs(number - target) == abs(closest - target):
            if number < closest:
                closest = number
                
    return closest
my_list = closest_number(numbers = [4, 8, 15, 20], target = 13)
print(my_list)