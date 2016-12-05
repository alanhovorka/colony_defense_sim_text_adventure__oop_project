from armory import Armory
from kitchen import Kitchen
from entry import EntryWay
from dining_room import DiningRoom
from courtyard import Courtyard
from walls import Walls
from bedroom import Bedroom
from rec import Rec
from character import Character
import random

class Player:    
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []
    
    def explore(self, location):
        location.get_description()
        search = True
        while search:
            action = input("\nWhat do you want to do?\n1. Search room\n2. Leave room\n")
            if action == "1":
                if not location.contents:
                    print("\nYou find nothing of value in the room.\n")
                else:
                    find = random.randrange(1, 3)
                    if find == 1:
                        found = random.randrange(len(location.contents))
                        item = location.contents.pop(found)
                        print("\nYou found a {}\n".format(item))
                        self.items.append(item)
                        self.check_items()
                    else:
                        print("\nNothing found yet\n")
            else:
                new_loc = location.get_direction()
                return new_loc
        
    def check_items(self):
        print("\nInventory: {}\n".format(', '.join(self.items)))
