from character import Character
import random
import time
import sys

#if else statement that adds more health and attack points if the player repairs everything
#Do we want to create a threshold that gives more hp the more tasks they complete?
#all_items found list 

class Player(Character):
	all_items = ["Knife", "Medkit (3/3) uses left", "Medkit (2/3) uses left", "Medkit (1/3) uses left", ".45 Automatic Pistol", "Survival Rifle", "Bag of Quikcrete", "Reactor Components", "Turret Components", "Wood boards", "Batteries (Ammo)", ".50 Caliber Ammo Box", "Safety Gear"] #all possible items, write a command that tells them they've found all possible items
	all_enemies = ["Raider Beserker", "Caspian Mole", "Raider Leader", "Raider Grunt", "Raider", "Feral dog", "Space Rat", "Malfunctioning Robot", "Malfunctioning Turret", "Raider Merc", "Giant Fire Ant", "Raider Bruiser"] 

	def __init__(self, name, health, attack_pts, location):
		super().__init__(name, health, attack_pts)
		self.location = location
		self.items = []
		self.items_found = []
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
			reaction = input("\nDo you want to attack? Y or N\n").lower()
			if reaction == "y":
				outcome = self.combat(location.enemy)
				if outcome:
					if outcome == self.name:
						print("\nGame over!\n")
						sys.exit()
					else:
						self.kill_list.append(outcome)
						if outcome == location.enemy.name:
							location.enemy = ""
						self.check_kill_list()
						self.check_health()
						#Here's where we put our win function for if they defeat the raiders
						if self.complete_kill_list() == True:
							print("You've killed all of the raiders!")
					fight = False
			else:
				print("{} attacks you!".format(location.enemy.name))
				outcome = location.enemy.combat(self)
				if outcome:
					if outcome == self.name:
						print("\nGame over!\n")
						sys.exit()
					else:
						self.kill_list.append(outcome)
						if outcome == location.enemy:
							location.enemy = ""
						self.check_kill_list()
						self.check_health()
						if self.complete_kill_list() == True:
							print("You've killed all of the raiders!")
					fight = False

					#win message here with sys.exit()
					#should not be able to flee

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
						self.items_found.append(item)
						self.check_items()
						if not location.contents:
							print("You've found all of the items!")
						else:
							print("There might be more to find in this room...")
					else:
						print("\nNothing found yet\n")
			elif action =="2":
				print("\nLocation reminder: ")
				location.get_description()
				next_room = location.get_direction()
				return next_room   
				#write a function here that looks for a special container and then runs a use function, maybe vary the input function based on the location.   
			else:
				pass
	
	def check_items(self):
		print("\nInventory: {}\n".format(', '.join(self.items)))
		#change this for the items_found list
		if self.items_found == self.all_items:
			print("\n You've found all the items. Make sure you use the building materials you found to repair your base to enter the endgame.\n")
		else:
			pass
		if "Medkit (3/3) uses left" in self.items:
			heal = lower(input("""\nWould you like to use your medkit? Y or N
				It contains bandages and drugs that boosts your health. It has three uses.\n"""))
			if heal == "y":
				self.items.remove("Medkit (3/3) uses left")
				self.items.append("Medkit (2/3) uses left")
				#is this correct?
				self.health += 15
			else:
				pass
		if "Medkit (2/3) uses left" in self.items:
			heal = lower(input("""\nWould you like to use your medkit? Y or N
				It contains bandages and drugs that boosts your health. It has two uses.\n"""))
			if heal == "y":
				self.items.remove("Medkit (2/3) uses left")
				self.items.append("Medkit (1/3) uses left")				
				self.health += 15
			else:
				pass
		if "Medkit (1/3) uses left" in self.items:
			heal = lower(input("""\nWould you like to use your medkit? Y or N
				It contains bandages and drugs that boosts your health. It has one use.\n"""))
			if heal == "y":
				self.items.remove("Medkit (1/3) uses left")
				self.health += 15
			else:
				pass

	def check_kill_list(self):
		print("\nKill list: {}\n".format(', '.join(self.kill_list)))

	#def complete_item_list(self):
	#	found_all_items = set(self.all_items) == set(self.items)
	#	return found_all_items
		
	def complete_kill_list(self):
		killed_all_enemies = set(self.all_enemies) == set(self.kill_list)
		return killed_all_enemies

	def turret_buff(self):
		pass

	#activates a turret buff that boosts hp for boss fight, print total health before fight

	def check_health(self):
		hp_check = input("Would you like to check your health points? y or n").lower()
		if hp_check == "y":
			print("\nYou're health is now at {}\n".format(self.health))
			self.check_items()
		else:
			pass





