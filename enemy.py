from character import Character

class Enemy(Character):
	"""docstring for Enemy"""
	def __init__(self, name, health, attack_pts):
		super().__init__(name, health, attack_pts)