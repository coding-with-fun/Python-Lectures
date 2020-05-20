"""
Enter number of rows: 4
       *
     *   *
   *   *   *
 *   *   *   *
   *   *   *
     *   *
       *
"""

rows = int(input("Enter number of rows: "))
space = rows - 1

for i in range(1, rows+1):
    for j in range(space):
        print(" ", end=" ")

    for k in range(i):
        print("*  ", end=" ")

    space = space - 1
    print()

"""
    Here, as the spaces are reduced to 0 in 1st iteration, we've to redefine the spaces.
    But this time, the 1st line has 1 space. And it increases with time. 
    Thus, we'll redefine space as 1. But this time, the space increases with every iteration.
    Even, this time the loop will go in reverse, so we'll take loop till 0 and decrement it every time.
"""
space = 1
for i in range(rows-1, 0, -1):
    for j in range(space, 0, -1):
        print(" ", end=" ")

    for k in range(i, 0, -1):
        print("*  ", end=" ")

    space = space + 1
    print()