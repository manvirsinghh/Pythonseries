import os
if(os.path.exists("c:\\Users\\Win\\Documents\\ab.txt")):
    os.remove("c:\\Users\\Win\\Documents\\ab.txt")
else:
    print("The file or directory does not exist")
print(os.path.isfile('c:\\Users\\Win\\Documents\\ab.txt')) # to check the file exist or not using this by passing file path s parameter