"""
Enter number of students: 2
For student  1 :
    Enter roll number: 21
    Enter name: Harsh
    Enter marks: 89
For student  2 :
    Enter roll number: 24
    Enter name: Shle
    Enter marks: 98

Output:
{'21': {'Roll No': '21', 'Marks': 89, 'Name': 'Harsh'}, '24': {'Roll No': '24', 'Marks': 98, 'Name': 'Shle'}}
"""

no = int(input("Enter number of students: "))

roll_no = {}
name = {}
marks = {}
stud = {}

cnt = 1
for a in range(no):
    count = str(cnt)
    print("For student ", a+1, ": ")
    roll_no[count] = input("    Enter roll number: ")
    name[count] = input("    Enter name: ")
    marks[count] = int(input("    Enter marks: "))

    stud[roll_no[count]] = {"Roll No": roll_no[count], "Marks": marks[count], "Name": name[count]}
    cnt = cnt + 1

print(stud)