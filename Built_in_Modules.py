# Built in Modules
# platform is also module and it is builtin and it has function system()

import platform
#  module_Name.function()
z =platform.system()    # It will give you the platform name on which you are currently working
print(z)

# Program to calculate area of circle
# area = pi*r**2

import math
print("Value of Pi is:",math.pi)
# r=float(input("Enter the radius:"))
# area=math.pi*r**2
# print("Area of circle is:",area)

# print(math.factorial(5))

# import all names - * will import all the builtin functions from math module
from math import *
print("Value of Pi is:",pi)
print("Factorial of 3 is:",factorial(3))
print("Square root is:",sqrt(25))

# import specific functions from modules
# In below syntax each time we have to include the builtin function separately
from math import pi,factorial
print(pi)
print(factorial(5))

#dir() function will give all the function available in respective module
import math
print("Default functions in builtin math module:\n",dir(math))   # List of functions available in math module

# calc is user defined it will show all the functions available in calc
import calc
print("Default functions in user defined calc module:\n",dir(calc))

#random modules-builtin module deals with random numbers
import random
print("Default functions in builtin random module:\n",dir(random))
print(random.randint(0,10))    # It will give random integer from given range it may include both the range values
print(random.random())    # It will never go beyond 1 it will print the random numbers below the 1
print(random.random()*100)    # It will never give the random number from 1 to 100

