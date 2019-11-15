import numpy as np


class GraphAdjMatrix:
    def __init__(self, matrix, size=0):
        self.size = size
        self.matrix = np.zeros((self.size, self.size),
                               dtype=({
                                   'names': ['is_inc', 'weight', 'row_vertex', 'column_vertex'],
                                   'formats': [int, float, 'S10', 'S10']}))

        names = [chr(ord('a') + i) for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j]['row_vertex'] = names[i]
                self.matrix[i][j]['column_vertex'] = names[j]
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

    def __setitem__(self, position, value):
        self.matrix[position[0]][position[1]]['weight'] = value

    def __getitem__(self, position):
        return self.matrix[position[0]][position[1]]

    def __str__(self):
        string = ""
        for i in range(self.size):
            for j in range(self.size):
                string += "{} ".format(str(self.matrix[i][j]))
            string += "\n"
        return string

    def add_edge(self, edge):
        if edge[0] not in self.matrix['row_vertex'] or edge[1] not in self.matrix['column_vertex']:
            return

        self.matrix[edge[0].name][edge[1].name] = 1
