from src.playerprofile import PlayerProfile
from src.mapfeatures.intersection import Intersection
from typing import Dict
from src.actions.action import Action


class MapState:
    def __init__(self, first_player_profile: PlayerProfile, second_player_profile: PlayerProfile, all_intersections: Dict[int, Intersection]):
        self.first_player_profile = first_player_profile
        self.second_player_profile = second_player_profile
        self.all_intersections = all_intersections

    def apply_action(self, action: Action, player: PlayerProfile):
        action.apply_action(player, self.all_intersections)
        self.first_player_profile.update_resources()
        self.second_player_profile.update_resources()
