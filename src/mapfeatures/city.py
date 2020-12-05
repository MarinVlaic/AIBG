from src.mapfeatures.intersection import Intersection


class City:
    def __init__(self, intersection: Intersection):
        self.intersection = intersection
        self.level = 1

    def upgrade(self):
        self.level = 2

    def __eq__(self, other):
        if self.level != other.level:
            return False
        if self.intersection != other.intersection:
            return False
        return True

    def __hash__(self):
        return hash(self.intersection) + hash(self.level)
