import random
game1 = "Zelda link to the past"
game2 = "World of warcraft"
game3 = "warcraft 2/3"
game4 = "mario world"
game5 = "Starcraft /2"
game6 = "secrets of mana"
game7 = "Starwars battel front 2"
game8 = "Starwars KOTOR"
game9 = "Starwars KOTOR 2"
game10 = "minecraft"
game11 = "Zelda ocrt"
game12 = "Zelda nes"
game13 = "Mario Party 1-3"
game14 = "Contra nes"
game15 = "Crystalas nes"
game16 = "ESO"
game17 = "Oblivian"
game18 = "Skyrim"
game19 = "Zelda links awakening Remake"
game20 = "FF 7"
game21 = "Mario kart all of them"

top_games = [game1, game2, game3, game4, game5, game6, game7, game8, game9, game10,
             game11, game12, game13, game14, game15, game16, game17, game18, game19,
             game20, game21]

high_score = [443, 950, 1000, 410, 875, 600, 550, 500, 395, 380]

##print(top_games)
##print(len(top_games))
##
##print(max(high_score))
##print(max(top_games))
##
##print(min(high_score))
##print(min(top_games))

top_games.append("World of warcraft")
top_games.sort()
top_games.reverse()
top_games.insert(0,"Zelda link to the past")
top_games.insert(6,"Zelda link to the past")
##print(top_games.count("Zelda link to the past"))
##print(top_games.count("World of warcraft"))
num = top_games.index("Zelda link to the past",True)
game = top_games.pop(int(num))
num = top_games.index("Zelda link to the past",True)
game = top_games.pop(int(num))
##print(game)
##print(top_games.count("Zelda link to the past"))
newlist = top_games.copy()
top_games.clear()
##print(top_games)
##print(newlist)


points = 0
if len(newlist) >= 22:
    points+=25
    
else:
    points-=25

if not top_games:
    points+=10
else:
    points-=25

if "World of warcraft" in newlist:
    points+=10
else:
    points-=10

if newlist.count("Zelda link to the past") > 1:
    points-=5
else:
    points+=5
if newlist.index("Zelda link to the past") == 0:
    points+=25
else:
    points-=25
    
if newlist.count("World of warcraft") > 1:
    points+=25
else:
    points-=25

for i in newlist:
    if "Pokemon" in i or "pokemon" in i:
        points-=100
    if "Halo" in i or "halo" in i:
        points -=100
    if "fortnite" in i or "Fortnite" in i:
        points -=10000000000000000000000000000000000
    
print(points)

if points >= 90:
    print("letter grade:A")

elif points >= 80:
    print("letter grade:B")

elif points >= 70:
    print("letter grade:C")

elif points >= 60:
    print("letter grade:D")
else:
    print("letter grade:F")

##print(top_games[num])
##top_games.remove(int(num))


##top_games.remove("Zelda link to the past")
##print(top_games)
##print(len(top_games))



##numbers = []
##x = 0
##while x != 100:
##    numbers.append(random.randint(1000, 10000))
##    x+=1
##print(numbers)
##print(max(numbers))
##print(min(numbers))
##numbers.sort()
##print(numbers)
##numbers.reverse()
##print(numbers)



##x=0
##while x != len(high_score):
##    print("looping",x)
##    high_score [x] +=1000
##    x+=1
##print(high_score)
##y = 0             
##while True:
##    print(y)
##    y+=38742984742
##    if y > 10000000000000:
##        break
