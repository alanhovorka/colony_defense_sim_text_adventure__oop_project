from character import Character
import random
import time

#need to create a use function
#if else statement that adds more health and attack points if the player repairs everything
#Do we want to create a threshold that gives more hp the more tasks they complete?

class Player(Character):
	all_items = ["Knife", ".45 Automatic Pistol", "Survival Rifle", "Bag of Quikcrete", "Reactor Components", "Turret Components", "Wood boards", "Batteries (Ammo)", ".50 Caliber Ammo Box", "36 .45 cartridges", "60 .308 cartridges"] #all possible items, write a command that tells them they've found all possible items
	all_enemies = ["Raider Beserker", "Caspian Mole", "Raider Leader", "Raider Grunt", "Raider", "Feral dog", "Space Rat", "Malfunctioning Robot", "Malfunctioning Turret", "Raider Merc", "Raider Bruiser"] #all possible enemies
	
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
	#is this ok?                  
	def check_items(self):
		print("\nInventory: {}\n".format(', '.join(self.items)))
		if items == all_items:
			print("\n You've found all the items. Make sure you use the building materials you found to repair your base to enter the endgame.\n")
		else:
			pass

	def check_kill_list(self):
		print("\nKill list: {}\n".format(', '.join(self.kill_list)))




