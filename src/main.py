from src.server_api import ServerRequestManager, class_map
from src.actions.action import Action
from src.mapfeatures.city import City
from src.mapfeatures.intersection import Intersection
from src.playerprofile import PlayerProfile
from src.map import *
from src.mapstate import MapState
from src.utils import *
import requests
import re
from src.actions.initial import Initial
import threading


game_id = int(input("Game id: "))
player_id = int(input("Player id: "))

train = bool(input("Is train: "))
url = 'http://localhost:9080/game/' if not train else 'http://localhost:9080/train/'

server_access_manager = ServerRequestManager(url, player_id, game_id)
response = server_access_manager.init_connection()
intersection_neighbourhood, tile_neighbourhood, tiles, resources = helper(response)

all_intersections = {}
for i in range(len(tile_neighbourhood)):
    all_intersections[i] = Intersection(get_tiles_neighs(tiles, tile_neighbourhood, i), i, get_intersection_neighs(intersection_neighbourhood, i))

player = PlayerProfile(player_id)
opponent_player = PlayerProfile(2 if player_id == 1 else 1)
map_state = MapState(player, opponent_player, all_intersections)

if player_id == 1:
    action = initial_actions(player, map_state, resources)
    t = threading.Thread(target=map_state.apply_action, args=(action, player))
    t.start()
    resp = requests.get(f"{url}doAction?playerID={player_id}&gameID={game_id}&action={action}").json()
    t.join()

    m = re.fullmatch('initial ([0-9]+) ([0-9]+) initial ([0-9]+) ([0-9]+)', resp['result'])
    i1, i2 = Initial(int(m.group(1)), int(m.group(2))), Initial(int(m.group(3)), int(m.group(4)))
    map_state.apply_action(i1, opponent_player)
    map_state.apply_action(i2, opponent_player)

    action = initial_actions(player, map_state, resources)
    t = threading.Thread(target=map_state.apply_action, args=(action, player))
    t.start()
    resp = requests.get(f"{url}doAction?playerID={player_id}&gameID={game_id}&action={action}").json()
    t.join()

else:
    spl = response['result']['action'].split(' ')
    action = Initial(int(spl[1]), int(spl[2]))
    map_state.apply_action(action, opponent_player)

    action = initial_actions(player, map_state, resources)
    t = threading.Thread(target=map_state.apply_action, args=(action, player))
    t.start()
    resp = requests.get(f"{url}doAction?playerID={player_id}&gameID={game_id}&action={action}").json()
    t.join()

    action = initial_actions(player, map_state, resources)
    t = threading.Thread(target=map_state.apply_action, args=(action, player))
    t.start()
    resp = requests.get(f"{url}doAction?playerID={player_id}&gameID={game_id}&action={action}").json()
    t.join()

    m = re.fullmatch('initial ([0-9]+) ([0-9]+) ([A-Za-z]+)( [0-9]+)*', resp['result'])
    i1 = Initial(int(m.group(1)), int(m.group(2)))
    i2 = class_map[m.group(3)](m.group(4)) if m.group(4) else class_map[m.group(3)]()
    map_state.apply_action(i1, opponent_player)
    map_state.apply_action(i2, opponent_player)

player.current_builder_intersection_position_id = player.cities[0].intersection.id
opponent_player.current_builder_intersection_position_id = opponent_player.cities[0].intersection.id

while player.get_score() < 16 and opponent_player.get_score() < 16:
    action = get_action(player, map_state, resources)
    t = threading.Thread(target=map_state.apply_action, args=(action, player))
    t.start()
    opponent_action = server_access_manager.do_action(action)
    t.join()

    map_state.apply_action(opponent_action, opponent_player)
