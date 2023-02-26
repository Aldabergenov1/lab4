import datetime

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

d = datetime.date(year, month, day)

year1 = int(input('Enter a year: '))
month1 = int(input('Enter a month: '))
day1 = int(input('Enter a day: '))

d1 = datetime.date(year1, month1, day1)

delta = d1 - d

print(f"Time difference is {delta.total_seconds()} seconnd")

