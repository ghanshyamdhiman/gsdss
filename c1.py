import calendar  
import datetime

    
yy = 2020
mm = 12

the_cal = calendar.TextCalendar(calendar.SUNDAY)
cal_display = the_cal.formatmonth(2020,11)
# display the calendar  
print(calendar.month(yy, mm))  
print(cal_display)
#print(the_cal.today())

week_days = the_cal.iterweekdays()


def print_time(r_time):
  return datetime.datetime(r_time)

the_time = [2020,12,29]

print(print_time(the_time))