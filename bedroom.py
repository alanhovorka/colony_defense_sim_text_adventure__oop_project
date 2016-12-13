from room import Room

#change to barracks
class Bedroom(Room):
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		You've entered the barracks. There is large pool of blood by one of the bunks. 
		Bloodied rags, sheets and other clothing lay on and around the bed. 
		A reminder of a failure. 
		You can head west to the reactor, east to the kitchen and south to the dining area. 
		\n"""
		self.contents = ["Safety Gear"]
		self.doors = {"w": "reactor", "e": "kitchen", "s":"dining"}
		self.special = []

	def get_random_enemy(self):
		return None
