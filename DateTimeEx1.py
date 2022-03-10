#Program (DateTimeEx1.py)
#Program to work with Date & Time
'''
#time()-function
import time;
sysdatetime = time.time();
print(sysdatetime);
'''

'''
#localtime()
import time;
currenttime = time.localtime(time.time());
print(currenttime);
#it gives struct_time as time-tuple with 9-values
'''

'''
#asctime()-function
import time;
formattedtime = time.asctime(time.localtime(time.time()));
print(formattedtime);
'''
'''
#calendar-module with month(year,month)
import calendar;
cal = calendar.month(2021,11);
cal = calendar.month(1947,8);
cal = calendar.month(2022,1);
print(cal);
'''

'''
#time module with altzone(Variable)
import time;
print(time.altzone);
'''

'''
#clock() from time-module
import time;
print(time.clock());
time.sleep(5);	#sleeps for 5 seconds
print(time.clock());
'''

'''
#ctime()
import time;
datetime = time.ctime();
print(datetime);
'''



'''
#ctime() with sleep()
import time;
print(time.ctime());
time.sleep(5);
print(time.ctime());
'''

'''
#digital-clock using ctime()
import time;
while True:
    print(time.ctime(),end="\t\r");
    time.sleep(1);
'''


'''
#timezone & tzname variables(time-module)
import time;
print(time.timezone);
print(time.tzname);
'''


#calendar module
import calendar;
#print(calendar.calendar(2020,2,1,6));
#print(calendar.calendar(2020,3,2,10));
#print(calendar.firstweekday());
#print(calendar.isleap(2021));
#print(calendar.isleap(2024));
#print(calendar.leapdays(2020,2030)); 

#print(calendar.month(2021,11,2,1));
#print(calendar.monthcalendar(2021,11));
#print(calendar.monthrange(2021,11));
#print(calendar.monthrange(2021,12));


#calendar.prcal(2021,2,1,6);
#calendar.prmonth(2021,11,2,1);

#calendar.setfirstweekday(6);
#print(calendar.firstweekday());
#calendar.prmonth(2021,11,2,1);

#print(calendar.weekday(2021,11,25)); 
gives weekday-code(0-6 mon-sun)