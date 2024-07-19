from typing import Any


def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print("the wrapper fucntion starts the execution")
        return original_function(*args,**kwargs)
    return wrapper_function


# class decorator_class(object):
#     def __init__(self,original_function):
#         self.original_function = original_function
#     def __call__(self,*args,**kwargs):
#         print(f'call method has executed this before {self.original_function.__name__}')
#         return self.original_function(*args,**kwargs)    
@decorator_function
def display():
    print('original_function ran')
display()
# decorated_display = decorator_function(display)
# decorated_display()
@decorator_function
def display_info(name,age):
    print(f'hey my name is {name} and my age is {age}')

display_info('john',20)