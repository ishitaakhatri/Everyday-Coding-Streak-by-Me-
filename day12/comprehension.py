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