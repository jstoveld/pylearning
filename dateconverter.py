import numpy as np
from datetime import datetime



#prints original date at time of call
original_date = datetime.now().strftime("%Y-%m-%d, %H:%M")
print("Current Time is now: " + str(original_date))


#sets our values to usable days, months and years
cdate=datetime.now()

day = cdate.strftime("%d")
month = cdate.strftime("%m")
year = cdate.strftime("%Y")
hour = cdate.strftime("%H")
minute = cdate.strftime("%M")

print("Date:",cdate.strftime("%d"))
print("Month:",cdate.strftime("%m"))
print("Year:",cdate.strftime("%Y"))
print("Hour:",cdate.strftime("%H"))
print("Minute:",cdate.strftime("%M"))



#takes our day and adds +1
day = int(day)+1
print("Tomorrow will be day: " + str(day))

#adds a minute
minute = int(minute)+1
print("In one minute it will be: " + str(minute))

#European format
euro_format = datetime.now().strftime("%d.%m.%Y")
print("Todays date in EU format is: " + str(euro_format))

#UK Format
uk_format = datetime.now().strftime("%d/%m/%Y")
print("Todays date in UK format is: " + str(uk_format))

#JPN Format
jpn_format = datetime.now().strftime("%Y/%m-%d")
print("Todays date in JPN format is: " + str(jpn_format))


#extract minutes
print ("We are in minute " +str(minute)+ " of the hour.") 


#2 days and a minute earlier
#not sure I understand this math below...
two_days_earlier = (int(day)-3)
one_minute_earlier = (int(minute)-2)
print("Two days and a minute earlier would be: "+str(month) +"/" +str(two_days_earlier) +"/" + str(year) + " " + str(hour) +":" +str(one_minute_earlier))



# # 2010-10-23 convert this into a datetime object
date_str = "2010-10-23"
dt_object = datetime.strptime(date_str, "%Y-%m-%d")
print("Date:", dt_object.date())
print(type(dt_object))



# def add_a_day():
#     day_plus_one = int(day) + 1
#     return day_plus_one
#     print(day_plus_one)
    
# add_a_day()


# add a day and print
# add a minute and print
# convert to euro format and print dd.mm.yyyy
# convert to UK standard and print dd/mm/yyyy
# convert to japanese standard and print yyyy/mm.dd
# extract minutes
# subtract 2 days and 1 minute
# 2010-10-23 convert this into a datetime object
