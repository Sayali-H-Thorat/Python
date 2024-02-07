# Function arguments

def my_fun(x):
    x = 8
    print("x is:",x)
my_fun(6)   # If we add explicitly print here even though print is present in function then it will print none. We can add print here only if there is return statement in function

# update the list element of index pos 1
def update(lst):
    print(id(lst))
    lst[1] = 25
    # lst[2] = 20
    print(id(lst))
    print("List is:",lst)
# lst = [10,20,30,40]
# update(lst)
update([10,20,30,40])
# Both the above syntax are same



