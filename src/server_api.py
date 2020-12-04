import requests
from src import map
from src.actions.action import Action
from src.actions.initial import Initial
from src.actions.buildtown import BuildTown
from src.actions.movenoroad import Move
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
        response = requests.get(f"{self.server_url}play?playerID={self.player_id}&gameID={self.game_id}")
        return map.Map(response.json())

    def check_action(self, action: Action) -> bool:
        response = requests.get(f"{self.server_url}canAction?playerId={self.player_id}&gameId={self.game_id}&action={action}")
        return True

    def do_action(self, action: Action) -> Action:
        response = requests.get(f"{self.server_url}doAction?playerId={self.player_id}&gameId={self.game_id}&action={action}").json()
        return self.__actionize(response.json()['result'])

    @staticmethod
    def __actionize(response):
        sp = response.split(' ')
        if len(sp) == 1:
            m = re.fullmatch('([A-Za-z]+)', response)
            if m is None:
                raise ValueError('Unexpected')
            return class_map[m.group(1)]()
        elif len(sp) == 2:
            m = re.fullmatch('([A-Za-z]+) ([0-9])+', response)
            if m is None:
                raise ValueError('Unexpected')
            return class_map[m.group(1)](int(m.group(2)))
        elif len(sp) == 3:
            return Initial(int(sp[1]), int(sp[2]))
        else:
            raise ValueError('Unexpected number of arguments')


