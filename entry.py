from room import Room

#no enemy here

class EntryWay(Room):
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		You step inside the colony's main entryway. There are opened boxes scattered about the hallway. They might contain something.
		Blood streaks lead north into the workshop. 
		You can head west into the armory, east to the living room and north to the workshop. 
		\n"""
		self.contents = ["Knife"]
		self.doors = {"n": "workshop", "e": "lr", "w": "armory", "s": "courtyard"}
		self.special = []
		
	def get_random_enemy(self):
		return None