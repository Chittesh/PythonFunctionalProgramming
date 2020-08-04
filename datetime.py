from Lib import datetime

x = datetime.datetime.now()

print(x)
#Year -moth - day - Time
#2020-08-04 15:36:06.407618

print(x.hour)           #15
print(x.day)            #4
print(x.minute)         #38
print(x.year)           #2020
print(x.month)          #8

some_day =datetime.datetime(2019, 12, 31)
# adding dates using time delta
print(some_day.day)         #31
time = some_day.time()
print(time)                 #00:00:00

#Adding dates using timedelta
new_day=some_day + datetime.timedelta(days=5)
print(new_day)              #2020-01-05 00:00:00
#adding weeks
new_day=some_day + datetime.timedelta(weeks=5)
print(new_day)              #2020-02-04 00:00:00







