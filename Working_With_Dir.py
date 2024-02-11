# Directory
# get current dir
import os
print()
print("Path of current dir is:\n",os.getcwd())   # It will give the current working directory's whole path  getcwd() means get current working directory
print()

# List python dir- how many files are present in dir
print("Files in current dir are:\n",os.listdir())
print()

# how to make dir
os.mkdir('My_Pics')   # mkdir is make directory It will create a directory in current directory. You can create directory once you cant create same name directory again, so you have to comment this once you make dir
print("List of directories after creating new dir:\n",os.listdir())  # listdir is list of directories it will give the list of directories
print()

# rename dir
# rename(old_dir_name,new_dir_name)
os.rename('My_Pics','New_dir')   #rename the old name with new one. Once you rename you cant use the same old name to rename because it already gets renamed
print("List of directories after renaming dir:\n",os.listdir())
print()

# deleting dir
os.rmdir('New_dir')   # It will remove the mentioned directory
print("List of directories after removing dir:\n",os.listdir())
print()

# Check if dir is present or not
# We put double backslash(\\) because if we put single backslash(\) then it might considered as escape sequence character
check_dir = os.path.isdir("C:\\Users\\thora\\PycharmProjects\\Project_python\\File_Systems")
print(check_dir)   # give answer in boolean
