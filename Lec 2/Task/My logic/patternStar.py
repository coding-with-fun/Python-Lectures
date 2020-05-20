"""
Enter no of rows: 4
       *
     *   *
   *   *   *
 *   *   *   *
"""

rows = int(input("Enter no of rows: "))
space = rows-1
# space logic made simple

for i in range(rows):
    for j in range(space):
        print(" ", end=" ")
        # One space here in loop

    for k in range(i+1):
        print(" * ", end=" ")
        # Three spaces here in end parameter

    print("")
    space = space-1
    # Change in decrement