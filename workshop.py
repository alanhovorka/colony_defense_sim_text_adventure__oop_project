from room import Room

class Workshop(Room):
	
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		You walk into the workshop.	It's in complete disarray. The roof has collasped at the far side of the room causing items and debries to spill across the floor. You can go north to the reactor, east to the dining area and south to the armory.
		\n"""
		self.doors = {"n": "reactor", "s": "armory", "e":"dining"}	
		self.contents = ["Bag of Quikcrete", "Reactor Components"]
		self.special = []
