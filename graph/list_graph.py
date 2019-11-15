class GraphAdjList:

    class Node:
        def __init__(self, name: str, neighbors=None):  # multi (name, weight) in set
            if neighbors is None:
                neighbors = set()
            self.name = name
            self.neighbors = neighbors

        def __str__(self):
            return "name = {}, neighbors = {}".format(self.name, self.neighbors)

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
        return node

    def add_edge(self, edge):
        if edge[0] not in self.nodes or edge[1] not in self.nodes:
            return

        first_node = self.find_by_name(edge[0].name)
        second_node = self.find_by_name(edge[1].name)

        first_node.neighbors.add(second_node)
        second_node.neighbors.add(first_node)

    def add_vertex(self, node):
        pass
