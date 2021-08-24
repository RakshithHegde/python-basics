#strings can sliced and we can return a range of characters by using slice 
#specify the start index and end, seperated by a colon, to return part of a string
b="Hello,World!"
print(b[3:6])

c="Hello,World!"
print(c[:6])

#negative indexing 
b = "Hello,World!"
print(b[-3:-1])

#modifying Strings
#Uppercase
a= "abcdoncwijdbcw"
print(a.upper())
#lowercase
f="SCHABDACBJDAQF"
print(f.lower())
#strip
A="  Hello  ,    World!       "
print(a.strip())

#replace string
a="Good Evening!"
print(a.replace("Evening","Night"))

#split()
a="What are you ,planning for today?"
print(a.split(","))