import numpy as np
from copy import deepcopy


class GraphAdjMatrix:
    def __init__(self, matrix, size=0):
        self._inquiry = []
        self.size = size
        self.matrix = np.zeros((self.size, self.size),
                               dtype=({
                                   'names': ['is_inc', 'weight'],
                                   'formats': [int, float]}))

        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    self.matrix[i][j]['weight'] = np.inf
                    self.matrix[i][j]['is_inc'] = 0
                else:
                    if matrix[i][j] == np.inf or matrix[i][j] == -np.inf:
                        self.matrix[i][j]['weight'] = matrix[i][j]
                        self.matrix[i][j]['is_inc'] = 0
                    else:
                        self.matrix[i][j]['weight'] = matrix[i][j]
                        self.matrix[i][j]['is_inc'] = 1

    def __setitem__(self, position, weight=1):
        if self.matrix[position[0]][position[1]]['is_inc'] == 0:
            self.matrix[position[0]][position[1]]['is_inc'] = 1
        self.matrix[position[0]][position[1]]['weight'] = weight

    def __getitem__(self, position):
        return self.matrix[position[0]][position[1]]

    def __str__(self):
        string = ""
        for i in range(self.size):
            for j in range(self.size):
                string += "{} ".format(str(self.matrix[i][j]))
            string += "\n"
        return string

    def add_vertex(self):
        self.size += 1
        old_matrix = self.matrix.copy()
        self.matrix = np.zeros((self.size, self.size), dtype=self.matrix.dtype)
        self.matrix[:old_matrix.shape[0], :old_matrix.shape[1]] = old_matrix

        for i in range(self.size):
            self.matrix[i][-1] = (0, np.inf)
            self.matrix[-1][i] = (0, np.inf)

    def remove_vertex(self, vertex_num):
        self.size -= 1
        old_matrix = self.matrix.copy()
        self.matrix = np.zeros((self.size, self.size), dtype=self.matrix.dtype)
        for i in range(self.size + 1):
            for j in range(self.size + 1):
                if i < vertex_num and j < vertex_num:
                    self.matrix[i][j] = old_matrix[i][j]
                elif i > vertex_num and j < vertex_num:
                    self.matrix[i - 1][j] = old_matrix[i][j]
                elif i < vertex_num and j > vertex_num:
                    self.matrix[i][j - 1] = old_matrix[i][j]
                elif i > vertex_num and j > vertex_num:
                    self.matrix[i - 1][j - 1] = old_matrix[i][j]

    def add_edge(self, edge, weight):
        if edge[0] >= self.size or edge[1] >= self.size:
            return

        self.__setitem__((edge[0], edge[1]), weight)

    def remove_edge(self, edge):
        if edge[0] >= self.size or edge[1] >= self.size:
            return

        if self.is_adjacent(edge):
            self.matrix[edge[0]][edge[1]]['weight'] = np.inf
            self.matrix[edge[0]][edge[1]]['is_inc'] = 0

    def is_adjacent(self, edge):

        if edge[0] >= self.size or edge[1] >= self.size:
            print("return")
            return

        return self.matrix[edge[0]][edge[1]]['is_inc'] == 1

    def get_neighbors(self, vertex_num):
        neighbors = []

        for i in range(self.size):
            if self.is_adjacent((vertex_num, i)):
                neighbors.append(i)

        return neighbors

    def floid(self):
        inquiry = [[i + 1 for i in range(self.size)] for _ in range(self.size)]

        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if self.matrix[i][j]['weight'] > self.matrix[i][k]['weight'] + self.matrix[k][j]['weight']:
                        inquiry[i][j] = inquiry[i][k]
                        self.matrix[i][j]['weight'] = self.matrix[i][k]['weight'] + self.matrix[k][j]['weight']

        self._inquiry = inquiry

    def place_station(self):
        graph = deepcopy(self)

        for i in range(graph.size):
            for j in range(i, graph.size):
                min_value = min(graph.matrix[i][j]['weight'], graph.matrix[j][i]['weight'])
                graph.matrix[i][j]['weight'] = min_value
                graph.matrix[j][i]['weight'] = min_value
                graph.matrix[i][j]['is_inc'] = 1
                graph.matrix[i][j]['is_inc'] = 1

        graph.floid()

        print(graph.matrix['weight'])

        def minimum_sum(matrix, size):
            min_index = 0
            max_min = np.inf
            for i in range(size):
                temp_max = -np.inf
                for j in range(size):
                    if i != j:
                        if matrix[i][j] > temp_max:
                            temp_max = matrix[i][j]
                if temp_max < max_min:
                    max_min = temp_max
                    min_index = i
            return min_index

        return minimum_sum(graph.matrix['weight'], graph.size)

    @staticmethod
    def gale_shapley(proposor, acceptor):

        pairs = {i: [] for i in range(len(proposor))}

        def has_empty(list_):
            flag = True
            for i in range(len(list_)):
                flag = flag and list_[i] != []

            return flag

        indexes = [0 for _ in range(len(proposor))]
        marked_props = []
        while not has_empty(pairs):
            for i in range(len(pairs)):
                if i not in marked_props:
                    pairs[proposor[i][indexes[i]]].append(i)
                    indexes[i] += 1
                    marked_props.append(i)

            for i in range(len(pairs)):
                if len(pairs[i]) > 1:
                    best_proposor, best_priority  = None, len(pairs)
                    for j in range(len(pairs[i])):
                        prop_prior = acceptor[i].index(pairs[i][j])
                        if prop_prior < best_priority:
                            best_proposor, best_priority = pairs[i][j], prop_prior

                    for x in pairs[i]:
                        if x != best_proposor:
                            pairs[i].remove(x)
                            marked_props.remove(x)
        return pairs

