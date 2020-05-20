rows = int(input("Enter no of rows: "))
space = rows*2-2
count = 1

for i in range(rows):
    for j in range(space):
        print(" ", end="")

    for k in range(i+1):
        print(count, " ", end=" ")
        count = count+1

    print("")
    space = space-2
