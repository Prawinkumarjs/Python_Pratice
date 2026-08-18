from datetime import datetime,time,timedelta,date
from zoneinfo import ZoneInfo

# date and time at present
print(datetime.now())

# date of today
print(date.today())

# time
today = datetime.now()
print(today.time())

# time specific min
print(today.time().minute)

# time specific hrs
print(today.time().hour)

# time specific microsecond
print(today.time().microsecond)

# time specific second
print(today.time().second)

# only hr and min
print(today.time().hour ,":", today.time().minute)

# only hr and min using inbuilt
timezone = ZoneInfo('Asia/Kolkata')
now = datetime.now(tz=timezone)

print(datetime.strftime(now,"%H%M"))

# month in names and date
print(datetime.strftime(today,"%h%m"))

string = "2026-28-08"
formatdate = datetime.strptime(string,"%Y-%d-%m")
print(formatdate)

# date or time calculation for particular 
print(formatdate-datetime.now())

# date or time calculation for particular days only
print((formatdate-datetime.now()).days , " naal na naa ooruku poren")

# auto update of the date
print(today+timedelta(1))
print(today+timedelta(-1))

# replace the time
noww = today.replace(2003,12,3)
print(noww)

# calculation of today's and tommrow
todays = datetime.now()
tommorows = todays + timedelta(1)
tommorows = tommorows.replace(hour=0, minute=0, second=0, microsecond=0)
difference = tommorows-todays
print(difference)

# time zone for tokyo
timeZones = ZoneInfo("Asia/Tokyo")
tokyonow = datetime.now(tz=timeZones)
print(tokyonow)