from .list_graph import GraphAdjList
from .matrix_graph import GraphAdjMatrix

import numpy as np


def test_get_set():
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    assert tuple(graph[0, 1]) == (1, 1, b'a', b'b'), graph[0, 1]
    assert tuple(graph[1, 1]) == (0, np.inf, b'b', b'b'), graph[0, 1]
