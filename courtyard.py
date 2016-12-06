from room import Room

class Courtyard(Room):
    def __init__(self, name):
        super().__init__(name)
        self.description = """\nYou are in the courtyard of a rimworld colony after just escaping a group of raiders.
The raiders likely know where you're at, but you've stumbled upon this walled in, abandoned colony from the when the planet was first settled.
You look at the main colony building. It's seen better days. It's likely no one has inhabited it in some time.
Keep in mind the raiders are likely to return and you should prepare accordingly.
You can go north into the colony building and search for supplies, and maybe a bed as you plan your next strategy. There's likely gear leftover. Whoever lived here left in a hurry a long time ago.
You can go south to inspect and mount the walls. There appears to be turrets all along the walls.\n"""
        self.doors = {"n": "entry", "s", "walls"}
        self.contents = []
