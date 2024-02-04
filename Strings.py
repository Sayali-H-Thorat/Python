'''
Sequences
Strings
Lists
tuples
sets
dictionary
'''
#Strings are sequence of characters enclosed within " " or ' ' quotations
#Display string
print("Hii")
print('Hii')

#Assign string to a variable
s = "Python is easy" #Single line string
print(s)

str1 = '''Python is easy to learn
than other languages'''   #Multiline string  ou can use """ """ also
print(str1)

#Indexing is a concept of reaching out to a particular character. Indexing always start from 0 for LHS and for RHS it start from -1
s= "Python is easy"
print(s[0]) # Output is:P
print(s[3]) # Output is:h
print(s[7]) # Output is:i
print(s[13]) # Output is:y
print(s[-1]) #Output is:y   AND this is known as negative indexing
print(s[-3]) #Output is:a

#Repitition * symbol is used to repeat the string
print(s * 3)

#Length of string  len() is used to print the length of string
print(len(s))

#Python does not support character datatype. Character is string of length 1
a = 'H'
print(a)
print(type(a))
print(len(a))

#Slicing
str2= "Python is easy"
#Values after colon gets excluded
print(s[0:6])    #it exclude 6th position
print(s[0:9])    #it prints 9 letters from start
print(s[0:])     #it will print the whole string
print(s[4:])     #It will print all the string start from 4th index
print(s[:12])    #It prints string start from o to 12th position
print(s[-3:-1])  #-3,-2,-1 It will include -3 and exclude -1
print(s[-5:-3])  #It will print space and e
print(s[-1:-3])  #start index never be higher if it is higher than it will print blank space
print(s[5:1])   #start index never be higher if it is higher than it will print blank space

#pass step value to slices
       #0123456789
str3 = "I Love Python"
print(str3[0:9])
print(str3[1:9:2])   #Here 2 is step value(it starts with 1 and prints the characters which are at 2nd pos from 1 and so on)
print(str3[0:9:2])
print(str3[::-1])  #It will reverse the whole string [: : -1]
print(str3[::2])   #It will do slicing from LHS
print(str3[::-2])   #It will do slicing as well as reverse the same

str4 = 'Hello World'
print(len(str4))
# print(str4[11]) #It will give the error as string index out of range
print(str4[6:30])  #It will start with index 6 and print the words from it and so on

#String methods
#strip() Remove white spaces from start and end of the string

s = '  You are awesome as always are'
print(s)
print(len(s))
print(s.strip())
print(s.lstrip()) #lstrip() removes white spaces from left hand side
print(s.rstrip()) #rstrip() removes white spaces from right hand side

#find() locate the substring in given string
#substring means more than one characters in sequence
print(s.find('are'))    #It will display at which position given substring is located It will display the first substring location
print(s.find('some'))

#count() It will count the number of occurences of specific character
print(s.count('a'))  #Display how many a's are there in whole string

#concanate() joins two strings together We can add spaces in three ways
#1-> 'Hello '
#2-> ' World'
#3-> x+' '+y
x = 'Hello'
y = 'World'
print(x+y)  #It will concate the string without adding space
print(x+' '+y)  #It will concate string with space in between
z = x+' '+y
print(z)

# a = "Hello"+100  #We can only concatenate str (not "int") to str
# print(a)

a = "Hello"+'100' #Here 100 is taken as string because it is in quotation
print(a)

a = "Hello"+str(100)  #We can convert the int to string using str() function
print(a)

#format()  It is also used to cocatenate the string
age = 23
marks = 95.5
txt = "My name is Sayali and I'm {} and my marks are {}"   #Here {} are placeholder
print(txt.format(age,marks))

#Strings are immutable 'str' object does not support item assignment
# Once we declared the string we cannot make any change to that string it means string is immutable
str5 = "Python"
print(str5)
# We cannot change the string
# s[1] = 'a'
# print(str5)

# We cannot delete or add anything to string bt we can delete whole string
# del_str5[1]


del str5 #It will delete str5 string
print(str5)  #It will give name error as we delete the string

