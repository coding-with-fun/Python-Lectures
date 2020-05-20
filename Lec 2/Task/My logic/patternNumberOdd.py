"""
Enter number of rows: 3
         1
      2  3  4
   5  6  7  8  9

This program gives proper output only till 3 rows.
"""

rows = int(input("Enter number of rows: "))
space = rows
cnt = 1

for i in range(1, rows+1):
    for j in range(space):
        print("  ", end=" ")

    for k in range(i*2-1):
        print(cnt, " ", end="")
        cnt = cnt + 1

    space = space - 1
    print()