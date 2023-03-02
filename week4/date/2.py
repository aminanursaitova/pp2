import datetime

x = datetime.timedelta(1)
y = datetime.date.today()
print("Yesterday: ", y-x, "\n", "Yoday: ", y, "\n", "Yomorrow: ", y+x, sep="")