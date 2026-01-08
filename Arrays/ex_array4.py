"""
rainz - 07/01/2026

4. Check if a number is prime

Create a function that receives a number and returns whether it is prime or not.

Example
Input: 7
Output: true
"""

def is_prime(num):
    divisors = 0
    for x in range(1, num + 1):
        if num % x == 0:
            divisors += 1

    if divisors == 2:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

is_prime(2)
