# Interface-> will have all methods are abstract
from abc import ABC, abstractmethod
# we need to import abstract class and abstract method
class BMW(ABC):   # ABC-Abstract class
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    @abstractmethod
    def start(self):  # abstract method without body
        pass

    @abstractmethod
    def stop(self):   # abstract method without body
        pass

    @abstractmethod
    def drive(self):   # abstract method without body
        pass
class Three_Series(BMW):
    def __init__(self,color,make,model,year):  # constructor
        self.color=color
        super().__init__(make,model,year)  # Invoking the parent class constructor

    def display(self):  # instance method
        print("Color is:",self.color)

    def start(self):  # concrete method with body
        print("Button start..")
    def stop(self):   # concrete method with body
        print("Button stop..")
    def drive(self):     # concrete method with body
        print("Three series being drive...")

ts=Three_Series('black','BMW','3Series',2020)
ts.start()
ts.stop()
ts.display()
ts.drive()