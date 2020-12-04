from tile import Tile
from typing import List


class Intersection:
    def __init__(self, neighbouring_tiles: List[Tile], id, neighbouring_intersection_ids):
        self.neighbouring_tiles = neighbouring_tiles
        self.id = id
        self.neighbouring_intersection_ids = neighbouring_intersection_ids
        self.captured = False
        self.roads_to_neighbouring_intersections = []
