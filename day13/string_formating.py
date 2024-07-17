#creating a dictionary 
employee = {'name':'john','age':29,'job':'software engineer'}

print('hey! there myself {0},also my age is {1} and i am a {2}'.format(employee['name'],employee['age'],employee['job']))

#another method 

print('hey! there myself {0[name]},also my age is {0[age]} and i am a {0[job]}'.format(employee))

#for list 

l = ['john',29,'software engineer']

print('hey! there myself {0[0]},also my age is {0[1]} and i am a {0[2]}'.format(l))

#now creating an object 

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person('jack',30)

print('hey! there myself {0.name} and also my age is {0.age}'.format(p1))

# print(f"hey my name is {p1.name} and my age is {p1.age}")




