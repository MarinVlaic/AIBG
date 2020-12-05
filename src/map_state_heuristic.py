from mapstate import MapState
from playerprofile import PlayerProfile
from typing import Dict


def get_map_state_grade(map_state: MapState, player: PlayerProfile, resources_dict: Dict[str, int]):
    counter = {
        "SHEEP": 0,
        "WOOD": 0,
        "WHEAT": 0,
        "CLAY": 0,
        "IRON": 0
    }
    for city in player.cities:
        for tile in city.intersection.neighbouring_tiles:
            if tile.type != "WATER" and tile.type != "DUST":
                counter[tile.type] += tile.weight
    return sum(counter.values())
