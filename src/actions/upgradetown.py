from src.actions.action import Action
from src.playerprofile import PlayerProfile
from src.mapfeatures.intersection import Intersection
from typing import Dict
from src.mapfeatures.city import City


class UpgradeTown(Action):
    def __init__(self, city: City):
        self.city = city

    def __repr__(self):
        return f'upgradetown {self.city.intersection.id}'

    def apply_action(self, player_profile: PlayerProfile, intersections: Dict[int, Intersection]):
        player_profile.resources["WHEAT"] -= 200
        player_profile.resources["IRON"] -= 300
        if isinstance(self.city, int):
            for city in player_profile.cities:
                if isinstance(self.city, int) and city.intersection.id == self.city:
                    self.city = city
        self.city.upgrade()
