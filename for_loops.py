#Looping statements
#objects in python are iterable,the term iterable means to iterate or move over the object or every element in the object

#we can use for loops to execute a block of code for iteration

#syntax of for loop
#my_seq = [1,2,3]
#for item in my_seq:
#    print(item)


my_list = [21,20,15,22,73,55,1000]
for iCnt in my_list:
    print(iCnt)

for i in my_list:
    print("hii")

#check for even numbers in my_list
for iCnt in my_list:
    if iCnt % 2 == 0:
        print(iCnt,"is even")
    else:
        print(iCnt,"is Odd")


#to add all elements in list
my_list = [21,20,15,22,73,55]
sum = 0
for iCnt in my_list:
    sum =sum+iCnt
    #0 = 0+21
    #21 = 21+20
    #41 = 41+15
    #56 = 56+22
    #78 = 78+73
    #151 = 151+55
    #206
    #print(sum)   #This will show all the above iterations if we write it in for loop
print("Sum of elements is:",sum)   #It will give you the final output

#Iteration over string
my_string = "Hello World"
for letter in my_string:
    # print(letter)  #This will print output in character array
    print(letter,end = " ")   #This will print op on single line
print()

#Above syntax can be written like below syntax also
for letter in 'Hello World':
    print(letter, end = " ")
print()

for letter in 'python':   #This will print hello till the number of letters in string gets finished
    print("Hello")

#How to iterate in tuples

tpl = (1,2,3,4,5)
for i in tpl:
    print(i)

for i in tpl:
    if i%2 ==0:
        print(i,"is even")
    else:
        print(i,"is odd")

# create list of tuples
lst = [(1,2),(3,4),(5,6),(7,8),(9,10)]
print(lst)    #This will print whole list of tuples
print(len(lst))   #This will give length of tuple elements

for iCnt in lst:   #This will print one tuple pair at a time of iteration
    print(iCnt)


#tuple unpacking

for iCnt1,iCnt2 in lst:   #By using this we can seperate the tuple elements
    print(iCnt1)
    print(iCnt2)


#Iteration using dictionary
d = {'k1':11,'k2':24,'k3':30,'k4':49,'k5':55}
#print only keys
for iCnt in d:
    print(iCnt)

#print only values
for iCnt in d:
    print(d[iCnt])

#print key and values
for iCnt1,iCnt2 in d.items():
    print(iCnt1,iCnt2)

#iteration over set
s = {10,21,30,45,50}
for iCnt in s:
    print(iCnt)

#Display numbers from 1 to 100  Here we have to use range function
for iCnt in range(1,101):
    print(iCnt, end =" ")
    # if iCnt %2 ==0:     This will print even numbers from 1 to 100
    #     print(iCnt,end = " ")
    #
print()


for i in range(50,70,2):   #Here we use step value along with range
    print(i,end = " ")
print()

#Print table of number OR Multiplication table of number
x = int(input("Enter a number to print table:"))
for iCnt in range(1,11):
    print(x*iCnt)

# This will print table in decorative format
for i in range(1,11):
    print(x,'X',i ,'=',x*i)    #2 X 1 = 2





