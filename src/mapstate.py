import json
from playerprofile import PlayerProfile
from intersection import Intersection
from move import Move


class MapState:
    def __init__(self, first_player_profile: PlayerProfile, second_player_profile: PlayerProfile, all_intersections: list[Intersection]):
        self.first_player_profile = first_player_profile
        self.second_player_profile = second_player_profile
        self.all_intersections = self.all_intersections

    def apply_move(self, move: Move):
        #TODO: apply logic to applaying move to the map state (call .aplly on move object)
        pass
