from character import Character
import random
import time

#need to create a use function and a reload function, maybe too complicated

class Player(Character):
    all_items = ["knife", ".45 automatic pistol", "Survival Rifle", "Concrete", "Wood boards", "Batteries (Ammo)", ".50 Caliber Ammo Box", "36 .45 cartridges", "60 .308 cartridges"] #all possible items, write a command that tells them they've found all possible items
    all_enemies = ["Raider Beserker", "Caspian Mole", "Raider Leader", "Raider Grunt", "Raider", "Feral dog"] #all possible enemies
    
    def __init__(self, name, health, attack_pts, location):
        super().__init__(name, health, attack_pts)
        self.location = location
        self.items = []
        self.kill_list = []
    
    def explore(self, location):
        location.get_description()
        if location.enemy:
            location.show_enemy()
            self.fight_or_flight(location)
        new_loc = self.search(location)
        return new_loc
        
    def fight_or_flight(self, location):
        fight = True
        while fight:
            reaction = input("\nDo you want to attack? y/n\n").lower()
            if reaction == "y":
                outcome = self.combat(location.enemy)
                if outcome:
                    if outcome == self.name:
                        print("\nGame over!\n")
                        exit()
                    else:
                        self.kill_list.append(outcome)
                        if outcome == location.enemy.name:
                            location.enemy = ""
                        self.check_kill_list()
                    fight = False
            else:
                print("{} attacks you!".format(location.enemy.name))
                outcome = location.enemy.combat(self)
                if outcome:
                    if outcome == self.name:
                        print("\nGame over!\n")
                        exit()
                    else:
                        self.kill_list.append(outcome)
                        if outcome == location.enemy:
                            location.enemy = ""
                        self.check_kill_list()
                    fight = False

    def search(self, location):
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
                print("\nLocation reminder: ")
                location.get_description()
                next_room = location.get_direction()
                return next_room
                        
    def check_items(self):
        print("\nInventory: {}\n".format(', '.join(self.items)))

    def check_kill_list(self):
        print("\nKill list: {}\n".format(', '.join(self.kill_list)))

