#  def square(num):
#     # result=[]
#     for n in num:
#          yield(n*n)
#     # return result

my_num =(n*n for n in [1,2,3,4,5]) #square([1,2,3,4,5])
print(list(my_num))

# for i in my_num:
#      print(i)
