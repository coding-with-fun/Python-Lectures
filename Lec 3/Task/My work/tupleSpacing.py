tup = (1, 1, "Asit", 'N', 45.5, "Harshal", (1, 1, "Asit", "Harshal", 'N', 45.5, 45.5), "Harsh")

for i in tup:
    if type(i) == int:
        print("Integer value: ", i)

    elif type(i) == float:
        print("         Float value: ", i)

    elif type(i) == str:
        print("     String value: ", i)

    else:
        print("--------------------------------------------------------------------")
        print("Starting of nested tuple.")
        for j in i:
            if type(j) == int:
                print("Integer value: ", j)

            elif type(j) == float:
                print("         Float value: ", j)

            elif type(j) == str:
                print("     String value: ", j)

        print("End of nested tuple.")
        print("--------------------------------------------------------------------")