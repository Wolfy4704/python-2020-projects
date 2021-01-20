#Verification function
#01/21
#Brayden Woodard

import datetime

def get_int(prompt, min, max):
    while True:
        try:
            input_string = input(prompt)
            input_int = int(input_string)  #for some reasom put input instead of int and sat here screaming at why i couldnt find the problem for 20 minutes then remembered the solution giude and im upset at how dumb of a mistake that was

            if(input_int >= min) and (input_int <= max):
                return input_int
            else:
                print("try again - ", end="")
        except:
            print("try again - ", end="")






month = get_int("enter todays month (1-12): ",1,12)
day = get_int("enter todays day (1-31): ",1,31)
year = get_int("enter todays year (2000-3000): ",2000,3000)

today = datetime.date(year,month,day)
print("today is a " + today.strftime("%A"))