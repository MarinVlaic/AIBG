import json
from playerprofile import PlayerProfile
from intersection import Intersection
from typing import List
from action import Action


class MapState:
    def __init__(self, first_player_profile: PlayerProfile, second_player_profile: PlayerProfile, all_intersections: List[Intersection]):
        self.first_player_profile = first_player_profile
        self.second_player_profile = second_player_profile
        self.all_intersections = self.all_intersections

    def apply_move(self, move: Action):
        #TODO: apply logic to applaying move to the map state (call .aplly on move object)
        pass
