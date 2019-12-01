from .node import Node

from collections import deque
import numpy as np
from copy import deepcopy
import math


class GraphAdjList:

    def __init__(self, nodes, first_node_name='a'):
        self.nodes = nodes
        self._number_connected_components = 1
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

        result_path = deque()
        path = deque()
        current_node = graph.nodes[0]
        path.append(current_node)

        while graph.order() == 0:
            while current_node.degree() == 0:
                result_path.append(current_node)
                path.pop()
                graph.remove_vertex(current_node)
                current_node = path[-1]

            next_node = current_node.get_neighbors()[0][0]
            graph.remove_double_edge((current_node, next_node))
            current_node = next_node
            path.append(current_node)

        return result_path

    def width_bypass(self, start_node=None):

        self._number_connected_components = 1
        for node in self.nodes:
            node.set_mark(None)
            node.set_marker(None)

        start_node = start_node or self.nodes[0]
        mark = 0
        start_node.set_mark(mark)

        queue = deque()
        queue.append(start_node)

        number_marked_nodes = 1
        while number_marked_nodes < len(self.nodes):
            node = queue[0]
            for neighbor, _ in node.get_neighbors():
                if neighbor not in queue:
                    if not neighbor.is_marked():
                        queue.append(neighbor)
                        neighbor.set_mark((0 if not node.is_marked() else node.get_mark()) + 1)
                        number_marked_nodes += 1
            queue.popleft()
            if not queue:
                for node in self.nodes:
                    if not node.is_marked():
                        self._number_connected_components += 1
                        node.set_mark(0)
                        queue.append(node)
                        number_marked_nodes += 1
                        break

    def number_of_connected_components(self):
        self.width_bypass()
        return self._number_connected_components

    def is_connected(self):
        return self.number_of_connected_components() == 1

    def is_bipartite(self):
        first_segment = []
        second_segment = []

        for node in self.nodes:
            node.set_mark(None)
            node.set_marker(None)

        start_node = self.nodes[0]
        start_node.set_mark(0)

        queue = deque()
        queue.append(start_node)

        number_marked_nodes = 1
        while number_marked_nodes < len(self.nodes):
            node = queue[0]
            for neighbor, _ in node.get_neighbors():
                if neighbor not in queue:
                    if not neighbor.is_marked():
                        queue.append(neighbor)
                        neighbor.set_mark(int(node.get_mark() == 0))
                        number_marked_nodes += 1
                    else:
                        if neighbor.get_mark() == node.get_mark():
                            return False, []
            queue.popleft()
            if not queue:
                for node in self.nodes:
                    if not node.is_marked():
                        node.set_mark(int(node.get_mark() == 0))
                        queue.append(node)
                        number_marked_nodes += 1
                        break
        for node in self.nodes:
            if node.get_mark() == 0:
                first_segment.append(node)
            else:
                second_segment.append(node)

        return True, [first_segment, second_segment]

    def has_cycle(self):
        for node in self.nodes:
            node.set_mark(None)
            node.set_marker(None)

        start_node = self.nodes[0]
        start_node.set_mark(0)

        queue = deque()
        queue.append(start_node)

        number_marked_nodes = 1
        while number_marked_nodes < len(self.nodes):
            node = queue[0]
            for neighbor, _ in node.get_neighbors():
                if neighbor not in queue:
                    if not neighbor.is_marked():
                        queue.append(neighbor)
                        neighbor.set_mark(int(node.get_mark() == 0))
                        neighbor.set_marker(node)
                        number_marked_nodes += 1
                    else:
                        if node.marker_node != neighbor:
                            return True
            queue.popleft()
            if not queue:
                for node in self.nodes:
                    if not node.is_marked():
                        node.set_mark(int(node.get_mark() == 0))
                        queue.append(node)
                        number_marked_nodes += 1
                        break
        return False

    def kruskal(self):
        node_list = [Node() for _ in range(self.order())]
        spanning_tree = GraphAdjList(node_list)

        edges = self.get_ordered_edges(self.get_edges())

        [(spanning_tree.nodes[i].set_mark(i), self.nodes[i].set_mark(i)) for i in range(spanning_tree.order())]

        if len(edges) // 2 + 1 < len(self.nodes):
            return []

        counter_edges = 0
        while counter_edges < spanning_tree.order() - 1:
            edge = edges[0]
            edge_components = [edge[0][0].get_mark(), edge[0][1].get_mark()]
            if edge_components[0] != edge_components[1]:
                counter_edges += 1
                spanning_tree.add_double_edge((edge[0][0], edge[0][1]))
                for node in spanning_tree.nodes:
                    if node.get_mark() == edge_components[0] or node.get_mark() == edge_components[1]:
                        node.set_mark(min(edge_components))
                        self.find_by_name(node.name).set_mark(min(edge_components))

            edges.pop(0)
            edges.pop(0)

        return spanning_tree

    def prim(self):
        node_list = [Node() for _ in range(self.order())]
        spanning_tree = GraphAdjList(node_list)

        start = self.nodes[0]

        passed = [start]
        start.set_mark(1)

        while len(passed) != self.order():

            min_weight = np.inf
            next_node = None
            cur_node = None

            for node in passed:
                for neighbor, weight in node.get_neighbors():
                    if not neighbor.is_marked():
                        temp_node = neighbor
                        temp_weight = node.get_neighbor_weight_by_name(neighbor.name)
                        if temp_weight < min_weight:
                            cur_node = node
                            min_weight = temp_weight
                            next_node = temp_node

            spanning_tree.add_double_edge((cur_node, next_node), cur_node.get_neighbor_weight_by_name(next_node.name))
            next_node.set_mark(1)
            passed.append(next_node)

        return spanning_tree

    def dijkstra(self, start_node=None):

        start_node = start_node or self.nodes[0]

        queue = [start_node]
        marked_names = []

        while queue:
            node = queue[0]
            for neighbor, weight in node.get_neighbors():
                if neighbor.name in marked_names:
                    continue
                else:
                    queue.append(neighbor)
                if not neighbor.is_marked() or \
                        weight + (0 if not node.is_marked() else node.get_mark()) < \
                        (0 if not neighbor.is_marked() else neighbor.get_mark()):
                    neighbor.set_marker(node)
                    neighbor.set_mark(weight + (0 if not node.is_marked() else node.get_mark()))

            marked_names.append(node.name)
            queue.remove(node)

    def gale_shapley(self, ranks):
        assert len(ranks[0]) == len(ranks[1])
        assert len(ranks[0][0]) == len(ranks[1][0])




