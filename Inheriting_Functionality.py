# Inheriting Functionality
class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):   # instance method
        print("Starting the car...\n")

    def stop(self):  # instance method
        print("Stopping the car...\n")

class Three_Series(BMW):
    def __init__(self,color,make,model,year):  # child class constructor
        BMW.__init__(self,make,model,year)    # parent class constructor
        self.color=color

    def display(self):
        print("Color is:",self.color)

ts=Three_Series('Black','BMW','3Series',2020)
# Method inheritance
ts.start()
ts.stop()
ts.display()
# Attribute inheritance
print("Model Manufacturer of Three_Series is:", ts.make)
print("Manufacturing year of Three_Series is:", ts.year)
print("Model name of Three_Series is:", ts.model)