from src.actions.action import Action
from typing import Dict
from src.playerprofile import PlayerProfile
from src.mapfeatures.intersection import Intersection


class Empty(Action):
    def __init__(self):
        pass

    def __repr__(self):
        return 'empty'

    def apply_action(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        pass
