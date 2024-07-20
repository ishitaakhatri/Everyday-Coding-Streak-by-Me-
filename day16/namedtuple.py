from collections import namedtuple
# variable = namedtuple('name of tuple',[elements of tuple])
colour = namedtuple('colour',['red','blue','green'])
colour = colour(55,66,77)
white = colour(255,655,755)
print(white.blue)