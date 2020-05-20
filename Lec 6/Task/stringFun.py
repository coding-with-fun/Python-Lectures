def wordRev(st):
    n = st.split(" ")

    for i in n:
        print(i[::-1], end=" ")


def charInter(st):
    n = st.split(" ")

    for i in n:
        l = len(i)

        for j in range(0, l, 2):
            print(i[j:j+2][::-1], end="")
        print(end=" ")


inp = int(input("Press 1 to do word wise reverse and press 2 for characters interchange."))
stri = input("Enter the string: ")
if inp > 0:
    if inp == 1:

        wordRev(stri)

    elif inp == 2:
        charInter(stri)

    else:
        print("Invalid input!!")
