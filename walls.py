from room import Room
import random

#spawn raid function using time, player function that they can check to see how long until they have to fight the raiders. 
#Should be able to intialitzie the raid at the walls if they have all the items
#If they run out of time, they break in and spawn randomly in rooms, rushing through the building
#Walls should be its own class
#Should be a use function that repairs the walls, turrets and locks the gate
#How to make turrets act as friendly npcs

class Walls(Room):
	#raid = ["Raider Beserker", "Raider Grunt", "Raider", "Raider", "Raider Merc", "Raider Bruiser"]
	#raidlead = ["Raider Leader"]
	turrets = ["South Turret 1", "South Turret 2", "Southeast Corner Turret", "Southwest Corner Turret", "West Turret", "East Turret"]
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		insert description
		\n"""
		self.contents = []
		self.doors = {"": "", "": ""}

#get 
#walls, contains enemies, but player chooses when to attack them. turrets to interact with and things to repair, use function 