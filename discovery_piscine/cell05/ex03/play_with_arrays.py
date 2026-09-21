#!/usr/bin/env python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
new_numbers = []

for number in numbers:
    if number > 5:
        new_numbers.append(number + 2)

new_numbers = set(new_numbers)

print(numbers)
print(new_numbers)
