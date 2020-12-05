import json
from src.mapfeatures import tile

def helper(response):
    resources = {
        "SHEEP": 0,
        "WOOD": 0,
        "WHEAT": 0,
        "CLAY": 0,
        "IRON": 0
    }
    full_map_info = response['result']

    intersection_neighbourhood = full_map_info['indexMap']
    tile_neighbourhood = full_map_info['intersectionCoordinates']
    map = full_map_info['map']

    tile_info = map['tiles']
    tiles = []
    for tile_row in tile_info:
        row_tiles = []
        for t in tile_row:
            if t is not None:
                if t['resourceType'] not in ["WATER", "DUST"]:
                    resources[t['resourceType']] += t['resourceWeight']
                row_tiles.append(tile.Tile(t))
        tiles.append(row_tiles)

    return intersection_neighbourhood, tile_neighbourhood, tiles, resources


def get_intersection_neighs(intersection_neighbourhood, index):
    return intersection_neighbourhood[index]


def get_tiles_neighs(tiles, tile_neighbourhood, index):
    return [tiles[neigh['y']][neigh['x']] for neigh in tile_neighbourhood[index]]

