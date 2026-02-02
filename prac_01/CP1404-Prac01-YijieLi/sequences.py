x = int(input("Enter x: "))
y = int(input("Enter y: "))

MENU = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y
4. Exit the program"""
print(MENU)

choice = input("Choose an option: ").strip()
while choice != "4":
    if choice == "1":
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print()
    elif choice == "2":
        for i in range(x, y + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print()
    elif choice == "3":
        for i in range(x, y + 1):
            print(i * i, end=" ")
        print()
    else:
        print("Invalid option")
    print(MENU)
    choice = input("Choose an option: ").strip()

print("Goodbye!")