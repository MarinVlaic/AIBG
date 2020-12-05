class PlayerProfile:
    def __init__(self, id):
        self.cities = []
        self.resources = {
            "SHEEP": 0,
            "WOOD": 0,
            "WHEAT": 0,
            "CLAY": 0,
            "IRON": 0
        }
        self.current_builder_intersection_position_id = None
        self.id = id
        self.owned_roads = set()

    def get_score(self) -> int:
        return sum(map(lambda x: x.level, self.cities))

    def has_enough_resources(self, resource_dict):
        for resource in resource_dict:
            if resource_dict[resource] > self.resources[resource]:
                return False
        return True

    def add_road(self, destination_intersection_id):
        if self.current_builder_intersection_position_id > destination_intersection_id:
            self.owned_roads.add((destination_intersection_id, self.current_builder_intersection_position_id))
        else:
            self.owned_roads.add((self.current_builder_intersection_position_id, destination_intersection_id))

    def __eq__(self, other):
        if other.id != self.id:
            return False
        else:
            retval = set(self.cities) == set(other.cities)
            if not retval:
                return False
            for resource in self.resources:
                retval = retval and self.resources[resource] == other.resources[resource]
            return retval

    def check_road(self, id1, id2):
        if id1 > id2:
            return (id2, id1) in self.owned_roads
        else:
            return (id1, id2) in self.owned_roads
