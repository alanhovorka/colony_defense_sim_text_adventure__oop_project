from room import Room

class Reactor(Room):

	#reactor condition
	reactor = "Offline"
	reactor_condition = "Damaged"

	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		#insert description
		\n"""
		self.contents = []
		self.doors = {"": "", "": ""}		