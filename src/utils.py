from src.mapstate import MapState
from src.playerprofile import PlayerProfile
from src.actions.move import Move
from src.actions.buildtown import BuildTown
from src.actions.upgradetown import UpgradeTown
from src.actions.buildroad import BuildRoad
from src.actions.empty import Empty
from src.actions.initial import Initial
from typing import Dict
from src.firstheuristic import *
from copy import deepcopy
from map_state_heuristic import get_map_state_grade


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
    return all_moves

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


def find_road_neighbour(intersection: Intersection, all_intersections: Dict[int, Intersection], possible_intersections, opponent_player):
    first_neighbours = intersection.neighbouring_intersection_ids
    second_neighbours = set()
    for first_neigh in first_neighbours:
        second_neighbours = second_neighbours.union(set(all_intersections[first_neigh].neighbouring_intersection_ids))
    second_neighbours = second_neighbours - set(first_neighbours) - {intersection.id}
    for value, possible_intersection in possible_intersections:
        if possible_intersection.id in second_neighbours and is_buildable(possible_intersection.id, all_intersections, opponent_player):
            first_neigh_id = set(possible_intersection.neighbouring_intersection_ids).intersection(set(first_neighbours))
            return all_intersections[first_neigh_id.pop()]


def initial_actions(player: PlayerProfile, map_state: MapState, resources: Dict[str, int]):
    possible_intersections = [(get_intersection_value(intersection, resources, map_state.all_intersections), intersection) for intersection in map_state.all_intersections.values()]
    possible_intersections.sort(key=lambda x: x[0], reverse=True)
    opponent_player = map_state.first_player_profile if map_state.first_player_profile != player else map_state.second_player_profile
    for value, possible_intersection in possible_intersections:
        if is_buildable(possible_intersection.id, map_state.all_intersections, opponent_player):
            intersection_choice = possible_intersection
            road_neighbour = find_road_neighbour(intersection_choice, map_state.all_intersections, possible_intersections, opponent_player)
            return Initial(intersection_choice.id, road_neighbour.id)


def get_action(player: PlayerProfile, map_state: MapState, resources: Dict[str, int]):
    possible_moves = []
    for move in get_all_available_moves(map_state, player):
        new_map_state = deepcopy(map_state)
        new_map_state.apply_action(move)
        if new_map_state.first_player_profile == player:
            possible_moves.append((get_map_state_grade(new_map_state, new_map_state.first_player_profile, resources), move))
        else:
            possible_moves.append((get_map_state_grade(new_map_state, new_map_state.second_player_profile, resources), move))


    possible_moves.sort(key=lambda x: x[0], reverse=True)
    return possible_moves[0]

