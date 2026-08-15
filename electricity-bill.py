
# Electricity Bill Program Using a Function

# The billing rules are:

# First 100 units → Rs. 5 per unit
# Next 100 units (101–200) → Rs. 7 per unit
# Above 200 units → Rs. 10 per unit


def electricity_bill(units):
    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    return bill


# Taking input from user
units = int(input("Enter the number of units consumed: "))

# Calling the function
bill = electricity_bill(units)

print("Electricity Bill = Rs.", bill)