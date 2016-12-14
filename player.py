from character import Character
import random
import time
import sys

class Player(Character):
	all_items = ["Knife", "Medkit (3/3) uses left", "Medkit (2/3) uses left", "Medkit (1/3) uses left", ".45 Automatic Pistol", "Survival Rifle", "Bag of Quikcrete", "Reactor Components", "Turret Components", "Safety Gear"] #all possible items, write a command that tells them they've found all possible items
	all_items_found = ["Knife", "Medkit (3/3) uses left", ".45 Automatic Pistol", "Survival Rifle", "Bag of Quikcrete", "Reactor Components", "Turret Components", "Safety Gear"]
	all_enemies = ["Raider Beserker", "Caspian Mole", "Raider Leader", "Raider Grunt", "Raider", "Feral dog", "Space Rat", "Malfunctioning Robot", "Malfunctioning Turret", "Raider Merc", "Giant Fire Ant", "Raider Bruiser"] 
	reactor_status = "Offline"
	reactor_condition = "Damaged"
	wall_condition = "Damaged"
	turret_power = "Offline"
	turret_condition = "Damaged"
	gate_power = "Offline"
	base_power = "Offline"
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
			reaction = input("\nDo you want to attack? y or n\n").lower()
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

#search should allow us to check inventory at the menu

	def search(self, location):
		search = True
		while search:
			if "Base Reactor" in location.special:
				action = input("\nWhat do you want to do?\n1. Search room\n2. Repair reactor\n3. Check inventory\n4. Leave room\n")
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
					if "Reactor Components" in self.items:								
						repair = input("""\nWould you like to repair the reactor with your Reactor Components? y or n\n""").lower()
						if repair == "y":
							if "Safety Gear" in self.items:
								self.items.remove("Reactor Components")
								self.items.remove("Safety Gear")
								Player.reactor_condition = "Repaired"
								Player.reactor_status = "Online"
								Player.base_power = "Online"
								if Player.reactor_condition == "Repaired" and Player.reactor_status == "Online":
									print("""\nYou put on the safety gear, eliminating all chance of during reapirs.\nYou've repaired the reactor and restored power to the base.\nIt still might be good to search the rest of the base before you repair the walls.\n""")
								else:
									print("""\nYou lack the required materials.\n""")
							else:
								dead = ''
								chance = random.randint(0,9)
								if chance > 4:
									self.items.remove("Reactor Components")
									Player.reactor_condition = "Repaired"
									Player.reactor_status = "Online"
									Player.base_power = "Online"
									if Player.reactor_condition == "Repaired" and Player.reactor_status == "Online":
										print("""\nDespite not having any safety gear, you manage to stay alive while repairing the reactor.\nYou've repaired the reactor and restored power to the base.\nIt still might be good to search the rest of the base before you repair the walls.\n""")
									else:
										pass	
								else:
									self.health = 0
									dead = self.name
								if dead:
									print("\nYou've been electrocuted while trying to repair the reactor.\nYou've died. Game over.\nTry finding the safety gear.\n")
									sys.exit()
									return dead
								else:
									pass
						else:
							pass
					else:
						print("""\nYou lack the required materials to complete this action.\n""")
				elif action == "3":
					inven_check = input("""\nWould you like to check your inventory? y or n\n""").lower()
					if inven_check == "y":
						self.check_items()
					else:
						pass
				else:
					print("\nLocation reminder: ")
					location.get_description()
					next_room = location.get_direction()
					return next_room			
			elif "Damaged Walls" in location.special:
				action = input("\nWhat do you want to do?\n1. Search room\n2. Repair walls \n3. Repair turrets\n4. Lock gate\n5. Turn on turrets\n6. Check Inventory\n7. Leave room\n")
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
				elif action == "2":
					if "Bag of Quikcrete" in self.items:
						repair = input("\nWould you like to repair the walls with your Quikcrete? y or n\n").lower()
						if repair == "y":
							self.items.remove("Bag of Quikcrete")
							Player.wall_condition ="Repaired"
							print("""\nYou look at the cracks and weak spots in the wall and apply concrete patching to the walls. You've repaired the southern wall.\n""")
						else:
							pass
					else:
						print("""\nYou lack the required materials to complete this action.\n""")
				elif action == "3":
					if "Turret Components" in self.items:
						repair = input("\nWould you like to repair the turrets with you Turret Components? y or n\n").lower()
						if repair == "y":
							self.items.remove("Turret Components")
							Player.turret_condition = "Repaired"
							print("""\nYou climb the walls and inspect the turrets. A few of them were damaged in the attack. You replace the components.\n""")
						else:
							pass
					else:
						print("""\nYou lack the required materials to complete this action.\n""")						
				elif action == "4":
					if Player.base_power == "Online":
						switch = input("\nWould you like to engage the main gate's lock now that power has been restored? y or n\n").lower()
						if switch == "y":
							Player.gate_power = "Online"
							print("""\nYou lock the main gate.\n""")
						else:
							pass
					else: 
						print("""\nYou'll need to turn the power back on before you can do this.\n""")						
				elif action == "5":
					if Player.base_power == "Online" and Player.turret_condition == "Repaired":
						switch = input("""Would you like to turn the turrets back on? \nWARNING: Doing this may cause the raiders to come back.\n y or n\n""").lower()
						if switch == "y":
							Player.turret_power = "Online"
							self.turret_buff()
							#insert raid functions



						else:
							pass
					else:
						print("""\nYou lack the required materials to complete this action.\n""")						
				elif action == "6":
					inven_check = input("""\nWould you like to check your inventory? y or n\n""").lower()
					if inven_check == "y":
						self.check_items()
					else:
						pass
				else:
					print("\nLocation reminder: ")
					location.get_description()
					next_room = location.get_direction()
					return next_room
			elif not location.special:
				action = input("\nWhat do you want to do?\n1. Search room\n2. Check Inventory\n3. Leave room\n")
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
				elif action == "2":
					inven_check = input("""\nWould you like to check your inventory? y or n\n""").lower()
					if inven_check == "y":
						self.check_items()
					else:
						pass				
				else:
					print("\nLocation reminder: ")
					location.get_description()
					next_room = location.get_direction()
					return next_room   
			else:
				pass







	#add stuff that boost attack points when picking up weapons
	def check_items(self):
		print("\nInventory: {}\n".format(', '.join(self.items)))
		if self.items_found == self.all_items:
			print("\n You've found all the items. Make sure you use the building materials you found to repair your base.\n")
		else:
			pass
		if "Medkit (3/3) uses left" in self.items:
			heal = input("""\nWould you like to use your medkit? y or n\nIt contains bandages and drugs that boosts your health.\nIt has three uses.\n""").lower()
			if heal == "y":
				self.items.remove("Medkit (3/3) uses left")
				self.items.append("Medkit (2/3) uses left")
				self.health += 15
			else:
				print("\nYou're health is now at {}\n".format(self.health))				
		if "Medkit (2/3) uses left" in self.items:
			heal = input("""\nWould you like to use your medkit? y or n\nIt contains bandages and drugs that boosts your health.\nIt has two uses.\n""").lower()
			if heal == "y":
				self.items.remove("Medkit (2/3) uses left")
				self.items.append("Medkit (1/3) uses left")				
				self.health += 15
			else:
				print("\nYou're health is now at {}\n".format(self.health))				
		if "Medkit (1/3) uses left" in self.items:
			heal = input("""\nWould you like to use your medkit? y or n\nIt contains bandages and drugs that boosts your health.\nIt has one use.\n""").lower()
			if heal == "y":
				self.items.remove("Medkit (1/3) uses left")
				self.health += 15
			else:
				print("\nYou're health is now at {}\n".format(self.health))				

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
			print("\nYou're health is {}\n".format(self.health))
			self.check_items()
		else:
			pass

