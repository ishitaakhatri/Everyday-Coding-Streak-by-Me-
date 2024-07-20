class employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = (f'{first}{last}@company.com')
    def full_name(self):
        return(f'{self.first} {self.last}')
emp_1 = employee('ishita','khatri')
emp_2 = employee('akshat','khatri')

print(emp_1.email)
print(emp_2.email)
print(emp_1.full_name())
