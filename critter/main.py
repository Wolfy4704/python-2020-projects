#critter
#12/20
#Brayden Woodard

import random

class Critter(object):
    days = 0
    hours = 0

    def __init__(self):
        self.age = 0
        self.health = 100
        self.hunger = 0
        self.weight = 0
        self.height = 0
        self.name = ""
        self.happy = 100
        self.isAlive = True

    def setName(self,name):
        if len(name) > 4 or len(name) < 4:
            if "uck" not in name:
                if "sh" not in name:
                    if "unt" not in name:
                        self.name = name

    def die(self):
        self.isAlive = False

    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getWeight(self):
        return self.weight
    def getHeight(self):
        return self.height
    def getHappy(self):
        return self.happy
    def getHunger(self):
        return self.hunger
    def getisAlive(self):
        return self.name

    def intro(self):
        print("hello my name is "+self.getName())

    def feed(self,food):
        if food == "pizza":
            self.hunger -= 12
        elif food == "cheese burger":
            self.hunger -= 18
        elif food == "steak":
            self.hunger -= 25
        elif food == "taco":
            self.hunger -= 5
        elif food == "cheesecake":
            self.hunger -= 100
        elif food == "abes left arm":
            self.hunger -= 7002
            self.die()
        else:
            self.hunger -= 10

    def pass_time(self, hours):
        for i in range(hours):
            self.hunger += 5
            if self.hunger > 50
                self.weight -=.5
                self.happy -= 15
                self.health -= 5
            if self.hunger < 0:
                self.weight += .5
                self.happy += 15
                self.health -= 2
            self.happy -= 5
            self.height += .01
            Critter.hours+=1
            if hours == 5:
                Critter.day+=1
                Critter.hours=0
            if Critter.days %10 == 0:
                self.age+=1
            if self.age >= 99:
                chance = random.randint(5)
                if chance == 0:
                    self.die()
    def play(self, time):
        self.pass_time(self, time)
        self.happy += 10 * time
        self.health += 2 * time
        if self.health > 100:
            self.health = 100
            if self.happy > 100:
                self.happy = 100

    def hud(self):
        print("Pet name: "+self.getName())
        print("Pet height: " + self.getHeight())
        print("Pet weight: " + self.getWeight())
        print("Pet age: " + self.getAge())
        health = self.getHealth()
        elif health > 80:
            print("health: great")
        elif health > 60:
            print("health: good")
        elif health > 50:
            print("health: fair")
        elif health == 0:
            self.die()
        else:
            print("health: poor")

        hunger = self.getHunger()
        if hunger > 40:
            print("hunger: starving")
        elif hunger > 20:
            print("hunger: really hungry")
        elif hunger > 410:
            print("hunger: full")
        else:
            print("hunger: hungry")
        if hunger == 100:
            self.die()
        if hunger == -100:
            self.die()

        happy = self.gethappy()
        if happy > 50:
            print("Happy: happy")
        elif happy > 35:
            print("happy: grumpy")
        else:
            print("happy: pissed off")





def main():

main()