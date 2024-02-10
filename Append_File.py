#Append to a file
# It will add data to previous data of the file
f = open('demo','a')
s = input("Enter some text:")
f.write(s)
print("Data is appended to file successfully")
f.close()
