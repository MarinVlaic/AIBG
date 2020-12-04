import requests
import server_api


game_id = int(input("Game id: "))
player_id = int(input("Player id: "))

train = bool(input("Is train: "))
url = 'http://localhost:9080/game/' if not train else 'http://localhost:9080/train/'

server_access_manager = server_api.ServerRequestManager(url, player_id, game_id)



