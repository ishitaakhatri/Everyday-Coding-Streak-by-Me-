a=[1,2,3,4,5,6,7]
target=int

def search(a,target):
 #i is for elements and value is for index 
    
 for i,value in enumerate(a):
    if (value==target):
        return i
    
 return -1    


# print(search(a,6))
#what if we want to use the same function in another file and with different array
#we can import the file
