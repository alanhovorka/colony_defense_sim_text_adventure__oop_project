from room import Room

#enemy here

class Armory(Room):
	"""docstring for Armory"""
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		The door slides open and you step inside the armory. Most of the equipment and weapons is gone.
		You spot a few lockers and boxes left untouched. 
		You can go north to the workshop or head east to the entry way. 
		\n"""
		self.contents = [".45 Automatic Pistol"]
		self.doors = {"n": "workshop", "e": "entry"}
