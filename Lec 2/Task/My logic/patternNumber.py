"""
Enter no of rows: 4
      1
    2   3
  4   5   6
7   8   9   10
"""

rows = int(input("Enter no of rows: "))
space = rows-1
# space logic made simple

count = 1

for i in range(rows):
    for j in range(space):
        print(" ", end=" ")
        # One space here in loop

    for k in range(i+1):
        print(count, " ", end=" ")
        # Three spaces here in end parameter
        count = count+1

    print("")
    space = space-1
    # Change in decrement