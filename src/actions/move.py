from src.actions.action import Action
from src.playerprofile import PlayerProfile
from typing import Dict
from src.mapfeatures.intersection import Intersection


class Move(Action):

    def __init__(self, intersection_id: int):
        self.intersection_id = intersection_id

    def apply_action(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        if not player_profile.check_road(self.intersection_id, player_profile.current_builder_intersection_position_id):
            player_profile.resources["SHEEP"] -= 50
            player_profile.resources["WHEAT"] -= 50
        player_profile.current_builder_intersection_position_id = self.intersection_id

    def __repr__(self):
        return f'move {self.intersection_id}'
