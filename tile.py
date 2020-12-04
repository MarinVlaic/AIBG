class Tile:
    def __init__(self, data):
        self.type = data['resourceType']
        self.weight = data['resourceWeight']
        self.x = data['x']
        self.y = data['y']

    def __str__(self):
        return 'type:' + self.type + ', weight:' + str(self.weight) + ', x:' + str(self.x) + ', y:' + str(self.y)