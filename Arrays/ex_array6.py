"""
█▀▀█ █▀▀█ ▀█▀ █▄─ █ █▀▀▀█ 
█▄▄▀ █▄▄█  █─ █ █ █ ▄▄▄▀▀ 
█─ █ █─ █ ▄█▄ █──▀█ █▄▄▄█
               07/01/2026
               
6. Sum only even numbers

Given an array of numbers, return the sum of only the even numbers.

Example
Input: [1, 2, 3, 4, 6]
Output: 12
"""

dirty_array = [1, 2, 3, 4, 6]
clean_array = []

for x in dirty_array:
    if x % 2 == 0:
        clean_array.append(x)

length = len(clean_array)

counter = 0
total = 0

while counter < length:
    total += clean_array[counter]
    counter += 1

print(f"The sum of {clean_array} is {total}")
