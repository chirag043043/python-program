import datetime
from datetime import timedelta
day=int(input('Enter day:'))
month=int(input('Enter month:'))
year=int(input('Enter year:'))
d=datetime.date(year,month,day)
print("date before 10 weeks",(d-timedelta(weeks=10)).strftime("%d-%m-%Y"))
print("date after 20 weeks",(d+timedelta(weeks=20)).strftime("%d-%m-%Y"))
