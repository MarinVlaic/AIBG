from mapfeatures.tile import Tile
from mapfeatures.intersection import Intersection
from math import log
from typing import Dict


def get_intersection_value(intersection: Intersection, resource_counters, all_intersections: Dict[int, Intersection]):
    # Calculate intersection entropy
    intersection_entropy = calculate_intersection_value(intersection, resource_counters)

    # Get first neighbours entropy
    first_neighbours = set(map(lambda index: all_intersections[index], intersection.neighbouring_intersection_ids))

    first_neighbours_entropy_sum = 0.0
    for first_neighbour in first_neighbours:
        first_neighbours_entropy_sum += calculate_intersection_value(first_neighbour, resource_counters)
    first_neighbours_entropy_sum /= len(first_neighbours)

    # Get second neighbours entropy
    second_neighbours = set()
    for first_neighbour in first_neighbours:
        second_neighbours.update(map(lambda index: all_intersections[index], first_neighbour.neighbouring_intersection_ids))
    second_neighbours_entropy_sum = 0.0
    for second_neighbour in second_neighbours:
        second_neighbours_entropy_sum += calculate_intersection_value(second_neighbour, resource_counters)
    second_neighbours_entropy_sum /= len(second_neighbours)

    return 0.7 * intersection_entropy + 0.2 * first_neighbours_entropy_sum + 0.1 * second_neighbours_entropy_sum


def calculate_tile_entropy(tile: Tile, resource_counters: Dict[str, int]):
    total_sum = sum(resource_counters.values())
    probability = float(resource_counters[tile.type]) / total_sum

    return tile.weight * probability * log(1/probability)


def calculate_intersection_value(intersection: Intersection, resource_counters: Dict[str, int]):
    tile_entropy_sum = 0
    for tile in intersection.neighbouring_tiles:
        tile_entropy_sum += calculate_tile_entropy(tile, resource_counters)
    return tile_entropy_sum
