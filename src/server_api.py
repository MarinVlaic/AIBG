import requests
from src import map
from action import Action
from typing import Tuple


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
        return Action(response.json()['result'])

    def do_initial_action(self, action: Tuple[Action]) -> Tuple[Action]:
        return (Action(), Action())