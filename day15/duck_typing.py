class duck:
    def quack(self):
        print('quack , quack')
    def fly(self):
        print('flap,flap!')

class person:
    def quack(self):
        print("i'm quacking like a duck...")
    def fly(self):
        print("i'm flying like a duck")


def quack_and_fly(thing):
    # if isinstance(thing,duck):#if this thing is an instance of duck or not 
    #     thing.quack()
    #     thing.fly()
    #     print()
    # else:
    #     print("that must be a duck")


    # asking for permission
#  if hasattr(thing,'quack'):#checking if the particular object have this quack method in it and if it has 
#      if callable(thing.quack):#check if it is callable or not 
#          thing.quack()
#  if hasattr(thing,'fly'):
#      if callable(thing.fly):
#          thing.fly()

# asking for forgivness   
 try:
    thing.quack()
    thing.fly()
    thing.bark()
 except AttributeError as e:
     print(e)      

d=duck()
quack_and_fly(d)
p=person()
quack_and_fly(p)