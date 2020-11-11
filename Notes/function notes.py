import datetime

def get_day_of_week(target) :
    try:
        thisdate = datetime.datetime.strptime(target,"%Y-%m-%d")
        dayofweek = thisdate.strftime("%A")
        return dayofweek
    except:
        return "invalid YYYY-MM-DD date"


print(get_day_of_week("2004-04-07"))
