"""
1 - Ask the user to enter a number and then use an if else structure to determine whether the number is even or odd.
"""

def even_or_odd():
    # Receive and validate whether the provided number is valid
    try:
        num = int(input("Enter the number you want to check: "))
    except ValueError:
        return "Invalid value. Please enter an integer."

    # Operation
    if num % 2 == 0:
        return f"The number {num} is even!"
    else:
        return f"The number {num} is odd!"

print(even_or_odd())