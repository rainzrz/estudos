"""
█▀▀█ █▀▀█ ▀█▀ █▄─ █ █▀▀▀█ 
█▄▄▀ █▄▄█  █─ █ █ █ ▄▄▄▀▀ 
█─ █ █─ █ ▄█▄ █──▀█ █▄▄▄█
               07/01/2026
               
3. Count occurrences

Create a function that counts how many times each number appears in an array.

Example
Input: [1, 2, 2, 3, 3, 3]
Output: {1: 1, 2: 2, 3: 3}
"""

def count_number_occurrences():
    dirty_array = [1, 2, 2, 3, 3, 3]
    counter = {}

    for x in dirty_array:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1

    print(counter)

count_number_occurrences()
