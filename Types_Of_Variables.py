# Types of variables
# There are two types of variables
# 1. Instance variables->Defined inside constructor method
# 2. Class/static variables->defined inside class bt outside constructor method

class Cars:
    color='Black'  # class/static variable
    def __init__(self):
        self.make='BMW'  # self.make and self.year are instance variables they write inside constructor
        self.year=2019
c1=Cars()
print("Manufacturer name:",c1.make)
print("Year of manufacturing:",c1.year)
print("Color of car is:",c1.color)
print(Cars.color)  # static variable accessed using class name
Cars.color='Red'
print("After modifying color is:",Cars.color)
print()

c2=Cars()
print("Manufacturer name:",c2.make)
print("Year of manufacturing:",c2.year)
print("Color of car is:",c2.color)
print("Color of car is:",Cars.color)
print()

# Global modification
Cars.color='Golden'
print("Color using c1:",c1.color)
print("Color using c2:",c2.color)
print("Color using Cars:",Cars.color)
print()

c2.color='white'
print("Color of color using 2nd object:",c2.color)
print("Color of car using class name:",Cars.color)
print("Color of class using 1st object:",c1.color)
# When you are modifying static variable using class it gets modified globally
# When you are modifying static variable using object it gets modified for only that object
print()

c1.color='silver'
print("Color using c2:",c2.color)
print("Color using Cars:",Cars.color)
print("Color using c1:",c1.color)
print()
