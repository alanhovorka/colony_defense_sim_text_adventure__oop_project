from room import Room
from player import Player
import sys

class Reactor(Room):
	reactor_status = "Offline"
	reactor_condition = "Damaged"
	def __init__(self, name):
		super().__init__(name)
		self.description = """\nAs you walk into the base's reactor room, you feel the electrical discharge in the air.
		You see that base's reactor was damaged during the last raid, likely an overload due to the EMP damage to turrets on the south wall.
		Repairing the reactor will bring power back online.\n"""
		self.contents = []
		self.special = []
		self.doors = {"e": "bedroom", "s": "workshop"}
		#how to get repair reactor to run, move this to the player class and have it be location specific. 
		#can we keep the class variables here then?
	#add some random integers to succeed in repairing the generator
	#safety gear eliminates the probablity of getting shocked to death
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
