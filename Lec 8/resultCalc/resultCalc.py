'''
1. Input student data. Rno, Name, Marks for 3 subs

2. Read data

3. Calc avg

4. Grade find store desc
    80 - 100 A
    60 - 80 B
    40 - 60 C
'''



Info = open("studInfo.txt", "w+")
Marks = open("studMarks.txt", "w+")

def writeData():
    Info.write("1 : Harsh \n")
    Info.write("2 : Patel \n")
    Info.write("3 : Karan \n")
    Info.write("4 : Het \n")

    Marks.write("1 : 32 75 36 \n")
    Marks.write("2 : 99 99 99 \n")
    Marks.write("3 : 99 99 99 \n")
    Marks.write("4 : 42 65 96 \n")

    # cnt = int(input("Enter the total number of students: "))

    # for i in range(cnt):
    #     print()
    #     marks = 0
    #     print("For student", i + 1, ":")
    #     rNo = input("Please enter the roll number: ")
    #     name = input("Please enter the name: ")

    #     print()

    #     print("For subject", marks + 1, " ")
    #     m1 = input("please enter marks: ")

    #     print("For subject", marks + 2, " ")
    #     m2 = input("please enter marks: ")

    #     print("For subject", marks + 3, " ")
    #     m3 = input("please enter marks: ")

    #     Info.writelines(rNo + " - " + name + " \n")
    #     Marks.writelines(rNo + " - " + m1 + " " + m2 + " " + m3 + " \n")

    readFile()


def readFile():
    Info.truncate(Info.tell() - 1)
    Marks.truncate(Marks.tell() - 1)

    Info.seek(0)
    Marks.seek(0)

    sInfo = (Info.read())
    sMarks = (Marks.read())

    calcGrade(sInfo, sMarks)


def calcGrade(sInfo, sMarks):
    lsInfo = sInfo.split("\n")
    lsMarks = sMarks.split("\n")

    mainInfo = []
    mainMarks = []

    for (i, j) in zip(lsInfo, lsMarks):
        sInfo = str(i)
        sMarks = str(j)

        spInfo = sInfo.split(" ")
        spMarks = sMarks.split(" ")

        spInfo.pop()
        spMarks.pop()

        mainInfo.append(spInfo)
        mainMarks.append(spMarks)

    avgDict = {}
    for (i, j) in zip(mainInfo, mainMarks):
        avg = (float((int(j[2]) + int(j[3]) + int(j[4])) / 3))
        avgDict[i[0]] = {"Roll no": i[0], "Name": i[2], "m1": int(j[2]), "m2": int(j[3]), "m3": int(j[4]), "Avg": int(avg)}

    printGrade(avgDict)

aGrade = open("aGrade.txt", "w+")
bGrade = open("bGrade.txt", "w+")
cGrade = open("cGrade.txt", "w+")

def printGrade(avgDict):        
    avgDict = sorted(avgDict.items(), key = lambda x: x[1]['Avg'], reverse=True)
    for i in avgDict:
        if float(i[1]['Avg']) <= 100 and float(i[1]['Avg']) >= 80:
            i[1]['Grade'] = "A"
            aGrade.writelines("\nRoll no: " + i[1]["Roll no"] + "\n \n" + "Name: " + i[1]["Name"] + "\n \n")
            aGrade.writelines("Avg marks: " + str(i[1]["Avg"]) + "\n \n" + "Grade: " + i[1]["Grade"] + "\n \n")
            aGrade.writelines("Marks of:\n     Subject 1: " + str(i[1]["m1"]) + "\n     Subject 2: "  + str(i[1]["m2"]) + "\n     Subject 3: "  + str(i[1]["m3"]))
            aGrade.writelines("\n \n" + "- - - - - - - - - - - - - - -" + "\n")

        elif float(i[1]['Avg']) < 80 and float(i[1]['Avg']) >= 50:
            i[1]["Grade"] = "B"
            bGrade.writelines("\nRoll no: " + i[1]["Roll no"] + "\n \n" + "Name: " + i[1]["Name"] + "\n \n")
            bGrade.writelines("Avg marks: " + str(i[1]["Avg"]) + "\n \n" + "Grade: " + i[1]["Grade"] + "\n \n")
            bGrade.writelines("Marks of:\n     Subject 1: " + str(i[1]["m1"]) + "\n     Subject 2: "  + str(i[1]["m2"]) + "\n     Subject 3: "  + str(i[1]["m3"]))
            bGrade.writelines("\n \n" + "- - - - - - - - - - - - - - -" + "\n")

        else:
            i[1]["Grade"] = "C"
            cGrade.writelines("\nRoll no: " + i[1]["Roll no"] + "\n \n" + "Name: " + i[1]["Name"] + "\n \n")
            cGrade.writelines("Avg marks: " + str(i[1]["Avg"]) + "\n \n" + "Grade: " + i[1]["Grade"] + "\n \n")
            cGrade.writelines("Marks of:\n     Subject 1: " + str(i[1]["m1"]) + "\n     Subject 2: "  + str(i[1]["m2"]) + "\n     Subject 3: "  + str(i[1]["m3"]))
            cGrade.writelines("\n \n" + "- - - - - - - - - - - - - - -" + "\n")
    
    aGrade.seek(0)
    bGrade.seek(0)
    cGrade.seek(0)

    print("The data of A grade is:")
    print("- - - - - - - - - - - - - - - ")
    print(aGrade.read())

    print("\nThe data of B grade is:")
    print("- - - - - - - - - - - - - - - ")
    print(bGrade.read())

    print("\nThe data of C grade is:")
    print("- - - - - - - - - - - - - - - ")
    print(cGrade.read())


writeData()

Info.close()
Marks.close()
aGrade.close()
bGrade.close()
cGrade.close()
