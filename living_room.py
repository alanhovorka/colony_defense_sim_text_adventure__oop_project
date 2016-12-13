from room import Room

class LivingRoom(Room):
	def __init__(self, name):
		super().__init__(name)
		self.description = """\nYou are in a living room. There are chairs and couches scattered around. A fireplace sits unlit
		You spot a book shelf, viewscreen, fireplace and a cabinet. 
		You can go north, south or west.\n"""
		self.doors = {"n": "dining", "s": "armory", "w": "entry"}
		self.contents = ["Survival Rifle"]
		self.special = []

	#add some items in the room that the player can collect