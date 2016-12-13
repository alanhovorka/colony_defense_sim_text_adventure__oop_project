from room import Room
import sys

class Reactor(Room):
	
	def __init__(self, name):
		super().__init__(name)
		self.description = """\nAs you walk into the base's reactor room, you feel the electrical discharge in the air.
		You see that base's reactor was damaged during the last raid, likely an overload due to the EMP damage to turrets on the south wall.
		Repairing the reactor will bring power back online.\n"""
		self.contents = []
		self.special = ["Base Reactor"]
		self.doors = {"e": "bedroom", "s": "workshop"}
