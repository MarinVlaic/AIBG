from src.actions.action import Action
from src.playerprofile import PlayerProfile
from typing import Dict
from src.mapfeatures.intersection import Intersection

class Move(Action):

    def __init__(self, intersection_id : int):
        self.intersection_id = intersection_id

    def apply_move(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        player_profile.current_builder_intersection_position = intersections[self.intersection_id]
        player_profile.resources["SHEEP"] -= 50
        player_profile.resources["WHEAT"] -= 50
