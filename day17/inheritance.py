class employee:
    # raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (f'{first}{last}@company.com')
    def full_name(self):
        return(f'{self.first} {self.last}')
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
class developers(employee):
    raise_amount=1.08
    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first, last, pay)#these attributes are being handled by employee class
        self.prog_lang =  prog_lang

dev_1 = developers('ishita','khatri',54000,'python')
dev_2 = developers('akshat','khatri',50000,'java')

# dev_1.raise_amount = 1.05#only changing for emp_1
print(dev_1.pay)
print(dev_1.raise_amount)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)