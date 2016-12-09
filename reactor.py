from room import Room

class Reactor(Room):
	"""docstring for Reactor"""
	def __init__(self, arg):
		super(Reactor, self).__init__()
		self.arg = arg
		