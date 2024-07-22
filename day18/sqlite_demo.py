import sqlite3
from employee_file_sqlite import Employee 

conn = sqlite3.connect(':memory:')#for storing in memory use (:memory:) and for storing in file use extension .db
# creating a curser
def insert_emp(emp):
    with conn:
       c.execute("INSERT INTO employee (first, last, pay) VALUES (?, ?, ?)", (emp.first, emp.last, emp.pay))

def get_emps_by_name(lastname):
    with conn:
     c.execute("SELECT * FROM employee WHERE last = ?", (lastname,))
     return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employee SET pay = :pay
                     WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
     c.execute("DELETE FROM employee WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

c = conn.cursor()
emp_1 = Employee('john','doe',80000)
emp_2 = Employee('jane','scharef',80000)

c.execute("""CREATE TABLE employee(
          first text,
          last text,
          pay integer
          )""")

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('doe')
print(emps)

conn.close()