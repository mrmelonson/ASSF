#Base classes for enemies
from stuff import printing
import random, index
class Enemy():
    
    enemyCount = 0

    flavour = [" strikes ", " hits ", " violently pushes ", " baps ", " uppercuts ", " bites ", " kicks "]

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.enemyCount += 1 

    def Deal(self, counter):
        damage = self.damage
        if counter:
            if random.randint(1,2) == 1:
                self.Take(True)
                return
            else:   
                damage = damage * 1.5
                printing.Print("You mess up the counter")

        index.player.health = index.player.health - damage
        printing.PrintHitByEnemy(self.name + self.flavour[random.randint(0,len(self.flavour) - 1)] + index.player.name + " for " + str(damage))
        if index.player.health < 0:
            index.player.HasDied()
    
    def Take(self, counter):
        damage = index.player.attack
        crit = index.player.Crit()
        if crit != 1:
            printing.PrintHitByPlayerCrit("Critical! 2x damage!")
            damage = damage * crit
        if counter:
            damage = damage * 2
            printing.PrintHitByPlayer(self.name +  " tries to attack but " + index.player.name + " counters " + self.name + " for " + str(damage))
        else:
            printing.PrintHitByPlayer(index.player.name + self.flavour[random.randint(0,len(self.flavour) - 1)] + self.name + " for " + str(damage))
        self.health = self.health - damage





