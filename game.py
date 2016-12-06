from player import Player
from armory import Armory
from kitchen import Kitchen
from entry import EntryWay
from dining_room import DiningRoom
from courtyard import Courtyard
from walls import Walls
from bedroom import Bedroom
from rec import Rec
from character import Character
from enemy import Enemy
import random
#win the game by killing all raiders or securing the base. 

class Game:
    def __init__(self):
        self.intro = """Welcome to Colony Defense Sim!
Each room will tell you which directions you can go and how you can protect your colony.
Complete the game by defeating the raiders. You can move north, south, east or west by typing n,s,e or w.
Type q to end the program.\n"""

    def show_intro(self):
        print("\nHello, {}. {} ".format(player.name, self.intro))

    def main(self):
        self.show_intro()
        run = True
        while run:
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
rec = Rec("Rec")
kitchen = Kitchen("kitchen")
entry = EntryWay("entry way")
walls = Walls("walls")
bedroom = Bedroom("bedroom")
courtyard = Courtyard("courtyard")
dining = DiningRoom("dining room")
player = Player(name, 20, 10, courtyard)
name = input("Enter name:  \n")

game.main()
