"""
calculator
"""

# float has decimal point

x = float(input("First number: "))
y = float(input("Second number: "))
z = x + y

# the , is used to ouput 1000000 as 1,000,000
# the .2f is used for rounding to 2 decimals or: round(x, 2)
print(f"{z:,.2f}")
