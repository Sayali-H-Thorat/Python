# In collections, we have counter objects   ++, -- are counter objects
# used to count object and iterate over it

from collections import Counter

# Sequence of items using counter
print(Counter(['a', 'b', 'z', 'z', 'x', 'a', 'z']))
# Above syntax will give the frequency of each character

print(Counter({'z': 3, 'a': 2, 'b': 1, 'x': 1}))  # using dictionary
print(Counter(z=3, a=2, b=1, x=1))  # Keyword arguments

# subclass of dictionary- OrderedDict
from collections import OrderedDict

# Normal Dictionary is also ordered
print("This is a dictionary:\n")
d = {}
d['a'] = 10
d['b'] = 20
d['c'] = 300
d['d'] = 400

for iCnt1, iCnt2 in d.items():
    print(iCnt1, iCnt2)
print()

# # deleting item
# # remove the 1st element
# d.pop('a')
#
# # Re-inserting the same
# # value gets inserted at end
# d['a'] =10
#
# for a,b in d.items():
#     print(a,b)
# print()

# we use ordered dictionary here and used function OrderedDict()
print("This is an ordered dictionary:\n")
od = OrderedDict()
od['a'] = 10
od['b'] = 20
od['c'] = 300
od['d'] = 400

for a, b in od.items():
    print(a, b)
print()
# deleting item
# remove the 1st element
od.pop('a')

# Re-inserting the same
# value gets inserted at end
od['a'] = 10

for a, b in od.items():
    print(a, b)

# NamedTuple:-Return tuple object. it is a sequence which is immutable

from collections import namedtuple

# declaring namedtuple
Employee = namedtuple('Emp', ['name', 'id', 'salary'])
E1 = Employee('John', 101, 350000)
# Access using index
print("Access using index no:", E1[1])
# Access using name of tuple/name
print("Access using tuple name:", E1.id)

E2 = Employee('Sayali', 102, 400000)
print("Name of 2nd employee:",E2.name)


E3 =['Sneha',111,450000]
# namedtuple has two functions:- _asdict and _make
print(E1._asdict())
print(E1._make(E3))

