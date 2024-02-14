# Polymorphism
# Poly-multi/many
# morphic-forms/shapes/behaviour
# Polymorphism refers to different types of behaviour based on data or object that the functions are dealing with

# Duck Typing: Dynamically passing parameters
# Bottom up approach
class Duck:
    def talk(self):
        print("Quack Quack..")

class Human:
    def talk(self):
        print("Hello")

class Cat:
    def talk(self):
        print("Meow")
# common method which accepts object of two classes. Classes must contain same method names.
def callTalk(obj):
    obj.talk()

d=Duck()
callTalk(d)

h=Human()
callTalk(h)

c= Cat()
callTalk(c)

# Duck typing for dependency injection
# dependency injection is injecting an object into another object as required
# Top down approach

class Flight:
    def __init__(self,engine):   # Constructor with one parameter
        self.engine=engine

    def StartEngine(self):    # instance method
        self.engine.start() # Common method for two classes

class AirbusEngine:  # 1st class
    def start(self):
        print("Starting airbus engine...")

class BoeingEngine:   #2nd class
    def start(self):
        print("Starting boeing engine...")

ae = AirbusEngine() # obj for 1st class
f=Flight(ae)        # obj of class which contains common start method
f.StartEngine()     # Call the method which contains start method

be=BoeingEngine()   #obj for 2nd class
f1=Flight(be)       # obj of class which contains common start method
f1.StartEngine()    # Call the method which contains start method
