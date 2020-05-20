ls = [8, 4, 12, 2, 12, 4, 9, 1, 3, 5, 13, 3]

ls1 = []
ls2 = []

ls.sort(reverse = -1)

print(ls)
total = sum(ls)
half = total/2
print("Half = ", half)
if total % 2 == 0:
    for i in ls:
        if sum(ls1) < sum(ls2):
            ls1.append(i)

        else:
            ls2.append(i)
    if sum(ls1) != sum(ls2):
        print("The entered elements aren't right!!")

    else:
        print("List 1 is:", ls1)
        print("The sum of list 1 is:", sum(ls1))
        print("List 2 is:", ls2)
        print("The sum of list 2 is:", sum(ls2))
