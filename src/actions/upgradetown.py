from action import Action
from src.playerprofile import PlayerProfile
from src.mapfeatures.intersection import Intersection
from typing import Dict

class UpgradeTown(Action):
    def __init__(self, city):
        self.city = city

    def __repr__(self):
        pass

    def apply_move(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        player_profile.resources["WHEAT"] = player_profile.resources.get("WHEAT") - 200
        player_profile.resources["IRON"] = player_profile.resources.get("IRON") - 300

        self.city.upgrade()