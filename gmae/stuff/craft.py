#Patrick Fennell z5218631
#Base for crafting

from stuff import printing, explore
import index
def CanCraft():
    if index.player.inventory['wood'] >= 2:
        return True
    else:
        return False

def Crafting():
    choices = []
    choice = ""

    printing.Print("You decide to craft a...")
    if index.player.inventory['wood'] >= 2:
        printing.PrintOpt("Torch")
        choices.append("torch")

    printing.PrintOpt("Back")
    choices.append("back")
    
    choice = input()
    choice = choice.lower()
    if choice in choices:
        if choice == "torch" and "torch" in choices:
            Craft("torch")
        elif choice == "back":
            explore.Idle()
        else:
            Crafting()

def Craft(item):
    item = item.lower()
    printing.Print("You crafted a " + str(item))
    if item == "torch":
        index.player.inventory['wood'] = index.player.inventory['wood'] - 2
        index.player.AddToInv("Torch", 1)
        
    explore.Idle()
    

        
    
    
        
        




