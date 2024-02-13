"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""
import datetime

# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'
#
# date = sample1.replace('Jan', 'January')
# sample1_date = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p')
# print(sample1_date)
# sample2_date = datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d')
# print(sample2_date)
# sample3_date = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
# print(sample3_date)
# sample4_date = datetime.datetime.strptime(sample4, '%d. %m.%Y - %H:%M:%S')
# print(sample4_date)






# Write a program to print yesterdays, today and tomorrow dates
# today = datetime.date.today()
# tdelta = datetime.timedelta(days=1)
# print(today - tdelta)
# print(today)
# print(today + tdelta)


# Write a program to convert given timestamp to dd.mm.yyyy format
# some_day = 1014163200
# new_date = datetime.datetime.fromtimestamp(some_day)
# new_formated_date = new_date.strftime("%d/%m/%Y")
# print (new_formated_date)

# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)


# def two_weeks_ago(ts):
#     dt = datetime.datetime.fromtimestamp(ts)
#     tdelta = datetime.timedelta(days=14)
#     new_dt = dt - tdelta
#     new_ts = new_dt.timestamp()
#     return new_ts
#
# print(two_weeks_ago())
# print(datetime.datetime.fromtimestamp(two_weeks_ago()))
