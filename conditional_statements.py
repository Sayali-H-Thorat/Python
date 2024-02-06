#Flow control statements will determine the order in which statements are executed at run time
#3 types of control statements
#1. conditional statements
#2. looping statements
#3. transfer statements

#control flow syntax makes use of colons and indentation

#conditional statements
#conditional statements evaluates until condition is true
#if, if...else, if.....elif....else

#syntax of if statements
#if condition:
     #statements

if 1<2:
    print('yes')

if 3<4:    #outer if
    print('first block')
    if 1<2:     #inner if
        print('second block')

#syntax of if else
#if condition:
     #statements
#else:
   #statements

if 1<2:
    print("This condition is true")
    # if 3<4:
    #     print("This is nested if")
else:
    print("This is else block")


#if..elif...else
#if condition:
    #statements
    # elif other condition:
       #Statements
#else:
   #statements / else block code

if 1>2:
    print("1 is greater than 2")
elif 3==3:
    print("3 is equal to 3")
else:
    print("Both the conditions are wrong")

#Nested if....elif ladder

name ='John'
if name == 'Bob':
    print("Hii Bob")
elif name =='Sam':
    print("Hii Sam")
elif name =='Ram':
    print("Hii Ram")
elif name == 'Tina':
    print("Hii Tina")
elif name == 'John':
    print("Hii John")
elif name == 'Maark':
    print("Hii Mark")
else:
    print("What is your name..?")

#Handle numbers
#Input() functions: Take input from user
#input() function take the input in the form of string so we have to convert it and this is known as typecasting
# x = int(input("Enter first number:"))
# y = int(input("Enter second number:"))
# print(x+y)

x = int(input("Enter a number:"))
if x ==0:
    print("Enter number is zero")
elif x%2 ==0:
    print(x,"is even number")
else:
    print(x,"is odd number")



