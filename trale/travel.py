#travel function
health = "good"
pace = "normal"
weather = "comftorable"
def travel (health, pace, weather):
    import random
    mph = 0
    weather_mod = 0
    hours = 0

    
    if pace == "normal":
        mph = 2
    elif pace == "slow":
        mph = 1
    elif pace == "fast":
        mph = 4

    if health == "bad":
        hours = 4
    elif health == "good":
        hours = 8
    elif health == "decent":
        hours = 6

    if weather == "blizzard":
        weather_mod = 0
    elif weather == "hot":
        weather_mod = .5
    elif weather == "rain":
        weather_mod = .25
    elif weather == "comftorable":
        weather_mod = 1

    miles = hours * mph * weather_mod
    random_mod = random.randint(0,5)
    return miles - random_mod

miles = travel(health, pace, weather)
print(miles)
