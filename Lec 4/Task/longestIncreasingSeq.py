ls = []

nIn = int(input("Enter total number of inputs: "))

for i in range(nIn):
    n = int(input("Enter number: "))
    ls.append(n)

ls1 = [[]]
ls1[-1].append(ls[0])

for i in range(1, nIn):
    if ls1[-1][-1] < ls[i]:
        ls1[-1].append(ls[i])

    else:
        ls1.append([])
        ls1[-1].append(ls[i])

print(ls1)
