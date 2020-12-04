from src.actions.action import Action
from src.playerprofile import PlayerProfile
from typing import Dict
from src.mapfeatures.intersection import Intersection


class MoveRoad(Action):

    def __init__(self, intersection_id : int):
        self.intersection_id = intersection_id

    def apply_action(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        player_profile.current_builder_intersection_position = intersections[self.intersection_id]
