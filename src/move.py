from playerprofile import PlayerProfile
from intersection import Intersection

class Move:
    def apply_move(self, player_profile: PlayerProfile, intersections: dict[int, Intersection]):
        # Abstract method that children have to implement
        pass

    def __repr__(self):
        pass
