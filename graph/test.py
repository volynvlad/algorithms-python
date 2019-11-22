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


def test_get_ordered_edges():
    number_nodes = 4
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]), 2)
    graph.add_double_edge((node_list[1], node_list[3]), 1)
    graph.add_double_edge((node_list[2], node_list[3]), 4)
    graph.add_double_edge((node_list[2], node_list[1]), 3)
    graph.add_double_edge((node_list[0], node_list[3]), -2)

    edges = graph.get_ordered_edges(graph.get_edges())

    for i in range(len(edges) - 1):
        assert edges[i][1] <= edges[i + 1][1]


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


def test_remove_edge():
    matrix = [[np.inf, 1, np.inf],
              [1, np.inf, np.inf],
              [np.inf, np.inf, np.inf]]
    graph = GraphAdjMatrix(matrix=matrix, size=3)

    graph.add_edge((1, 2), 3)
    graph.add_edge((2, 1), 3)

    assert graph.is_adjacent((1, 2))
    assert graph.is_adjacent((2, 1))

    graph.remove_edge((1, 2))
    assert not graph.is_adjacent((1, 2))

    node_list = [Node('a'), Node('b'), Node('c')]

    graph = GraphAdjList(node_list)
    graph.add_edge((node_list[1], node_list[2]))
    graph.add_edge((node_list[2], node_list[1]))
    graph.add_edge((node_list[0], node_list[2]))

    assert graph.is_adjacent((node_list[1], node_list[2]))
    assert graph.is_adjacent((node_list[2], node_list[1]))
    assert graph.is_adjacent((node_list[0], node_list[2]))
    assert not graph.is_adjacent((node_list[2], node_list[0]))

    graph.remove_edge((node_list[0], node_list[2]))
    graph.remove_edge((node_list[1], node_list[2]))
    assert not graph.is_adjacent((node_list[0], node_list[2]))
    assert not graph.is_adjacent((node_list[1], node_list[2]))


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


def test_euler_cycle():
    number_nodes = 6
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    correct_answer = ['a', 'b', 'c', 'd', 'f', 'c', 'e', 'a', 'd', 'e', 'f', 'a']

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[0], node_list[3]))
    graph.add_double_edge((node_list[0], node_list[4]))
    graph.add_double_edge((node_list[0], node_list[5]))

    graph.add_double_edge((node_list[4], node_list[2]))
    graph.add_double_edge((node_list[4], node_list[3]))
    graph.add_double_edge((node_list[4], node_list[5]))

    graph.add_double_edge((node_list[2], node_list[1]))
    graph.add_double_edge((node_list[2], node_list[3]))
    graph.add_double_edge((node_list[2], node_list[5]))

    graph.add_double_edge((node_list[5], node_list[3]))

    path = graph.euler_cycle()

    for node, correct_answer in zip(path, correct_answer):
        assert node.name == correct_answer

    graph.remove_edge((node_list[0], node_list[1]))
    graph.remove_edge((node_list[1], node_list[0]))

    assert graph.euler_cycle() == []


def test_width_bypass():
    number_nodes = 9
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[1], node_list[2]))
    graph.add_double_edge((node_list[0], node_list[2]))
    graph.add_double_edge((node_list[2], node_list[3]))
    graph.add_double_edge((node_list[2], node_list[4]))
    graph.add_double_edge((node_list[5], node_list[6]))
    graph.add_double_edge((node_list[7], node_list[8]))

    graph.width_bypass()

    assert node_list[0].get_mark() == 0
    assert node_list[1].get_mark() == 1
    assert node_list[2].get_mark() == 1
    assert node_list[3].get_mark() == 2
    assert node_list[4].get_mark() == 2
    assert node_list[5].get_mark() == 0
    assert node_list[6].get_mark() == 1
    assert node_list[7].get_mark() == 0
    assert node_list[8].get_mark() == 1


def test_number_of_connected_components():
    number_nodes = 8
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[1], node_list[2]))
    graph.add_double_edge((node_list[0], node_list[2]))
    graph.add_double_edge((node_list[2], node_list[3]))
    graph.add_double_edge((node_list[2], node_list[4]))
    graph.add_double_edge((node_list[5], node_list[6]))

    assert graph.number_of_connected_components() == 3

    graph.width_bypass()
    graph.add_double_edge((node_list[2], node_list[5]))

    assert graph.number_of_connected_components() == 2


def test_is_connected():
    number_nodes = 8
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[1], node_list[2]))
    graph.add_double_edge((node_list[0], node_list[2]))
    graph.add_double_edge((node_list[2], node_list[3]))
    graph.add_double_edge((node_list[2], node_list[4]))
    graph.add_double_edge((node_list[5], node_list[6]))

    graph.width_bypass()

    assert not graph.is_connected()

    graph.add_double_edge((node_list[2], node_list[5]))
    graph.add_double_edge((node_list[5], node_list[7]))

    graph.width_bypass()

    assert graph.is_connected()


def test_is_bipartite():
    number_nodes = 8
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[1], node_list[2]))
    graph.add_double_edge((node_list[0], node_list[2]))
    graph.add_double_edge((node_list[2], node_list[3]))
    graph.add_double_edge((node_list[2], node_list[4]))
    graph.add_double_edge((node_list[5], node_list[6]))
    graph.add_double_edge((node_list[2], node_list[5]))
    graph.add_double_edge((node_list[5], node_list[7]))

    is_bipartite, *args = graph.is_bipartite()

    assert not is_bipartite

    graph.remove_edge((node_list[0], node_list[1]))

    is_bipartite, *args = graph.is_bipartite()

    assert is_bipartite

    graph.add_double_edge((node_list[4], node_list[6]))

    is_bipartite, *args = graph.is_bipartite()

    assert is_bipartite


def test_has_cycle():
    number_nodes = 6
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[1], node_list[2]))
    graph.add_double_edge((node_list[0], node_list[2]))

    assert graph.has_cycle()

    graph.remove_edge((node_list[0], node_list[1]))
    graph.remove_edge((node_list[1], node_list[0]))

    assert not graph.has_cycle()

    graph.add_double_edge((node_list[3], node_list[1]))
    graph.add_double_edge((node_list[3], node_list[4]))
    graph.add_double_edge((node_list[4], node_list[0]))

    assert graph.has_cycle()

    graph.remove_double_edge((node_list[3], node_list[1]))

    assert not graph.has_cycle()

    graph.add_double_edge((node_list[2], node_list[4]))

    assert graph.has_cycle()


def test_spanning_tree():

    number_nodes = 5
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]), 2)
    graph.add_double_edge((node_list[0], node_list[3]), 3)
    graph.add_double_edge((node_list[1], node_list[2]), 3)
    graph.add_double_edge((node_list[1], node_list[3]), 4)
    graph.add_double_edge((node_list[1], node_list[4]), 1)
    graph.add_double_edge((node_list[3], node_list[4]), 2)

    spanning_tree_with_adj_condition = graph.spanning_tree(adjacent_condition=True)
    spanning_tree_without_adj_condition = graph.spanning_tree(adjacent_condition=False)

    assert spanning_tree_with_adj_condition == spanning_tree_without_adj_condition

    assert spanning_tree_without_adj_condition.nodes[0].get_neighbors_names() == {'b'}
    assert spanning_tree_without_adj_condition.nodes[1].get_neighbors_names() == {'e', 'a', 'c'}
    assert spanning_tree_without_adj_condition.nodes[2].get_neighbors_names() == {'b'}
    assert spanning_tree_without_adj_condition.nodes[3].get_neighbors_names() == {'e'}
    assert spanning_tree_without_adj_condition.nodes[4].get_neighbors_names() == {'b', 'd'}
