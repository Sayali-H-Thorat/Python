# Check if file exist or not and display content file on the screen
# html, database are binary files
import os,sys  # path is in os, so we need to import this two modules without this we cant check if file is present or not
if os.path.isfile('file1.txt'):
    f = open('file1.txt','r')
    s = f.read()
    print("File is present in system and content of file is:\n",s)
    f.close()
else:
    print("SORRY!!!File does not exists...")
    sys.exit()
print()

# For .py file
if os.path.isfile('Append_File.py'):
    f = open('Append_File.py','r')
    s = f.read()
    print("File is present in system and content of file is:\n",s)
    f.close()
else:
    print("SORRY!!!File does not exists...")
    sys.exit()
print()

# Check file is present or not (boolean op)
# if present give true else false
check_file =os.path.isfile('sayali.txt')
print(check_file)
