import _datetime
from _datetime import datetime as dt

now = dt.now() #current Time
next = now + _datetime.timedelta(minutes = 5) #Add 5 mins

current_time = now.strftime("%H:%M:%S")
next_time = next.strftime("%H:%M:%S")

print("MPS updated at {}\nIt will update again at {}".format(current_time, next_time))