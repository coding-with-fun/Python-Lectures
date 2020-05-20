# String all methods.
a = "hello"

# Returns the length of the string
print(len(a))
# Output : 5

# Capitalizes first letter of string
print(a.capitalize())
# Output : Hello

# Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
# str.count(sub, start= 0,end=len(string))

str = "this is string example"
sub = "i"
print("count:", str.count(sub, 4, 21))
# Output : count: 2

# Determines if string str occurs in string, or in a substring of string if starting index beg and ending index end
# are given. str.find(str, beg=0, end=len(string))
str1 = "this is string example"
str2 = "exam"
print(str1.find(str2))
# Output : 15

# The method join() returns a string in which the string elements of sequence have been joined by str separator.
s = "-"
seq = ("a", "b", "c")  # This is sequence of strings.
print(s.join(seq))
# Output : a-b-c

# he method split() returns a list of all the words in the string, using str as the separator (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
str = "this is string example"
print(str.split(' '))

# Output : ['this', 'is', 'string','example']

# The method isupper() checks whether all the case-based characters (letters) of the string are uppercase.
str = "THIS IS STRING EXAMPLE"
print(str.isupper())
# Output : True

str = "THIS is string example"
print(str.isupper())
# False

# Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
str = "hello"
print(str.islower())
# Output : True

# The method lower() returns a copy of the string in which all case-based characters have been lowercased.
str = "THIS IS STRING EXAMPLE"
print(str.lower())
# Output : this is string example

str = "hello"
print(str.upper())
# Output:HELLO

# # The method replace() returns a copy of the string in which the occurrences of old have been replaced with new,
# optionally restricting the number of replacements to max.
str = "this is string example"
print(str.replace("is", "was"))
# Output : thwas was string example

b = "-55"
# Returns true if string contains only digits and false otherwise.
print(b.isdigit())
# Output : True
