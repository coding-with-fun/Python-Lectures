n = int(input("Enter number of lines: "))
patt = input("Enter the desired pattern symbol: ")


def pat(n, patt):
    space = n - 1

    for i in range(n):
        for j in range(space):
            print(" ", end=" ")

        for k in range(i + 1):
            print(patt, end="   ")

        print("")
        space = space - 1


pat(n, patt)
