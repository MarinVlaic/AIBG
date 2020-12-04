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
        self.current_builder_intersection_position = None
        self.id = id

    def get_score(self) -> int:
        return sum(map(lambda x: x.level, self.cities))

    def has_enough_resources(self, resource_dict):
        for resource in resource_dict:
            if resource_dict[resource] > self.resources[resource]:
                return False
        return True

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
