def main():
    x = int(input("What's X? "))
    print("X squared is ", square(x), "!", sep="")


def square(n):
    return n * n


main()
