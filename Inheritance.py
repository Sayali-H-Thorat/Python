# Inheritance: It is process of defining new object using existing object
# Inheritance allows us to define a class that inherits all the methods and properties from another class
# It also signifies Parent-Child relationship
# Parent class: It is class being inherited from, also called base class or super class
# Child class: It is a class that inherits from another class also called derived class

# Let's see inheritance in action by implementing BMW usecase
# create class BMW with fields make,model,year. BMW is the parent class
# Three_Series and Five_series are child classes of BMW with cruiseControlEnabled and parkingAssistantEnabled as their own fields

class BMW: #parent class
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year


class Three_Series(BMW):    # inheritance/child class
    def __init__(self,cruiseControlEnabled,make,year,model):   # constructor of Three_Series class
        self.cruiseControlEnabled = cruiseControlEnabled
        BMW.__init__(self, make, model, year)  # Inheriting parent class constructor method


ts=Three_Series(True,"BMW",2018,'328i')
print("Three_Series model information")
# Attribute inheritance
print("cruiseControlEnabled:", ts.cruiseControlEnabled)
print("Model Manufacturer of Three_Series is:", ts.make)
print("Manufacturing year of Three_Series is:", ts.year)
print("Model name of Three_Series is:", ts.model)
print()

class Five_Series(BMW):
    def __init__(self,parkingAssistantEnabled,make,model,year):   # Constructor of Five_Series class
        self.parkingAssistantEnabled = parkingAssistantEnabled    #Field of Five_Series
        BMW.__init__(self,make,model,year)   # Inhering from parent class constructor

fs=Five_Series(True,"BMW",'535i',2019)
print("Five_Series model information")
# Attribute inheritance
print("parkingAssistantEnabled:", fs.parkingAssistantEnabled)
print("Model Manufacturer of Five_Series is:", fs.make)
print("Manufacturing year of Five_Series is:", fs.year)
print("Model name of Five_Series is:", fs.model)
