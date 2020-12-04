class Intersection:
    def __init__(self, neighbouring_tiles, id, neighbouring_intersection_ids):
        self.neighbouring_tiles = neighbouring_tiles
        self.id = id
        self.neighbouring_intersection_ids = neighbouring_intersection_ids
        self.captured = False
        self.roads_to_neighbouring_intersections = []
