from algorithms_python.graph.Node import Node
from algorithms_python.graph.list_graph import GraphAdjList
from algorithms_python.graph.matrix_graph import GraphAdjMatrix

import numpy as np


if __name__ == "__main__":

    number_nodes = 6
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]
    for node in node_list:
        print(str(node))

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[1], node_list[2]))
    graph.add_double_edge((node_list[0], node_list[2]))
    graph.add_double_edge((node_list[2], node_list[3]))
    graph.add_double_edge((node_list[2], node_list[4]))

    graph.width_bypass()

    assert node_list[0].get_mark() == 0
    assert node_list[1].get_mark() == 1
    assert node_list[2].get_mark() == 1
    assert node_list[3].get_mark() == 2
    assert node_list[4].get_mark() == 2
    assert node_list[5].get_mark() == 3

