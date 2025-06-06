# 1. Write user's name to file
# Using open() and close()

name = input("Enter your name: ")
file_out = open("name.txt", "w")
file_out.write(name)
file_out.close()


# 2. Read name from file and greet
# Using open() and close()

file_in = open("name.txt", "r")
stored_name = file_in.read().strip()  # .strip() to remove newline if any
file_in.close()
print(f"Hi {stored_name}!")


# 3. Read first 2 numbers in numbers.txt and add
# Using with and readline()

with open("numbers.txt", "r") as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    total = number1 + number2
    print(f"Sum of first two numbers: {total}")  # Expected output: 59


# 4. Read all numbers and calculate total
# Using with and for loop

with open("numbers.txt", "r") as file:
    total_all = 0
    for line in file:  # each line is a string
        number = int(line)
        total_all += number
    print(f"Total of all numbers: {total_all}")


# 4. Read all numbers and calculate total
# Using with and for loop

with open("numbers.txt", "r") as file:
    total_all = 0
    for line in file:  # each line is a string
        number = int(line)
        total_all += number
    print(f"Total of all numbers: {total_all}")
