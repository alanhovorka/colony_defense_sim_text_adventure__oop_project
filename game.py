from player import Player
from armory import Armory
from kitchen import Kitchen
from entry import EntryWay
from dining_room import DiningRoom
from courtyard import Courtyard
from walls import Walls
from bedroom import Bedroom
from rec import Recreation
from room import Room
from character import Character
from living_room import LivingRoom
from enemy import Enemy
import random
import time
#win the game by killing all raiders or securing the base. 
#you can use time to trigger an event
#If they collect all of the items and complete the tasks they win because the raiders can't get in. 
#If not, the player has to fight them all
#importing too much garbage, clean this up

class Game:
    def __init__(self):
        self.intro = """Welcome to Colony Defense Sim!
You are the sole survivor of a rimworld colony built into a mountain. Raiders attacked your fledgling homestead and have killed the other colonists, your friends and family.
After burying the dead, you survey the colony. The only way into the colony is through the south wall and its crumbling in portions. 
You see that the main power to the base is offline, leaving the autoturrets offline and the main gate unlocked. 
You'll have to search your base for whatever supplies are left. The colony was running low on supplies before the raider attack and it has left the base mostly barren. 
You might find some items leftover, however. You'll need to find ammo, weapons and building supplies to fix the south walls.  
Each room will tell you which directions you can go and how you can protect your colony.
Complete the game by defeating the raiders and repairing your base. You can move north, south, east or west by typing n,s,e or w.
Type q to end the program.\n"""

    def show_intro(self):
        print("\nHello, {}. {} ".format(player.name, self.intro))

    def main(self):
        self.show_intro()
        #start = time.time()
        run = True
        while run:
            #if time.time() >= (start +120):
            #    print("\n\n MESSAGE \n\n")
            #    break
            new_loc = player.explore(player.location)
            if new_loc == "armory":
                loc = armory
            elif new_loc == "kitchen":
                loc = kitchen
            elif new_loc == "entry":
                loc = entry
            elif new_loc == "dining":
                loc = dining
            elif new_loc == "walls":
                loc = walls
            elif new_loc == "bedroom":
                loc = bedroom
            elif new_loc == "courtyard":
                loc = courtyard
            elif new_loc == "rec":
                loc = rec
            elif new_loc == "lr":
                loc = lr
            elif new_loc == "q":
                print("Exit game")
                run = False
                break
            else:
                print(new_loc)
                loc = player.location
            player.location = loc


game = Game()
armory = Armory("armory")
rec = Recreation("Rec")
kitchen = Kitchen("kitchen")
entry = EntryWay("entry way")
walls = Walls("walls")
lr = LivingRoom("lr")
bedroom = Bedroom("bedroom")
walls = Walls("walls")
courtyard = Courtyard("courtyard")
dining = DiningRoom("dining room")
player = Player(name, 20, 10, courtyard)
name = input("Enter name:  \n")

game.main()
