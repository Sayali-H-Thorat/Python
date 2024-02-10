# copy file
# image is in binary format
# open(img_name,read binary mode)
f = open('m13.jpg','rb')
# open(new file name,write binary mode)
f1 = open('Radhe_Radhe.jpg','wb')
for iCnt in f:
    f1.write(iCnt)

# For .py file
f2 = open('Create_File.py', 'r')
f3 = open('Jay_Shree_Krishna.py', 'w')
for iCnt in f2:
    f3.write(iCnt)