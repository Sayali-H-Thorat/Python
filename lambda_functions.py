# Lambda functions
# Lambda are small anonymous(unknown) functions that will not have any name.
# Lambda functions may take any number of arguments but only one single expression

# syntax of lambda
# lambda argument_list:expression
# Simple function
def result(x):
    return x*x
print(result(2))

# above function using lambda function
f = lambda x:x*x
print(f(2))

# function to print power using lambda function
f = lambda x:x**3
print(f(2))

# sum of two numbers using lambda function
# lambda take only one expression and arguments may be one or more than one
# arguments and arg in the variable should be same
f = lambda x,y:x+y
print(f(10,11))

# join strings using lambda
z =lambda x,y:x+y
print(z('hello',' world'))

# lambda to multiply 3 numbers
z =lambda a,b,c:a*b*c
print(z(2,3,5))

# Methods in lambda functions
# filter() : filters out elements based on logic and conditions
# filter(lambda_function,iterable)

# Retrieve only even numbers from the given list
# filter function is not list so, we have to explicitly add list before filter function
lst = [10,20,30,55,17,91,44]
result=list(filter(lambda x:x%2 == 0,lst))
print("even elements from list are:",result)

# map() - maps out sequence elements based on logic and conditions
# map(lambda_function,iterable)

# In the list double the numbers and print them
lst =[1,2,3,4,5,6,7]
result=list(map(lambda x:x*2,lst))
print("Double of each element from list is:",result)

# reduce(): reduces the sequence elements based on logic and condition
# reduce(lambda_function,iterable)
# import reduce using : from functools import reduce
# In the given list reduce the sum of all the elements in list
from functools import reduce
lst = [10,20,30,40,50]
result =reduce(lambda x,y:x+y,lst)
print("Addition of list elements is: ",result)

# 'int' object is not iterable
# a =50
# b = list(a)
# print(b)
