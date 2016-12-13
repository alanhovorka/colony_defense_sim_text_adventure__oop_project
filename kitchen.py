from room import Room

class Kitchen(Room):
	
	def __init__(self, name):
		super().__init__(name)
		self.description = """\nYou are in the kitchen.
		You can head west to the barracks and south to the dining area.
		\n"""
		self.contents = ["Metkit"]
		self.doors = {"w":"bedroom", "s":"dining"}
		self.special = []
