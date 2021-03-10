#Write a Python program to calculate the number of days between two dates.

from  datetime import date,timedelta
sdate = date(2015-9-25) #starting date
edate = date(2025,9,25)#Ending date
diffrence = edate - sdate #caluculate the no. of dates between sdate and edate
for i in range(diffrence.days):
    day = sdate + timedelta(days=i)
    print(day)
