# Types of arguments
def add(a,b):    # a,b are known as formal arguments
    c = a+b
    print(c)
add(4,5)    #4,5 are actual arguments

# Actual arguments are of 4 types
# 1)positional argument
# 2)Default argument
# 3)Variable length argument
# 4)Keyword variable length argument

# 1)positional argument
def person(name,age):
    print("Name is:",name)
    print("Age is:",age)
person('John',25)
person(age=30,name='Sam')   #If you are changing the position assign the values to the arguments while calling the function

# 2)Default argument
def Average(a=10,b=20):
    print((a+b)/2)
Average()
Average(a =20)
Average(a =20,b=30)

# Variable length argument
def Sum(a,b):
    c =a+b
    print(c)
Sum(10,20)

# Rewriting of Sum function
# * holds multiple values bt we can't put * for 1st argument
def Sum(a,*b):   #*args *b holds multiple values start from 2nd to last
    c = a
    for iCnt in b:
        c = c+iCnt
#         10 =10+20
#         30 =30+30
#         60 =60+40
#         100 = 100+50
#        150
#         print(c)  #It will shows all the steps
    print(c)   #It will shows the final op
Sum(10,20,30,40,50)

# 4)Keyword variable length arguments
# ** to put the description for 2nd argument
def Person(name,**Data):
    print(name)
    print(Data)
    # for loop is for iteration over the function for data and it will give op in key and value pairs
    for iCnt1,iCnt2 in Data.items():
        print(iCnt1,iCnt2)
# Person('John',30,'Pune',7058943568)
Person('John',age=30,City='Pune',Mobile_No=7058943568)

