num = [1,2,3,4,5,6,7,8]
#by using loops
# new_list = []

# for n in num:
#      new_list.append(n*n)

# print(new_list)

#by comprehension

new_list = [n*n for n in num] 

print(new_list)

#i want 'n' for each 'n' in nums if n is even 

# new_list = []
# for n in num:
#     if(n%2==0):
#         new_list.append(n)

# print(new_list)

#now using comprehension 

new_list = [n for n in num if (n%2==0)]
print(new_list)

#another example 
my_list = [(letters,num) for letters in 'abcdefg' for num in range(4)]
print(my_list)

#dictionary comprehension 
names = ['ishita','akshat','tarak','mansi','dhol']
courses = ['aids','aids','aids','bsc','bca']
students = zip(names,courses)
# print(list(students))

# my_dict = {}
# for names,courses in students:
#     my_dict[names] = courses

# print(my_dict)  
my_dict = {names : courses for names,courses in students} 
print(my_dict) 

#set comprehension 

numbers = [1,1,1,2,3,3,4,4,4,4,4,5,5,6,7,7,7,7]
# my_set = set()
# for n in  numbers:
#     my_set.add(n)
# print(my_set)

my_set = {n for n in numbers}
print(my_set)    