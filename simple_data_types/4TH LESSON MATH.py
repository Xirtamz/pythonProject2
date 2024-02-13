# import math                           #MATH
#
#
# x = 90
# print(math.sin(math.radians(x)))        #smena uglov na radian

# import calendar
# print(calendar.month(2024, 2, w=1, l=1)) #w-width l-lengh
#
# print(calendar.calendar(2024, c=5, m=4)) #c-difference between m-amount in 1 line\
# print(calendar.weekday(2024, 2, 8)) #day of the week
# print(calendar.isleap(2024))
# print(calendar.isleap(2023))
# print(calendar.isleap(2022))
# print(calendar.isleap(2021))

# print(calendar.leapdays(2000, 2024))

# import time                           #TIME

# start = time.time()
# # print(start)
# # time.sleep(3)       #ot4et nazad
#
# stop = time.time()
#
# print(stop - start)

# print(time.gmtime().tm_year) #vozvrat goda
# print(time.localtime())
# print(time.asctime())


import datetime                                             #DATETIME
#
d = datetime.date(2024, 5, 9)
# print(d.replace(day=15))
#
# print(d.isoweekday())
# print(d.weekday())
#
today = datetime.date.today()
# print(today)                #str
# print(repr(today))
# print(repr(math.sin))

# print(d - today)
#
tdelta = datetime.timedelta(days=7, hours=28)
# print(today + tdelta)
x = 1707412314
#
print(tdelta.total_seconds())
print(x - tdelta.total_seconds())

# t = datetime.time(18, 23, 42)
# print(t)
# t2 = datetime.time(23, 10, 32)
# print(t)

# dt = datetime.datetime(2024, 3, 16, 17, 12, 33)
# print(dt)
# print(type(dt))
#
# print(dt.date())
# print(dt.time())

# tdelta = datetime.timedelta(days=3,  hours=20)
# print(dt - tdelta)
# print((datetime.datetime.today() + tdelta).time())
# print(dt.timestamp())
# new_date = datetime.datetime.fromtimestamp(1710601953)
# print(new_date)


# dt = datetime.datetime.today()
# print(dt.strftime('%A %d ==-===- %B'))              # in between write anything
# # print(datetime.datetime.strftime())
# date = 'November 12 2023 18:22'
# new_date = datetime.datetime.strptime(date, '%B %d %Y %H:%M')
# print(new_date)

# date = date.replace('Juuli', 'July')    # change language diffs

