import xlsxwriter

def inputDetails(nInp):
    studict = {}

    for i in range(nInp):
        rNo = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        studict[rNo] = {"Roll no": rNo, "Name": name, "Marks": marks}

    dictFile = {}
    for i in sorted(studict):
        dictFile[int(i)] = {"Roll no": studict[i]["Roll no"], "Name": studict[i]["Name"], "Marks": studict[i]["Marks"], "Grade": ""}

    return dictFile


def grade(sDict):
    for i in sDict:
        if int(sDict[i]["Marks"]) > 79:
            sDict[i]["Grade"] = "A"

        elif int(sDict[i]["Marks"]) < 80 and int(sDict[i]["Marks"]) > 59:
            sDict[i]["Grade"] = "B"

        elif int(sDict[i]["Marks"]) < 60 and int(sDict[i]["Marks"]) > 39:
            sDict[i]["Grade"] = "C"
        
        else:
            sDict[i]["Grade"] = "Fail"

    return(sDict)

def writeExcel(studict):
    workbook = xlsxwriter.Workbook("resultSortedExcel.xlsx")
    worksheet = workbook.add_worksheet("Result")

    row = col = 0

    worksheet.write(row, col, "Roll no")
    worksheet.write(row, col + 1, "Name")
    worksheet.write(row, col + 2, "Marks")
    worksheet.write(row, col + 3, "Grade")

    row = 1
    for i in studict:
        worksheet.write(row, col, studict[i]["Roll no"])
        worksheet.write(row, col + 1, studict[i]["Name"])
        worksheet.write(row, col + 2, studict[i]["Marks"])
        worksheet.write(row, col + 3, studict[i]["Grade"])

        row += 1

    workbook.close()


nInp = int(input("Enter total number of students: "))

studict = inputDetails(nInp)

studict = grade(studict)

writeExcel(studict)
