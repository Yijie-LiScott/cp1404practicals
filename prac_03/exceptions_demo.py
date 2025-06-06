"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user enters something that cannot be converted to an integer (e.g. a string "abc" or a float "5.5")
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters 0 as the denominator, because dividing by zero is not allowed in mathematics or Python.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, we can use while loop to ask for valid non-zero user input for denominator to avoid ZeroDivisionError.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter a non-zero denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")