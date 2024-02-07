# Functions:group of statements OR block of statements that perform particular task
# input()
# print()

# syntax of functions
# def function_name(arguments/parameters):
#      function_body
# function_name(argument values/parameters value)

# Function may or may not have arguments
# function should be explicitly called

def greet():
    print("Let's learn Python")
    print("Python is easy")
greet()   # calling/invoking function

# function to add two numbers
def Add(x,y):
    z = x+y
    print("Addition is:",z)
#   print(x+y)        We can add two numbers without using third variable
Add(10,11)
Add(21,51)

# average of two numbers
def Avg(a,b):
    c = (a+b)/2
    print("Average of two numbers is:",c)
Avg(10,20)

# Functions can execute the task or functions can return something
# Program to do the addition of two numbers and return the answer
def add(x,y):
    z = x+y
    return z
print("Adition of two no is:",add(10,11))
# result =add(10,11)
# print("Addition is:",result)

# Function to return average
def Average(a,b):
    return (a+b)/2
print("Average of two numbers is:",Average(10,11))

# Function can return multiple values
def Calc(a,b):
    x =a+b
    y =a-b
    z =a*b
    u =a/b
    return(x,y,z,u)

print("Result is:",Calc(20,10))  #it will print in tuple format means on single line
# iteration over function
for iCnt in Calc(20,10):
    print(iCnt)

print("By using third variable along with for loop")
result = Calc(20,10)    #it will print in tuple format means on single line
print(result)
for iCnt in result:
    print(iCnt)




