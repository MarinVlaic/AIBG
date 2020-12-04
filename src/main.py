import requests

game_id = int(input("Game id: "))
player_id = int(input("Player id: "))

train = bool(input("Is train: "))
url = 'http://localhost:9080/' if not train else 'http://localhost:9080/train'




