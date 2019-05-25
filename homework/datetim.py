from datetime import datetime

today = datetime.today()
yesterday = today.replace(day=today.day-1)
month_ago = today.replace(month=today.month-1)
print(today)
print(yesterday)
print(month_ago)

some = '01/01/17 12:10:03.234567'
realDate = datetime.strptime(some,'%d/%m/%y %H:%M:%S.%f')
print(realDate, type(realDate))