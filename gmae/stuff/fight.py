#Patrick Fennell z5218631
#base for fighting

from stuff import printing, explore
from stuff import enemy as enemypg
import random, index

def Fight(name, health, damage):
    enemy = enemypg.Enemy(name, health, damage)

    printing.Print("A wild " + enemy.name + " has appeared!")

    while enemy.health > 0:
        choice = ''

        printing.PrintHitByPlayer("Your health is " + str(index.player.health))
        printing.PrintHitByEnemy(enemy.name + "'s health is " + str(enemy.health))

        printing.PrintOpt("Attack")
        printing.PrintOpt("Counter")
        printing.PrintOpt("Run")

        choice = input().lower()

        if choice == "attack":
            enemy.Take(False)
            enemy.Deal(False)
        elif choice == "counter":
            enemy.Deal(True)
        elif choice == "run":
            printing.Print("You try to make a break for it...")
            if CanRun():
                Run()
            else:
                printing.Print("The " + enemy.name + " catches up to you")
                enemy.Deal(False)
        else:
            printing.Print("You stumble giving the " + enemy.name + " a chance to attack")
            enemy.Deal(False)
    printing.Print("You defeated the " + enemy.name)
    explore.Idle()

def CanRun():
    if random.randint(1,5) == 1:
        return True
    else:
        return False
            
def Run():
    printing.Print("You manage to lose them")
    printing.Print("you rest for a little bit after running so far and for so long")
    explore.Idle()



