# Types of methods
# There are 3 types of methods
# 1. Instance method
# 2. Class method
# 3. static method

class Student:
    school='Wadia College'   # class/static it works as global variable. We can reassign/redeclare variable
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):  # instance method-Method which takes self as argument is instance method.
        return (self.m1+self.m2+self.m3)/3

    @classmethod   # Writing this is not mandatory but its good programming practice
    def info(cls):  #class method:->Take any other arguments than self
        # cls.school='Modern College'  #Here we modify the value
        return cls.school

    @staticmethod    # We have to write this here if we dont then it will give error
    def display():    #Static method will not have anything inside bracket
        print("This is static method")

s1=Student(50,78,98)
print("Marks of 1st sub is:",s1.m1)
print("Marks of 2nd sub is:",s1.m2)
print("Marks of 3rd sub is:",s1.m3)
print("Average marks of 3 sub is:",s1.avg())   # instance method call
print("Name of school is:",s1.info())  # class method call
s1.display()   # static method call
