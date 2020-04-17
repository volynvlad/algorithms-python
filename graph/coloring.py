import numpy as np
from copy import deepcopy

from graph.list_graph import GraphAdjList
from graph.node import Node


def gis(list_graph: GraphAdjList):
    copy_graph = deepcopy(list_graph)
    vertices_colors = {}
    not_colored_vertices = [vertex for vertex in copy_graph.nodes]
    c = 1

    while len(not_colored_vertices) != 0:
        print(f"c = {c}")
        vertices_colors[c] = []
        available = [vertex for vertex in copy_graph.nodes if not vertex.is_marked()]

        while len(available) != 0:
            print(f"available - {[x.number for x in available]}")
            node_degrees = [vertex.degree() if vertex.degree() != 0 else graph.order() + 1
                            for vertex in copy_graph.nodes]
            index_min = int(np.argmin(node_degrees))

            [print(f"{x[0]}, {x[1]}") for x in zip(copy_graph.nodes, node_degrees)]
            print(f"remove - {copy_graph.nodes[index_min]}")

            not_colored_vertices.remove(copy_graph.nodes[index_min])
            vertices_colors[c].append(copy_graph.nodes[index_min].number)
            copy_graph.nodes[index_min].set_mark(c)

            available.remove(copy_graph.nodes[index_min])
            for vertex in copy_graph.nodes[index_min].get_neighbors():
                available.remove(vertex)
                copy_graph.remove_double_edge((copy_graph.nodes[index_min], vertex[0]))
                for vertex_neighbor in vertex[0].get_neighbors():
                    copy_graph.remove_double_edge((vertex[0], vertex_neighbor[0]))
                copy_graph.remove_double_edge((vertex[0], copy_graph.nodes[index_min]))

        c += 1
    return vertices_colors


if __name__ == "__main__":
    number_nodes = 5
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[1], node_list[2]))
    graph.add_double_edge((node_list[1], node_list[3]))
    graph.add_double_edge((node_list[3], node_list[4]))
    graph.add_double_edge((node_list[4], node_list[0]))

    colors = gis(graph)
    [print(color, colors[color]) for color in colors]


if __name__ != "__main__":
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

    colors = gis(graph)
    print(f"colors = {colors}")
