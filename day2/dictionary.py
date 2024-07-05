students = {'name':"ishita",'age':"20",'courses':['python','javascript','dsa']}
print(students)
#printing the specific value
print(students['name'])
print(students['courses'])
print(students.get('age'))
#what if we print a value that doesn't exist
#print(students['page'])
#if we don't want an error 
print(students.get('page'))
#if we want a specific notation instead of none
print(students.get('pages','not fount'))
#adding a new value
students['phone']='666-666-6666'
print(students)
#updaing a value 
students['name']='akshat'
print(students)
#using update function
students.update({'name':'mansi','gamil':'mansi.-@gmail.com','phone':'000-000-0000'})
print(students)
#deleting a key
del students['phone']
print(students)
students.pop('courses')
print(students)
#length of dictionary
print(len(students))
#to know about keys
print(students.keys())
#to know the values
print(students.values())
#to know the items 
print(students.items())
#to loop through keys
for keys in students:
     print(keys)
#to loop through values
for values in students:
     print(values)
#to loop through items
for key,values in students.items():
    print(key,values)        

