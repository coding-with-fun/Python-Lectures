def ins(nLine):
    
    for i in range(nLine):
        string1 = input("Enter the string: ")

        if string1 == "":
            break
        
        file.write(string1)
        file.write("\n ")


def pri():
    file.seek(0)
    print()
    strFile = file.read()
    print("The content of file is:\n",strFile )

    lsFile = strFile.split("\n")
    lnFile = len(lsFile) - 1

    wordCnt = len(strFile.split(" "))

    pos = file.tell() - (2 * lnFile)
    
    print("Total number of printed lines are:", lnFile)
    print("Total number of characters are:", pos)
    print("Total number of words are:", wordCnt - 1)


# Take input
nLine = int(input("Enter total number of lines: "))

# File open
file = open("fileCountElements.txt", "w+")

# Pass func to insert elements
ins(nLine)

# Pass func to print elements
pri()

# Close file
file.close()
