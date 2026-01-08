"""
rainz - 07/01/2026
               
2. Find the different number

In an array where all numbers are even except one, find the odd number. Or all are odd except one even number.

Example
Input: [2, 4, 6, 9, 8]
Output: 9
"""

def find_different_number(dirty_array):
    even_array = []
    odd_array = []

    for x in dirty_array:
        if x % 2 == 0:
            even_array.append(x)
        else:
            odd_array.append(x)

    if len(even_array) == 1:
        return even_array[0]
    else:
        return odd_array[0]

result = find_different_number([2, 4, 6, 9, 8])
print(result)
