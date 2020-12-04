from src.playerprofile import PlayerProfile
from src.intersection import Intersection

class Move:
    def apply_move(self, first_palyer_profile: PlayerProfile, second_player_profile: PlayerProfile, intersections: dict[int, Intersection]):
        # Abstract method that children have to implement
        pass
