#Patrick Fennell z5218631
#base for locations in the game

import random
from stuff import printing, craft, fight

def Explore(player):
    num = random.randint(0,10)
    printing.Print("You walk around for a bit")
    if num == 6:
        printing.Print("You come across a small river")
        printing.Print("You cant see a way across and it's too cold to swim")
        River()
    elif num == 7:
        printing.Print("you come across a strange rock...")
        printing.Print("On closer inspection it is just a normal rock")
        Idle()
    elif num == 5 or num == 4:
        printing.Print("You stumble across a small cave")
        printing.Print("It looks dark inside")
        if "torch" in player.inventory:
            printing.Print("Explore cave?")
        else:
            printing.Print("Hmm, it looks too dark to explore")
            printing.Print("Maybe if you had a torch...")
            Idle()
    elif num == 8:
        fight.Fight("Wolf", random.randint(20,25), random.randint(2,5))
    else:
        printing.Print("You find nothing of interest")
        printing.Print("You seem more lost now...")
        Idle()

def CollectWood():
    printing.Print("You go to collect wood")
    printing.Print("Amazingly in a forrest of trees you find some!")
    index.player.AddToInv("wood", random.randint(1,3))
    Idle()

def Idle():
    choice = ""
    choices = []
    printing.Print("You are idle")
    printing.Print("What would you like to do?")

    if (index.player.inventory['wood'] > 2) == False:
        printing.PrintOpt("Collect wood")
        choices.append("collect wood")

    if craft.CanCraft():
        printing.PrintOpt("Craft")
        choices.append("craft")

    printing.PrintOpt("Explore")
    choices.append("explore")

    printing.PrintOpt("Check inventory (inv)")
    choices.append("inv")
    
    choice = input()
    choice = choice.lower()
    if choice in choices:
        if choice == "collect wood" and "collect wood" in choices:
            CollectWood()
        elif choice == "explore" and "explore" in choices:
            Explore()
        elif choice == "inv":
            index.player.CheckInv()
            Idle()
        elif choice == "craft" and "craft" in choices:
            craft.Crafting()
        else:
            Idle()
    else:
        Idle()

def River():
    choice = ''

    while choice != 'y' and choice != 'n':
        printing.PrintOpt("Investigate river? (y/n?)")
        choice = input() 

    if choice == 'y':
        printing.Print("You walk down closer to the river")
        printing.Print("You see a pebble")

        choice = ''

        while choice != 'y' and choice != 'n':
            printing.PrintOpt("Pick up pebble? (y/n?)")
            choice = input() 

        if choice == 'y':
            printing.Print("You decide to pick up the pebble")
            index.player.AddToInv("pebble", 1)
        else:
            printing.Print("You do not need a pebble at this time")

        printing.Print("you investigate a bit further...")
        if random.randint(1,3) == 3:
            printing.Print("You see somthing shiny in the water...")
            printing.Print("Wow you found some gold coins!")
            index.player.AddToInv("gold coin", random.randint(1,5))
        else:
            printing.Print("you don't find anything of interest")
        Idle()        
    else:
        printing.Print("You decide to turn back")
        Idle()

def Cave():
    choice = ''

    while choice != 'y' and choice != 'n':
        printing.PrintOpt("Investigate Cave? (y/n?)")
        choice = input() 

    if choice == 'y':
        printing.Print("You light the torch and head inside")
        
    else:
        Idle()

