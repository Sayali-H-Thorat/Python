# Encapsulation -
# Protecting properties(attributes/variables) and functionalities of one object from another object
# Encapsulation can also be defined as binding/ writing data and code into single unit

class Student:
    def __init__(self):
        self.id=123
        self.name='Sayali'

s1 =Student()
print("Id is:",s1.id)
print("Name is:",s1.name)
print()

# How to make fields private using __ at the beginning means it gets private
# Below code will give error
# class Students:
#     def __init__(self):
#         self.__id =545
#         self.__name = 'Sneha'
# #         __id and __name are private fields here
#
# s2 = Students()
# print("Id is:",s2.id)
# print("Name is:",s2.name)

# Access private fields using instance method
#Encapsulation using default constructor
class Students:
    def __init__(self):
        self.__id =535
        self.__name = 'Snehanjali'
#         __id and __name are private fields here
    def display(self):    # instance method
        print("Id is:",self.__id)
        print("Name is:",self.__name)

s3 = Students()
s3.display()
print()

#Encapsulation using Parameterised constructor
class Students:
    def __init__(self,id,name):   #Parameterised constructor
        self.__id =id
        self.__name = name
#         __id and __name are private fields here
    def display(self):
        print("Id is:",self.__id)
        print("Name is:",self.__name)

s4 = Students(655,'Savi')
s4.display()
print()

# Access private fields using name mangling syntax
class Student:
    def __init__(self):
        self.__id=656
        self.__name='Radha'
s4 = Student()
# Below two are name mangling syntax
print("Id is:",s4._Student__id)   # name mangling syntax
print("Name is:",s4._Student__name)  # name mangling syntax
