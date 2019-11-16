class GraphAdjList:

    def __init__(self, nodes):
        self.nodes = nodes

    def __str__(self):
        result = ""
        for node in self.nodes:
            result += "node: {}\n".format(str(node))
        return result

    def find_by_name(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def add_edge(self, edge, weight=1):
        if edge[0] not in self.nodes or edge[1] not in self.nodes:
            return

        edge[0].neighbors.append((edge[1], weight))

    def add_vertex(self, node):
        pass

    def is_adjacent(self, edge):

        if edge[0] not in self.nodes or edge[1] not in self.nodes:
            return

        return edge[1] == edge[0].get_neighbor_by_name(edge[1].name)
