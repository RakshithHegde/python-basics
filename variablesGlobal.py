#variables that are created outside of a function are Global variables
x= "awesome"

def myfunc() :
    print("python is " + x)

myfunc()    
#if you create a variable with the same name as global variable inside a function this vairable will be local and can only be used inside the function,the global variable will remain as it is
def func():
    x= "fantastic"
    print("python is " + x)
func()

print("python is " + x)

#to create a global variable inside a function  use global keyword
def task():
    global y
    y = "fabulous"
task()
print("python is " + y)    

#use global keyword to change the global variable inside a function
z = "peace"

def preach():
    global z
    z = "war"
preach()
print("value of z is :" +z)    