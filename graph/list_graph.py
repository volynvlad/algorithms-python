from .Node import Node


class GraphAdjList:

    def __init__(self, nodes, first_node_name='a'):
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].name = chr(ord(first_node_name) + i)

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

    def remove_edge(self, edge):
        if edge[0] not in self.nodes or edge[1] not in self.nodes:
            return

        if self.is_adjacent(edge):
            for vertex, weight in edge[0].get_neighbors():
                if vertex == edge[1]:
                    edge[0].get_neighbors().remove((edge[1], weight))

    def add_vertex(self):
        self.nodes.append(Node(chr(ord(self.nodes[-1].name) + 1)))

    def remove_vertex(self, remove_node):
        if remove_node in self.nodes:
            for node in self.nodes:
                for neighbor_node, _ in node.get_neighbors():
                    if node != remove_node and remove_node == neighbor_node:
                        node.get_neighbors().remove(remove_node)
            return self.nodes.remove(remove_node)
        return None

    def is_adjacent(self, edge):

        if edge[0] not in self.nodes or edge[1] not in self.nodes:
            return

        return edge[1] == edge[0].get_neighbor_by_name(edge[1].name)

    @staticmethod
    def get_neighbors(node):
        return node.neighbors

    def is_eulerian(self):
        graph = self.__init__(self.nodes.copy())

        for node in graph.nodes:
            if node.degree() % 2 != 0:
                return False

