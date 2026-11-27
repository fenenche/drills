def sum_above(numbers, limit):
    total = 0

    for number in numbers:
        if number > limit:
            total += number
    
    return total

print(sum_above([10, 3, 25, 8, 40], 9))
