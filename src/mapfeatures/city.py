from intersection import Intersection

class City:
    def __init__(self, intersection: Intersection):
        self.intersection = intersection
        self.level = 1

    def upgrade(self):
        self.level = 2
