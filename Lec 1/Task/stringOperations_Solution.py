str = "This is string example"

print("Reversed string is: "+str[::-1])

ss = str.split(" ")
print("Reversed words are: "+ss[0][::-1]+" "+ss[1][::-1]+" "+ss[2][::-1]+" "+ss[3][::-1])

print("Reversed letters are: "+ss[0][0:2][::-1])

print("*".join(ss))

print("Replaced by was is: "+ss[0]+" "+ss[1].replace("is","was")+" "+ss[2]+" "+ss[3])

n = float(input("Enter"))
print(n)