"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter the sales: $"))
if sales < 1000:
    print("The user gets a 10% bonus.")
    bonus = sales * 0.10
    print("The bonus is $%.2f" % bonus)
else :
    print("The user gets a 15% bonus.")
    bonus = sales * 0.15
    print("The bonus is $%.2f" % bonus)