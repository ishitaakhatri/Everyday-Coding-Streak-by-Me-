def square(x):
    return x * x
f = square 
print(square(5))
print(square)
print(f)#fucntion square is now being copied in variable f 

#now coping the square fucntion to another function 

def my_map(func,arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square,[1,2,3,4,5])

print(squares)
