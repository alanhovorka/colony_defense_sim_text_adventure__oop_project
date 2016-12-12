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
	#add some random integers to succeed in repairing the generator
	def repair_reactor(self):
			if "Reactor Components" in items:
				repair = input("Would you like to repair the reactor with your Reactor Components? Y or N")
				if repair == "Y":
					remove.player.items("Reactor Components")
					reactor.reactor_condition = "Repaired"
					print("You've repaired the reactor.")
				else: 
					pass
			else:
				pass
	
