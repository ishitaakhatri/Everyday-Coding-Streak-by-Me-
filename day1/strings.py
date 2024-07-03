message = "hello world"
#printing the message 
print(message)
#finding the length
print(len(message))
#indexing
print(message[9])
#slashing
print(message[2:9],message[:5],message[6:])
#reversing a string
print(message[::-1])
#counting number of variables 
print(message.count('l'))
#to find the index
print(message.find('w'))
#replacing a word in string 
print(message.replace('world','universe'))
print(message.replace('l','q'))
#concatination of string
greeting = 'hello'
name = 'ishita'
print(greeting+ ', '+ name + '. '+'welcome!')
#another way for concatination
str = '{},{}.welcome'.format(greeting,name)
print(str)
#another way for concatination
str1 = f'{greeting}, {name}. welcome!'
print(str1)