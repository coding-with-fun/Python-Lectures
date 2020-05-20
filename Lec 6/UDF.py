#A function is a block of organized, reusable code that is used to perform a single, related action.

#Functions provide better modularity for your application and a high degree of code reusing.

#As you already know, Python gives you many built-in functions like print(),len() etc.
#but you can also create your own functions.
#These functions are called user-defined functions.

#Function blocks begin with the keyword def followed by the function name and parentheses().

#Any input parameters or arguments can be placed within these parentheses.
#You can also define parameters inside these parentheses.

#The code block within every function starts with a colon (:) and is indented.

#The statement return [expression] exits a function.

#A return statement with no arguments is the same as return None.


#Let's see some examples

#############################################################################


#function without arguement with return "none"

def fn1():

    print "This is User Define function !"

    return

#function fn1() call
fn1()

#Output: This is User Define function !


#function with single argument without return

def fn2(str):

    print str

#function fn2() call
fn2("HELLO WORLD !")

#Output: HELLO WORLD !

#function with multiple argument without return

def fn3(a,b):

    print a + b
    print a - b
    print a * b
    print a / b
    print a % b

#function fn3() call
fn3(10,5)
# 15
# 5
# 50
# 2.0
# 0



#function with no argument with return

def fn4(a,b):

    c=a+b

    return  c

#function fn4() call
d=fn4(20,20)

print d

#Output:40