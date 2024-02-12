# inner class:-> Class inside another class
# create a class Car and inner class Engine

class Cars:   # Outer class
    def __init__(self,make,year):
        self.make=make
        self.year=year

    class Engine:   # Inner class of car
        def __init__(self,number):
            self.number=number

        def start(self):
            print("Engine Started!!!")

        class Vehicle:    #Inner class of engine
            def __init__(self,color):
                self.color=color

            def drive(self):
                print("Lets drive the car..")

c1=Cars('Thar',2020)
print("Company of car is:",c1.make)
print("Year of Manufacturing is:",c1.year)
eng=c1.Engine(12345)   # When you create obj of inner class you have to write outer class obj and then inner class name
print("Number of engine is:",eng.number)
eng.start()
v=eng.Vehicle('Black')
v.drive()
print("Color of car is:",v.color)
