ls = [1, 2, 3, 'a', 'b', 'c', 4, 5, 'd', 'e', [6, 7, 8, 9, 'f', 'g', 'h', 'i'], [10, 'j', 11, 'k'], 12, 'l']

for i in ls:
    if type(i) == str:
        print(" ", i, " ")

    elif type(i) == int:
        print(i)

    elif type(i) == list:
        for j in i:
            if type(j) == str:
                print(" ", j, " ")

            elif type(j) == int:
                print(j)
