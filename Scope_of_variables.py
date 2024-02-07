# Scope of variables
# Local variables- Accesible inside function only
# Global variables- Accesible throughout the program

x = 123   # x is global variable here
def display():
    y =458
    print("Value of x inside function:",x)
    print("Value of y:",y)
# display()   This will change the sequence of execution
print("Value of x outside function:",x)
display()

#Accessing global variables with same name
a =10    # Global variable
def display():
    a =11   # local variable
    print("local var",a)
    print(globals()['a'])      # If name of local and global variables are same then we have to use globals() function
print("Outside main",a)
display()
