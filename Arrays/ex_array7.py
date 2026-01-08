"""
rainz - 07/01/2026

7. Find the largest number

Create a function that finds the largest value in an array, without using built-in functions.

Example
Input: [10, 5, 20, 8]
Output: 20
"""

def find_largest_number(int_array=[]):
    largest_number = int_array[0]
    for x in int_array:
        if x > largest_number:
            largest_number = x
    return largest_number

print(find_largest_number([10, 5, 20, 8]))



