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

    @classmethod
    def set_raise_rate(cls,amount):
        cls.raise_amount = amount
    @staticmethod
    def working_day(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True
    
emp_1 = employee('ishita','khatri',54000)
emp_2 = employee('akshat','khatri',50000)

# emp_1.raise_amount = 1.05#only changing for emp_1
employee.set_raise_rate(1.05)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(employee.raise_amount)

import datetime

my_date = datetime.date.today()
print(employee.working_day(my_date))