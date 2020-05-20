s = {'A', "A", 99, 96.5}

for i in s:
    if type(i) == int:
        print(i)

    elif type(i) == float:
        print("     ", i)

    elif type(i) == str:
        print("         ", i)