# Function passed as parameter

def display(func):
    return "hii " + func


def name():
    return "John"

# here display function has parameter, so we call that function and pass another function as parameter
print(display(name()))

def show(arg):
    return "how are you " +arg
print(display(show("Sam")))

# Nested Functions-Function inside fun
# 1).Outer fun contain one parameter and another is without parameter
def Outer_fun(fun):
    def Inner_fun():
        return 'hi,' + fun
    return Inner_fun()
print(Outer_fun('Tina'))

# 2).Both functions have parameter
def Outer_function(fun1):
    def Inner_function(arg1):
        return 'Hello,' + arg1 + fun1
        # return 'Hello,' + fun1 + arg1
        # return fun1 + arg1 + 'Hello,'
        # return fun1 + 'Hello,' + arg1
        # return arg1 + 'Hello,' + fun1
    return Inner_function(' How are you ')
print(Outer_function(' guyz '))

# 3).Outer function empty and inner function have one argument
def Outer_fun():
    def Inner_fun(msg):
        return msg + ' Sayali'
    return Inner_fun("Have a good day")
print(Outer_fun())

# 4). Inner and outer both functions without arguments
def outer_fun():
    def inner_fun():
        return "Hello " + "Sayali"
    return inner_fun()
print(outer_fun())


#Passing sequence type to the function
def my_fun(lst):
    for iCnt in lst:
        if iCnt % 2 ==0:
            print(iCnt)
my_fun([10,20,30,47,55,60])
