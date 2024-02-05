#Range function
#range() function returns a sequence of numbers starting from 0(by default) and increments by 1(by default), ends at specified number or it
#will return a range object bt passing range value

r = range(5)    #range(0,5) 0,1,2,3,4
print(r)

for iCnt in r:
    print(iCnt)

for j in range(1,6):    #1,2,3,4,5
    print(j)      #It will print vertically

for z in range(1,15,2):   #Here 2 is step value
    print(z, end=' ')   #For writing on single line horizontally
print()   #It will add space after output. If we cant add this print after writing end then this will add the op of both syntax together

for y in range(-5,7):
    print(y,end=' ')
print()

