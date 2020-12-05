import src.server_api as server_api
from src.actions.action import Action
from src.mapfeatures.city import City
from src.mapfeatures.intersection import Intersection
from src.playerprofile import PlayerProfile
from src.map import *
from src.mapstate import MapState

game_id = int(input("Game id: "))
player_id = int(input("Player id: "))

train = bool(input("Is train: "))
url = 'http://localhost:9080/game/' if not train else 'http://localhost:9080/train/'

server_access_manager = server_api.ServerRequestManager(url, player_id, game_id)

intersection_neighbourhood, tile_neighbourhood, tiles, resources = helper(server_access_manager.init_connection())

all_intersections = {}
for i in range(len(tile_neighbourhood)):
    all_intersections[i] = Intersection(get_tiles_neighs(tiles, tile_neighbourhood, i), i, get_intersection_neighs(intersection_neighbourhood, i))

player = PlayerProfile(player_id)
opponent_player = PlayerProfile(2 if player_id == 1 else 1)
map_state = MapState(player, opponent_player, all_intersections)


