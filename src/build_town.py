from src.action import Action
from src.playerprofile import PlayerProfile
from src.intersection import Intersection
from typing import Dict

class Build_town(Action):
    def __init__(self, intersection_index):
        self.intersection_index = intersection_index

    def __repr__(self):
        pass

    def apply_move(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        player_profile.resources["SHEEP"] = player_profile.resources.get("SHEEP") - 100
        player_profile.resources["WOOD"] = player_profile.resources.get("WOOD") - 100
        player_profile.resources["WHEAT"] = player_profile.resources.get("WHEAT") - 100
        player_profile.resources["CLAY"] = player_profile.resources.get("CLAY") - 100
        player_profile
        intersections.get(self.intersection_index).captured = True



        pass

