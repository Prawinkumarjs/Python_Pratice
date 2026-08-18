from datetime import datetime, time, timedelta, date
from zoneinfo import ZoneInfo


# ==========================================
# 1. CURRENT DATE AND TIME
# ==========================================

# Current date and time
print(datetime.now())

# Today's date only
print(date.today())

# Current time only
today = datetime.now()
print(today.time())


# ==========================================
# 2. ACCESSING TIME COMPONENTS
# ==========================================

# Current minute
print(today.time().minute)

# Current hour
print(today.time().hour)

# Current microsecond
print(today.time().microsecond)

# Current second
print(today.time().second)

# Only hour and minute
print(today.time().hour, ":", today.time().minute)


# ==========================================
# 3. strftime() AND strptime()
# ==========================================

# Current time in IST
timezone = ZoneInfo("Asia/Kolkata")
now = datetime.now(tz=timezone)

# Format: HHMM
print(datetime.strftime(now, "%H%M"))

# Month name + month number
print(datetime.strftime(today, "%h%m"))


# Convert string → datetime
string = "2026-28-08"

formatdate = datetime.strptime(string, "%Y-%d-%m")

print(formatdate)


# ==========================================
# 4. DATE / TIME CALCULATIONS
# ==========================================

# Difference between a particular date and now
print(formatdate - datetime.now())

# Difference in number of days
difference = formatdate - datetime.now()

print(
    difference.days,
    "naal na naa ooruku poren"
)


# Add one day
print(today + timedelta(1))

# Subtract one day
print(today + timedelta(-1))


# ==========================================
# 5. REPLACE DATE / TIME
# ==========================================

# Replace year, month and day
noww = today.replace(2003, 12, 3)

print(noww)


# ==========================================
# 6. CALCULATE TIME UNTIL TOMORROW
# ==========================================

todays = datetime.now()

# Tomorrow
tommorows = todays + timedelta(1)

# Set tomorrow to 00:00:00
tommorows = tommorows.replace(
    hour=0,
    minute=0,
    second=0,
    microsecond=0
)

# Difference between now and tomorrow midnight
difference = tommorows - todays

print(difference)


# ==========================================
# 7. TIME ZONES
# ==========================================

# Tokyo time
timeZones = ZoneInfo("Asia/Tokyo")

tokyonow = datetime.now(tz=timeZones)

print(tokyonow)