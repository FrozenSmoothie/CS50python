"""
Basics of the Basics
"""

# remove whitespace
# .strip()
# capitalizing first letter of name
# .capitalize()
# capitalizing every word
# .title()

# retrieve name
name = input("What's your name? ").strip().title()

# split into first name and last name
firstName, lastName = name.split(" ")

# greeting
print("Hello, \"" + name + "\"!")
print("Hello, " + name + "!")
print(f"Hello, {name}!")
print(f"Hello, {firstName}!")
print(f"Hello, {lastName}!")

# str -> literal text
# int -> numbers without decimal
# operators -> +-*/%


