class PlayerProfile:
    def __init__(self):
        self.cities = []
        self.resources = {"SHEEP": 0, "WOOD": 0, "WHEAT": 0, "CLAY": 0, "IRON": 0}
        self.current_builder_intersection_position = None

    def get_score(self) -> int:
        # TODO: Calculate player score (sum of city levels)
        pass
