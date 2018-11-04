from datetime import date
from datetime import*
from Utility import Utility
import time
import calendar

my_date = date.today()
current_Time = datetime.now().time()
day_Of_Week = calendar.day_name[my_date.weekday()]

helper = Utility()
arrival_Time = helper.getNextBusTime("Ellicott", current_Time)
print(arrival_Time)
difference = datetime.combine(date.today(), arrival_Time) - datetime.combine(date.today(), current_Time)

time = str(difference)
mins = int(time.split(":")[1])
hour = int(time.split(":")[0])
mins = hour * 60 + mins
print(f"Bus will arrive in {mins} mins")


