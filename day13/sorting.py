#sorted fucntion and sort fucntion 

li = [9,5,7,2,4,6,3,1,8]
#what if we want that to be sorted in reverse order 
s_li = sorted(li,reverse=True)#here returning the sorted list and not making any change in the original 
print('original_list:',li)
print('sorted_list:',s_li)

li.sort(reverse=True)#here the function is returning none and sorting the original list 

print('original_list after using sort:',li)

#for tuples we can not use sort() we can only use sorted 
tup = (9,5,7,2,4,6,3,1,8)
s_tup = sorted(tup)
print(s_tup)

#same for dictionary(only sorting the keys) 

dictionsry = {'name':'john','job':'software developer','age':29,'os':'mac'}
s_dictionary = sorted(dictionsry)
print('sorted dictionary is:',s_dictionary) 

#sorting the abs values by using the key parameter 

num = [-6,-4,-1,2,3,4,5]

s_num = sorted(num,key=abs)

print(s_num)

