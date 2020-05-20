"""
stu = {'12':{'Roll no':'12', 'Name':'Harsh', 'Marks':'23'}}
"""

roll_no = {}
marks = {}
name = {}
stud = {}

cnt = 1
i = str(cnt)
roll_no[i] = input("Enter roll no: ")
marks[i] = int(input("Enter marks: "))
name[i] = input("Enter name: ")

stud[roll_no[i]] = {roll_no[i]: {"Roll No": roll_no[i], "Marks": marks[i], "Name": name[i]}}

print(stud[roll_no[i]])
