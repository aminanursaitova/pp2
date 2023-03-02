import datetime
def difference(dt2, dt1):
  datetime.timedelta = dt2 - dt1
  return datetime.timedelta.days * 24 * 3600 + datetime.timedelta.seconds

def ed():
  y = int(input("Enter your date's year in format YYYY:"))
  m = int(input("Enter your date's month in format M:"))
  d = int(input("Enter your date's day in format D:"))
  return (datetime.datetime(y, m, d))

date1 = ed()
date2 = ed()
print("The difference between given dates in seconds is: " (difference(date2, date1)), sep= "")
print()
