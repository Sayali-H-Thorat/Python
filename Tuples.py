#Tuple is a sequence/collection which is ordered and immutable
#Written using () brackets
#We cannot use methods on tuples such as append(),extend(),insert(),remove(),clear() etc

tpl = ()  #empty tuple
print(tpl)
print(type(tpl))

# tpl1=(10.5)    #This will give output as float type
# print(type(tpl1))

tpl1=('hii',)  #This will give output as tuple
print(tpl1)
print(type(tpl1))

tpl = (10,20,30,'xyz',-50)
print(tpl)
print(type(tpl))

#Repetition
print(tpl*3)
print(tpl+tpl)

#length of tuple
print(len(tpl))

#indexing, slicing[]
tpl2 = (10,20,30,'xyz',-50)
print(tpl2[2])
print(tpl[3])

#slicing [start:stop:step]
print(tpl2[0:3])
print(tpl2[3:])
print(tpl2[3:-1])

# tpl2.append(60) #'tuple' object has no attribute 'append'
# print(tpl2)

# tpl2.clear() 'tuple' object has no attribute 'clear'
# print(tpl2)

#tuple index
tpl3 = (1,20,'hi','2','Hello',20)
print(tpl3.index('2'))   #It will give the index of element 2

#count()
print(tpl3.count(20))  #it will give the occurrence of that element

#create a tuple using single character as elements
t2 = ('j','a','v','a')
print(t2)
print(t2[2])
# print(t2[2.0] #tuple indices must be integers or slices, not float

#Nested tuple-> Tuple inside tuple
tpl4 = ('Python',(1,2,3),('xyz'),('a'))
print(tpl4)
print(tpl4[2])
print(tpl4[3])
# print(tpl4[4])  #It will give tuple index out of range

print(tpl4[1][1])
print(tpl4[2][2])
print(tpl4[0][2:])

#tuple concatenation
t1 = (1,2,3)
t2 = (4,5,6)
print(t1+t2)
t3 = t1+t2
print(t3)
print(t1+(4,5,6))
print((1,2,3)+(4,5,6))

#tuple membership test  in and not in
tpl = ('"abc"','1',0,'abc')
print("abc" in tpl)

#change tuple element
x = ('python','django','excel')
print(x)
# x[1] = 'java' #'tuple' object does not support item assignment
# print(x)
y = list(x)   #convert tuple to list
print(y)
y[1] = 'java'  #By using this syntax we can change the tuple element
print(y)
z = tuple(y)  #Convert list to tuple
print(z)

#Add elements to tuple
x = ('python','django','excel')
print(x)
y = list(x)
print(y)
y.append('sql')  #append() method used to add element in tuple bt 1st we have to convert tuple into list
print(y)
y.extend('html')    #If we write extend syntax like this it will print multiple elements like 'h','t','m','l' etc.
y.extend(['html','mysql'])  #If we have to add multiple elements at the end then inside round brackets() we have to write square brackets[] and elements to add in tuple
z = tuple(y)
print(z)


#Delete tuple
#Tuple element cannot be deleted, instead we can delete complete tuple
t3 = (10,20,30)
print(t3)
# del t3[1]  #'tuple' object doesn't support item deletion
# print(t3)

# del t3  #This will delete whole tuple
# # print(t3)

#Tuple constructor->tuple(())
tpl = tuple(('USA',10,20,30,40,50,'SAYALI'))
print(tpl)

tup = (1,2,3,5)
print(tup[0])  #This is indexing ->It will return the element which is present at oth position
print(tup.index(1))  #This is index method ->This will return the index of given element

#Tuple methods
'''
1.index()
2.count()
'''
