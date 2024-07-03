#creating a list
courses= ['maaths','physics','chemistry','biology']
print(courses)
#finding length
print(len(courses))
#indexing
print(courses[2])
print(courses[-1])
#slashing
print(courses[1:3])#not including the last element
#modifying the list
#adding element
courses.append('art')#adding the element the the last
print(courses)
#to a specific location
courses.insert(2,'psychology')
print(courses)
#adding multiple values
courses_2=['compsci','english']
courses.extend(courses_2)
print(courses)
#what if we use append
courses.append(courses_2)
print(courses)
#what if we use insert
courses.insert(3,courses_2)
print(courses)
#removing elements
courses.remove(courses_2)
print(courses)
#removing from last
courses.pop()
print(courses)
#reverse a string
courses.reverse()
print(courses)
#sorting the list
courses.sort()
print(courses)#in alphabetical order
#for number list
numbers=[2,5,9,1,6]
numbers.sort()#by default ascending order
print(numbers)
#what if we want in decending
numbers.sort(reverse=True)
print(numbers)
courses.sort(reverse=True)
print(courses)
#if we don't want to alter the original list
sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)
#min,max,sum
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(min(courses))
print(max(courses))
#finding a value
print(courses.index('english'))
print('psychology'in courses)
print('stats'in courses)
#looping values
for item in courses:
 print(item)#here item takes on the value that is equal to length of the list
 #item here is just a variable
 #for getting index along use enumerate
for index,item in enumerate(courses):
 print(index,item) 
#starting from a specific element 
for index,item in enumerate(courses,start=2):
 print(index,item)

#converting list to string 
str = ', '.join(courses)  
print(str)
print(len(str))


 
#TUPLES
#
#
#
#can't modify tuples
names = ('ram','shyam','ellie')
print(names)
#names[0] = 'ishita'
#looping
for item in names:
 print(item)



#SETS
fruits = {'apple','banana','dragonfruit','kiwi','lichi','pomogranet','apple'}#it don't care about order
print(fruits)
#don't care about duplicate

#finding common elements
winter_fruits = {'apple','banana','kiwi','pear','orange'}
print(fruits.intersection(winter_fruits))
#difference
print(fruits.difference(winter_fruits))
#union
print(fruits.union(winter_fruits))
