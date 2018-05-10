#patrick Fennell z5218631
#12/04/18
#A small snowy forest
#made in python 3

from stuff import player as playerpg, printing, explore

printing.PrintTitle()
printing.Print("You wake up, your head is hurting and you are cold")
printing.Print("You struggle to remember your own name..")

name = input()
player = playerpg.Players(name)

printing.Print("Thats right it's " + player.name)
printing.Print("You look around")
printing.Print("Nothing but trees and snow")

#fight.Fight("Wolf", 20, 2)

answer = ''

while answer != 'y' and answer != 'n':
    printing.PrintOpt("Should you go exploring? (y/n)")
    answer = input()

if answer == 'y':
    explore.Explore()
else:
    explore.Idle()





