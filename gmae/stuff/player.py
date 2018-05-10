#functions and storage vars for player
import random

class Players():
    
    from stuff import printing

    health = 100
    maxhealth = 100
    attack = 5

    inventory = {'wood': 0,
            'pebble' : 0,
            'gold coin' : 0,
            'torch' : 0}
    
    def __init__(self, name):
        self.name = name

    def Heal(self):
        oldhealth = self.health
        self.health += 10
        if self.health > self.maxhealth:
            health = 100
        Players.printing.PrintHitByPlayer("You healed " + str(health - oldhealth) + " health")


    def AddToInv(self, item, amount):
        item = item.lower()
        self.inventory[item] = self.inventory[item] + amount
        Players.printing.PrintGain("You gained " + str(amount) + " " + str(item) + "!")

    def CheckInv(self):
        i = 0
        for key, value in self.inventory.items():
            if value < 1:
                pass
            else:
                Players.printing.PrintItem(key + " x " + str(value))
                i+=1
        if i < 1:
            Players.printing.Print("You are not carrying anything")

    def HasDied(self):
        Players.printing.Print("Well...")
        Players.printing.Print("Looks like you have died")
        Players.printing.Print("That sucks huh :/")
        exit()

    def Crit(self):
        if random.randint(1,4) == 4:
            return 2
        else:
            return 1

    def PrintStatus(self):
        Players.printing.PrintHitByPlayer("Your health is " + str(self.health)) 
        Players.printing.PrintHitByPlayer("Your attack is " + str(self.attack))

    