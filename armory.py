from room import room

class Armory(room):
	"""docstring for Armory"""
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		#insert description
		\n"""
		self.contents = []
		self.doors = {"": "", "": ""}
