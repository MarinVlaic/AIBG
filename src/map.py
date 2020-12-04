import json
from src.mapfeatures import tile


class Map:
    def __init__(self, response):
        full_map_info = response['result']

        self.intersection_neighbourhood = full_map_info['indexMap']
        self.tile_neighbourhood = full_map_info['intersectionCoordinates']
        self.map = full_map_info['map']

        self.tile_info = self.map['tiles']
        self.tiles = []
        self.create_tiles()

    def create_tiles(self):
        self.tiles = []
        for tile_row in self.tile_info:
            row_tiles = []
            for t in tile_row:
                if t is not None:
                    row_tiles.append(tile.Tile(t))
            self.tiles.append(row_tiles)

    def get_intersection_neighs(self, index):
        return self.intersection_neighbourhood[index]

    def get_tiles_neighs(self, index):
        return [self.tiles[neigh['y']][neigh['x']] for neigh in self.tile_neighbourhood[index]]


def main():
    with open('../../karta1.json') as map_file:
        full_map = Map(json.load(map_file))
    print(full_map.get_intersection_neighs(40))
    [print(neigh) for neigh in (full_map.get_tiles_neighs(40))]


if __name__ == '__main__':
    main()
