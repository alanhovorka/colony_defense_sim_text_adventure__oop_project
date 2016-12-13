from enemy import Enemy
import random

class Room:
	enemies = ["Feral dog", "Giant Fire Ant", "Caspian Mole", "Space Rat", "Malfunctioning Robot", "Malfunctioning Turret"]

	#do I need separate enemy lists or can I just desginate to spawn enemies within an index range?

	def __init__(self, name):
		self.name = name
		self.description = ""
		self.contents = []
		self.special = []
		self.doors = {}
		self.enemy = self.get_random_enemy()
		
	def get_description(self):
		print("{}".format(self.description))

	def get_direction(self):
		direction = input("Which way? ").lower()
		if direction == "q":
			return direction
		elif direction in self.doors:
			location = self.doors[direction]
			return location
		else:
			return "\nNot an option\n"
	def get_random_enemy(self):
	#should be able to write an if statement that assigns
	#health to specific enemies i.e. raiders
	# return Enemy(random.choice(enemies), random.randint(4, 6), random.randint(2, 4))
		rand_index = random.randrange(len(Room.enemies))
		random_enemy = Room.enemies.pop(rand_index)
		return Enemy(random_enemy, random.randint(4, 6), random.randint(2, 4))

	def show_enemy(self):
		print("There is a {} in the room!".format(self.enemy.name))
	#repeat some of these functions with tweaks for the raid