from room import Room

class DiningRoom(Room):
	def __init__(self, name):
		super().__init__(name)
		self.description = """\nYou are in the dining room.
		insert more description
		\n"""
		self.contents = []
		self.doors = {"": "", "": ""}
