# Recursive functions - recursion is a function calling itself again and again
# Factorial

'''
factorial(3)=3*2*1
factorial(3) = 3*factorial(2)
factorial(2) = 2*factorial(1)
factorial(1) = 1*factorial(0)
factorial(0) = 1

factorial(n) =n*factorial(n-1)

'''

def factorial(iNum):
    if iNum ==0:
        return 1
    else:
        return iNum*factorial(iNum-1)
print(factorial(0))
print(factorial(3))
print(factorial(4))

#Factorial using recursive function
def fact(iNum):
    if iNum ==0:
        return 1
    else:
        return iNum*fact(iNum-1)
print(fact(2))
print(fact(5))

