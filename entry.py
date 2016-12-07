from room import Room

class EntryWay(Room):
	"""docstring for Entry"""
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		#insert description
		\n"""
		self.contents = []
		self.doors = {"": "", "": ""}	