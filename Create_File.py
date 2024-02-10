# create file in exclusive file creation mode
# f =open('file1.txt','w')  When we create file using w mode every time it gets created or get override

# When we create file in x mode then we can't create same file again for single use
f =open('file1.txt','x')
s =input("Enter some txt:")
f.write(s)
print("File is created in x mode and data is added to file... ")
f.close()