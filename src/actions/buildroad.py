from src.actions.action import Action
from src.mapfeatures.intersection import Intersection
from src.playerprofile import PlayerProfile
from typing import Dict


class BuildRoad(Action):
    def __init__(self, destination_id: int):
        self.destination_id = destination_id

    def apply_action(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        player_profile.resources['WOOD'] -= 100
        player_profile.resources['CLAY'] -= 100

        player_profile.add_road(self.destination_id)

