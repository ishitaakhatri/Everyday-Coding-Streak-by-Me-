def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func
 
my_msg = outer_func('hello')
#we can only pass arguments to the function but not to the variable but we can call the function by using the name of the varibale 

my_msg() 
        