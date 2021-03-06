import requests
from src import map
from src.actions.action import Action
from src.actions.initial import Initial
from src.actions.buildtown import BuildTown
from src.actions.move import Move
from src.actions.upgradetown import UpgradeTown
from src.actions.empty import Empty
from src.actions.buildroad import BuildRoad
import re

class_map = {
    'buildtown': BuildTown,
    'buildroad': BuildRoad,
    'move': Move,
    'upgradetown': UpgradeTown,
    'empty': Empty
}


class ServerRequestManager:
    def __init__(self, server_url, player_id, game_id):
        self.server_url = server_url
        self.game_id = game_id
        self.player_id = player_id

    def init_connection(self):
        response = requests.get(f"{self.server_url}/game/play?playerID={self.player_id}&gameID={self.game_id}")
        return response.json()

    def check_action(self, action: Action) -> bool:
        response = requests.get(f"{self.server_url}canAction?playerID={self.player_id}&gameID={self.game_id}&action={action}")
        return True

    def do_action(self, action: Action) -> Action:
        response = requests.get(f"{self.server_url}doAction?playerID={self.player_id}&gameID={self.game_id}&action={action}").json()
        return self.__actionize(response['result'])

    @staticmethod
    def __actionize(response):
        sp = response.split(' ')
        if len(sp) == 1:
            return class_map[sp[0]]()
        elif len(sp) == 2:
            return class_map[sp[0]](int(sp[1]))
        elif len(sp) == 3:
            return Initial(int(sp[1]), int(sp[2]))
        else:
            raise ValueError('Unexpected number of arguments')


