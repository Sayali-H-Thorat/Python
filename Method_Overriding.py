# Method overriding
# When child/derived/sub class inherits from parent/base/super class sometimes they use same methods but with different functionality

class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the car...\n")

    def stop(self):
        print("Stopping the car..\n")

class Three_Series(BMW):
    def __init__(self,color,make,model,year):   # Own constructor
        self.color=color
        BMW.__init__(self,make,model,year)   # Parent class constructor

    def start(self): # Overriding parent class method
        print("Button start..\n")

    def stop(self):   # Overriding parent class method
        print("Button stop...\n")

    def display(self):   # Own method
        print(self.color)

ts=Three_Series('Black','BMW','3Series',2020)
ts.start()
ts.stop()
ts.display()