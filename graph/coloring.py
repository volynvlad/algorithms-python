import numpy as np
from copy import deepcopy

from graph.list_graph import GraphAdjList
from graph.node import Node


def gis(list_graph: GraphAdjList):
    copy_graph = deepcopy(list_graph)
    related_colors = {}
    c = 1
    while not copy_graph.is_all_vertexes_marked():
        related_colors[c] = []
        available = [vertex for vertex in copy_graph.nodes if not vertex.is_marked()]
        while len(available) != 0:
            node_degrees = [vertex.degree() for vertex in copy_graph.nodes]
            v_num = node_degrees[int(np.argmin(node_degrees))]
            copy_graph.nodes[v_num].set_mark(c)
            list_graph.find_by_name(copy_graph.nodes[v_num].name).set_mark(c)
            related_colors[c].append(copy_graph.nodes[v_num].number)
            print(copy_graph.nodes[v_num])
            copy_graph.remove_vertex(copy_graph.nodes[v_num])
        c += 1
    return related_colors


if __name__ == "__main__":
    number_nodes = 10
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[1], node_list[2]))
    graph.add_double_edge((node_list[2], node_list[3]))
    graph.add_double_edge((node_list[3], node_list[4]))
    graph.add_double_edge((node_list[4], node_list[0]))

    graph.add_double_edge((node_list[5], node_list[6]))
    graph.add_double_edge((node_list[6], node_list[7]))
    graph.add_double_edge((node_list[7], node_list[8]))
    graph.add_double_edge((node_list[8], node_list[9]))
    graph.add_double_edge((node_list[9], node_list[5]))

    graph.add_double_edge((node_list[0], node_list[5]))
    graph.add_double_edge((node_list[1], node_list[6]))
    graph.add_double_edge((node_list[2], node_list[7]))
    graph.add_double_edge((node_list[3], node_list[8]))
    graph.add_double_edge((node_list[4], node_list[9]))

    related_colors = gis(graph)
    print(related_colors)
