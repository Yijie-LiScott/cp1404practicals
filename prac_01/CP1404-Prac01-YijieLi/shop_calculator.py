"""
get number_of_items  // prompt: "Number of items: "
total = 0.0
for i from 1 to number_of_items
    get price  // prompt: "Price of item: "
    total = total + price
if total > 100
    total = total * 0.9  // apply 10% discount
print "Total price for", number_of_items, "items is $", total formatted to 2 decimal places
"""
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total = 0.0

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9  # apply 10% discount

print(f"Total price for {number_of_items} items is ${total:.2f}")
