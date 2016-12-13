	
	def search(self, location):
		search = True
		while search:
			if not location.special:
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
				else:
					print("\nLocation reminder: ")
					location.get_description()
					next_room = location.get_direction()
					return next_room   
				#write a function here that looks for a special container and 
				#then runs a use function, maybe vary the input function 
				#based on the location.   
			elif location.special == "Base Reactor":
				action = input("\nWhat do you want to do?\n1. Search room\n2. Repair reacto\n3. Leave room\n")
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
						repair = input("Would you like to repair the reactor with your Reactor Components? Y or N").lower()
						if repair == "y":
							if "Safety Gear" in self.items:
								self.items.remove("Reactor Components")
								reactor_condition = "Repaired"
								reactor_status = "Online"
								if reactor_condition == "Repaired" and reactor_status == "Online":
									print("""\nYou put on the safety gear, eliminating all chance of during reapirs. 
									You've repaired the reactor and restored power to the base.
									It still might be good to search the rest of the base before you repair the walls.\n""")
								else:
									pass
							else:
								dead = ''
								chance = random.randint(0,9)
								if chance > 3:
									self.items.remove("Reactor Components")
									reactor_condition = "Repaired"
									if reactor_condition == "Repaired":
										print("""\nDespite not having any safety gear, you manage to stay alive while repairing the reactor.\n""")
									else:
										pass
								else:
									self.health = 0
									dead = self.name
								if dead:
									print("\nYou've been electrocuted while trying to repair the reactor. You've died. Game over. Try finding the safety gear.\n")
									sys.exit()
									return dead
								else:
									pass

						else:
							pass
					else:
						pass
				else:
					print("\nLocation reminder: ")
					location.get_description()
					next_room = location.get_direction()
					return next_room
			else:
				pass




#player
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



#reactor
	def repair_reactor(self):
			if "Reactor Components" in self.items:
				repair = input("Would you like to repair the reactor with your Reactor Components? Y or N").lower()
				if repair == "y":
					if "Safety Gear" in self.items:
						self.items.remove("Reactor Components")
						reactor.reactor_condition = "Repaired"
						print("""\nYou put on the safety gear, eliminating all chance of during reapirs. 
							You've repaired the reactor.
							It still might be good to search the rest of the base before you repair the walls.\n""")
					else:
						dead = ''
						chance = random.randint(0,9)
						if chance > 3:
							self.items.remove("Reactor Components")
							reactor.reactor_condition = "Repaired"
							print("""\nDespite not having any safety gear, you manage to stay alive while repairing the reactor.\n""")
						else:
							self.health = 0
							dead = self.name
						if dead:
							print("\nYou've been electrocuted while trying to repair the reactor. You've died. Game over. Try finding the safety gear.\n")
							sys.exit()
							return dead
						else:
							pass
				else: 
					pass
			else:
				pass
	def reactor_online(self):
		if reactor_condition == "Repaired":
			reactor_status = "Online"
			print("""\nBy repairing the reactor, you've restored power to the base. 
				You can return to the walls and lock the gate and turn on the turrets if they're repaired.\n""")
		else:
			pass
