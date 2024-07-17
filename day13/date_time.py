import datetime

d = datetime.date(2016, 7, 24)
t_dy = datetime.date.today()
print(d)
print(t_dy.weekday())

#time delta 

tdelta = datetime.timedelta(days=6)
date = t_dy + tdelta
print(t_dy + tdelta)
print(t_dy - tdelta)
print(date - t_dy)

#time (hours:minutes:seconds.miliseconds)

t = datetime.time(9,54,10,20000)
print(t)

#whole date-time 
dt = datetime.datetime(2012,3,24,12,3,8,3000)
print(dt)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utc = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utc)