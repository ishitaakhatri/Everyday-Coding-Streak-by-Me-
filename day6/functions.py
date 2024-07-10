#creating a function
def hello_func():
    pass

print(hello_func())
#defining a function
def hello():
    print("hello there..!")

hello()  
#passing arguments 
def greetings(name,course):
    print('hi,{} welcome to {}.'.format(name,course))

greetings('ishita','btech')      
#passing a default argument 
def hi_there(course,name='cheeki'):
    print('hi,{} welcome to {}.'.format(name,course))

hi_there('science')
