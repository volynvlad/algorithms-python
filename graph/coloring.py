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

    def get_clique(graph_: list_graph):
        copy_graph_ = deepcopy(graph_)
        minimum_vertex_degree = min(copy_graph_.nodes, key=lambda vertex: vertex.degree())
        while minimum_vertex_degree.degree() != copy_graph_.order() - 1:
            copy_graph_.remove_vertex(minimum_vertex_degree)
            minimum_vertex_degree = min(copy_graph_.nodes, key=lambda vertex: vertex.degree())
        return [vertex for vertex in graph_.nodes if vertex in copy_graph_.nodes]

    def get_vertices_to_color(not_colored_vertices_, adjacent_vertices_colors_):
        vertex_to_color_ = next(iter(not_colored_vertices_))
        for vertex in not_colored_vertices_:
            len_vertex = len(adjacent_vertices_colors_[vertex.number])
            len_vertex_to_color = len(adjacent_vertices_colors_[vertex_to_color_.number])
            if len_vertex > len_vertex_to_color or \
                    (len_vertex == len_vertex_to_color and vertex.degree() > vertex_to_color_.degree()):
                vertex_to_color_ = vertex

        return vertex_to_color_

    copy_graph = deepcopy(list_graph)
    vertices_colors = {}
    not_colored_vertices = [vertex for vertex in copy_graph.nodes]
    adjacent_vertices_colors = {vertex.number: set() for vertex in not_colored_vertices}

    clique = get_clique(copy_graph)

    num_used_colors = len(clique)

    for color, vertex in enumerate(clique):
        vertices_colors[vertex.number] = color
        not_colored_vertices.remove(vertex)
    for vertex in clique:
        for neighbor, _ in vertex.get_neighbors():
            adjacent_vertices_colors[neighbor.number].add(vertices_colors[vertex.number])

    while len(not_colored_vertices) != 0:
        vertex_to_color = get_vertices_to_color(not_colored_vertices, adjacent_vertices_colors)
        available_colors = set(range(num_used_colors)) - adjacent_vertices_colors[vertex_to_color.number]

        color, num_used_colors = (min(available_colors), num_used_colors) \
            if available_colors else (num_used_colors, num_used_colors + 1)

        vertices_colors[vertex_to_color.number] = color
        not_colored_vertices.remove(vertex_to_color)

        for neighbor, _ in vertex_to_color.get_neighbors():
            adjacent_vertices_colors[neighbor.number].add(color)

    return vertices_colors
