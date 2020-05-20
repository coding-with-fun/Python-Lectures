import csv, os
from os import path


# Function to input the data from users.
def inputData(cnt):
    result = []

    for i in range(cnt):
        print("For student ", i + 1, ":")
        result.append([])

        result[-1].append(int(input("Enter roll number: ")))
        result[-1].append(input("Enter name of student: "))
        result[-1].append(int(input("Enter marks: ")))

    return result


# Function to calculate the grades.
def grade(result):
    for i in result:
        if i[2] > 79:
            i.append("A")

        elif i[2] > 59 and i[2] < 80:
            i.append("B")

        elif i[2] > 39 and i[2] < 60:
            i.append("C")

        else:
            i.append("D")

    result.sort()

    return result


# Function to write data in CSV file
def writeCSV(rows, file):
    fields = ["Roll no", "Name", "Marks", "Grade"]
    
    write = csv.writer(file)

    if file.tell() == 0:
        write.writerow(fields)

    write.writerows(rows)


# Function to read data from CSV file
def readCSV(file):
    fields = rows = []

    string = csv.reader(file)

    fields = next(string)

    for i in fields:
        print("%10s"%i, end=" ")
    print()


    for i in string:
        rows.append(i)

    for i in sorted(rows):
        for j in i:
            print("%10s"%j, end=" ")
        print()
    print()


#  The initial logic.
def initial():
    file = open("resultSortedCSV.csv", "a+")
    while True:
        # Gives choice for reading or writing of data.
        print("Press 'r' to read or press 'w' to write  or press 'c' to clear data in the CSV file or press any other key to exit.")
        choiceMain = input("\nEnter your choice: ")

        if choiceMain == 'r' or choiceMain == 'R':
            # Check existance of file.
            if file.tell() > 0:
                # Enters here if file exists

                file.seek(0)
                readCSV(file)
            
            else:
                print("\nThe data does't exist in the file!!\n")
        
        elif choiceMain == 'c' or choiceMain == 'C':
            file.seek(0)
            file.truncate(file.tell())

        elif choiceMain == 'w' or choiceMain == 'W':
            # Enters if user wants to write data.
            print()
            cntInp = int(input("Enter total number of students: "))

            # Call input function
            result = inputData(cntInp)

            # Call grading function
            result = grade(result)


            # Check existance of file.
            if file.tell() > 0:
                # Enters here if file exists            

                # Gives choice for appending or overwriting the data.
                print("\nThe past data already exists. You want to append data or overwrite the data?")
                choice1 = input("Press 'a' to append and 'o' to override: ")

                if choice1 == 'a' or choice1 == 'A':
                    writeCSV(result, file)

                elif choice1 == 'o' or choice1 == 'O':
                    file.seek(0)
                    file.truncate(file.tell())
                    writeCSV(result, file)
            
            else:
                # Enters here if file doesn't exist

                # Gives choice for creating new file.
                print("\nThere isn't any past data. Do you want to create a new file?")
                choice = input("Press 'y' to create new file and 'n' to deny: ")

                if choice == 'y' or choice == 'Y':
                    writeCSV(result, file)

                elif choice == 'n' or choice == 'N':
                    print("File not created. Data can't be entered.")

                else:
                    print("Invalid input!!")

        else:
            # Gives option to delete the file before exiting
            print("\nDo you want to delete the file before exiting?")
            delFile = input("Press 'y' to delete file or any other key to exit: ")

            if delFile == 'y' or delFile == 'Y':
                os.remove("resultSortedCSV.csv")

            break
    file.close()


# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# Main logic
initial()