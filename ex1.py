def largest_even(numbers):
    max_even = None

    for num in numbers:
        if num % 2 == 0:
            if max_even is None or num > max_even:
                max_even = num
    return max_even 

print(largest_even([3, 8, 15, 22, 7, 14]))





