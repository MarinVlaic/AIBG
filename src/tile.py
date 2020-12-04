
class Tile:
    def __init__(self, data):
        self.type = data['resourceType']
        self.weight = data['resourceWeight']
        self.x = data['x']
        self.y = data['y']