import os
from os import path


def inputData(noStud):
    dictStudRaw = {}

    for i in range(noStud):
        rollNo = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        dictStudRaw[int(rollNo)] = {"Roll no": rollNo, "Name": name, "Marks": marks}

    dictStud = {}

    for i in sorted(dictStudRaw):
        dictStud[int(i)] = {"Roll no: ": dictStudRaw[i]["Roll no"], "Name: ": dictStudRaw[i]["Name"], "Marks: ": dictStudRaw[i]["Marks"], "Grade: ": ""}

    return dictStud


def countGrade(dictStud):
    for i in dictStud:
        if int(dictStud[i]["Marks: "]) > 79:
            dictStud[i]["Grade: "] = "A"

        elif int(dictStud[i]["Marks: "]) < 80 and int(dictStud[i]["Marks: "]) > 59:
            dictStud[i]["Grade: "] = "B"

        elif int(dictStud[i]["Marks: "]) < 60 and int(dictStud[i]["Marks: "]) > 39:
            dictStud[i]["Grade: "] = "C"
        
        else:
            dictStud[i]["Grade: "] = "Fail"

    return(dictStud)


def writeFile(file, dictStud):
    file.seek(file.tell())
    for i in dictStud:
        file.write("\nRoll number: ")
        file.write(dictStud[i]["Roll no: "])

        file.write("\nName: ")
        file.write(dictStud[i]["Name: "])

        file.write("\nMarks: ")
        file.write(dictStud[i]["Marks: "])

        file.write("\nGrade: ")
        file.write(dictStud[i]["Grade: "])
        file.write("\n")
    

def readFile(file):
    file.seek(0)
    
    print(file.read())


def initial():
    file = open("gradeSortedFile.txt", "a+")

    while True:
        count = 0
        print("Press 'r' to read data from file or 'w' to write data in the file or press 'c' to clear data in file or press any other key to exit.")
        choice = input("Enter your choice: ")

        if choice == 'r' or choice == 'R':
            if file.tell() > 0:
                readFile(file)

            else:
                print("The file is empty!!")

        elif choice == 'c' or choice == 'R':
            file.seek(0)
            file.truncate(file.tell())


        elif choice == 'w' or choice == 'W':
            noStud = int(input("Enter number of students: "))

            dictStud = inputData(noStud)

            dictStud = countGrade(dictStud)

            if file.tell() > 0:
                print("There is some data in the file. Do you want to append the data or overwrite it?")
                choice1 = input("Press 'o' to overwrite data and 'a' to append data: ")

                if choice1 == 'o' or choice1 == 'O':
                    file.seek(0)
                    file.truncate(file.tell())
                    writeFile(file, dictStud)

                elif choice1 == 'a' or choice1 == 'A':
                    file.seek(file.tell())
                    writeFile(file, dictStud)

                else:
                    print("Invalid input!!")

            else:
                print("There isn't any data in the file. Do you want to create a new file?")
                choice1 = input("Press 'y' to create a new file or press any other key to discard: ")

                if choice1 == 'y' or choice1 == 'Y':
                    writeFile(file, dictStud)

                else:
                    print("File not created!!")


        else:
            print("\nDo you want to delete the file before exiting?")
            delFile = input("Press 'y' to delete file or any other key to exit: ")

            if delFile == 'y' or delFile == 'Y' or file.tell() == 0:
                if path.exists("gradeFile.txt"):
                    os.remove("gradeFile.txt")

            break

    file.close()


# ---------------------------------------------------------------------------------------------------------------------------------------------

# Main logic
initial()