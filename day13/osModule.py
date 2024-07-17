import os 

print(dir(os))

#getting the current working directory

print(os.getcwd())

#change directory 

# os.chdir('/users/admin/desktop/WEB_DEV')

print(os.getcwd())

#list directory 

print(os.listdir())

#creating new folder (creating a new directory)

# os.mkdir('os-demo-2')
#or
#making directories recursively
# os.makedirs('os-demo-2/sub-dir-1')

# print(os.listdir())
#removing or deleting directory 
# os.rmdir('os-demo-2')
#or
#removing directoris recursively
# os.removedirs('os-dir-2')
# print(os.listdir())

#renaming a file 

# os.rename('day1','starting')
# os.rename('starting','day1')
# print(os.listdir())

#print all info of a file 

print(os.stat('day1'))

#traverse directory recursively 

for dirpath,dirnames,filenames in os.walk('/Users/Admin/Desktop/python'):
    print('current_path:',dirpath)
    print('directories:',dirnames)
    print('files:',filenames)
    print()


