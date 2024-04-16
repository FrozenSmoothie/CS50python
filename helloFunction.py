# defining hello() function with to as argument and World as default
def hello(to="World"):
    print(f"Hello, {to}")


# retrieving name
name = input("What's your name? ").strip().title()

# using function
hello()
hello(to=name)
hello(name)
