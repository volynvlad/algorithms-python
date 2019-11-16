from algorithms_python.graph.Node import Node
from algorithms_python.graph.list_graph import GraphAdjList
from algorithms_python.graph.matrix_graph import GraphAdjMatrix

import numpy as np


if __name__ == "__main__":
    node_list = [Node('a'), Node('b'), Node('c'), Node('d')]

    graph = GraphAdjList(node_list)
    graph.add_edge((node_list[1], node_list[2]))
    graph.add_edge((node_list[2], node_list[1]))
    graph.add_edge((node_list[0], node_list[2]))
    graph.add_double_edge((node_list[0], node_list[3]))

    print(graph)

    graph.remove_edge((node_list[0], node_list[2]))
    graph.remove_edge((node_list[1], node_list[2]))
    print(graph)
