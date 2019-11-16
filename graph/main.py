from algorithms_python.graph.list_graph import GraphAdjList
from algorithms_python.graph.matrix_graph import GraphAdjMatrix

import numpy as np


if __name__ == "__main__":
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    print(graph)
