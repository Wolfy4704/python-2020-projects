#Getting the Day of the Week
#01/21
#Brayden Woodard

import datetime

def get_day_of_week(target):
    try:
        this_date = datetime.datetime.strptime(target, "%Y-%m-%d")
        day_of_week = this_date.strftime("%A")
        return day_of_week

    except:
        return "invalid YYYY-MMM-DD date"




print(get_day_of_week("2021-01-10"))
print(get_day_of_week("1776-07-04"))
print(get_day_of_week("1918-11-11"))
print(get_day_of_week("3-16-2001"))
