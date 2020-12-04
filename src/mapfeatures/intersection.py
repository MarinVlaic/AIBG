from src.mapfeatures.tile import Tile
from typing import List


class Intersection:
    def __init__(self, neighbouring_tiles: List[Tile], id, neighbouring_intersection_ids):
        self.neighbouring_tiles = neighbouring_tiles
        self.id = id
        self.neighbouring_intersection_ids = neighbouring_intersection_ids
        self.captured = False
        self.roads_to_neighbouring_intersections_ids = []

    def add_road(self, other):
        if self.is_neighbour(other):
            self.roads_to_neighbouring_intersections_ids.append(other.id)
            other.roads_to_neighbouring_intersections_ids.append(self.id)
        else:
            raise ValueError('Not neighbours')

    def is_neighbour(self, other):
        return other.id in self.neighbouring_intersection_ids
