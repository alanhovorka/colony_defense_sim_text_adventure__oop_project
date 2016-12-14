from enemy import Enemy
from room import Room
from player import Player
import random
import sys

#spawn raid function using time, player function that they can check to see how long until they have to fight the raiders. 
#Should be able to intialitzie the raid at the walls if they have all the items
#If they run out of time, they break in and spawn randomly in rooms, rushing through the building
#Walls should be its own class
#Should be a use function that repairs the walls, turrets and locks the gate
#How to make turrets act as friendly npcs
#need of a list of items in the rooms
class Walls(Room):
	raid = ["Raider Beserker", "Raider Grunt", "Raider", "Raider", "Raider Merc", "Raider Bruiser"]
	raidlead = ["Raider Leader"]

	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		You stand at the walls protecting your base.
		You see that the south wall has been damaged and will need to be repaired.
		The main gate is offline and unlocked.
		The turrets are offline and damaged. 
		You can head north to the courtyard. 
		\n"""
		self.contents = []
		self.doors = {"n": "courtyard"}
		self.special = ["Damaged Walls"]
		#self.

	def get_random_enemy(self):
		return None

	def raid(self):
		if Player.turret_power == "Online" and Player.self.location =="walls":
			print("it works")
		else:	
			pass

	def spawn_raiders(self):
		pass

#repeat some of these functions with tweaks for the raid

#should be able to write an if statement that assigns
	#health to specific enemies i.e. raiders
	# return Enemy(random.choice(enemies), random.randint(4, 6), random.randint(2, 4))

#walls, contains enemies, but player chooses when to attack them. turrets to interact with and things to repair, use function 
#can get enemies to spawn by using the random enemy function and to change from pass to the function once the conditions are fulfilled
#method that checks to see if the 

#the raiders come shambling back over the horizon, beaten and bruised. You catch them by surprise with your turrets. They weren't expecting the defenses to be back online
#You manage to kill a few of them before they climb the walls and bust open the gate again. Prepare to fight. 