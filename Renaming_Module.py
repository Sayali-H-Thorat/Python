# Naming module - We can name the module file whatever we want, but it must have extension .py
# Renaming: We can rename a module by creating an alias(nick name) name while importing the module using 'as' keyword

import calc as calculation   # Here we rename calc as calculation so in during accessing methods from calc we have to write new name
print(calculation.add(10,11))

x = calculation.Person['city']
print("City of person is:",x)

# import from module
# We can choose to import only parts from module by using from keyword

from calc import Person
# Here we write from calc so there is no need to write calc before person print(calc.Person['name']) No need to write this syntax
print("Name of person from calc is:",Person['name'])

from calc import *
# * will include all the methods from calc
print("Element at 3rd pos is:",lst[3])
greet('Sneha!!!')

#numpy: builtin module It deals with arrays
# We have to install numpy using:- pip install numpy
# import numpy
# print(dir(numpy))

# To install pandas:- pip install pandas



