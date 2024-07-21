class employees :
    def __init__(self,first,last):
        self.first =  first
        self.last =  last
    @property#even if ther are methods still we can call them as attributes in an object 
    def email(self):
        return(f"{self.first}.{self.last}@companyname.com")
    @property
    def fullname(self):
        return(f"{self.first}-{self.last}") 
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ') 
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('delete names')
        self.first = None
        self.last = None    
    
emp_1 = employees('john','smiths')
emp_2 = employees('sam','builder')
emp_1.first = 'james'
emp_1.fullname = 'maxi swift'
print(emp_1.first)
print(emp_1.email)
print(emp_1.last)
print(emp_1.fullname)
del emp_1.fullname
        