from room import Room
import random

#spawn raid function using time, player function that they can check to see how long until they have to fight the raiders. 
#Should be able to intialitzie the raid at the walls if they have all the items
#If they run out of time, they break in and spawn randomly in rooms, rushing through the building
#Walls should be its own class
#Should be a use function that repairs the walls, turrets and locks the gate
#How to make turrets act as friendly npcs

#need of a list of items in the rooms


class Walls(Room):
	#raid = ["Raider Beserker", "Raider Grunt", "Raider", "Raider", "Raider Merc", "Raider Bruiser"]
	#raidlead = ["Raider Leader"]
	condition = "Damaged"
	base_power = "Offline" #Turning the power back on in the reactor room should flip this to online
	turret_power = "Offline"
	gate_powerr = "Offline"
	turrets_condition = [] #maybe a dictionary of the npcs and their damaged conditions and when it's all functional triggers the raid  {"South Turret 1": "Damaged", "South Turret 2": "functional"}
	turrets = ["South Turret 1", "South Turret 2", "Southeast Corner Turret", "Southwest Corner Turret", "West Turret", "East Turret"]
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		insert description
		\n"""
		self.contents = []
		self.doors = {"": "", "": ""}

	def repair_wall(self):
		if "Concrete" in player.items:
			remove.player.items("Concrete")
			condition = "Repaired"
			print("You look at the  've repaired the southern wall.")
		else:
			pass


#player input option to turn on the turrets, asks for input when the power is online. if reactor.reactor = "Online": switch = input()

#get 
#walls, contains enemies, but player chooses when to attack them. turrets to interact with and things to repair, use function 
#can get enemies to spawn by using the random enemy function and to change from pass to the function once the conditions are fulfilled
#method that checks to see if the 