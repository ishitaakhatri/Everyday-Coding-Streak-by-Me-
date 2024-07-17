#opening the text file 
# f = open('python.txt','r')#can have 'r' reading the file,'w' for writing, 'a' for append,'r+'to read and write

# print(f.name)
# print(f.mode)

# using context managment 

# f.close()

with open('python.txt','r') as f:
    f_contents = f.read()#reading 20 characters from the file 
    # f_contents = f.readlines()
    # f_contents = f.readline()
    print(f_contents)
    # for line in f :
    #     print(line,end='')

    # writing in file 
    with open('python.txt','w') as f:
        f_content = f.write('hey my name is ishita')
        





