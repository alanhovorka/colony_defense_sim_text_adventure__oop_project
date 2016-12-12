from room import Room

#enemy here

class Armory(Room):
	"""docstring for Armory"""
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		
		\n"""
		self.contents = [".45 Automatic Pistol"]
		self.doors = {"n": "workshop", "e": "entry"}
