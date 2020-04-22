from copy import deepcopy

from graph.list_graph import GraphAdjList
from graph.node import Node


def gis(list_graph: GraphAdjList):

    def get_possible_vertices_to_color(not_colored, adjacent_colors, color):
        vertices = []
        for vertex in not_colored:
            if color not in adjacent_colors[vertex.number]:
                vertices.append(vertex)
        return vertices

    copy_graph = deepcopy(list_graph)
    vertices_colors = {}
    not_colored_vertices = [vertex for vertex in copy_graph.nodes]
    adjacent_vertices_colors = {vertex.number: set() for vertex in not_colored_vertices}
    c = 1

    while len(not_colored_vertices) != 0:
        available = get_possible_vertices_to_color(not_colored_vertices, adjacent_vertices_colors, c)
        available_degrees = [(available[i], copy_graph.nodes[i].degree()) for i in range(len(available))]

        while len(available) != 0:
            min_vertex, degree = min(available_degrees, key=lambda item: item[1])
            if c not in adjacent_vertices_colors[min_vertex.number]:
                vertices_colors[min_vertex.number] = c
                not_colored_vertices.remove(min_vertex)
                for neighbor, _ in min_vertex.get_neighbors().copy():
                    adjacent_vertices_colors[neighbor.number].add(c)
                    if neighbor in available:
                        available.remove(neighbor)
                        for available_degree in available_degrees:
                            if available_degree[0] == neighbor:
                                available_degrees.remove(available_degree)
                    copy_graph.remove_double_edge((neighbor, min_vertex))

            available_degrees.remove((min_vertex, degree))
            available.remove(min_vertex)

        c += 1
    return vertices_colors


def dsatur(list_graph: GraphAdjList):

    def get_vertices_to_color():
        vertices = []

        return vertices

    copy_graph = deepcopy(list_graph)
    vertices_colors = {}
    not_colored_vertices = [vertex for vertex in copy_graph.nodes]
    adjacent_vertices_colors = {vertex.number: set() for vertex in not_colored_vertices}
    c = 1

    while len(not_colored_vertices) != 0:
        vertex_to_color = get_vertices_to_color()
        pass

    return vertices_colors


if __name__ != "__main__":
    number_nodes = 5
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[1], node_list[2]))
    graph.add_double_edge((node_list[1], node_list[3]))
    graph.add_double_edge((node_list[3], node_list[4]))
    graph.add_double_edge((node_list[0], node_list[4]))

    colors = gis(graph)
    print(colors)


if __name__ == "__main__":
    number_nodes = 10
    node_list = [Node(chr(ord('a') + i)) for i in range(number_nodes)]

    graph = GraphAdjList(node_list.copy())

    graph.add_double_edge((node_list[0], node_list[1]))
    graph.add_double_edge((node_list[1], node_list[2]))
    graph.add_double_edge((node_list[2], node_list[3]))
    graph.add_double_edge((node_list[3], node_list[4]))
    graph.add_double_edge((node_list[4], node_list[0]))

    graph.add_double_edge((node_list[5], node_list[7]))
    graph.add_double_edge((node_list[7], node_list[9]))
    graph.add_double_edge((node_list[9], node_list[6]))
    graph.add_double_edge((node_list[6], node_list[8]))
    graph.add_double_edge((node_list[8], node_list[5]))

    graph.add_double_edge((node_list[0], node_list[5]))
    graph.add_double_edge((node_list[1], node_list[6]))
    graph.add_double_edge((node_list[2], node_list[7]))
    graph.add_double_edge((node_list[3], node_list[8]))
    graph.add_double_edge((node_list[4], node_list[9]))

    colors = gis(graph)
    print(f"colors = {colors}")
