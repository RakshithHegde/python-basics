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

#concatenation of 2 strings
a = "Hi"
b= "Have a good day"
c = a + "!," + b
print(c)

#format
age = 20
text = "My name is rk, and I am {}"
print(text.format(age))
#we can pass multiple values through format method as it can take unlimited number of arguments
PetrolStation="Indian Oil"
Petrolrate = 104.98
PetrolAmount = 6000
Myday = "Today I went to fill petrol at {} the petrol rate was {}//l and I spent {}rs "
print(Myday.format(PetrolStation,Petrolrate,PetrolAmount))

NextDay="I paid {2}rs today at {0} as the rate of petrol was {1}//l"
print(NextDay.format(PetrolStation,Petrolrate,PetrolAmount))