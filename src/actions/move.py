from src.actions.action import Action
from src.playerprofile import PlayerProfile
from typing import Dict
from src.mapfeatures.intersection import Intersection


class Move(Action):

    def __init__(self, intersection_id: int):
        self.intersection_id = intersection_id

    def apply_action(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        player_profile.current_builder_intersection_position = intersections[self.intersection_id]

        if self.intersection_id not in intersections[self.intersection_id].roads_to_neighbouring_intersections:
            player_profile.resources["SHEEP"] -= 50
            player_profile.resources["WHEAT"] -= 50

    def __repr__(self):
        return f'move {self.intersection_id}'
