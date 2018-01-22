import os

#get files
file_list = os.listdir (r"/Users/JL/Documents/python/udacity/prank")
print (file_list)
#verify and change folder
current_path = os.getcwd()
print (current_path)
os.chdir (r"/Users/JL/Documents/python/udacity/prank")
#rename files, delete numbers in file name
for file_name in file_list:
 os.rename (file_name, file_name.translate(None, "0123456789"))
os.chdir(r"/usr/bin")

