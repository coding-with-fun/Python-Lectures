def lsFun(*listFun):
    if len(listFun) == 1:
        for i in listFun:
            print(i)

    elif len(listFun) == 2:
        ls4 = []
        for i in listFun[0]:
            ls4.append(i)
        for i in listFun[1]:
            ls4.append(i)
        ls4.sort()
        print("\nThe sorted list is:", ls4)

    elif len(listFun) == 3:
        ls4 = []
        for i in listFun[0]:
            ls4.append(i)
        for i in listFun[1]:
            ls4.append(i)
        for i in listFun[2]:
            ls4.append(i)
        ls4.sort()
        print("\nThe sorted list is:", ls4)
        print("Maximum value is:", max(ls4))
        print("Minimum value is:", min(ls4))


n = int(input("\nEnter number of lists (max. 3): "))

ls1 = input("\nEnter the integer elements of list 1 with spaces in between: ")
ls1 = ls1.split(" ")

list1 = []
for i in ls1:
    list1.append(int(i))

if n == 1:
    lsFun(list1)

if n < 4:
    ls2 = input("Enter the integer elements of list 2 with spaces in between: ")
    ls2 = ls2.split(" ")

    list2 = []
    for i in ls2:
        list2.append(int(i))

    if n == 2:
        lsFun(list1, list2)

if n == 3:
    ls3 = input("Enter the integer elements of list 3 with spaces in between: ")
    ls3 = ls3.split(" ")

    list3 = []
    for i in ls3:
        list3.append(int(i))

    lsFun(list1, list2, list3)
