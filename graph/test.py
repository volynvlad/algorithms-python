from .list_graph import GraphAdjList
from .matrix_graph import GraphAdjMatrix
from .Node import Node

import numpy as np


def test_get_set():
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    assert tuple(graph[0, 1]) == (1, 1, b'a', b'b'), graph[0, 1]
    assert tuple(graph[1, 1]) == (0, np.inf, b'b', b'b'), graph[0, 1]

    node_list = [Node('a', {'b'}), Node('b', {'a'}), Node('c')]

    graph = GraphAdjList(node_list)

    assert graph.nodes == node_list
    assert graph.nodes[0].get_neighbors() == {'b'}
    assert graph.nodes[1].get_neighbors() == {'a'}


def test_is_adjacent():
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    assert graph.is_adjacent((0, 1))

    node_list = [Node('a'), Node('b'), Node('c')]

    graph = GraphAdjList(node_list)

    graph.add_edge((node_list[0], node_list[1]))
    print(graph)

    assert graph.is_adjacent((node_list[0], node_list[1]))
    assert not graph.is_adjacent((node_list[1], node_list[0]))


def test_add_edge():
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    graph.add_edge((1, 2), 3)
    graph.add_edge((2, 1), 3)
    print("graph")
    print(graph)

    assert graph.is_adjacent((1, 2))
    assert graph.is_adjacent((2, 1))

    node_list = [Node('a'), Node('b'), Node('c')]

    graph = GraphAdjList(node_list)
    graph.add_edge((node_list[1], node_list[2]))
    graph.add_edge((node_list[2], node_list[1]))
    graph.add_edge((node_list[0], node_list[2]))

    assert graph.is_adjacent((node_list[1], node_list[2]))
    assert graph.is_adjacent((node_list[2], node_list[1]))
    assert graph.is_adjacent((node_list[0], node_list[2]))
    assert not graph.is_adjacent((node_list[2], node_list[0]))
