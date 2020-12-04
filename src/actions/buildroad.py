from src.actions.action import Action
from src.mapfeatures.intersection import Intersection
from src.playerprofile import PlayerProfile
from typing import Dict


class BuildRoad(Action):
    def __init__(self, intersection1: int, intersection2: int):
        self.id_int1 = intersection1
        self.id_int2 = intersection2

    def apply_action(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        player_profile.resources['WOOD'] -= 100
        player_profile.resources['CLAY'] -= 100

        intersections[self.id_int1].roads_to_neighbouring_intersections_ids.append(self.id_int2)
        intersections[self.id_int2].roads_to_neighbouring_intersections_ids.append(self.id_int2)

