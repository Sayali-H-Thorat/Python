# prevent method overriding
# super() is builtin function used to envoke parent class constructor and parent class method from child class constructor and method and
# super() will make child class inherit all the methods and properties from its parent.

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
        super().__init__(make,model,year)   # Parent class constructor here we add super() method and remove self

    def start(self): # Overriding parent class method
        super().start()   # Access the parent class start method
        print("Button start..\n")

    def stop(self):   # Overriding parent class method
        print("Button stop...\n")
        super().stop()  # Access the parent class start method

    def display(self):   # Own method
        print("Color is:",self.color)

ts=Three_Series('Black','BMW','3Series',2020)
ts.start()
ts.stop()
ts.display()