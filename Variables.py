#Variables are box/container for storing value

a = 10
print(a)

a ="John"
print(a)

#Case sensitivity
name = "My name is Sayali"
Name = "My name is Sayali"
NAME = "My name is Sayali"
print(name,Name,NAME)

#We cannot have constant variables in python
pi = 3.142
print(pi)

pi = 2.172
print("Value of pi is :",pi)
print("Address of pi is:",id(pi))

#More on variables
a = 10
b = a
print("Value of a is :",a)
print("Value of b is :",b)
#To find base address of variables in python we have to use id()
print("Address of a is:",id(a))
print("Address of b is:",id(b))

c = 11
print("Value of c is :",c)
print("Address of c is:",id(c))

#Variable Assignments
#1.Multiple Variables,Single assignment
a=b=c=5
print("Value of a is :",a)
print("Value of b is :",b)
print("Value of c is :",c)
print("Value of a b and c is:",a,b,c)

#2.Multiple variables, Multiple Assignments
x =10
y=20
z=30
print("Value of x,y and z is :",x,y,z)

#OR we can write above syntax in different type also
x,y,z=40,50,60
print("Value of x,y and z is :",x,y,z)

#Values and types
a = 200
print(a)
#type() return datatype of varible
print(type(a))

demo="Sayali"
print(demo)
print(type(demo))




