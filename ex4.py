def count_divisible(numbers, divisor):
    count = 0
    for number in numbers:
        if number % divisor == 0:
            count += 1

    return count



print(count_divisible([3, 6, 7, 9, 12], 3))
