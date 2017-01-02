from enemy import Enemy
from room import Room
import random
import sys

class Walls(Room):
	raiders = ["Raider Beserker", "Raider Grunt", "Raider", "Raider", "Raider Merc", "Raider Bruiser"]

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
		self.enemy = []

	def get_random_enemy(self):
		return None

	def spawn(self):
		for raider in Walls.raiders:

			#new_enemy = random.choice(Walls.raiders)
			self.enemy.append(Enemy(raider, random.randint(5, 10), random.randint(5, 10)))
		self.enemy.append(Enemy("Raider Leader", random.randint(10, 15), random.randint(10, 15) ))
		print("The raiders have returned!")


	def show_enemy(self):
		for i in self.enemy:
			print(i.name)
			print("In the group of raiders, there is a {} with {} HP and {} attack points!".format(i.name, i.health, i.attack_pts))

#should be able to write an if statement that assigns
	#health to specific enemies i.e. raiders
	# return Enemy(random.choice(enemies), random.randint(4, 6), random.randint(2, 4))

#walls, contains enemies, but player chooses when to attack them. turrets to interact with and things to repair, use function 
#can get enemies to spawn by using the random enemy function and to change from pass to the function once the conditions are fulfilled
#method that checks to see if the 

#the raiders come shambling back over the horizon, beaten and bruised. You catch them by surprise with your turrets. They weren't expecting the defenses to be back online
#You manage to kill a few of them before they climb the walls and bust open the gate again. Prepare to fight. 