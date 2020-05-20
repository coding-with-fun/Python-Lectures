# Defination for input
def inpFile(lines):
    for i in range(lines):
        string = input("Enter the string: ")

        if string == "":
            break

        file.write(string)
        file.write("\n")

# Defination for printing
def printFile():
    print()
    file.seek(0)
    strFile = file.read()

    lsFile = strFile.split("\n")
    lsFile.remove(lsFile[-1])
    lsFile.reverse()

    print("The reversed file lines are:")
    for i in lsFile:
        print(i)


# Main logic
lines = int(input("Enter total number of lines: "))

# Open file
file = open("reverseFile.txt", "w+")

# Call input function
inpFile(lines)

# Call print function
printFile()

file.close()
