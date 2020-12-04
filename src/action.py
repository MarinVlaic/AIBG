from playerprofile import PlayerProfile
from intersection import Intersection
from typing import Dict


class Action:
    def __init__(self, action):
        pass

    def __repr__(self):
        pass

    def apply_move(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        # Abstract method that children have to implement
        pass
