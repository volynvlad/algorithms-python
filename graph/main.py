from algorithms_python.graph.list_graph import GraphAdjList
from algorithms_python.graph.matrix_graph import GraphAdjMatrix

import numpy as np


if __name__ == "__main__":
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    print((1, 1, b'a', b'b'), " ", graph[0, 1])
    print((0, np.inf, b'b', b'b'), " ", graph[1, 1])

    print(graph)
