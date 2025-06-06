import random

# Line 1: randint(5, 20)
print(random.randint(5, 20))
# This returns a random integer between 5 and 20, inclusive
# Smallest possible value: 5
# Largest possible value: 20
# Sample outputs observed: 5, 7, 13, 20, etc.

# Line 2: randrange(3, 10, 2)
print(random.randrange(3, 10, 2))
# This returns a random number from the sequence: 3, 5, 7, 9
# Smallest possible value: 3
# Largest possible value: 9
# Could it produce a 4? → No, because 4 is not in the step sequence from 3 to 10 with step 2
# Sample outputs observed: 3, 5, 9, 7

# Line 3: uniform(2.5, 5.5)
print(random.uniform(2.5, 5.5))
# This returns a random float between 2.5 and 5.5
# Smallest possible value: 2.5 (theoretically)
# Largest possible value: 5.5 (theoretically)
# Sample outputs observed: 3.812, 5.321, 2.501, etc.

# Generate a random number between 1 and 100 (inclusive)
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
