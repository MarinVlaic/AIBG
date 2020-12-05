from src.mapstate import MapState
from src.playerprofile import PlayerProfile
from src.actions.move import Move
from src.actions.buildtown import BuildTown
from src.actions.upgradetown import UpgradeTown
from src.actions.buildroad import BuildRoad
from src.actions.empty import Empty
from typing import Dict


def get_all_available_moves(mapstate: MapState, player: PlayerProfile):
    selected_player = mapstate.first_player_profile
    opposing_player = mapstate.second_player_profile
    if selected_player.id != player.id:
        selected_player, opposing_player = opposing_player, selected_player

    all_moves = []
    current_builder_position_id = mapstate.all_intersections[selected_player.current_builder_intersection_position_id].id

    # Generate moves
    for available_intersection_id in mapstate.all_intersections[current_builder_position_id].neighbouring_intersection_ids:
        # Check if there is no road
        if player.check_road(current_builder_position_id, available_intersection_id):
            all_moves.append(Move(available_intersection_id))
        else:
            if player.has_enough_resources({"SHEEP": 50, "WHEAT": 50}):
                all_moves.append(Move(available_intersection_id))

    # Generate build cities
    if player.has_enough_resources({"SHEEP": 100, "WOOD": 100, "WHEAT": 100, "CLAY": 100}):
        if is_buildable(current_builder_position_id, mapstate.all_intersections, opposing_player):
            all_moves.append(BuildTown(current_builder_position_id))

    # Generate upgrade cities

    if player.has_enough_resources({"WHEAT": 200, "IRON": 300}):
        [all_moves.append(UpgradeTown(i)) for i in player.cities if i.level == 1]

    # Generate build roads

    if player.has_enough_resources({"WOOD": 100, "CLAY": 100}):
        for n in mapstate.all_intersections[current_builder_position_id].neighbouring_intersection_ids:
            if is_road_buildable(current_builder_position_id, n, mapstate.all_intersections, player, opposing_player):
                all_moves.append(BuildRoad(n))

    # Generate empty
    all_moves.append(Empty())

def is_buildable(intersection_id, intersections, opposing_player: PlayerProfile):
    intersection = intersections[intersection_id]
    counter = 0
    for n in intersection.neighbouring_intersection_ids:
        if intersections[n].captured:
            return False
        counter += int(opposing_player.check_road(intersection_id, n))
        if counter == 2:
            return False
    return True


def is_road_buildable(intersection_from_id, intersection_to_id, intersections, player:PlayerProfile, opposing_player: PlayerProfile):
    for opposing_player_city in opposing_player.cities:
        if opposing_player_city.intersection.id in (intersection_to_id, intersection_from_id):
            return False

    counter_to = 0
    counter_from = 0
    for opponent_road in opposing_player.owned_roads:
        if intersection_from_id in opponent_road:
            counter_from += 1
        if intersection_to_id in opponent_road:
            counter_to += 1
        if counter_from == 2 or counter_to == 2:
            return False

    for player_city in player.cities:
        if player_city.intersection.id in (intersection_to_id, intersection_from_id):
            return True

    for player_road in player.owned_roads:
        if intersection_from_id in player_road or intersection_to_id in player_road:
            return True

    return False


def initial_actions(player: PlayerProfile, map_state: MapState, resources: Dict[str, int]):
    pass


def get_action(player: PlayerProfile, map_state: MapState, resources: Dict[str, int]):
    pass
