#List is a collection/sequence which is ordered and mutable
#List can store multiple elements and can maintain order of them
#List can include duplicate elements
#Lists are written using [] brackets
#List is mutable

List1 = []      #Empty list
print(List1)
print(type(List1))

#List is heterogeneous
List2 = [10,20,30,'Python',-10,30.5]
print(List2)

#length of list
print(len(List2))

#Repetition
print(List2*3)

#Indexing
print(List2[0])
print(List2[5])
print(List2[-3])
# print(List2[6]) #list index out of range

#Slicing
print(List2[0:3])
print(List2[-5:0])   #It will give you empty list
print(List2[-3:-1])
print(List2[-1:-3])  #-1 is greater than -3 hence it will display empty list. Slicing will never give any error
print(List2[3:1])    #It will give empty list
print(List2[:4])    #It will print the values start from 0 to 4

print(List2[::-1])  #It will print the whole list in reverse order
print(List2[::2])   #It will print altenate characters from the list

#List methods to add and remove elements from list

#append() We can use append() method to add elements in list.It will add elements at the end of list
List2.append(40)
print(List2)
List2.append('Hii')
print(List2)

#insert()  It use to insert element at specific position
List2.insert(1,'HELLO')
print(List2)

#extend() It will add multiple elements at the end of list
List2.extend([50,60,70,'Sayali'])
print(List2)

#How to remove elements from list
# 1.->remove()
List2.remove(50)
print(List2)

#pop() It always remove last element from list LIFO
List2.pop()
print(List2)

#pop(index)
List2.pop(1)  #It will remove element which is at 1st index
print(List2)

#del   It will delete that positions element
del List2[3]
print(List2)

List2.remove('Hii')
print(List2)

#sort the list arrange the list in ascending or descending order
List2.sort()
print(List2)

List2.reverse()  #reverse the list
print(List2)

List2.sort(reverse = True) #sort and reverse the list
print(List2)
#
# List2.append('Hi')
# print(List2)

#max and min element
print(max(List2))  #If we have string then not supported between instances of 'str' and 'int' It cant compare string and int
print(min(List2))

#join/concatenate/combine list
l1 = [10,20,30]
l2 = [40,50,60]

#variations for concatenate the string
print(l1+l2)
l3 = l1+l2
print(l3)
print(l1+[40,50,60])
print([10,20,30]+[40,50,60])


#copy Lists->copy(),list()
l1=[10,20,30]
print(l1)
l2=l1.copy() #copy() method  will copy the elements of l1 to l2
print(l2)
l3=list(l1)  #list() method is also used to copy elements from one list to another
print(l2)
l4=l1   #This will also do the copy bt this is not a method this is assignment
print(l4)

#Lists are mutable
lst = ['USA','UK','INDIA']
print(lst)
lst[1]='CANADA'
print(lst)
lst.append('GERMANY')
print(lst)
lst.insert(1,'FRANCE')
print(lst)
lst.remove('USA')
print(lst)

#Nested Lists- List inside another list
lst = ['Hello',[10,20,30],['Good afternoon']]
print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[-2])
# print(lst[4])   #It will give IndexError as list index out of range
print(lst[0][4])
print(lst[1][1])
print(lst[2][0])
print(lst[1][-2])
print(lst[0][2:6])

#List membership test->'in' and 'not in'
lst=[1,2,'10','hii',10.5,"'bye'"]
print(1 in lst)
print(10 in lst)
print('hii' not in lst)
print("bye" in lst)
print("hii" in lst)
print('1 in lst')
print("'bye in lst'")
print(1 and 'hii' in lst)

#List constructor->List(()) this is syntax for list constructor
myList=list(('USA','India','London'))
print(myList)

#index() -> It will give you the index of element
l1 = [10,20,30,40,50,10,10,20,20,40,10]
print(l1.index(30))

#count() -> It will return the occurrence of list element
print(l1.count(10))

#clear() It will clear all the elements of list
l1.clear()
print(l1)

# del l1  #It will delete whole list with its existence
# print(l1)

#Deleting/removing multiple list elements
new_List = [1,2,3,-1,10,12]
print(new_List)
del new_List[3:5]  #It will delete two elements from the list This is slicing syntax for deletetion so here we can delete sequential elements
print(new_List)

#    0 1 2 3 4
#    -5-4-3-2 -1
p = [1,2,3,4,5]
print(p[0:-3])
#This will give op as[1,2]

#List methods
'''1)append
2)insert()
3)extend()
4)remove()
5)pop()
6)pop(index)
7)del
8)copy()
9)list()
10)list(())
11)max()
12)min()
13)sort()
14)sort(reverse = True)
15)index()
16)count()
17clear()
18)len()'''




