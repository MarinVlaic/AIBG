from src.actions.action import Action
from src.playerprofile import PlayerProfile
from src.mapfeatures.intersection import Intersection
from src.mapfeatures.city import City
from typing import Dict


class BuildTown(Action):
    def __init__(self, intersection_index):
        self.intersection_index = intersection_index

    def __repr__(self):
        return f"buildtown {self.intersection_index}"

    def apply_action(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        player_profile.resources["SHEEP"] -= 100
        player_profile.resources["WOOD"] -= 100
        player_profile.resources["WHEAT"] -= 100
        player_profile.resources["CLAY"] -= 100

        player_profile.cities.append(City(intersections[self.intersection_index]))

        intersections[self.intersection_index].captured = True
