#Dictionary is a collection which is ordered but unindexed
#it is a key value pair
#written using {}
#it is mutable


d = {}
print(d)
print(type(d))

dict1 = {1:'John',2:'Bob',3:'Sam','Name':'Sayali'}
print(dict1)

mydict = {
    'brand':'bmw',
    'model':'3series',
    'year':2024
}

print(mydict)

#Accessing items

# print(mydict['brand'])
x = mydict['brand']
print(x)

print(mydict.items())   #It will give all items in a map/dict

#change the value
#change year to 2019
mydict['year']=2019
print(mydict)

#length of dict
print(len(mydict))

#Adding items to dict
#Adding an item to dictionary is done by using an index key and assigning a value to it
mydict['color']='black'
print(mydict)
print(len(mydict))

#remove items
#pop(key)   It will remove key and its value
mydict.pop('year')
print(mydict)

#popitem() -remove last inserted item
mydict.popitem()
print(mydict)

#del
del mydict['model']
print(mydict)

#copy element of one dictionary to another
#There are two methods to copy element from one dictionary to another dictionary->copy(), dict()
d1 = {1:10,2:20,3:30,4:40}
print(d1)
d2 = d1.copy()
print(d2)

d2 = dict(d1)
print(d2)

#Join dictionaries
#update() method
d1 = {1:10,2:20,3:30,4:40}
d2 = {5:50}
d1.update(d2)   #No need to use third variable for update method
print(d1)
d2.update(d1)   #It will print elements of d2 first and then elements of d1
print(d2)


#Nested dictionaries
# my_stuff1 = {'key1':'Apple', 'key2':'Pineapple','key3':{'key4':'Kivi'}}
# print(my_stuff1)
# print(type(my_stuff1))
#in key4 we can use (),[] and we can write single string alson
my_stuff = {'key1':'Apple', 'key2':'Pineapple','key3':{'key4':['Kivi','Mango','Chikoo']}}
print(my_stuff)
print(my_stuff['key1'])
print(my_stuff['key2'])
print(my_stuff['key3'])
#Below syntax is used to print the nested dctionary elements
#We have to use key of outer and inner dictionary only then we can print elements of nested dictionary
print(my_stuff['key3']['key4'])

#We can print single element of nested dictionary using below syntax
print(my_stuff['key3']['key4'][2])

#Below syntax will print key4 last element in upper letters
print(my_stuff['key3']['key4'][2].upper())

#Below syntax will print key4 last element in lower letters
print(my_stuff['key3']['key4'][2].lower())

#By using below syntax we can use slicing in dictionary
print(my_stuff['key3']['key4'][2][3:])
print(my_stuff['key3']['key4'][1][3:])

#Dictionary Constructor-> dict()
#In dictionary constructor we can write key name as string without using inverted commas("",'')
#It uses equal to = instead of colon
#for dictionary constructor we use single round brackets
d1 = dict(name = 'ford',model='ikon',year=2017)
print(d1)
print(d1['name'])

d1['name']='Audi'   # Here we update the value of key
print(d1)

#Looping through
#To access keys
k=d1.keys()
#iCnt is iteration variable
print("for loop to print key")
for iCnt in k:    #for iCnt in d1.keys():
    print(iCnt)

#To access values
v = d1.values()
print("for loop to print values")
for iCnt in v:
    print(iCnt)
#Above and below both the syntax will work same
print("for loop to print values")
for iCnt in d1.values():
    print(iCnt)

#Below syntax will print only keys
print("for loop to print key")
for iCnt in d1:
    print(iCnt)

#Below syntax will print only values
print("for loop to print values")
for iCnt in d1:
    print(d1[iCnt])   #d1['name']

print("for loop to print key and values together means this will 1st print key and then values")
for iCnt in d1:
    print(iCnt)
    print(d1[iCnt])

#loop through both keys and values by using items()
print("for loop using two iterators to print key and values together")
for i,j in d1.items():
    print(i,j)






