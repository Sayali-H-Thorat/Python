# File: Collection of information/data. This data could be text data,binary data(audio/images/video).

#opening a file
# f =open('filename',mode)

# close file
# f.close()

# modes
'''
1-> w: write to a file(everytime it write new content to a file)
2-> r: read from file
3-> a: append to a file(Current content of file will not get deleted)
4-> x: Exclusive creation mode(creates a new file only once
'''

# binary files
# wb(write binary),rb(read binary),ab(append binary)

# Write a string to file.
'''
f = open('demo.txt','w')
s =input("Enter a text:")
f.write(s)
print("File is created and text is written into it.")
f.close()
'''

# For taking multiple line input /paragraph
f =open('demo','w')
print("type # when you done writing...")
s = ' '
while s!='#':
    s=input("Enter the data:")
    f.write('\n')
    f.write(s)
f.close()