import os

file_list = os.listdir (r"/Users/JL/Documents/python/udacity/message")
print (file_list)
current_path = os.getcwd()
print (current_path)
os.chdir (r"/Users/JL/Documents/python/udacity/message")

for file_name in file_list:
    os.rename (file_name, file_name.translate(None, "0123456789PQRSTUVWXYZ"))
os.chdir(r"/usr/bin")
