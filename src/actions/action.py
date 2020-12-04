from src.playerprofile import PlayerProfile
from src.mapfeatures.intersection import Intersection
from typing import Dict


class Action:
    def __repr__(self):
        pass

    def apply_action(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        # Abstract method that children have to implement
        pass
