# Student name

import datetime

# Define the get_verified_integer function
def get_verified_integer(prompt, min, max):

  # loop until correct input received
  while True:
    try:
      inputString = input(prompt)  # get user input
      inputInt = int(inputString)  # try to convert to int

      if (inputInt >= min) and (inputInt <= max):  # verify range
        return inputInt            # success!
      else:
        print("Try again - ",end="")   # bad input - try again
    except:
        print("Try again - ",end="")   # bad input - try again

# main program starts here
month = get_verified_integer("Please enter today's month (1-12): ",1,12)
day   = get_verified_integer("Please enter today's day (1-31): ",1,31)
year  = get_verified_integer("Please enter today's month (2000 - 2030): ",2000,2030)

# build date object and print out the day of the week
today = datetime.date(year,month,day)
print("Today is a " + today.strftime("%A"))