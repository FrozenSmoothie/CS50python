# main part of the code on top of the file
def main():
    name = input("What's your name? ").strip().title()
    hello(name)


async def hello(to="world"):
    print("Hello,", to)

# this calls main() after which main() calls hello()
main()
