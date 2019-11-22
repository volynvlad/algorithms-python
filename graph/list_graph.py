from .Node import Node

from collections import deque
from copy import deepcopy
import math


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

    def __eq__(self, graph_adj_tree):
        for node1, node2 in zip(self.nodes, graph_adj_tree.nodes):
            if node1 != node2:
                return False
        return True

    def find_by_name(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def get_edges(self):
        edges = []

        for node in self.nodes:
            for neighbor, weight in node.get_neighbors():
                edges.append(((node, neighbor), weight))

        return edges

    @staticmethod
    def get_ordered_edges(edges, reverse=False):
        def take_second(elem):
            return elem[1]

        edges.sort(key=take_second, reverse=reverse)

        return edges

    def add_edge(self, edge, weight=1):
        correspond_edge = (self.find_by_name(edge[0].name), self.find_by_name(edge[1].name))
        if correspond_edge[0] not in self.nodes or correspond_edge[1] not in self.nodes:
            return

        correspond_edge[0].neighbors.append((correspond_edge[1], weight))

    def add_double_edge(self, edge, weight=1):
        self.add_edge(edge, weight)
        self.add_edge((edge[1], edge[0]), weight)

    def remove_edge(self, edge):
        correspond_edge = (self.find_by_name(edge[0].name), self.find_by_name(edge[1].name))
        if correspond_edge[0] not in self.nodes or correspond_edge[1] not in self.nodes:
            return

        if self.is_adjacent(correspond_edge):
            for vertex, weight in correspond_edge[0].get_neighbors():
                if vertex == correspond_edge[1]:
                    correspond_edge[0].get_neighbors().remove((correspond_edge[1], weight))

    def remove_double_edge(self, edge):
        self.remove_edge(edge)
        self.remove_edge((edge[1], edge[0]))

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

    def vertexes_degree(self):
        return sum([x.degree() for x in self.nodes])

    def order(self):
        return len(self.nodes)

    @staticmethod
    def get_neighbors(node):
        return node.neighbors

    def euler_cycle(self):
        graph = deepcopy(self)

        for node in graph.nodes:
            if node.degree() % 2 != 0:
                return []

        full_path = []
        paths = [[]]
        path = []
        current_node = graph.nodes[0]
        path.append(current_node)

        while True:
            for node in graph.nodes:
                if node.degree() == 0:
                    graph.remove_vertex(node)

            if current_node.degree() == 0:
                paths.append(path)
                current_node = graph.nodes[0]
                path = [current_node]
            if current_node.degree() == 0 or graph.order() == 0:
                break

            next_node = current_node.get_neighbors()[0][0]
            graph.remove_edge((current_node, next_node))
            graph.remove_edge((next_node, current_node))
            current_node = next_node
            path.append(current_node)
        j = 0
        paths.pop(0)
        for i in range(1, len(paths)):
            while j < len(paths[0]):
                if paths[i][0].name == paths[0][j].name:
                    for vertex in paths[i]:
                        full_path.append(vertex)
                else:
                    full_path.append(paths[0][j])
                j += 1

        return full_path

    def width_bypass(self, start_node=None):

        for node in self.nodes:
            node.set_mark(None)

        node = start_node or self.nodes[0]
        mark = 0
        node.set_mark(mark)

        watched_nodes_names = []
        prev_watched_nodes_names = None

        number_of_marked_nodes = 1
        while number_of_marked_nodes < len(self.nodes):
            for node in self.nodes:
                if node.name not in watched_nodes_names:
                    if node.get_mark() == mark:
                        for neighbor, _ in node.get_neighbors():
                            if not neighbor.is_marked():
                                neighbor.set_mark(mark + 1)
                                number_of_marked_nodes += 1
                    elif not node.is_marked() and not node.is_any_neighbors_marked() \
                            and watched_nodes_names == prev_watched_nodes_names:
                        mark = -1
                        node.set_mark(0)
                        number_of_marked_nodes += 1
                        break
            prev_watched_nodes_names = watched_nodes_names.copy()
            for node in self.nodes:
                if node.name not in watched_nodes_names and node.is_marked() and node.is_all_neighbors_marked():
                    watched_nodes_names.append(node.name)

            mark += 1

    def number_of_connected_components(self):
        number_of_connected_components = 0

        self.width_bypass()

        for node in self.nodes:
            if node.get_mark() == 0:
                number_of_connected_components += 1

        return number_of_connected_components

    def is_connected(self):
        return self.number_of_connected_components() == 1

    def is_bipartite(self):
        first_segment = []
        second_segment = []

        for node in self.nodes:
            node.set_mark(None)

        node = self.nodes[0]
        mark = 0
        node.set_mark(mark)

        watched_nodes_names = []
        prev_watched_nodes_names = None
        number_of_marked_nodes = 1

        while number_of_marked_nodes < len(self.nodes):
            for node in self.nodes:
                if node.name not in watched_nodes_names:
                    if node.get_mark() == mark:
                        for neighbor, _ in node.get_neighbors():
                            if not neighbor.is_marked():
                                neighbor.set_mark(mark + 1)
                                neighbor.set_marker(node)
                                number_of_marked_nodes += 1
                            else:
                                if math.fabs(neighbor.get_mark() - node.get_mark()) % 2 == 0:
                                    return False, []
                    elif not node.is_marked() and not node.is_any_neighbors_marked() \
                            and watched_nodes_names == prev_watched_nodes_names:
                        mark = -1
                        node.set_mark(0)
                        number_of_marked_nodes += 1
                        break
            prev_watched_nodes_names = watched_nodes_names.copy()
            for node in self.nodes:
                if node.name not in watched_nodes_names and node.is_marked() and node.is_all_neighbors_marked():
                    watched_nodes_names.append(node.name)

            mark += 1

        for node in self.nodes:
            if node.get_mark() % 2 == 0:
                first_segment.append(node)
            else:
                second_segment.append(node)

        return True, [first_segment, second_segment]

    def has_cycle(self):
        graph = deepcopy(self)
        queue = deque()

        queue.append(graph.nodes[0])
        while len(queue) != 0:
            node = queue[0]
            for neighbor, _ in node.get_neighbors():
                if neighbor in queue:
                    return True
                queue.append(neighbor)
            for neighbor, _ in node.get_neighbors():
                graph.remove_double_edge((node, neighbor))

            queue.popleft()
        return False

    def spanning_tree(self, adjacent_condition=True):
        names = []

        node_list = [Node() for _ in range(len(self.nodes))]

        spanning_tree = GraphAdjList(node_list)

        edges = self.get_ordered_edges(self.get_edges())

        if len(edges) // 2 + 1 < len(self.nodes):
            return []

        spanning_tree.add_double_edge((edges[0][0][0], edges[0][0][1]), edges[0][1])
        names.append(edges[0][0][0].name)
        names.append(edges[0][0][1].name)
        edges.pop(0)
        edges.pop(0)
        while len(spanning_tree.nodes) != len(names):
            for edge, weight in edges:
                if adjacent_condition:
                    if edge[0].name in names and edge[1].name in names:
                        continue
                    elif edge[0].name in names or edge[1].name in names:
                        spanning_tree.add_double_edge(tuple(edge), weight)
                    else:
                        continue
                else:
                    spanning_tree.add_double_edge(tuple(edge), weight)
                if spanning_tree.has_cycle():
                    spanning_tree.remove_double_edge(tuple(edge))
                else:
                    edges.remove((edge, weight))
                    edges.remove(((edge[1], edge[0]), weight))
                    if not edge[0].name in names:
                        names.append(edge[0].name)
                    if not edge[1].name in names:
                        names.append(edge[1].name)
        return spanning_tree


