# Original list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Without running the code, predicted answers:
# numbers[0] → 3
# numbers[-1] → 2
# numbers[3] → 1
# numbers[:-1] → [3, 1, 4, 1, 5, 9]
# numbers[3:4] → [1]
# 5 in numbers → True
# 7 in numbers → False
# "3" in numbers → False
# numbers + [6, 5, 3] → [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Now test and modify the list:
numbers[0] = "ten"
numbers[-1] = 1

# Print all elements except the first two
print(numbers[2:])

# Print whether 9 is in the list
print(9 in numbers)
