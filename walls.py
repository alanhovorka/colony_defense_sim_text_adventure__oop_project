from room import Room
import random

#spawn raid function using time, player function that they can check to see how long until they have to fight the raiders. 
#Should be able to intialitzie the raid at the walls if they have all the items
#If they run out of time, they break in and spawn randomly in rooms, rushing through the building
#Walls should be its own class

class Walls(Room):
	"""docstring for Walls"""
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		insert description
		\n"""
		self.contents = []
		self.doors = {"": "", "": ""}

#walls, contains enemies, but player chooses when to attack them. turrets to interact with and things to repair, use function 