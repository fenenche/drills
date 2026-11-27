def count_letter(text, letter):
    count = 0
    target = letter.lower()

    for char in text:
        if char.lower() == target:
            count += 1

    return count

print(count_letter("banana", "a"))
