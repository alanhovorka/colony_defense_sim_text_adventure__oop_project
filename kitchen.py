from room import Room

class Kitchen(Room):
	
	def __init__(self, name):
		super().__init__(name)
		self.description = """\nYou are in the kitchen.
		insert more description
		\n"""
		self.contents = []
		self.doors = {"":"", "":""}
