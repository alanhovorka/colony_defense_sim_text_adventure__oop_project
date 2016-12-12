from room import Room

class Workshop(Room):
	
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		#insert description
		\n"""
		self.doors = {"": "", "": ""}	
		self.contents = ["Concrete", "Components"]

		
