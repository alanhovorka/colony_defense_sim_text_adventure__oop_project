class Room:
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.doors = {}

    def get_description(self):
        print("{}".format(self.description))

    def search_room(self):
        pass

    def attack(self):
        pass

    def get_direction(self):
        direction = input("Which way? ").lower()
        if direction == "q":
            return direction
        elif direction in self.doors:
            location = self.doors[direction]
            return location
        else:
            return "\nNot an option\n"
