class Node:
    def __init__(self, name: str, neighbors=None):  # multi (name, weight) in set
        if neighbors is None:
            neighbors = []
        self.name = name
        self.neighbors = neighbors

    def __str__(self):
        string = "Node["
        string += "name = {}".format(self.name)
        if self.neighbors is None:
            string += ", neighbors = {}".format(self.neighbors)
        else:
            string += ", neighbors = "
            for neighbor in self.neighbors:
                string += "({} {})".format(str(neighbor[0]), neighbor[1])
        return string + "]"

    def __eq__(self, node):
        if self is None or node is None:
            return False
        return self.name == node.name

    def get_neighbors(self):
        return self.neighbors

    def get_neighbor_by_name(self, name):
        for neighbor in self.neighbors:
            if neighbor[0].name == name:
                return neighbor[0]
        return None

    def get_neighbor_weight_by_name(self, name):
        for neighbor in self.neighbors:
            if neighbor[0].name == name:
                return neighbor[1]
        return None
