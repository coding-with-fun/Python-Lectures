# Function to input data in file
def inputStr():

    # Function call to read file
    readFile()

    if fileOne.seek(0, 2) != 0:
        print("Press ''o'' to overwrite data of file or press ''a'' to append data.")
        choice = input("Enter your choice: ")

        if choice == 'o' or choice == 'O':
            fileOne.seek(0)
            fileOne.truncate(fileOne.tell())
            print("\n")

            # Function call to write file
            writeFile()
        
        elif choice == 'a' or choice == 'A':
            fileOne.seek(0, 2)
            print("\n")

            # Function call to write file
            writeFile()
    
    else:
        fileOne.seek(0, 2)

        # Function call to write file
        writeFile()

    print("\n")


# Function to write file
def writeFile():
    print("Please leave the string empty to exit input.")
    while True:
        string = input("Enter the string: ")

        if string != "":
            fileOne.write(string)
            fileOne.write("\n")

        else:
            break


# Function to read file
def readFile():
    if fileOne.seek(0, 2) == 0:
        print("The file is empty!!")

    else:
        print("The content of the file is:")
        fileOne.seek(0)
        print(fileOne.read())

        # Function call to clear file
        clearFile()
    
    print("\n")


# Function to replace word
def replaceWord():
    if fileOne.seek(0, 2) != 0:
        print("Replace word here")
        print("Please be specific. It is case sensitive.")

        oldStr = input("Enter the word to be replaced: ")
        newStr = input("Enter the new word: ")

        # Read data of file
        fileOne.seek(0)
        oldString = fileOne.read()

        # Replace word
        newString = oldString.replace(oldStr, newStr)

        fileOne.seek(0)
        fileOne.truncate(0)

        # Write file with new word
        fileOne.writelines(newString)
        print("\n")

        # Function call to read file
        readFile()

    else:
        print("There is no data to be replaced!!")
        print("\n")


# Function to clear data of file
def clearFile():
    print("Press ''c'' to clear the content of the file.")
    choice = input("Enter your choice: ")

    if choice == 'c' or choice == 'C':
        fileOne.seek(0)
        fileOne.truncate(0)
        print("File cleared!!")


# Initial function call
def initial():
    while True:
        print("Press ''r'' to read the contents of the file or press ''w'' to enter data in file or press ''n'' to replace any word of file.")
        choice = input("Enter your chocie: ")
        
        # To read file
        if choice == 'r' or choice == 'R':
            print("\n")

            # Function call to read file
            readFile()

        # To write file
        elif choice == 'w' or choice == 'W':
            print("\n")

            # Function call to write file
            inputStr()

        # To replace word
        elif choice == 'n' or choice == 'N':
            print("\n")

            # Function call to replace word
            replaceWord()

        else:
            break


# Main logic
# Open file
# This is custom location
fileOne = open("/home/harsh/Harsh/makeFile/replaceWord.txt", "a+")

# Call initial function
initial()

# Close file
fileOne.close()
