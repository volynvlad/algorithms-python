import numpy as np


class GraphAdjMatrix:
    def __init__(self, matrix, size=0):
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
