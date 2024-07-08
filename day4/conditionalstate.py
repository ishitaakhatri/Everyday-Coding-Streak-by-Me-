if True:

 print("the value is true")
#conditional statemenets
language='python'
if language=='python':
 print("yes the language is python") 
#other statemenets
x=10
y=20
if x>y:
 print("x is greater than y")
if x>=y:
 print("x is greater than equal to y")
if x<y:
 print("x is less than y")  
if x<=y:
 print("x is less than equal to y") 
if x==y:
 print("x is equal to y")   
if x!=y:
 print("x is not equal to y") 
#if-else statements
name='babyishita'
if name=='ishita':
 print("name is ishita")
else:
 print("name not fount") 
#elif statements
food="egg"
if food=="veggie":
 print("the food found is a veggie")
elif food=="fruit":
 print("the food found is a fruit")
elif food=="egg":
 print("the food fount is an egg....!!!!yeeeyyyyy") 
else:
 print("no match")   
#and/or/not
user='admin'
logged_in=True
if user=='admin' and logged_in:
 print("user is valid")
else:
 print("user is invalid")
 #or statement
print("trying with or") 
user='admin'
logged_in=True
if user=='admin' or logged_in:
 print("user is valid")
else:
 print("user is invalid")
#not statement
if not logged_in:
 print("please login")
else:
  print("welcome")
#id checking by (is)
a=[1,2,3]
b=[1,2,3]
print(a == b)
print(id(a))
print(id(b))
print(a is b)
