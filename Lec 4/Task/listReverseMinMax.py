intL = []
charL = []

inp = input("Enter the value in char and int with space in between: ")

spl = inp.split(' ')

for i in spl:
    if i.isdigit():
        a = int(i)
        intL.append(a)

    else:
        charL.append(i)

if len(intL) != 0:
    print("The min value in int is: ", min(intL))
    print("The max value in int is: ", max(intL))

if len(charL) != 0:
    charL.reverse()
    print("The reversed string is: ", charL)
