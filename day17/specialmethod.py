
class employee:
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (f'{first}{last}@company.com')
    def full_name(self):
        return(f'{self.first} {self.last}')
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # __repr__
    #_str__    

    def __repr__(self):
        return (f"employee('{self.first}','{self.last}',{self.pay})")
    def __str__(self):
        return (f"{self.first} - {self.email}")
    # __add__
    def __add__(self , other):
        return (self.pay + other.pay)
        
emp_1 = employee('ishita','khatri',54000)
emp_2 = employee('akshat','khatri',50000)

emp_1.raise_amount = 1.05#only changing for emp_1

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(employee.raise_amount)
print(repr(emp_1))
print(str(emp_1))
print(emp_1 + emp_2)