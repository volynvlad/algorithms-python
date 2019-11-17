from algorithms_python.graph.Node import Node
from algorithms_python.graph.list_graph import GraphAdjList
from algorithms_python.graph.matrix_graph import GraphAdjMatrix

import numpy as np


if __name__ == "__main__":
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
    print(path)

    for vertex in path:
        print(str(vertex))

