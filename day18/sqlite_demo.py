import sqlite3
from employee_file_sqlite import Employee 

conn = sqlite3.connect(':memory:')#for storing in memory use (:memory:) and for storing in file use extension .db
# creating a curser
c = conn.cursor()
emp_1 = Employee('john','doe',80000)
emp_2 = Employee('jane','scharef',80000)

c.execute("""CREATE TABLE employee(
          first text,
          last text,
          pay integer
          )""")

c.execute("INSERT INTO employee(first,last,pay) VALUES ('ishita','khatri','50000')")
c.execute(f"INSERT INTO employee(first,last,pay) VALUES ('{emp_1.first}','{emp_1.last}','{emp_1.pay}')")
conn.commit()
c.execute(f"INSERT INTO employee(first,last,pay) VALUES ('{emp_2.first}','{emp_2.last}','{emp_2.pay}')")
conn.commit()
c.execute("SELECT * FROM employee WHERE last = 'khatri'")
print(c.fetchall())
c.execute("SELECT * FROM employee WHERE last = ?",('scharef',))
print(c.fetchall())
c.execute("SELECT * FROM employee WHERE last = ?",('doe',))
print(c.fetchall())

conn.commit()

conn.close()