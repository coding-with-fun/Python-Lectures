s = "This is string example"

'''
Reverse string
'''
reverse = s[::-1]
print("Reverse string is: "+reverse)
print()

'''
Reverse words
'''
words = s.split(" ")
revWords = [revWord[::-1] for revWord in words]
revStr = " ".join(revWords)
print("Reversed words are: "+revStr)
print()

'''
Split and join
'''
splitString = s.split(" ")
print("Splitted string is: ")
print(splitString)

joinString = "*".join(splitString)
print("Joined string is: "+joinString)
print()
print("Interchanged chars are: "+splitString[0][1]+splitString[0][0]+splitString[0][3]+splitString[0][2])
print()

'''
Replace is
'''
seperateString = s.split(" ")
for x in range(len(seperateString)):
    if seperateString[x]=="is":
        seperateString[x]="was"
joinString = " ".join(seperateString)
print("Edited string is: "+joinString)
print()
