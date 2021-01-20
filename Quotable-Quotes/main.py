#quotable quotes 9.1
#01/21
#Brayden woodard

import random

def select_quote():

    quotes = ("My fake plants died because I did not pretend to water them - Mitch Hedberg", \
            "There cannot be a crisis next week.  My schedule is already full. - Henry Kissinger", \
            "Weather forecast for tonight: dark. - George Carlin", \
            "All generalizations are false, including this one. - Mark Twain", \
            "Why do they call it rush hour when nothing moves? - Robin Williams")
    num_quotes = len(quotes)
    index = random.randint(0,num_quotes)
    print(quotes[index])

    return select_quote

select_quote()
select_quote()



