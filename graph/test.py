from .list_graph import GraphAdjList
from .matrix_graph import GraphAdjMatrix
from .Node import Node

import numpy as np


def test_get_set():
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    assert tuple(graph[0, 1]) == (1, 1), graph[0, 1]
    assert tuple(graph[1, 1]) == (0, np.inf), graph[0, 1]

    node_list = [Node('a'), Node('b'), Node('c')]

    graph = GraphAdjList(node_list)
    graph.add_edge((node_list[0], node_list[1]))
    graph.add_edge((node_list[1], node_list[0]))

    assert graph.nodes == node_list
    assert graph.nodes[0] == node_list[0]
    assert graph.nodes[1] == node_list[1]


def test_is_adjacent():
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    assert graph.is_adjacent((0, 1))

    node_list = [Node('a'), Node('b'), Node('c')]

    graph = GraphAdjList(node_list)

    graph.add_edge((node_list[0], node_list[1]))

    assert graph.is_adjacent((node_list[0], node_list[1]))
    assert not graph.is_adjacent((node_list[1], node_list[0]))


def test_add_edge():
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    graph.add_edge((1, 2), 3)
    graph.add_edge((2, 1), 3)

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


def test_add_vertex():
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    graph.add_vertex()

    assert graph.size == 4
    assert graph.matrix['weight'][0][1] == 1
    assert graph.matrix['weight'][3][3] == np.inf

    assert graph.matrix['is_inc'][0][1] == 1
    assert graph.matrix['is_inc'][3][3] == 0

    node_list = [Node('a'), Node('b'), Node('c')]

    graph = GraphAdjList(node_list)
    graph.add_vertex()

    assert len(graph.nodes) == 4
    assert graph.nodes[-1].name == chr(ord('c') + 1)


def test_remove_vertex():
    matrix = [[np.inf, np.inf, 1],
              [np.inf, np.inf, np.inf],
              [1, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    graph.remove_vertex(1)
    assert graph.size == 2
    assert tuple(graph[0, 1]) == (1, 1)
    assert tuple(graph[1, 0]) == (1, 1)

    node_list = [Node('a'), Node('b'), Node('c')]
    graph = GraphAdjList(node_list.copy())
    graph.add_edge((node_list[0], node_list[2]))
    graph.add_edge((node_list[1], node_list[2]))
    graph.add_edge((node_list[1], node_list[0]))

    assert graph.is_adjacent((node_list[1], node_list[2]))
    assert graph.is_adjacent((node_list[1], node_list[0]))
    graph.remove_vertex(node_list[1])

    assert graph.is_adjacent((node_list[0], node_list[2]))
    assert not graph.is_adjacent((node_list[1], node_list[0]))
    assert not graph.is_adjacent((node_list[1], node_list[2]))


def test_neighbors():
    matrix = [[np.inf, 2, 1],
              [np.inf, np.inf, 3],
              [1, 3, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    assert graph.get_neighbors(1) == [2]
    assert graph.get_neighbors(2) == [0, 1]

    node_list = [Node('a'), Node('b'), Node('c')]
    graph = GraphAdjList(node_list.copy())
    graph.add_edge((node_list[0], node_list[2]))
    graph.add_edge((node_list[1], node_list[2]))
    graph.add_edge((node_list[1], node_list[0]))

    for node_neighbor in graph.get_neighbors(node_list[0]):
        assert node_neighbor[0] in [node_list[2]]
    for node_neighbor in graph.get_neighbors(node_list[1]):
        assert node_neighbor[0] in [node_list[2], node_list[0]]
