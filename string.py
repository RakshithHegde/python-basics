#strings in python are surrounded by either single quotes or double
print("Hi")
print('Hi')

a = "Hello"
print(a)

#Multiline strins can be assigned by using three double/single quotes
x = """Hi today I am learning
python basics soon i will 
complete the basics and go 
to advance topics"""
print(x)
#stings are arrays of bytes representing unicode characters
e= "Have ,a,nice,day! "
print(e[2])

#since strings are basically arrays we actually can loop through the characters with for loop

for x in "babayaga":
    print(x)

#to calculate the length of a string use len function
r= "Good game" 
print(len(r))

#searching a keyword in string can be done by using in keyword
text = "Rolls royce is my dream car"
print("royce" in text)

#this can also be done by using if loop
text = "Rolls royce is my dream car"
if "royce" in text:
    print("yes ,it is present")
#to check if a word is not present
text= "Audi is a cheap company"
print("costly" not in text)    
