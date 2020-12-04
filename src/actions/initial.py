from src.actions.action import Action
from src.playerprofile import PlayerProfile
from typing import Dict
from src.mapfeatures.intersection import Intersection

class Initial(Action):
    def __init__(self, i1, i2):
        self.first_intersection = i1
        self.second_intersection = i2

    def __repr__(self):
        return f"initial {self.first_intersection} {self.second_intersection}"

    def apply_action(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        pass