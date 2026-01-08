"""
rainz - 07/01/2026
               
1. Remove duplicate numbers from an array

Given an array of integers, return a new array containing only unique values, keeping the original order.

Example
Input: [1, 2, 2, 3, 4, 4]
Output: [1, 2, 3, 4]
"""

dirty_array = [1, 2, 2, 3, 4, 4]
clean_array = []

for x in dirty_array:
    if x not in clean_array:
        clean_array.append(x)

print(clean_array)
