ls1 = [1, 2, 3, 4, 5]
ls2 = [1, 2, 3, 4]

ls1C = []
ls2C = []
for i in ls1:
    ls1C.append(str(i))
a = "".join(ls1C)

for i in ls2:
    ls2C.append(str(i))
b = "".join(ls2C)

Sum = int(a) + int(b)
Mul = int(a) * int(b)

print("Sum is: ", Sum)
print("Mul is: ", Mul)

sumL = [str(Sum)]
mulL = [str(Mul)]

sumF = []
mulF = []

for i in sumL[0]:
    sumF.append(int(i))
print(sumF)

for i in mulL[0]:
    mulF.append(int(i))
print(mulF)