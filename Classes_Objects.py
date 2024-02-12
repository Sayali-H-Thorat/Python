# Python supports object-oriented programming
# Everything in python is made up of objects.
# Objects have three things:
# 1. Identity/Name
# 2. Properties/Attribute/Variables/Fields
# 3. Functionality/Behaviour

# There are four principles of OOP's
# 1.Encapsulation
# 2.Inheritance
# 3.Polymorphism
# 4.Abstraction

# objects: objects are instance of a class.
# class: class is a design/sketch/blueprint to create objects

# Create a python class named product which will have three variables
# name,description,price

class Product:
    def __init__(self):     # init is predefined constructor method  self points to current object being created
        self.name='Iphone'    #Variables and there values
        self.description = 'Its Awsome Iphone 14Pro max'
        self.price=120000
# Objects are always outside of class
p1 =Product()      # create an object
# To access the fields
print(p1.name)
print(p1.description)
print(p1.price)
print()
p2=Product()
print(p2.name)
print(p2.description)
print(p2.price)
