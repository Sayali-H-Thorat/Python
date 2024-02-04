#sets
#set is a collection which is unordered- Order of elements chang every time
#sets are written using {} brackets
#Sets exclude duplicate elements and it is mutable


s =set()   #Empty set
print(s)
print(type(s))

#Access items
s = {10,20,30,'xyz',10,20}  #It dont allow duplicate elements.
print(s)
# print(s[0]) #We can do this with set

#Sets does not support indexing slicing and repetition

#Add elements to set
#add()
s = {10,20,30,'xyz',10,20}
s.add(40)  #It will add 40 to set bt we never know at which position it will get added
print(s)

#update-> Add multiple elements to set
s.update([50,60,50,70])
print(s)

#Length of set
print(len(s))

#Remove items
#remove() remove element from set
s1= {10,20,30,40,'abc'}
print(s1)
s1.remove(40)
print(s1)

# s1.remove(40)  #It will give the keyerror because that element is already deleted
# print(s1)

#discard()
s1.discard('abc')
print(s1)

s1.discard(40)  #It will give you the output even though we already deleted that element OR element is not there in set still it will give you op
print(s1)

#pop()
s2 = {'abc','pqr','lmn'}
print(s2)
# s2.pop()  #we dont know this method remove which element
x = s2.pop()  #This method will remove random element by using x variable we stores pop element value in it and then it will display which element get popped
print(x)
print(s2)

#clear()
s1.clear()
print(s1)  #This will display empty set set()

#del
# del s1   #This will delete whole set with that variable declaration
# print(s1) #name 's1' is not defined

#join sets  ->union() and update()
set1 = {10,20,30}
set2 = {40,50,60}
# print(set1+set2)  #unsupported operand type(s) for +: 'set'

set3 = set1.union(set2)   #It will concatenate two sets. union method requires third variable for concatenation
print(set3)

# update()
set1.update(set2)  #for update we dont need third variable to concatenate the set
print(set1)

#copy sets = copy(),set()

s1 = {1,2,3,4,(2+3j)}
print(s1)
s2 = s1.copy()
print("This output is using copy method",s2)

s2=set(s1)
print("This output is using set method",s2)

#difference()
x = {'apple','microsoft','google'}
y = {'amazon','fb','google'}
z = x.difference(y)   #x-y   remaining in x will be our output.
print(z)
z = y.difference(x)  #In y-x remaining in y will be our output common elements get illuminating
print(z)

#issubset()
x = {'a','b','c','d'}
y = {'e','f','g','h','i','j','d','k','a','b','c'}
z = x.issubset(y)
print(z)  #It will give ouput as true as elements of x are present in y

#issuperset()
x = {'f','g','h','i','j','d','k','a','b','c'}
y = {'c','h','k'}
z =x.issuperset(y)
print(z)  #It will give op as true because y contains the elements which are present in x

#intersection() It will give common elements from both sets
x = {1,2,3,4,'5'}
y = {"5","'1'",2,3,5,6}
z = x.intersection(y)
print(z)

#set constructor->set(())
myset = set(('rose','jasmine','lily','orchids')) #It will print all the elements in {} this brackets
print(myset)

#frozen set
#converting set into frozen set when a set is converted into frozen set
#we cannot use update() remove() and clear() operations on set

s = {1,2,3}
print(s)
print(type(s))

f = frozenset(s)
print(f)
print(type(f))

# f.remove(2)  #'frozenset' object has no attribute 'remove'
# print(f)

# f.update([4,5])   #'frozenset' object has no attribute 'update'
# print(f)

# f.clear()  #'frozenset' object has no attribute 'clear'
# print(f)

# del f
# print(f) #name 'f' is not defined because it deletes the frozenset



