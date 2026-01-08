"""
2 - Ask the user for their age and, based on that, use an if elif else structure to classify the age into categories according to the following conditions:

Child: 0 to 12 years old;
Teenager: 13 to 18 years old;
Adult: over 18 years old.
"""

def identify_age():
    # Receive and handle the data type
    try:
        age = int(input("What is your age?: "))
    except ValueError:
        return "Invalid age, please try again."

    # Perform the classification
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 18:
        return "Teenager"
    elif age > 18:
        return "Adult"
    else:
        return "Invalid age, please try again."


print(identify_age())
