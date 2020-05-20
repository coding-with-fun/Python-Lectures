stud = {}
roll_no = {}
name = {}
marks = {}

cnt = 1
while True:
    if stud == {}:
        print("There are no elements in the dictionary.")

    else:
        print()
        print("Data is:")
        print(stud)

    print("Do you want to insert element??")
    contInput = input("Press i to insert and n to not insert: ")

    if contInput == "n":
        if stud == {}:
            print("There isn't any data")

        else:
            print()
            print("Data is:")
            print(stud)
        break

    elif contInput == "i":

        no = int(input("Enter number of students: "))

        for a in range(no):
            count = str(cnt)
            print("For student ", a + 1, ": ")
            roll_no[count] = input("    Enter roll number: ")
            name[count] = input("    Enter name: ")
            marks[count] = int(input("    Enter marks: "))

            stud[roll_no[count]] = {"Roll No": roll_no[count], "Marks": marks[count], "Name": name[count]}
            cnt = cnt + 1

    else:
        print("Invalid input!!")
