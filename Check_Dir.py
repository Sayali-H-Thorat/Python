# Check if dir is present or not
# We put double backslash(\\) because if we put single backslash(\) then it might considered as escape sequence character
import os
print("Path of current dir is:\n",os.getcwd())

check_dir = os.path.isdir("C:\\Users\\thora\\PycharmProjects\\Project_python\\File_Systems\\NewYork")
print(check_dir)   # give answer in boolean

