"""
list = ["a", 1, ["a", 1, "xyz"]]

print(type(list))

for i in list:
    print(i)

for i in range(len(list)):
    print("index", i)
    print("list value", list[i])
    if i == 2:
        print("list value", list[i][i])

for i in range(20, 30):
    print("index", i)

# single line for loop
a = [i for i in range(5)]
print(a)
"""
for i in range(9):
    print(i)