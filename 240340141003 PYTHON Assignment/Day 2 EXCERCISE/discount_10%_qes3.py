
#3) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.


def calculate_cost(quantity):
    cost = quantity * 100
    if cost > 1000:
        discount = cost * 0.10
        cost = cost - discount
    return cost




quantity = int(input("Enter the quantity: "))

total_cost = calculate_cost(quantity)


print("Your total cost is: ", total_cost)