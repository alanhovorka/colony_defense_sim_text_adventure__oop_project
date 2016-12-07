from room import Room

class Bedroom(Room):
	"""docstring for Bedroom"""
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		#insert description
		\n"""
		self.contents = []
		self.doors = {"": "", "": ""}	